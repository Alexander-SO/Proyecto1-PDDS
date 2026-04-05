import json
import os
import sys
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings")

import django
django.setup()
from django.test import Client
from django.db import connection
from django.test.utils import CaptureQueriesContext
from conduit.apps.authentication.models import User
from conduit.apps.articles.models import Article, Tag

def seed_data():
    if Article.objects.count() >= 30:
        return

    user, created = User.objects.get_or_create(
    username="benchuser",
    defaults={
        "email": "bench@example.com"
    }
    )

    if created:
        user.set_password("benchpass123")
        user.save()

    profile = user.profile

    tags = []
    for i in range(5):
        tag, _ = Tag.objects.get_or_create(tag="tag{}".format(i), slug="tag{}".format(i))
        tags.append(tag)

    for i in range(30):
        article = Article.objects.create(
            slug="article-{}".format(i),
            title="Article {}".format(i),
            description="Benchmark article {}".format(i),
            body="Lorem ipsum dolor sit amet {}".format(i),
            author=profile
        )
        article.tags.add(*tags[: (i % 5) + 1])

        if i % 2 == 0:
            profile.favorite(article)

def run_benchmark(iterations=5):
    client = Client()

    # Hacemos login para activar la lógica de favorited
    client.post("/api/users/", data=json.dumps({
        "user": {
            "username": "tempbench",
            "email": "tempbench@example.com",
            "password": "tempbench123"
        }
    }), content_type="application/json", HTTP_HOST="localhost")

    user = User.objects.filter(username="benchuser").first()
    client.force_login(user)

    times = []
    query_counts = []

    for _ in range(iterations):
        start = time.perf_counter()
        with CaptureQueriesContext(connection) as ctx:
            response = client.get("/api/articles", HTTP_HOST="localhost")
        elapsed = (time.perf_counter() - start) * 1000.0

        assert response.status_code == 200, response.status_code

        times.append(elapsed)
        query_counts.append(len(ctx.captured_queries))

    print("Iterations:", iterations)
    print("Avg time (ms): {:.2f}".format(sum(times) / len(times)))
    print("Min time (ms): {:.2f}".format(min(times)))
    print("Max time (ms): {:.2f}".format(max(times)))
    print("Avg query count:", sum(query_counts) / len(query_counts))
    print("Query counts:", query_counts)

if __name__ == "__main__":
    seed_data()
    run_benchmark()

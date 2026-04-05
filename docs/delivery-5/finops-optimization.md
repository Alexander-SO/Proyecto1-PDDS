# FinOps Optimization — Articles Endpoint

## Contexto

Durante el análisis del sistema se identificó que el endpoint:

GET /api/articles

presentaba un alto número de consultas SQL y un tiempo de respuesta elevado, especialmente al listar múltiples artículos.

---

## Problema identificado

El serializer de artículos realizaba operaciones costosas por cada elemento:

- Conteo de favoritos (`favorited_by.count()`)
- Verificación de favoritos por usuario (`has_favorited`)
- Acceso a relaciones ManyToMany (`tags`)

Esto generaba un patrón tipo **N+1 queries**.

---

## Solución implementada

Se aplicaron las siguientes optimizaciones:

### 1. Prefetch de relaciones
.prefetch_related('tags')

### 2. Annotate para conteo de favoritos
.annotate(favorites_count=Count('favorited_by', distinct=True))

### 3. Precálculo de favoritos del usuario

Se obtienen los IDs de artículos favoritos una sola vez y se pasan al serializer.

## Resultado Técnico

| Métrica         | Antes    | Después  |
| --------------- | -------- | -------- |
| Tiempo promedio | 32.80 ms | 16.72 ms |
| Queries SQL     | 42       | 3        |


## Impacto
49% reducción en latencia
92.9% reducción en consultas SQL
Menor carga sobre la base de datos
Mejor escalabilidad del sistema

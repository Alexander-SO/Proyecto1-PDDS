# Benchmark Results — Before vs After

## Metodología

Se creó un script de benchmark (`benchmarks/benchmark_articles.py`) que:

- Genera datos de prueba
- Ejecuta múltiples requests al endpoint `/api/articles`
- Mide tiempo de respuesta y número de queries SQL

---

## Resultados

### BEFORE

Iterations: 5  
Avg time: 32.80 ms  
Queries: 42  

### AFTER

Iterations: 5  
Avg time: 16.72 ms  
Queries: 3  

---

## Mejora obtenida

### Latencia
Reducción del 49%

### Queries
Reducción del 92.9%

---

## Estimación FinOps

Tomando como referencia una instancia estándar de AWS Lightsail (~USD 5/mes):

- Antes: ~79 millones requests/mes
- Después: ~155 millones requests/mes

Costo por millón de requests:

- Antes: ~$0.063
- Después: ~$0.032

---

## Conclusión

La optimización reduce significativamente el costo computacional por request y mejora la eficiencia del sistema sin aumentar la complejidad arquitectónica.

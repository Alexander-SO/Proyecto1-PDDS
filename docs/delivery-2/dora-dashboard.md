# Delivery 2 — Dashboard DORA (4 métricas)

## Contexto
Este proyecto es académico y no tiene un pipeline de despliegue a producción.  
Por lo tanto, se definen proxies medibles con GitHub para aproximar las métricas DORA.

## Fuentes de datos
- Pull Requests (tiempos de apertura → merge)
- GitHub Actions (estado de workflows)
- Commits a `main`
- Issues etiquetados como incidentes (si se usan)

---

## 1) Deployment Frequency (Frecuencia de despliegue)
**Proxy:** número de merges a `main` por semana (o releases/tags si se crean).  
**Cómo medir:** GitHub → Insights → Pulse / o conteo de merges a main.

---

## 2) Lead Time for Changes (Tiempo de entrega)
**Proxy:** tiempo desde que se abre un PR hasta que se mergea a `main`.  
**Cómo medir:** timestamps PR opened_at → merged_at.

---

## 3) Change Failure Rate (Tasa de fallos por cambio)
**Proxy:** porcentaje de PRs a `main` cuyo workflow “Governance CI” falla al menos una vez.  
**Cómo medir:** GitHub Actions runs asociados al PR.

---

## 4) Mean Time To Restore (MTTR)
**Proxy:** tiempo desde que se detecta un fallo (workflow rojo en main o issue “incident”) hasta que se mergea el fix a `main`.  
**Cómo medir:** primer fallo timestamp → PR fix merged timestamp.

---

## Dashboard (plantilla)
| Métrica | Definición (proxy) | Fuente | Valor actual |
|---|---|---|---|
| Deployment Frequency | # merges a main / semana | PRs / Insights | N/A (línea base) |
| Lead Time | PR open → PR merged | PR timestamps | N/A (línea base) |
| Change Failure Rate | % PRs con CI fallido | Actions | N/A (línea base) |
| MTTR | fallo → fix merged | Actions/Issues | N/A (línea base) |

## Nota
Se establece esta definición desde la semana 4 para recolectar datos consistentes en las siguientes entregas.

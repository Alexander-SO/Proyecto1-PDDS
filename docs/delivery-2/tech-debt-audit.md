# Delivery 2 — Tech Debt Audit (Hotspots) + Plan Strangler Fig

## Contexto
El repositorio del equipo tiene un historial de commits corto, por lo que el churn por `git log` aún no refleja “hotspots reales” de evolución.
Por esa razón, este audit prioriza hotspots usando:
- criticidad de negocio (auth, contenido),
- centralidad (número de endpoints afectados),
- tamaño y complejidad (radon),
- riesgo de cambios futuros (seguridad/performance).

## Evidencia de Complejidad (radon)
Hallazgos relevantes:
- `authentication/serializers.py` contiene componentes rank B (ej. `LoginSerializer` B(6))
- `authentication/backends.py` contiene rank B (ej. `JWTAuthentication` B(6))
- `articles/views.py` concentra la mayor cantidad de endpoints y lógica

---

## Hotspot #1 — conduit/apps/articles/views.py
### Por qué es hotspot
- Concentra múltiples flujos críticos: list/create/update articles, feed, favorites, comments, tags.
- Alto impacto: cualquier bug afecta funcionalidades centrales del sistema.
- Riesgo futuro: performance (feed/list), permisos, filtros y cambios de negocio.

### Strangler Fig Plan (refactor incremental)
**Objetivo:** separar lógica de dominio de las Views y reducir acoplamiento.

Fase 1 (bajo riesgo)
- Introducir capa de “services” sin cambiar endpoints:
  - `conduit/apps/articles/services/`
  - mover lógica de:
    - feed query building
    - favorite/unfavorite
    - comment create/delete
- Mantener las Views como adaptadores (solo orquestan).

Fase 2 (riesgo medio)
- Crear endpoints paralelos `/api/v2/articles/...` para los flujos más críticos (ej. feed/list),
  usando las nuevas capas de servicios.
- Mantener ambos caminos activos (v1 y v2).

Fase 3 (riesgo controlado)
- Migrar consumidores internos a v2.
- Deprecar v1 gradualmente y remover lógica antigua.

Impacto esperado:
- Menor complejidad en Views.
- Facilita pruebas unitarias (services testables sin request/response).
- Aísla cambios de performance sin tocar API pública al inicio.

---

## Hotspot #2 — conduit/apps/authentication/backends.py
### Por qué es hotspot
- Implementa JWTAuthentication: superficie directa de seguridad.
- Pequeños cambios pueden romper login o introducir vulnerabilidades.
- Complejidad B detectada.

### Strangler Fig Plan
Fase 1 (bajo riesgo)
- Extraer funciones puras:
  - parse/validate token
  - decode JWT
  - manejo de errores
  a `conduit/apps/authentication/jwt_utils.py`
- Agregar pruebas unitarias a esas funciones (cuando existan tests).

Fase 2 (riesgo medio)
- Introducir backend nuevo `JWTAuthenticationV2` con validaciones más claras,
  manteniendo el backend actual en paralelo y con feature flag (config).

Fase 3
- Migrar settings para usar V2.
- Remover V1 cuando el comportamiento esté validado.

Impacto esperado:
- Menor riesgo al hacer cambios de seguridad.
- Código más legible/auditable.
- Facilita agregar controles (expiración, claims, rotación).

---

## Hotspot #3 — conduit/apps/authentication/serializers.py
### Por qué es hotspot
- Define validación y transformación de input en login/registro.
- Un error aquí puede permitir inputs inválidos o romper compatibilidad.
- Se detectó rank B (LoginSerializer B(6)).

### Strangler Fig Plan
Fase 1 (bajo riesgo)
- Extraer validaciones complejas a funciones puras en `validation.py`
- Mantener el serializer como “orquestador” (llama a validación y arma respuesta)

Fase 2
- Introducir serializer V2 (por ejemplo `LoginSerializerV2`) y endpoint opcional `/api/v2/users/login`
- Mantener v1 y v2 en paralelo

Fase 3
- Migración gradual y retiro del serializer legacy

Impacto esperado:
- Validaciones probables de cambiar quedan aisladas.
- Permite endurecer reglas sin romper el endpoint legacy de inmediato.
- Mejora testabilidad.

---

## Priorización (riesgo/impacto)
1) `articles/views.py` — mayor impacto funcional y superficie de cambio
2) `authentication/backends.py` — alto riesgo de seguridad
3) `authentication/serializers.py` — riesgo de inputs/validación y compatibilidad

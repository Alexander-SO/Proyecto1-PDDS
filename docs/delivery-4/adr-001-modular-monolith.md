# ADR-001 — Estrategia de arquitectura: Monolito modular con extracción progresiva de servicios internos

## Estado
Propuesto

## Contexto

El sistema actual es un backend legacy basado en Django, organizado como un monolito con varios módulos funcionales dentro de `conduit/apps`, principalmente:

- `authentication`
- `articles`
- `profiles`

Durante las fases anteriores se identificaron varios problemas relevantes:

1. **Fricción de onboarding**: el entorno legacy requiere configuraciones especiales por el uso de Python 3.5.
2. **Ausencia de pruebas automatizadas significativas**: la cobertura actual es muy baja.
3. **Hotspots de deuda técnica**:
   - `conduit/apps/articles/views.py`
   - `conduit/apps/authentication/backends.py`
   - `conduit/apps/authentication/serializers.py`
4. **Dependencias entre contextos**: aunque existen módulos separados, todavía hay acoplamiento entre autenticación, artículos y perfiles.
5. **Riesgo de cambios grandes**: una reescritura completa o una migración directa a microservicios tendría un costo alto y un riesgo elevado para un sistema sin suficiente gobernanza técnica previa.

Además, la fase de Governance mostró que el sistema ya comenzó a incorporar mecanismos de control de calidad (CI, quality gates, análisis de complejidad), pero todavía no tiene el nivel de madurez necesario para una arquitectura distribuida.

---

## Decisión

Se propone adoptar una estrategia de **monolito modular**, reforzando la separación entre dominios existentes y extrayendo progresivamente lógica de negocio hacia una capa de servicios internos, antes de considerar una migración a microservicios.

Esto implica:

1. Mantener el despliegue como una sola aplicación.
2. Reducir la lógica concentrada en `views.py` y `serializers.py`.
3. Crear módulos de servicios por dominio, por ejemplo:
   - `conduit/apps/authentication/services/`
   - `conduit/apps/articles/services/`
   - `conduit/apps/profiles/services/`
4. Establecer límites más claros entre contextos.
5. Evaluar una posible separación física de servicios solo después de mejorar pruebas, observabilidad y estabilidad.

---

## Alternativas consideradas

### 1. Migración directa a microservicios
**Ventajas**
- Aislamiento fuerte entre dominios
- Escalabilidad independiente
- Despliegue más flexible en el futuro

**Desventajas**
- Incrementa la complejidad operativa
- Requiere observabilidad, pruebas y contratos entre servicios
- Alto riesgo para un sistema legacy con baja cobertura de tests
- Coste de migración elevado para el tamaño actual del proyecto

### 2. Reescritura completa del sistema
**Ventajas**
- Permitiría modernizar el stack desde cero
- Posibilidad de rediseñar toda la arquitectura

**Desventajas**
- Riesgo muy alto
- Tiempo de implementación elevado
- Pérdida de conocimiento ya incorporado en el sistema actual
- Poco realista para una evolución progresiva

### 3. Mantener el sistema exactamente como está
**Ventajas**
- No requiere inversión inmediata
- No introduce riesgo de cambio

**Desventajas**
- Mantiene la deuda técnica
- Dificulta el mantenimiento futuro
- No resuelve hotspots ni mejora la calidad del diseño

---

## Consecuencias

### Consecuencias positivas
- Reduce el acoplamiento interno sin aumentar la complejidad operativa de microservicios.
- Facilita pruebas unitarias futuras al separar lógica de negocio de las views.
- Mejora mantenibilidad en los hotspots ya identificados.
- Es compatible con una estrategia incremental como Strangler Fig.
- Permite una transición más segura para un sistema legacy.

### Consecuencias negativas
- No resuelve de inmediato todos los problemas estructurales.
- Requiere disciplina para mantener límites claros entre módulos.
- Parte del sistema seguirá compartiendo runtime y base de datos.
- La mejora es gradual, no inmediata.

---

## Riesgos

1. **Refactorización parcial sin consistencia**
   - Riesgo: mover lógica a servicios sin una convención clara puede empeorar la arquitectura.
   - Mitigación: definir una estructura uniforme por dominio.

2. **Falsa sensación de modularidad**
   - Riesgo: el sistema puede parecer modular sin serlo realmente si los servicios siguen muy acoplados.
   - Mitigación: limitar dependencias cruzadas y documentar interfaces internas.

3. **Cambios sin suficiente validación**
   - Riesgo: al haber poca cobertura de tests, refactorizar puede romper funcionalidad.
   - Mitigación: priorizar refactor en módulos pequeños y validar endpoints críticos.

---

## Costos

### Costos técnicos
- Reorganización de módulos internos
- Extracción de lógica desde views/serializers/backends
- Ajustes en imports y pruebas manuales/automatizadas

### Costos de equipo
- Tiempo de diseño y definición de convenciones
- Curva de aprendizaje para nuevos patrones internos

### Costos operativos
- Bajos en comparación con microservicios, porque se mantiene una sola aplicación y un solo despliegue

---

## Impacto esperado

- Menor dificultad para mantener módulos críticos
- Mejor separación de responsabilidades
- Reducción progresiva de deuda técnica
- Base más sólida para futuras decisiones arquitectónicas
- Mejor experiencia de desarrollo al trabajar sobre dominios más claros

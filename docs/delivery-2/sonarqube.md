# Delivery 2 — SonarQube (SonarCloud) + Quality Gates

## Objetivo
Configurar análisis estático y un Quality Gate que bloquee degradaciones de calidad.

## Configuración en el repositorio
- Archivo: `sonar-project.properties`
- Workflow: `.github/workflows/governance.yml` (job `sonar`)

## Cómo activarlo (pasos de equipo)
1. Crear proyecto en SonarCloud para el repo `Alexander-SO/Proyecto1-PDDS`.
2. Definir:
   - `sonar.projectKey`
   - `sonar.organization`
   y reemplazar los placeholders en `sonar-project.properties`.
3. Crear secret en GitHub:
   - `SONAR_TOKEN` (Settings → Secrets and variables → Actions)
4. Verificar en un PR que:
   - corre “SonarCloud Scan”
   - se reporta Quality Gate

## Quality Gate propuesto
Inicial (realista para legacy):
- Coverage mínimo: 0% (no hay tests aún), con objetivo de aumentar en entregas posteriores.
- Bloquear nueva deuda severa:
  - Bugs/Vulnerabilities/Critical issues deben ser 0 o no incrementar.
  - Maintainability Rating no debe degradar.
  - Security Hotspots revisados progresivamente.

## Nota sobre cobertura
`coverage.xml` se genera en el job `quality` y se descarga en el job `sonar` para reportarlo en SonarCloud.

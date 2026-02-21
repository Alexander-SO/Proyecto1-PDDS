# Delivery 2 — Governance & Technical Debt Audit

## 1) Governance Pipeline (CI)
Workflow: `.github/workflows/governance.yml`

Se ejecuta en:
- Pull Requests hacia `main`
- Push a `main`

Métricas generadas:
- **Code Coverage** (pytest-cov) → `coverage.xml` (artifact)
- **Cyclomatic Complexity** (radon) → `radon-report.txt` (artifact)

Artifacts:
- Se suben como `governance-reports` en GitHub Actions.

---

## 2) Quality Gates (bloqueo por degradación)
Script: `scripts/quality_gates.sh`

Gates implementados:
- Coverage: baseline inicial 0% (legacy sin tests; se documenta como deuda a mejorar)
- Cyclomatic Complexity: falla si aparece complejidad **C o peor** en `conduit/apps`

Resultado esperado:
- Un PR que viole gates → falla el workflow → bloquea merge.

---

## 3) SonarQube (SonarCloud)
Configuración:
- `sonar-project.properties`
- Documentación: `docs/delivery-2/sonarqube.md`

El job `sonar` está preparado para correr cuando exista `SONAR_TOKEN`.
Esto permite análisis estático y Quality Gate desde SonarCloud.

---

## 4) Tech Debt Audit + Hotspots + Strangler Fig
Documento: `docs/delivery-2/tech-debt-audit.md`

Incluye:
- Top 3 hotspots (por riesgo/impacto y complejidad)
- Plan incremental usando **Strangler Fig** con fases (bajo riesgo → medio → retiro legacy)

---

## 5) DORA Metrics Dashboard (4 métricas)
Documento: `docs/delivery-2/dora-dashboard.md`

Define proxies medibles en GitHub para:
- Deployment Frequency
- Lead Time for Changes
- Change Failure Rate
- MTTR

Se establece como baseline para recolección consistente en entregas futuras.

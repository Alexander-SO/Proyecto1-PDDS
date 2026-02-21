# ![Django DRF Example App](project-logo.png)

> ### Example Django DRF codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld-example-apps) API spec.

<a href="https://thinkster.io/tutorials/django-json-api" target="_blank"><img width="454" src="https://raw.githubusercontent.com/gothinkster/realworld/master/media/learn-btn-hr.png" /></a>

This repo is functionality complete — PR's and issues welcome!

## Installation

1. Clone this repository: `git clone git@github.com:gothinkster/productionready-django-api.git`.
2. `cd` into `conduit-django`: `cd productionready-django-api`.
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
5. Install Python 3.5.2: `pyenv install 3.5.2`.
6. Create a new virtualenv called `productionready`: `pyenv virtualenv 3.5.2 productionready`.
7. Set the local virtualenv to `productionready`: `pyenv local productionready`.
8. Reload the `pyenv` environment: `pyenv rehash`.

If all went well then your command line prompt should now start with `(productionready)`.

If your command line prompt does not start with `(productionready)` at this point, try running `pyenv activate productionready` or `cd ../productionready-django-api`. 

If pyenv is still not working, visit us in the Thinkster Slack channel so we can help you out.
## Delivery 1 — Discovery & Reverse Engineering

Objetivo: comprender el sistema legacy mediante ingeniería inversa y documentar su estructura funcional y técnica.

Actividades principales:

- **Onboarding Log (DevEx Audit)**  
  Documentación del proceso de instalación y ejecución del sistema legacy (Python 3.5 / Django 1.10) e identificación de friction points.

- **Context Map (DDD)**  
  Identificación de los principales Bounded Contexts del sistema:
  - Authentication & Identity
  - Articles & Content
  - Profiles & Social Graph

- **Backlog Recovery**  
  Reconstrucción de funcionalidades existentes a partir del análisis del código fuente y endpoints API.

Documento completo:

- Delivery 1 Report: [docs/Delivery_1.pdf](docs/Delivery_1.pdf)

## Delivery 2 — Governance & Technical Debt Audit

Objetivo: establecer una estrategia de calidad y gobierno técnico para el sistema legacy mediante métricas automatizadas y análisis de deuda técnica.

Actividades principales:

- **Governance Pipeline (CI)**  
  Configuración de un workflow de GitHub Actions que ejecuta análisis de calidad en Pull Requests, incluyendo métricas de cobertura de código y complejidad ciclomática.

- **Quality Gates & SonarQube**  
  Definición de Quality Gates automáticos para prevenir degradación de calidad y configuración de análisis estático mediante SonarQube/SonarCloud.

- **Tech Debt Audit (Hotspots)**  
  Identificación de los principales hotspots del sistema basada en riesgo e impacto, junto con un plan de refactorización incremental usando el patrón Strangler Fig.

- **DORA Metrics Dashboard**  
  Definición de un dashboard con las cuatro métricas DORA utilizando datos provenientes de GitHub (PRs, Actions y commits).

Documentación detallada:

- Governance summary: [docs/delivery-2/governance.md](docs/delivery-2/governance.md)
- Tech debt audit: [docs/delivery-2/tech-debt-audit.md](docs/delivery-2/tech-debt-audit.md)
- SonarQube setup: [docs/delivery-2/sonarqube.md](docs/delivery-2/sonarqube.md)
- DORA dashboard: [docs/delivery-2/dora-dashboard.md](docs/delivery-2/dora-dashboard.md)
## Delivery 2 — Governance & Technical Debt Audit
- Governance summary: [docs/delivery-2/governance.md](docs/delivery-2/governance.md)
- Tech debt audit + Strangler Fig plan: [docs/delivery-2/tech-debt-audit.md](docs/delivery-2/tech-debt-audit.md)
- SonarQube/SonarCloud setup: [docs/delivery-2/sonarqube.md](docs/delivery-2/sonarqu

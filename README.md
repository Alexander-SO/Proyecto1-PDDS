# ![Django DRF Example App](project-logo.png)

> ### Example Django DRF codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld-example-apps) API spec.

# Proyecto: Modernización y Optimización de API Django Legacy

Este proyecto consiste en la evolución de una aplicación backend legacy basada en Django, tomada del repositorio original de [https://github.com/gothinkster/django-realworld-example-app](https://github.com/gothinkster/django-realworld-example-app) como parte de una serie de ejercicios académicos enfocados en la integración de prácticas de ingeniería de software moderna.

El objetivo principal fue transformar un sistema existente mediante técnicas de:
- análisis de arquitectura (Discovery)
- gobernanza técnica (CI/CD y métricas)
- seguridad (DevSecOps)
- estrategia arquitectónica (ADR)
- optimización de rendimiento y costos (FinOps)

---

## Descripción del sistema

El sistema es una API REST construida con Django que permite gestionar:

- usuarios y autenticación
- artículos (creación, listado, favoritos)
- perfiles de usuario
- comentarios y tags

Originalmente, el sistema presentaba características típicas de un sistema legacy:

- dependencias obsoletas (Python 3.5, Django 1.x)
- bajo nivel de pruebas
- alto acoplamiento interno
- dificultades de onboarding
- problemas de rendimiento en endpoints críticos

---

## Objetivo del proyecto

Aplicar prácticas de **Staff Engineering** para:

- mejorar la mantenibilidad del sistema
- introducir gobernanza técnica
- fortalecer la seguridad
- optimizar el rendimiento
- mejorar la experiencia de desarrollo (DevEx)
- reducir el costo computacional por request (FinOps)

---

## Entregas del proyecto
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

## Delivery 3 – Security Hardening (DevSecOps)
Objetivo: Implementar mejoras de seguridad enfocadas en la **cadena de suministro de software** y en fortalecer el flujo de desarrollo seguro del proyecto.

### SBOM (Software Bill of Materials)
Se generó un SBOM del proyecto utilizando **Trivy** en formato **CycloneDX**, el cual documenta todas las dependencias utilizadas por la aplicación.

- Archivo generado: [docs/delivery-3/sbom.json](docs/delivery-3/sbom.json)
- Esto permite analizar riesgos en dependencias externas y facilita auditorías de seguridad. 

### Escaneo y remediación de vulnerabilidades
Se ejecutó un escaneo de vulnerabilidades utilizando **Trivy** sobre las dependencias del proyecto.
Resultados iniciales:
- CRITICAL: 3
- HIGH: 4
- MEDIUM: 7
- LOW: 1

Se identificaron vulnerabilidades en dependencias críticas del sistema y se aplicaron las siguientes actualizaciones:
- Django 1.10.5 → Django 1.11.27
- PyJWT 1.4.2 → PyJWT 1.5.1

Después de aplicar los cambios se ejecutó nuevamente el escaneo para verificar la remediación.
- Evidencia disponible en:
- [docs/delivery-3/trivy-before.txt](docs/delivery-3/trivy-before.txt)
- [docs/delivery-3/trivy-after.txt](docs/delivery-3/trivy-after.txt)

### Protección de secretos
Se implementó un **hook de pre-commit** utilizando `detect-secrets` para prevenir que claves API o credenciales sean accidentalmente subidas al repositorio.
Se generó un archivo baseline:
- .secrets.baseline

Durante las pruebas se introdujo un secreto ficticio y el commit fue bloqueado correctamente por el hook.

### Documentación
La documentación completa de esta fase se encuentra en:
- [docs/delivery-3/security.md](docs/delivery-3/security.md)
- [docs/delivery-3/vulnerability-remediation.md](docs/delivery-3/vulnerability-remediation.md)
- [docs/delivery-3/secrets-protection.md](docs/delivery-3/secrets-protection.md)

## Delivery 4 – Architecture Strategy & DevEx

Objetivo:Mejorar la experiencia de desarrollo (DevEx) y se definir una estrategia arquitectónica para la evolución del sistema.

### One-Command Setup

Se implementó un entorno reproducible utilizando Docker, permitiendo levantar el proyecto con un solo comando:
docker compose up --build


Esto resuelve los problemas de configuración del entorno legacy identificados en fases anteriores.

Documentación:
[docs/delivery-4/devex-setup.md](docs/delivery-4/devex-setup.md)

### ADR – Estrategia arquitectónica

Se propuso una estrategia de evolución basada en un **monolito modular**, priorizando la reducción de acoplamiento interno antes de considerar microservicios.

Documento ADR:
[docs/delivery-4/adr-001-modular-monolith.md](docs/delivery-4/adr-001-modular-monolith.md)


### Enfoque

La decisión se basa en:

- La estructura actual del proyecto
- Los hotspots identificados en fases anteriores
- El nivel actual de madurez técnica del sistema

El objetivo es reducir la deuda técnica de forma incremental y segura.

---

## Delivery 5 – FinOps Optimization

Objetivo: Optimizar el rendimiento del sistema mediante análisis y refactorización de un endpoint crítico.

### Endpoint optimizado

GET /api/articles


### Resultados

- 49% mejora en tiempo de respuesta
- 92.9% reducción en consultas SQL


### Enfoque

Se identificó un problema de tipo N+1 queries y se aplicaron optimizaciones utilizando:

- `prefetch_related`
- `annotate`
- caching a nivel de request


### Benchmark

Ver resultados completos:

[docs/delivery-5/benchmark-results.md](docs/delivery-5/benchmark-results.md)


### Impacto FinOps

La optimización reduce el costo unitario por request y mejora la capacidad de procesamiento por instancia.

---
## Ejecución del proyecto
Opción recomendada (Docker)

docker compose up --build 

Luego acceder a:

http://localhost:8000/api/tags

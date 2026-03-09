# Delivery 3 – Endurecimiento de Seguridad (DevSecOps)

## Descripción general

En esta fase se buscó mejorar la postura de seguridad de la aplicación Django legacy abordando riesgos asociados a la cadena de suministro de software. Para ello se realizaron tres actividades principales:

1. Generación de un SBOM (Software Bill of Materials)
2. Escaneo y remediación de vulnerabilidades
3. Protección de secretos mediante un hook de pre-commit

---

## Generación del SBOM

Se generó un SBOM utilizando la herramienta **Trivy** en formato estándar **CycloneDX**.

Comando utilizado:

trivy fs --format cyclonedx --output docs/delivery-3/sbom.json .

Archivo generado:
docs/delivery-3/sbom.json


Este archivo contiene un inventario completo de las dependencias utilizadas por el proyecto, permitiendo analizar riesgos de seguridad en la cadena de suministro.

---

## Enfoque de seguridad

El objetivo de esta fase no fue únicamente detectar vulnerabilidades, sino demostrar un flujo de trabajo de desarrollo seguro donde:

- las dependencias del sistema son inventariadas
- las vulnerabilidades se detectan automáticamente
- se aplican actualizaciones de seguridad controladas
- se previene la exposición accidental de secretos en el repositorio

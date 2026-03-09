# Protección de Secretos

## Objetivo

Evitar que credenciales, tokens o claves API sean accidentalmente subidas al repositorio.

---

## Intento inicial

Inicialmente se intentó implementar la protección utilizando el framework **pre-commit**, con la configuración almacenada en:

.pre-commit-config.yaml


El hook ejecuta un análisis sobre los archivos staged antes de cada commit y compara los resultados con una línea base.

---
## Configuración de línea base

Se generó un archivo de referencia:

.secrets.baseline

Comando utilizado:
detect-secrets scan > .secrets.baseline


Este archivo permite identificar únicamente secretos nuevos que puedan introducirse en el repositorio.

---

## Prueba de funcionamiento

Se introdujo un secreto ficticio para validar el mecanismo:


Intento de commit:
git commit -m "test: add dummy secret"


Resultado:

El commit fue **bloqueado por el hook**, demostrando que el mecanismo de protección funciona correctamente.

---

## Beneficio de seguridad

Este mecanismo reduce el riesgo de filtración accidental de credenciales y fortalece el flujo de desarrollo seguro del proyecto.

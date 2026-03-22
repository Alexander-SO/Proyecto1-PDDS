# One-Command Setup (DevEx)

## Objetivo

Reducir la fricción de onboarding identificada en fases anteriores, permitiendo levantar el entorno completo del proyecto con un solo comando.

---

## Problema identificado

En Delivery 1 se detectaron dificultades importantes para ejecutar el proyecto:

- Dependencia de Python 3.5 (legacy)
- Problemas de compatibilidad con OpenSSL
- Configuración manual compleja del entorno

Esto generaba una mala experiencia para nuevos desarrolladores.

---

## Solución implementada

Se creó un entorno reproducible utilizando **Docker y Docker Compose**, encapsulando todas las dependencias del sistema.

Archivos creados:
# One-Command Setup (DevEx)

## Objetivo

Reducir la fricción de onboarding identificada en fases anteriores, permitiendo levantar el entorno completo del proyecto con un solo comando.

---

## Problema identificado

En Delivery 1 se detectaron dificultades importantes para ejecutar el proyecto:

- Dependencia de Python 3.5 (legacy)
- Problemas de compatibilidad con OpenSSL
- Configuración manual compleja del entorno

Esto generaba una mala experiencia para nuevos desarrolladores.

---

## Solución implementada

Se creó un entorno reproducible utilizando **Docker y Docker Compose**, encapsulando todas las dependencias del sistema.

Archivos creados:
Dockerfile
docker-compose.yml


---

## Ejecución

El sistema puede levantarse con un solo comando:

---

docker compose up --build


Este comando:

1. Construye la imagen del proyecto
2. Instala dependencias automáticamente
3. Ejecuta migraciones de base de datos
4. Inicia el servidor en el puerto 8000

---

## Validación
Se verificó el correcto funcionamiento accediendo al endpoint:
GET /api/tags/

Respuesta obtenida:
HTTP 200 OK
{"tags":[]}


---

## Impacto en la experiencia de desarrollo (DevEx)

- Elimina la necesidad de configurar Python 3.5 manualmente
- Reduce errores de entorno ("works on my machine")
- Disminuye el tiempo de onboarding
- Permite levantar el sistema en menos de 5 minutos

---

## Conclusión

La implementación de Docker Compose resuelve el principal problema de onboarding identificado, mejorando significativamente la experiencia de desarrollo del proyecto.

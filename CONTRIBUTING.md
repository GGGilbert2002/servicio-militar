# Guía de Contribución – Proyecto Servicio Militar Coro

Gracias por contribuir. Sigue estas reglas estrictas para mantener el orden y la calidad.

##  Estructura de ramas (GitFlow simplificado)

- `main` – Rama de producción. **Protegida**. Solo se reciben merges desde `develop` o `hotfix/*` mediante Pull Request con aprobación.
- `develop` – Rama de integración continua. Base para las funcionalidades nuevas.
- `feature/*` – Para nuevas características. **Siempre** desde `develop`. Ejemplo: `feature/dashboard-estadisticas`
- `hotfix/*` – Para correcciones urgentes en producción. Desde `main`. Ejemplo: `hotfix/error-bd`
- `release/*` – Preparación de versiones (opcional). Desde `develop` hacia `main`.

##  Nombramiento de ramas

Formato: `tipo/descripcion-corta-en-minusculas-con-guiones`

- **Tipos permitidos**: `feature`, `hotfix`, `release`, `docs`, `chore`
- **Descripción corta**: máximo 4 palabras, sin números de incidencia.

Ejemplos válidos:
- `feature/registro-reclutas`
- `hotfix/correcion-parroquias`
- `docs/actualizar-readme`

##  Estándar de commits – Conventional Commits

Todos los mensajes de commit deben seguir este formato:

# Innovatech Backend

Microservicio HTTP desarrollado en Python para Innovatech Chile.
Desplegado en AWS EC2 mediante contenedores Docker con pipeline CI/CD.

## Tecnologías
- Python 3.11
- Docker (multi-stage build)
- GitHub Actions (CI/CD)
- AWS EC2

## Requisitos
- Docker
- Docker Compose

## Cómo ejecutar localmente

```bash
docker compose up --build
```

El servicio queda disponible en `http://localhost:3000`

## Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| /status  | GET    | Estado del backend |

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| PORT     | Puerto del servidor (default: 3000) |

## Pipeline CI/CD

El pipeline se activa con push a la rama `deploy` y realiza:
1. Build de la imagen Docker
2. Push a Docker Hub
3. Deploy automático en EC2

## Persistencia

Se utiliza named volume `backend_data` para persistir datos
aunque el contenedor se reinicie.

## Arquitectura

- EC2-Backend: subred privada 10.0.2.0/24
- Solo accesible desde EC2-Frontend
- Puerto 3000 habilitado en backend-sg
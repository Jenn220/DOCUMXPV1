## Crear Repositorio

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/repositories/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "R001",
  "port": 9562,
  "username": "admin",
  "password": "admin123",
  "databaseName": "mxp-dev",
  "authType": "Bearer"
}
```

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": "21",
  "messages": [],
  "data": {
    "id": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
    "code": "R001",
    "port": 9562,
    "username": "admin",
    "password": "admin123",
    "databaseName": "mxp-dev",
    "authTypeId": "Bearer",
    "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                      |
| ------------------- | ------------------------------------------------ |
| `code`              | Código de respuesta interno ("21" = éxito)       |
| `messages`          | Array de mensajes informativos                   |
| `data`              | Objeto con la información del repositorio creado |
| `data.id`           | ID único generado para el repositorio            |
| `data.code`         | Código del repositorio                           |
| `data.port`         | Puerto del repositorio                           |
| `data.username`     | Nombre de usuario                                |
| `data.password`     | Contraseña                                       |
| `data.databaseName` | Nombre de la base de datos                       |
| `data.authTypeId`   | Tipo de autenticación                            |
| `data.statusId`     | ID del estado del repositorio                    |

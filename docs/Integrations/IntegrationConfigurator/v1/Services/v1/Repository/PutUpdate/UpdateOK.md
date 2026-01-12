## Actualizar Repositorio

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/repositories/update
```

### Parámetros de Query

| Key  | Value                                  | Description                           |
| ---- | -------------------------------------- | ------------------------------------- |
| `id` | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID único del repositorio a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "code": "R001",
  "port": 9562,
  "username": "admin",
  "password": "admin123",
  "databaseName": "mxp-dev",
  "authType": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

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
    "authTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                           |
| ------------------- | ----------------------------------------------------- |
| `code`              | Código de respuesta interno ("21" = éxito)            |
| `messages`          | Array de mensajes informativos                        |
| `data`              | Objeto con la información actualizada del repositorio |
| `data.id`           | ID único del repositorio                              |
| `data.code`         | Código del repositorio                                |
| `data.port`         | Puerto del repositorio                                |
| `data.username`     | Nombre de usuario                                     |
| `data.password`     | Contraseña                                            |
| `data.databaseName` | Nombre de la base de datos                            |
| `data.authTypeId`   | ID del tipo de autenticación                          |
| `data.statusId`     | ID del estado del repositorio                         |

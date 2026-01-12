## Obtener Repositorio por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/repositories/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                          |
| ---- | -------------------------------------- | ------------------------------------ |
| `id` | `6bd36e91-c0de-4b6d-87b8-5dea7f2c2274` | ID único del repositorio a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
    "code": "R001",
    "port": 9562,
    "username": "admin",
    "password": "admin123",
    "databaseName": "mxp-dev",
    "authTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "url": "https://apim-hera.azure-api.net/mxpi-init-prepro1",
    "repositoryDescription": "Repostirorio para mxp legacy"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                        | Descripción                               |
| ---------------------------- | ----------------------------------------- |
| `code`                       | Código de respuesta interno (20 = éxito)  |
| `messages`                   | Array de mensajes informativos            |
| `data`                       | Objeto con la información del repositorio |
| `data.id`                    | ID único del repositorio                  |
| `data.code`                  | Código del repositorio                    |
| `data.port`                  | Puerto del repositorio                    |
| `data.username`              | Nombre de usuario                         |
| `data.password`              | Contraseña                                |
| `data.databaseName`          | Nombre de la base de datos                |
| `data.authTypeId`            | ID del tipo de autenticación              |
| `data.statusId`              | ID del estado del repositorio             |
| `data.url`                   | URL del repositorio                       |
| `data.repositoryDescription` | Descripción del repositorio               |

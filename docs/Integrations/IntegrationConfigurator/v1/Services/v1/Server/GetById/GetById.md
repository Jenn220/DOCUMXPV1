## Obtener Servidor por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/servers/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                       |
| ---- | -------------------------------------- | --------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID único del servidor a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "123456",
    "code": "S001",
    "name": "mysql",
    "typeServerId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
    "url": "https://server.com",
    "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                              |
| ------------------- | ---------------------------------------- |
| `code`              | Código de respuesta interno (20 = éxito) |
| `messages`          | Array de mensajes informativos           |
| `data`              | Objeto con la información del servidor   |
| `data.id`           | ID único del servidor                    |
| `data.code`         | Código del servidor                      |
| `data.name`         | Nombre del servidor                      |
| `data.typeServerId` | ID del tipo de servidor                  |
| `data.url`          | URL del servidor                         |
| `data.statusId`     | ID del estado del servidor               |

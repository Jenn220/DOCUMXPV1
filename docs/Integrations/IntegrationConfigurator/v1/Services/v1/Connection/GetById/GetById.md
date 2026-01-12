## Obtener Conexión por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/connections/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                         |
| ---- | -------------------------------------- | ----------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID único de la conexión a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "712feaea-8228-4f03-9457-3ce36e618c56",
    "code": "C001",
    "serverId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
    "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
    "adapterId": "6f5672e8-32fc-4195-b1f0-326f9e2ac82f",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Conexión database maxpoint legacy",
    "description": "alguna descripción"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                              |
| ------------------- | ---------------------------------------- |
| `code`              | Código de respuesta interno (20 = éxito) |
| `messages`          | Array de mensajes informativos           |
| `data`              | Objeto con la información de la conexión |
| `data.id`           | ID único de la conexión                  |
| `data.code`         | Código de la conexión                    |
| `data.serverId`     | ID del servidor                          |
| `data.repositoryId` | ID del repositorio                       |
| `data.adapterId`    | ID del adaptador                         |
| `data.statusId`     | ID del estado de la conexión             |
| `data.name`         | Nombre de la conexión                    |
| `data.description`  | Descripción de la conexión               |

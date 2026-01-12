## Obtener Conexión por Código

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/connections/getByCode
```

### Parámetros de Query

| Key    | Value  | Description                       |
| ------ | ------ | --------------------------------- |
| `code` | `C001` | Código de la conexión a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
    "code": "C001",
    "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
    "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
    "adapterId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
    "name": "Conexión database maxpoint legacy",
    "description": "alguna desc.",
    "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
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
| `data.name`         | Nombre de la conexión                    |
| `data.description`  | Descripción de la conexión               |
| `data.statusId`     | ID del estado de la conexión             |

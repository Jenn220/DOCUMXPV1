## Crear Conexión

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/connections/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "C001",
  "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
  "adapterId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e2",
  "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e3",
  "description": "alguna desc.",
  "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
}
```

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
  "data": {
    "id": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3",
    "code": "C001",
    "serverId": "a4d9ba2b-7b84-47bf-b298-033ffd446729",
    "adapterId": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c08",
    "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
    "name": "Conexión database maxpoint legacy",
    "description": "alguna desc.",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                     |
| ------------------- | ----------------------------------------------- |
| `code`              | Código de respuesta interno (10 = éxito)        |
| `messages`          | Array de mensajes informativos                  |
| `data`              | Objeto con la información de la conexión creada |
| `data.id`           | ID único generado para la conexión              |
| `data.code`         | Código de la conexión                           |
| `data.serverId`     | ID del servidor                                 |
| `data.adapterId`    | ID del adaptador                                |
| `data.repositoryId` | ID del repositorio                              |
| `data.name`         | Nombre de la conexión                           |
| `data.description`  | Descripción de la conexión                      |
| `data.statusId`     | ID del estado de la conexión                    |

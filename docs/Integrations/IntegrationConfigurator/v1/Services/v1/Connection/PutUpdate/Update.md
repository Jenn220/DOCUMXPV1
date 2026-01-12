## Actualizar Conexión

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/connections/update
```

### Parámetros de Query

| Key  | Value    | Description                          |
| ---- | -------- | ------------------------------------ |
| `id` | `123456` | ID único de la conexión a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
  "adapterId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e2",
  "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e3",
  "description": "alguna desc.",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

```json
{
  "code": 11,
  "messages": ["upated succesfully"],
  "data": {
    "id": "712feaea-8228-4f03-9457-3ce36e618c56",
    "code": "C001",
    "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
    "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e3",
    "adapterId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e2",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Conexión database maxpoint legacy",
    "description": "alguna desc."
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                          |
| ------------------- | ---------------------------------------------------- |
| `code`              | Código de respuesta interno (11 = éxito)             |
| `messages`          | Array de mensajes informativos                       |
| `data`              | Objeto con la información actualizada de la conexión |
| `data.id`           | ID único de la conexión                              |
| `data.code`         | Código de la conexión                                |
| `data.serverId`     | ID del servidor                                      |
| `data.repositoryId` | ID del repositorio                                   |
| `data.adapterId`    | ID del adaptador                                     |
| `data.statusId`     | ID del estado de la conexión                         |
| `data.name`         | Nombre de la conexión                                |
| `data.description`  | Descripción de la conexión                           |

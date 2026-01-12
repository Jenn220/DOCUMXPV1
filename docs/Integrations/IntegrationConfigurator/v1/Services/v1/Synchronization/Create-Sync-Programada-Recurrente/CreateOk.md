## Crear Sincronización

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/create
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "Sincronizacion de Menu v3",
  "franchiseId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "hourToExecute": "2024-05-22T20:20:01",
  "integrations": [
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    },
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo               | Tipo   | Requerido | Descripción                                    |
| ------------------- | ------ | --------- | ---------------------------------------------- |
| `name`              | string | Sí        | Nombre de la sincronización (máx: 100)         |
| `franchiseId`       | string | No        | ID de la franquicia (máx: 255)                 |
| `userId`            | string | Sí        | ID del usuario (máx: 255)                      |
| `hourToExecute`     | string | No        | Fecha y hora programada de ejecución (máx: 50) |
| `integrations`      | array  | Sí        | Lista de integraciones (mínimo 1 elemento)     |
| `integrations[].id` | string | Sí        | ID de la integración (máx: 100)                |

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
  "data": {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "name": "Sincornizacion de Menu v3",
    "status": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "observations": "",
    "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "hourToExecute": "2024-05-22T04:37:24.617Z",
    "integrations": [
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "order": 1
      },
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "order": 2
      }
    ],
    "franchiseId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                       | Descripción                               |
| --------------------------- | ----------------------------------------- |
| `code`                      | Código de respuesta interno (10 = creado) |
| `messages`                  | Array con mensajes del resultado          |
| `data`                      | Objeto con los datos de la sincronización |
| `data.id`                   | ID único de la sincronización creada      |
| `data.name`                 | Nombre de la sincronización               |
| `data.status`               | ID del estado de la sincronización        |
| `data.observations`         | Observaciones de la sincronización        |
| `data.userId`               | ID del usuario que creó la sincronización |
| `data.hourToExecute`        | Fecha y hora programada de ejecución      |
| `data.integrations`         | Array con las integraciones asociadas     |
| `data.integrations[].id`    | ID de la integración                      |
| `data.integrations[].order` | Orden de ejecución de la integración      |
| `data.franchiseId`          | ID de la franquicia asociada              |

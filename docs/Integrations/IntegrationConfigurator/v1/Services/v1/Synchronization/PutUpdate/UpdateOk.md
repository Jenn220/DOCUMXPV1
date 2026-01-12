## Actualizar Sincronización (Parcial)

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/update
```

### Parámetros de Query

| Key  | Value                                  | Description                          |
| ---- | -------------------------------------- | ------------------------------------ |
| `id` | `7654cb16-e955-4605-8579-b891a67f94c7` | ID de la sincronización a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchiseId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "status": "A",
  "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
  "userId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "hourToExecute": ""
}
```

### Descripción del Cuerpo de la Solicitud

| Campo           | Tipo   | Requerido | Descripción                                    |
| --------------- | ------ | --------- | ---------------------------------------------- |
| `franchiseId`   | string | No        | ID de la franquicia (máx: 255)                 |
| `status`        | string | No        | Estado de la sincronización (mín: 1, máx: 1)   |
| `observations`  | string | No        | Observaciones (máx: 300)                       |
| `userId`        | string | No        | ID del usuario (máx: 255)                      |
| `hourToExecute` | string | No        | Fecha y hora programada de ejecución (máx: 50) |

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

```json
{
  "code": 10,
  "messages": ["upated succesfully"],
  "data": {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "name": "Sincornizacion de Menu v3",
    "status": "f316a140-f62e-493e-b00e-7fbc19d9bbb5",
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
| `code`                      | Código de respuesta interno (10 = éxito)  |
| `messages`                  | Array con mensajes del resultado          |
| `data`                      | Objeto con los datos de la sincronización |
| `data.id`                   | ID único de la sincronización             |
| `data.name`                 | Nombre de la sincronización               |
| `data.status`               | ID del estado de la sincronización        |
| `data.observations`         | Observaciones de la sincronización        |
| `data.userId`               | ID del usuario asociado                   |
| `data.hourToExecute`        | Fecha y hora programada de ejecución      |
| `data.integrations`         | Array con las integraciones asociadas     |
| `data.integrations[].id`    | ID de la integración                      |
| `data.integrations[].order` | Orden de ejecución de la integración      |
| `data.franchiseId`          | ID de la franquicia asociada              |

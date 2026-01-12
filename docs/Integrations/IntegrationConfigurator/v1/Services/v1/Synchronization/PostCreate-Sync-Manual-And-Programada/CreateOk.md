## Crear Sincronización

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/create
```

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

### Descripción de Campos

| Campo               | Tipo   | Restricciones                                       | Descripción                      |
| ------------------- | ------ | --------------------------------------------------- | -------------------------------- |
| `name`              | string | Máximo: 100 caracteres, **Obligatorio**             | Nombre de la sincronización      |
| `franchiseId`       | string | Máximo: 255 caracteres, Opcional                    | ID de la franquicia              |
| `userId`            | string | Máximo: 255 caracteres, **Obligatorio**             | ID del usuario                   |
| `hourToExecute`     | string | Máximo: 50 caracteres, null cuando no es programado | Hora de ejecución programada     |
| `integrations`      | array  | Mínimo: 1 elemento                                  | Lista de integraciones asociadas |
| `integrations[].id` | string | Máximo: 100 caracteres                              | ID de cada integración           |

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

| Campo                | Descripción                                           |
| -------------------- | ----------------------------------------------------- |
| `code`               | Código de respuesta interno (10 = éxito)              |
| `messages`           | Array de mensajes informativos                        |
| `data`               | Objeto con la información de la sincronización creada |
| `data.id`            | ID único generado para la sincronización              |
| `data.name`          | Nombre de la sincronización                           |
| `data.status`        | Estado de la sincronización                           |
| `data.observations`  | Observaciones                                         |
| `data.userId`        | ID del usuario                                        |
| `data.hourToExecute` | Hora de ejecución programada                          |
| `data.integrations`  | Array de integraciones con orden asignado             |
| `data.franchiseId`   | ID de la franquicia                                   |

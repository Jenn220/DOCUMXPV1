## Actualizar Drive-Thru por ID

### Método HTTP

`PUT`

### URL

```
{{server_internalClients}}/api/v1/drivethru/update_drivethru_by_id
```

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "00000000-0000-0000-0000-000000000000",
  "name": "Drive Thru 1",
  "order_id": "1",
  "status": {
    "id": "00000000-0000-0000-0000-000000000000",
    "status_name": "Active",
    "description": "Active status",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                | Tipo   | Descripción                                            |
| -------------------- | ------ | ------------------------------------------------------ |
| `id`                 | string | Identificador del drive-thru                           |
| `name`               | string | Nombre del drive-thru                                  |
| `order_id`           | string | Identificador de orden                                 |
| `status`             | object | Estado del drive-thru                                  |
| `status.id`          | string | Identificador del estado                               |
| `status.status_name` | string | Nombre del estado                                      |
| `status.description` | string | Descripción del estado                                 |
| `status.created_at`  | string | Fecha y hora de creación del estado (formato ISO)      |
| `status.updated_at`  | string | Fecha y hora de actualización del estado (formato ISO) |

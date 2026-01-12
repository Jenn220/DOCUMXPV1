## Procesar Lote de Órdenes

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/order/batch_orders_batch
```

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "requests": [
    {
      "order_id": "ORDER-12345",
      "ui_reference_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "ui_started_at": "2024-12-08T10:00:00Z",
      "ui_finished_at": "2024-12-08T10:30:00Z",
      "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "cdn_name": "CDN Ecuador",
      "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
      "restaurant_name": "KFC Quito Centro",
      "cash_register_subscription": "8028a2ff-c639-6df4-68e8-8982c0256be3",
      "cash_register_subscription_name": "Caja 001",
      "user_seller_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "user_seller_name": "Juan Perez",
      "status_order_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "totals": {
        "result": {
          "subtotal": 15.5,
          "total": 16.5
        }
      },
      "payments": [],
      "items": [],
      "channel": {
        "_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
        "name": "POS"
      },
      "events": []
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                        | Tipo   | Descripción                                          |
| -------------------------------------------- | ------ | ---------------------------------------------------- |
| `requests`                                   | array  | Lista de órdenes a procesar en lote                  |
| `requests[].order_id`                        | string | Identificador único de la orden                      |
| `requests[].ui_reference_uuid`               | string | UUID de referencia de la interfaz de usuario         |
| `requests[].ui_started_at`                   | string | Fecha y hora de inicio en la UI (formato ISO)        |
| `requests[].ui_finished_at`                  | string | Fecha y hora de finalización en la UI (formato ISO)  |
| `requests[].cdn_id`                          | string | Identificador de la cadena                           |
| `requests[].cdn_name`                        | string | Nombre de la cadena                                  |
| `requests[].restaurant_id`                   | string | Identificador del restaurante                        |
| `requests[].restaurant_name`                 | string | Nombre del restaurante                               |
| `requests[].cash_register_subscription`      | string | Identificador de la suscripción de caja registradora |
| `requests[].cash_register_subscription_name` | string | Nombre de la caja registradora                       |
| `requests[].user_seller_id`                  | string | Identificador del usuario vendedor                   |
| `requests[].user_seller_name`                | string | Nombre del usuario vendedor                          |
| `requests[].status_order_id`                 | string | Identificador del estado de la orden                 |
| `requests[].totals`                          | object | Totales de la orden                                  |
| `requests[].totals.result`                   | object | Resultado de totales                                 |
| `requests[].totals.result.subtotal`          | number | Subtotal de la orden                                 |
| `requests[].totals.result.total`             | number | Total de la orden                                    |
| `requests[].payments`                        | array  | Lista de pagos                                       |
| `requests[].items`                           | array  | Lista de items de la orden                           |
| `requests[].channel`                         | object | Canal de venta                                       |
| `requests[].channel._id`                     | string | Identificador del canal                              |
| `requests[].channel.name`                    | string | Nombre del canal                                     |
| `requests[].events`                          | array  | Lista de eventos                                     |

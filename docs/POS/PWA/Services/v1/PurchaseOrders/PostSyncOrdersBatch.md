## Sincronizar Órdenes por Lotes

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/purchaseorders/api/v1/order/sync_orders_batch
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "requests": [
    {
      "order_id": "902499bf-284f-4f2e-80b7-60ef60c6bd9c",
      "franchise_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
      "order_status": "COMPLETED"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                      | Tipo   | Descripción                            |
| -------------------------- | ------ | -------------------------------------- |
| `requests`                 | array  | Lista de solicitudes de sincronización |
| `requests[].order_id`      | string | Identificador único de la orden        |
| `requests[].franchise_id`  | string | Identificador de la franquicia         |
| `requests[].restaurant_id` | string | Identificador del restaurante          |
| `requests[].order_status`  | string | Estado de la orden                     |

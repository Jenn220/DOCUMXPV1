## Remover Pagos por ID de Orden

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/purchaseorders/api/v1/order/remove_payments_by_order_id
```

### Headers

| Key          | Value            | Descripción                       |
| ------------ | ---------------- | --------------------------------- |
| Content-Type | application/json | Tipo de contenido de la solicitud |
| show_modal   | true             | Indicador para mostrar modal      |

### Parámetros de Query

| Key                | Value                                | Descripción                           |
| ------------------ | ------------------------------------ | ------------------------------------- |
| order_id           | 902499bf-284f-4f2e-80b7-60ef60c6bd9c | Identificador de la orden             |
| cash_register      | aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0 | Identificador de la caja registradora |
| cash_register_name | Caja 2                               | Nombre de la caja registradora        |
| user_seller_name   | Juan Perez                           | Nombre del usuario vendedor           |
| user_seller        | c17b6e8d-88a5-9eb5-1f44-aeec161494da | Identificador del usuario vendedor    |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "payment_id": ["payment-uuid-1", "payment-uuid-2"],
  "events": [
    {
      "event_type": "PAYMENT_REMOVED",
      "timestamp": "2025-12-08T10:00:00Z"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                 | Tipo   | Descripción                                 |
| --------------------- | ------ | ------------------------------------------- |
| `payment_id`          | array  | Lista de identificadores de pagos a remover |
| `events`              | array  | Lista de eventos relacionados               |
| `events[].event_type` | string | Tipo de evento                              |
| `events[].timestamp`  | string | Fecha y hora del evento (formato ISO)       |

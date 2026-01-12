## Eliminar Pagos por ID de Orden

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/order/remove_payments_by_order_id
```

### Parámetros de Query

| Key                | Value                                | Descripción                           |
| ------------------ | ------------------------------------ | ------------------------------------- |
| order_id           | 902499bf-284f-4f2e-80b7-60ef60c6bd9c | Identificador de la orden             |
| cash_register      | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador de la caja registradora |
| cash_register_name | Caja 2                               | Nombre de la caja registradora        |
| user_seller_name   | Juan Perez                           | Nombre del usuario vendedor           |
| user_seller        | 3fa85f64-5717-4562-b3fc-2c963f66afa6 | Identificador del usuario vendedor    |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "payment_id": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
  "events": []
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo  | Descripción                                  |
| ------------ | ----- | -------------------------------------------- |
| `payment_id` | array | Lista de identificadores de pagos a eliminar |
| `events`     | array | Lista de eventos                             |

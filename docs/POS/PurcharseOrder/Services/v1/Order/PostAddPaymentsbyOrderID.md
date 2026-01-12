## Agregar Pagos por ID de Orden

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/order/add_payments_by_order_id
```

### Parámetros de Query

| Key                | Value                                | Descripción                           |
| ------------------ | ------------------------------------ | ------------------------------------- |
| order_id           | 902499bf-284f-4f2e-80b7-60ef60c6bd9c | Identificador de la orden             |
| cash_register      | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador de la caja registradora |
| cash_register_name | Caja 001                             | Nombre de la caja registradora        |
| user_seller_name   | Juan Perez                           | Nombre del usuario vendedor           |
| user_seller        | 3fa85f64-5717-4562-b3fc-2c963f66afa6 | Identificador del usuario vendedor    |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "payment_method_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "payment_method_name": "Tarjeta de Crédito",
  "amount": 25.75,
  "meta_data": {
    "external_reference": "TRX-98765"
  },
  "events": []
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                          | Tipo   | Descripción                          |
| ------------------------------ | ------ | ------------------------------------ |
| `id`                           | string | Identificador del pago               |
| `payment_method_id`            | string | Identificador del método de pago     |
| `payment_method_name`          | string | Nombre del método de pago            |
| `amount`                       | number | Monto del pago                       |
| `meta_data`                    | object | Metadatos del pago                   |
| `meta_data.external_reference` | string | Referencia externa de la transacción |
| `events`                       | array  | Lista de eventos                     |

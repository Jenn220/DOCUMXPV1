## Agregar Pagos por ID de Orden

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/purchaseorders/api/v1/order/add_payments_by_order_id
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
| user_seller        | c17b6e8d-88a5-9eb5-1f44-aeec161494da | Identificador del usuario vendedor    |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "payment_method_id": "568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d",
  "payment_type": "CASH",
  "amount": 25.5,
  "currency": "USD",
  "transaction_id": "TXN123456789"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo               | Tipo   | Descripción                      |
| ------------------- | ------ | -------------------------------- |
| `payment_method_id` | string | Identificador del método de pago |
| `payment_type`      | string | Tipo de pago                     |
| `amount`            | number | Monto del pago                   |
| `currency`          | string | Moneda del pago                  |
| `transaction_id`    | string | Identificador de la transacción  |

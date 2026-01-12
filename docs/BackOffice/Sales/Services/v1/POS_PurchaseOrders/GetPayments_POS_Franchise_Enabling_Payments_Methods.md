## Obtener Resumen de Ventas

### Método HTTP

`GET`

### URL

```
{{server-bo}}/api/v1/sales/summary
```

### Parámetros de Query

| Key             | Value                                  | Description        |
| --------------- | -------------------------------------- | ------------------ |
| `cdn_id`        | `bc2d88ba-da1e-4db7-55fe-32d1205ac4af` | ID de la cadena    |
| `restaurant_id` | `24260579-fadf-7b3f-aac7-5e16faff96d1` | ID del restaurante |
| `period_id`     | `26617b88-3c44-4c0b-87d7-616ec6339ffd` | ID del período     |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Data returned succesfully",
  "data": {
    "_id": "736df2ee-d615-4869-969f-10f4ecf465a1",
    "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
    "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
    "period_id": "ce066034-90a6-4110-929e-9f739cef7396",
    "summary": {
      "total_transactions": 50,
      "average_ticket": 6.86,
      "invoice_count": 50,
      "invoice_total": 342.73,
      "credit_note_count": 1,
      "credit_note_total": 0.5,
      "pending_order_count": 0,
      "pending_order_total": 0,
      "surplus_missing": 0,
      "cashier_total": 1,
      "coupons_total": 0,
      "coupons_count": 0
    }
  }
}
```

#### Descripción de la Respuesta Exitosa

| Campo                              | Description                       |
| ---------------------------------- | --------------------------------- |
| `code`                             | Código de respuesta (200 = éxito) |
| `description`                      | Descripción del resultado         |
| `data`                             | Objeto con los datos del resumen  |
| `data._id`                         | ID único del resumen              |
| `data.cdn_id`                      | ID de la cadena                   |
| `data.restaurant_id`               | ID del restaurante                |
| `data.period_id`                   | ID del período                    |
| `data.summary`                     | Objeto con el resumen de ventas   |
| `data.summary.total_transactions`  | Total de transacciones            |
| `data.summary.average_ticket`      | Ticket promedio                   |
| `data.summary.invoice_count`       | Cantidad de facturas              |
| `data.summary.invoice_total`       | Total de facturas                 |
| `data.summary.credit_note_count`   | Cantidad de notas de crédito      |
| `data.summary.credit_note_total`   | Total de notas de crédito         |
| `data.summary.pending_order_count` | Cantidad de órdenes pendientes    |
| `data.summary.pending_order_total` | Total de órdenes pendientes       |
| `data.summary.surplus_missing`     | Sobrante o faltante               |
| `data.summary.cashier_total`       | Total de cajeros                  |
| `data.summary.coupons_total`       | Total de cupones                  |
| `data.summary.coupons_count`       | Cantidad de cupones               |

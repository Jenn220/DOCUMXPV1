## Sincronización por Lotes de Resumen de Conciliación

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/conciliation/batch_conciliation_summary_sync
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "summary_restaurants": [
    {
      "_id_summary_restaurant": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
      "period_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "data_conciliation": {
        "payment_methods": [],
        "totals": {
          "total_income": 1000.5,
          "total_egress": 100.0,
          "total_withdrawn": 50.0,
          "total_transactions": 850.5,
          "total_pos_calculated": 850.5,
          "total_difference": 0.0,
          "total_declaredvalue": 850.5
        },
        "excess_and_missing_comment": null
      },
      "data_summary_restaurant": {
        "total_transactions": 10,
        "average_ticket": 85.05,
        "invoice_count": 8,
        "invoice_total": 800.0,
        "credit_note_count": 2,
        "credit_note_total": 50.5,
        "pending_order_count": 0,
        "pending_order_total": 0.0,
        "surplus_missing": 0.0,
        "cashier_total": 850.5
      },
      "restaurant_summary_completed": true,
      "restaurant_summary_at": "2024-12-08T10:30:00Z",
      "created_user": "user-id",
      "updated_user": "user-id",
      "created_at": "2024-12-08T10:00:00Z",
      "updated_at": "2024-12-08T10:30:00Z"
    }
  ],
  "conciliations_cash_registers": [],
  "events": []
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                 | Tipo    | Descripción                                            |
| --------------------------------------------------------------------- | ------- | ------------------------------------------------------ |
| `summary_restaurants`                                                 | array   | Lista de resúmenes de restaurantes                     |
| `summary_restaurants[]._id_summary_restaurant`                        | string  | Identificador único del resumen del restaurante        |
| `summary_restaurants[].cdn_id`                                        | string  | Identificador de la cadena                             |
| `summary_restaurants[].restaurant_id`                                 | string  | Identificador del restaurante                          |
| `summary_restaurants[].period_id`                                     | string  | Identificador del período                              |
| `summary_restaurants[].data_conciliation`                             | object  | Datos de conciliación                                  |
| `summary_restaurants[].data_conciliation.payment_methods`             | array   | Lista de métodos de pago                               |
| `summary_restaurants[].data_conciliation.totals`                      | object  | Totales de conciliación                                |
| `summary_restaurants[].data_conciliation.totals.total_income`         | number  | Total de ingresos                                      |
| `summary_restaurants[].data_conciliation.totals.total_egress`         | number  | Total de egresos                                       |
| `summary_restaurants[].data_conciliation.totals.total_withdrawn`      | number  | Total retirado                                         |
| `summary_restaurants[].data_conciliation.totals.total_transactions`   | number  | Total de transacciones                                 |
| `summary_restaurants[].data_conciliation.totals.total_pos_calculated` | number  | Total calculado por POS                                |
| `summary_restaurants[].data_conciliation.totals.total_difference`     | number  | Diferencia total                                       |
| `summary_restaurants[].data_conciliation.totals.total_declaredvalue`  | number  | Valor total declarado                                  |
| `summary_restaurants[].data_conciliation.excess_and_missing_comment`  | null    | Comentario sobre excesos y faltantes                   |
| `summary_restaurants[].data_summary_restaurant`                       | object  | Datos del resumen del restaurante                      |
| `summary_restaurants[].data_summary_restaurant.total_transactions`    | number  | Total de transacciones                                 |
| `summary_restaurants[].data_summary_restaurant.average_ticket`        | number  | Ticket promedio                                        |
| `summary_restaurants[].data_summary_restaurant.invoice_count`         | number  | Cantidad de facturas                                   |
| `summary_restaurants[].data_summary_restaurant.invoice_total`         | number  | Total de facturas                                      |
| `summary_restaurants[].data_summary_restaurant.credit_note_count`     | number  | Cantidad de notas de crédito                           |
| `summary_restaurants[].data_summary_restaurant.credit_note_total`     | number  | Total de notas de crédito                              |
| `summary_restaurants[].data_summary_restaurant.pending_order_count`   | number  | Cantidad de órdenes pendientes                         |
| `summary_restaurants[].data_summary_restaurant.pending_order_total`   | number  | Total de órdenes pendientes                            |
| `summary_restaurants[].data_summary_restaurant.surplus_missing`       | number  | Sobrante o faltante                                    |
| `summary_restaurants[].data_summary_restaurant.cashier_total`         | number  | Total de caja                                          |
| `summary_restaurants[].restaurant_summary_completed`                  | boolean | Indica si el resumen del restaurante está completado   |
| `summary_restaurants[].restaurant_summary_at`                         | string  | Fecha y hora del resumen del restaurante (formato ISO) |
| `summary_restaurants[].created_user`                                  | string  | Usuario que creó el registro                           |
| `summary_restaurants[].updated_user`                                  | string  | Usuario que actualizó el registro                      |
| `summary_restaurants[].created_at`                                    | string  | Fecha y hora de creación (formato ISO)                 |
| `summary_restaurants[].updated_at`                                    | string  | Fecha y hora de última actualización (formato ISO)     |
| `conciliations_cash_registers`                                        | array   | Lista de conciliaciones de cajas registradoras         |
| `events`                                                              | array   | Lista de eventos                                       |

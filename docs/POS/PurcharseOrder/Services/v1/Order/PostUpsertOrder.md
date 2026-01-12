## Crear o Actualizar Orden

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/order/upsert_order?franchise=bc2d8ada-e25e-1bb7-55fe-32d1205ac4af&restaurant=24260579-faf8-763f-aac7-5e16faff96d1
```

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "order_id": "902499bf-284f-4f2e-80b7-60ef60c6bd9c",
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
  "status_order_description": "Completado",
  "user_sesion": {
    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "user_name": "Juan Perez"
  },
  "conciliation_id": null,
  "status_order_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "totals": {
    "result_presentation": {
      "taxes": [],
      "subtotal_taxes": [],
      "subtotal": 15.5,
      "subtotal_without_taxes": 13.84,
      "total_discount": 0.0,
      "tip": 1.0,
      "total": 16.5
    },
    "result": {
      "taxes": [],
      "subtotal_taxes": [],
      "subtotal": 15.5,
      "subtotal_without_taxes": 13.84,
      "total_discount": 0.0,
      "tip": 1.0,
      "total": 16.5
    },
    "result_per_plu": []
  },
  "payments": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "payment_method_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "payment_method_name": "Efectivo",
      "amount": 16.5,
      "event_id": null,
      "event_code": null,
      "meta_data": {
        "external_reference": "REF-12345",
        "method_name": "Efectivo",
        "data_transaction": null,
        "normalizedTransaction": null
      },
      "cash_register": "8028a2ff-c639-6df4-68e8-8982c0256be3",
      "cash_register_name": "Caja 001",
      "user_seller_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "user_seller_name": "Juan Perez",
      "created_at": "2024-12-08T10:30:00Z"
    }
  ],
  "items": [
    {
      "menu_id": "9bdeeb7f-136c-8f6a-489b-d9fc02db904a",
      "menu_description": "Combo Familiar",
      "category_id_plu": "9bdeeb7f-136c-8f6a-489b-d9fc02db904a",
      "category_description_plu": "Combos",
      "classification_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "classification_description": "Producto Principal",
      "plu_parent_id": null,
      "plu_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "plu_name": "Combo Familiar 8 piezas",
      "plu_description": "Combo familiar con 8 piezas de pollo",
      "plu_pvp": 15.5,
      "plu_quantity": 1,
      "plu_customization": [],
      "subsidy": null
    }
  ],
  "channel": {
    "_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
    "name": "POS"
  },
  "document_type": {
    "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Factura"
  },
  "invoice": null,
  "credit_note": null,
  "driveThru": null,
  "pickup": null,
  "customer": null,
  "authorizations": [],
  "deleted_order": null,
  "orderParent": [],
  "seller": {
    "user_seller_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "user_seller_name": "Juan Perez",
    "user_seller_rol": "Cajero",
    "user_seller_profile": "Vendedor"
  },
  "period_id": null,
  "events": [],
  "status_order_sync_id": null,
  "status_order_sync": null,
  "company_tax_data": null,
  "data_invoice": null,
  "order_comment": ""
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                               | Tipo   | Descripción                                          |
| --------------------------------------------------- | ------ | ---------------------------------------------------- |
| `order_id`                                          | string | Identificador único de la orden                      |
| `ui_reference_uuid`                                 | string | UUID de referencia de la interfaz de usuario         |
| `ui_started_at`                                     | string | Fecha y hora de inicio en la UI (formato ISO)        |
| `ui_finished_at`                                    | string | Fecha y hora de finalización en la UI (formato ISO)  |
| `cdn_id`                                            | string | Identificador de la cadena                           |
| `cdn_name`                                          | string | Nombre de la cadena                                  |
| `restaurant_id`                                     | string | Identificador del restaurante                        |
| `restaurant_name`                                   | string | Nombre del restaurante                               |
| `cash_register_subscription`                        | string | Identificador de la suscripción de caja registradora |
| `cash_register_subscription_name`                   | string | Nombre de la caja registradora                       |
| `user_seller_id`                                    | string | Identificador del usuario vendedor                   |
| `user_seller_name`                                  | string | Nombre del usuario vendedor                          |
| `status_order_description`                          | string | Descripción del estado de la orden                   |
| `user_sesion`                                       | object | Información de la sesión del usuario                 |
| `user_sesion.user_id`                               | string | Identificador del usuario en sesión                  |
| `user_sesion.user_name`                             | string | Nombre del usuario en sesión                         |
| `conciliation_id`                                   | null   | Identificador de conciliación                        |
| `status_order_id`                                   | string | Identificador del estado de la orden                 |
| `totals`                                            | object | Totales de la orden                                  |
| `totals.result_presentation`                        | object | Resultado de presentación                            |
| `totals.result_presentation.taxes`                  | array  | Lista de impuestos                                   |
| `totals.result_presentation.subtotal_taxes`         | array  | Lista de subtotales de impuestos                     |
| `totals.result_presentation.subtotal`               | number | Subtotal de la orden                                 |
| `totals.result_presentation.subtotal_without_taxes` | number | Subtotal sin impuestos                               |
| `totals.result_presentation.total_discount`         | number | Total de descuentos aplicados                        |
| `totals.result_presentation.tip`                    | number | Propina                                              |
| `totals.result_presentation.total`                  | number | Total de la orden                                    |
| `totals.result`                                     | object | Resultado final                                      |
| `totals.result.taxes`                               | array  | Lista de impuestos                                   |
| `totals.result.subtotal_taxes`                      | array  | Lista de subtotales de impuestos                     |
| `totals.result.subtotal`                            | number | Subtotal de la orden                                 |
| `totals.result.subtotal_without_taxes`              | number | Subtotal sin impuestos                               |
| `totals.result.total_discount`                      | number | Total de descuentos aplicados                        |
| `totals.result.tip`                                 | number | Propina                                              |
| `totals.result.total`                               | number | Total de la orden                                    |
| `totals.result_per_plu`                             | array  | Resultado por PLU                                    |
| `payments`                                          | array  | Lista de pagos                                       |
| `payments[].id`                                     | string | Identificador del pago                               |
| `payments[].payment_method_id`                      | string | Identificador del método de pago                     |
| `payments[].payment_method_name`                    | string | Nombre del método de pago                            |
| `payments[].amount`                                 | number | Monto del pago                                       |
| `payments[].event_id`                               | null   | Identificador del evento                             |
| `payments[].event_code`                             | null   | Código del evento                                    |
| `payments[].meta_data`                              | object | Metadatos del pago                                   |
| `payments[].meta_data.external_reference`           | string | Referencia externa del pago                          |
| `payments[].meta_data.method_name`                  | string | Nombre del método de pago                            |
| `payments[].meta_data.data_transaction`             | null   | Datos de la transacción                              |
| `payments[].meta_data.normalizedTransaction`        | null   | Transacción normalizada                              |
| `payments[].cash_register`                          | string | Identificador de la caja registradora                |
| `payments[].cash_register_name`                     | string | Nombre de la caja registradora                       |
| `payments[].user_seller_id`                         | string | Identificador del usuario vendedor                   |
| `payments[].user_seller_name`                       | string | Nombre del usuario vendedor                          |
| `payments[].created_at`                             | string | Fecha y hora de creación del pago (formato ISO)      |
| `items`                                             | array  | Lista de items de la orden                           |
| `items[].menu_id`                                   | string | Identificador del menú                               |
| `items[].menu_description`                          | string | Descripción del menú                                 |
| `items[].category_id_plu`                           | string | Identificador de categoría del PLU                   |
| `items[].category_description_plu`                  | string | Descripción de la categoría del PLU                  |
| `items[].classification_id`                         | string | Identificador de clasificación                       |
| `items[].classification_description`                | string | Descripción de la clasificación                      |
| `items[].plu_parent_id`                             | null   | Identificador del PLU padre                          |
| `items[].plu_id`                                    | string | Identificador del PLU                                |
| `items[].plu_name`                                  | string | Nombre del PLU                                       |
| `items[].plu_description`                           | string | Descripción del PLU                                  |
| `items[].plu_pvp`                                   | number | Precio de venta al público del PLU                   |
| `items[].plu_quantity`                              | number | Cantidad del PLU                                     |
| `items[].plu_customization`                         | array  | Personalizaciones del PLU                            |
| `items[].subsidy`                                   | null   | Subsidio aplicado                                    |
| `channel`                                           | object | Canal de venta                                       |
| `channel._id`                                       | string | Identificador del canal                              |
| `channel.name`                                      | string | Nombre del canal                                     |
| `document_type`                                     | object | Tipo de documento                                    |
| `document_type._id`                                 | string | Identificador del tipo de documento                  |
| `document_type.name`                                | string | Nombre del tipo de documento                         |
| `invoice`                                           | null   | Información de la factura                            |
| `credit_note`                                       | null   | Información de la nota de crédito                    |
| `driveThru`                                         | null   | Información de drive-thru                            |
| `pickup`                                            | null   | Información de recogida                              |
| `customer`                                          | null   | Información del cliente                              |
| `authorizations`                                    | array  | Lista de autorizaciones                              |
| `deleted_order`                                     | null   | Información de orden eliminada                       |
| `orderParent`                                       | array  | Ordenes padre                                        |
| `seller`                                            | object | Información del vendedor                             |
| `seller.user_seller_id`                             | string | Identificador del usuario vendedor                   |
| `seller.user_seller_name`                           | string | Nombre del usuario vendedor                          |
| `seller.user_seller_rol`                            | string | Rol del usuario vendedor                             |
| `seller.user_seller_profile`                        | string | Perfil del usuario vendedor                          |
| `period_id`                                         | null   | Identificador del período                            |
| `events`                                            | array  | Lista de eventos                                     |
| `status_order_sync_id`                              | null   | Identificador de estado de sincronización de orden   |
| `status_order_sync`                                 | null   | Estado de sincronización de orden                    |
| `company_tax_data`                                  | null   | Datos fiscales de la empresa                         |
| `data_invoice`                                      | null   | Datos de la factura                                  |
| `order_comment`                                     | string | Comentario de la orden                               |

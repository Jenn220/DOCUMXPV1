## Sincronización por Lotes de Análisis de Órdenes

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/orderanalytics/batch_order_order_analytics_sync
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "transaction": {
      "point_of_sale": {
        "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
        "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
        "cash_register_id": "8028a2ff-c639-6df4-68e8-8982c0256be3",
        "cash_register_name": "Caja 001",
        "user_seller_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "user_seller_name": "Juan Perez",
        "device_os_name": "Windows",
        "source_app_name": "POS Desktop",
        "half_integration_id": 1,
        "half_integration_name": "Sistema POS"
      },
      "client": {
        "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "Maria",
        "last_name": "Garcia",
        "phone": "0998765432",
        "email": "maria.garcia@example.com",
        "gov_id_type": "CI",
        "gov_id_number": "1234567890",
        "external_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "additional_info": null
      },
      "order": {
        "order_id": "ORDER-12345",
        "createdAt": "2024-12-08T10:30:00Z",
        "selected_shipping_method": "pickup",
        "accumulate_points": true,
        "redeem_points": false,
        "stock": true,
        "discount": false,
        "order_comment": "",
        "annulation_comment": null,
        "products": [],
        "stock_details": null
      },
      "shipping_method": null,
      "payments": {
        "totals": [],
        "shipping_cost": null,
        "extra_charges": null,
        "taxes": [],
        "discounts": [],
        "payment_methods": []
      },
      "marketing": null,
      "additional_info_transaction": null
    },
    "feBuilder": {
      "companyTaxData": null,
      "dataInvoice": null,
      "dataCredit": null,
      "document_code": null
    },
    "pubDevice": null,
    "promotions": null
  }
]
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                | Tipo    | Descripción                                  |
| ---------------------------------------------------- | ------- | -------------------------------------------- |
| `[].id`                                              | string  | Identificador único del registro             |
| `[].transaction`                                     | object  | Información de la transacción                |
| `[].transaction.point_of_sale`                       | object  | Información del punto de venta               |
| `[].transaction.point_of_sale.cdn_id`                | string  | Identificador de la cadena                   |
| `[].transaction.point_of_sale.restaurant_id`         | string  | Identificador del restaurante                |
| `[].transaction.point_of_sale.cash_register_id`      | string  | Identificador de la caja registradora        |
| `[].transaction.point_of_sale.cash_register_name`    | string  | Nombre de la caja registradora               |
| `[].transaction.point_of_sale.user_seller_id`        | string  | Identificador del usuario vendedor           |
| `[].transaction.point_of_sale.user_seller_name`      | string  | Nombre del usuario vendedor                  |
| `[].transaction.point_of_sale.device_os_name`        | string  | Nombre del sistema operativo del dispositivo |
| `[].transaction.point_of_sale.source_app_name`       | string  | Nombre de la aplicación origen               |
| `[].transaction.point_of_sale.half_integration_id`   | number  | Identificador de la integración              |
| `[].transaction.point_of_sale.half_integration_name` | string  | Nombre de la integración                     |
| `[].transaction.client`                              | object  | Información del cliente                      |
| `[].transaction.client.client_id`                    | string  | Identificador del cliente                    |
| `[].transaction.client.name`                         | string  | Nombre del cliente                           |
| `[].transaction.client.last_name`                    | string  | Apellido del cliente                         |
| `[].transaction.client.phone`                        | string  | Teléfono del cliente                         |
| `[].transaction.client.email`                        | string  | Correo electrónico del cliente               |
| `[].transaction.client.gov_id_type`                  | string  | Tipo de documento de identidad               |
| `[].transaction.client.gov_id_number`                | string  | Número de documento de identidad             |
| `[].transaction.client.external_id`                  | string  | Identificador externo del cliente            |
| `[].transaction.client.additional_info`              | null    | Información adicional del cliente            |
| `[].transaction.order`                               | object  | Información de la orden                      |
| `[].transaction.order.order_id`                      | string  | Identificador de la orden                    |
| `[].transaction.order.createdAt`                     | string  | Fecha y hora de creación (formato ISO)       |
| `[].transaction.order.selected_shipping_method`      | string  | Método de envío seleccionado                 |
| `[].transaction.order.accumulate_points`             | boolean | Indica si acumula puntos                     |
| `[].transaction.order.redeem_points`                 | boolean | Indica si redime puntos                      |
| `[].transaction.order.stock`                         | boolean | Indica si hay stock disponible               |
| `[].transaction.order.discount`                      | boolean | Indica si tiene descuento                    |
| `[].transaction.order.order_comment`                 | string  | Comentario de la orden                       |
| `[].transaction.order.annulation_comment`            | null    | Comentario de anulación                      |
| `[].transaction.order.products`                      | array   | Lista de productos                           |
| `[].transaction.order.stock_details`                 | null    | Detalles de inventario                       |
| `[].transaction.shipping_method`                     | null    | Método de envío                              |
| `[].transaction.payments`                            | object  | Información de pagos                         |
| `[].transaction.payments.totals`                     | array   | Lista de totales                             |
| `[].transaction.payments.shipping_cost`              | null    | Costo de envío                               |
| `[].transaction.payments.extra_charges`              | null    | Cargos adicionales                           |
| `[].transaction.payments.taxes`                      | array   | Lista de impuestos                           |
| `[].transaction.payments.discounts`                  | array   | Lista de descuentos                          |
| `[].transaction.payments.payment_methods`            | array   | Lista de métodos de pago                     |
| `[].transaction.marketing`                           | null    | Información de marketing                     |
| `[].transaction.additional_info_transaction`         | null    | Información adicional de la transacción      |
| `[].feBuilder`                                       | object  | Constructor de facturación electrónica       |
| `[].feBuilder.companyTaxData`                        | null    | Datos fiscales de la empresa                 |
| `[].feBuilder.dataInvoice`                           | null    | Datos de la factura                          |
| `[].feBuilder.dataCredit`                            | null    | Datos de crédito                             |
| `[].feBuilder.document_code`                         | null    | Código del documento                         |
| `[].pubDevice`                                       | null    | Dispositivo de publicación                   |
| `[].promotions`                                      | null    | Promociones aplicadas                        |

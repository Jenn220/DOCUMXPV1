## Construir Documento de Factura Electrónica

### Método HTTP

`POST`

### URL

```
{{serverFeBuilder}}/api/v1/builderDocument
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "type_document": "FACTURA-ECU",
  "transaction": {
    "point_of_sale": {
      "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurant_id": "e17d03da-b8b6-f424-febc-3a767b6401bb",
      "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "cash_register_name": "EC-CAJA001",
      "user_seller_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "user_seller_name": "Daniel Llerena",
      "device_os_name": "ios",
      "source_app_name": "Maxpoint 2.0",
      "half_integration_id": 3,
      "half_integration_name": "App"
    },
    "client": {
      "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "name": "María José ",
      "last_name": "Hernández Zurita ",
      "phone": "+593986610329",
      "email": "mari_jhz@hotmail.com",
      "gov_id_type": "CI",
      "gov_id_number": "0929691038",
      "external_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "additional_info": {
        "birthdate": ""
      }
    },
    "order": {
      "order_id": "0001292432-010103",
      "createdAt": "2025-05-15 13:53:40",
      "invoice_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
      "invoice_key_aut": "4323432534654765686789798679789",
      "products": [
        {
          "plu_id": "401",
          "plu_name": "COMBO IDEAL",
          "plu_quantity": 1,
          "plu_description": "",
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            }
          }
        }
      ]
    },
    "payment_methods": [
      {
        "payment_methods_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
        "processor": "DEUNA",
        "currency_code": "USD",
        "payment_method_code": "93",
        "transaction_type": "credit",
        "transaction_id": "",
        "transaction_status": "APPROVED",
        "tid": null,
        "mid": null,
        "authorization_code": null,
        "voucher": null,
        "reference_number": null,
        "exact_payment": true,
        "customer_cash_amount": "0.0000",
        "total_bill": 6.5,
        "acquirer": {
          "code": " ",
          "name": " "
        },
        "card": {
          "mask": "360857XXXXXXX2001",
          "bin": "360857",
          "last_four_digits": "2001",
          "brand": "diners_club",
          "external_card_brand_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
          "holder": " ",
          "card_country": " "
        },
        "transaction_date": {
          "date": "2024-09-11 05:14:41",
          "time_zone_type": 3,
          "time_zone_name": "America/Guayaquil"
        },
        "additional_info_payment_methods": null
      }
    ],
    "additional_data": [
      {
        "key": "MARCA",
        "value": "TOYOTA"
      }
    ]
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                             | Tipo    | Descripción                                                            |
| --------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `type_document`                                                                   | string  | Tipo de documento electrónico (FACTURA-ECU)                            |
| `transaction`                                                                     | object  | Orden general con información de los puntos de venta                   |
| `transaction.point_of_sale`                                                       | object  | Punto de venta con información física de quien y cómo realizó la venta |
| `transaction.point_of_sale.cdn_id`                                                | string  | Identificador de la franquicia                                         |
| `transaction.point_of_sale.restaurant_id`                                         | string  | Identificador del restaurante                                          |
| `transaction.point_of_sale.cash_register_id`                                      | string  | Identificador de caja                                                  |
| `transaction.point_of_sale.cash_register_name`                                    | string  | Nombre o código de caja                                                |
| `transaction.point_of_sale.user_seller_id`                                        | string  | Identificador de cajero o vendedor                                     |
| `transaction.point_of_sale.user_seller_name`                                      | string  | Nombre de cajero/usuario                                               |
| `transaction.point_of_sale.device_os_name`                                        | string  | Sistema operativo donde se está vendiendo                              |
| `transaction.point_of_sale.source_app_name`                                       | string  | Origen de aplicativo                                                   |
| `transaction.point_of_sale.half_integration_id`                                   | number  | ID de canal (medio de integración)                                     |
| `transaction.point_of_sale.half_integration_name`                                 | string  | Nombre de canal                                                        |
| `transaction.client`                                                              | object  | Datos del cliente comprador y de cliente de facturación                |
| `transaction.client.client_id`                                                    | string  | Identificador del cliente                                              |
| `transaction.client.name`                                                         | string  | Nombre del cliente                                                     |
| `transaction.client.last_name`                                                    | string  | Apellido del cliente                                                   |
| `transaction.client.phone`                                                        | string  | Teléfono del comprador                                                 |
| `transaction.client.email`                                                        | string  | Correo del comprador                                                   |
| `transaction.client.gov_id_type`                                                  | string  | Tipo de documento                                                      |
| `transaction.client.gov_id_number`                                                | string  | Identificación de gobierno del contribuyente                           |
| `transaction.client.external_id`                                                  | string  | ID de referencia                                                       |
| `transaction.client.additional_info`                                              | object  | Información adicional                                                  |
| `transaction.client.additional_info.birthdate`                                    | string  | Cumpleaños                                                             |
| `transaction.order`                                                               | object  | Detalles de los productos, precios y modificadores utilizados          |
| `transaction.order.order_id`                                                      | string  | ID de orden generada por el Punto de Ventas                            |
| `transaction.order.createdAt`                                                     | string  | Fecha de creación de orden de venta                                    |
| `transaction.order.invoice_id`                                                    | string  | ID de factura (cuando es una nota de crédito)                          |
| `transaction.order.invoice_key_aut`                                               | string  | Clave de autorización de factura (cuando es una nota de crédito)       |
| `transaction.order.products`                                                      | array   | Detalles de items                                                      |
| `transaction.order.products[].plu_id`                                             | string  | ID de producto                                                         |
| `transaction.order.products[].plu_name`                                           | string  | Nombre del producto vendido                                            |
| `transaction.order.products[].plu_quantity`                                       | number  | Cantidad de producto vendido                                           |
| `transaction.order.products[].plu_description`                                    | string  | Comentario de producto vendido                                         |
| `transaction.order.products[].price`                                              | object  | Detalles de precios                                                    |
| `transaction.order.products[].price.total_per_plu`                                | object  | Detalle por unidad                                                     |
| `transaction.order.products[].price.total_per_plu.currency_code`                  | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_per_plu.subtotal_without_taxes`         | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_per_plu.discount_percentage`            | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_per_plu.discounts_value`                | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_per_plu.subtotal_include_discounts`     | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_per_plu.tax_value`                      | number  | Valor de impuesto                                                      |
| `transaction.order.products[].price.total_per_plu.total`                          | number  | Total                                                                  |
| `transaction.order.products[].price.total_per_plu.taxes`                          | array   | Detalles de impuestos                                                  |
| `transaction.order.products[].price.total_per_plu.taxes[].name`                   | string  | Nombre del impuesto                                                    |
| `transaction.order.products[].price.total_per_plu.taxes[].code`                   | string  | Código del impuesto                                                    |
| `transaction.order.products[].price.total_per_plu.taxes[].subtotal_without_taxes` | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_per_plu.taxes[].percentage`             | number  | Porcentaje del impuesto                                                |
| `transaction.order.products[].price.total_per_plu.taxes[].total`                  | number  | Total del impuesto                                                     |
| `transaction.order.products[].price.total_price`                                  | object  | Detalles de totales por la cantidad de producto                        |
| `transaction.order.products[].price.total_price.currency_code`                    | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_price.subtotal_without_taxes`           | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_price.discount_percentage`              | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_price.discounts_value`                  | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_price.subtotal_include_discounts`       | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_price.tax_value`                        | number  | Valor de impuesto                                                      |
| `transaction.order.products[].price.total_price.total`                            | number  | Total                                                                  |
| `transaction.order.products[].price.total_price.taxes`                            | array   | Detalles de impuestos                                                  |
| `transaction.order.products[].price.total_price.taxes[].name`                     | string  | Nombre del impuesto                                                    |
| `transaction.order.products[].price.total_price.taxes[].code`                     | string  | Código del impuesto                                                    |
| `transaction.order.products[].price.total_price.taxes[].subtotal_without_taxes`   | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_price.taxes[].percentage`               | number  | Porcentaje del impuesto                                                |
| `transaction.order.products[].price.total_price.taxes[].total`                    | number  | Total del impuesto                                                     |
| `transaction.payment_methods`                                                     | array   | Métodos de pago utilizados para la transacción                         |
| `transaction.payment_methods[].payment_methods_id`                                | string  | ID del método de pago                                                  |
| `transaction.payment_methods[].processor`                                         | string  | Procesador de pago                                                     |
| `transaction.payment_methods[].currency_code`                                     | string  | Código de moneda                                                       |
| `transaction.payment_methods[].payment_method_code`                               | string  | Código de método de pago                                               |
| `transaction.payment_methods[].transaction_type`                                  | string  | Tipo de transacción                                                    |
| `transaction.payment_methods[].transaction_id`                                    | string  | Identificador de la orden                                              |
| `transaction.payment_methods[].transaction_status`                                | string  | Estado de transacción                                                  |
| `transaction.payment_methods[].tid`                                               | string  | TID                                                                    |
| `transaction.payment_methods[].mid`                                               | string  | MID                                                                    |
| `transaction.payment_methods[].authorization_code`                                | string  | Código de autorización                                                 |
| `transaction.payment_methods[].voucher`                                           | string  | Voucher                                                                |
| `transaction.payment_methods[].reference_number`                                  | string  | Número de referencia                                                   |
| `transaction.payment_methods[].exact_payment`                                     | boolean | Si es pago exacto                                                      |
| `transaction.payment_methods[].customer_cash_amount`                              | string  | Monto en efectivo del cliente                                          |
| `transaction.payment_methods[].total_bill`                                        | number  | Total de la cuenta                                                     |
| `transaction.payment_methods[].acquirer`                                          | object  | Información del adquirente                                             |
| `transaction.payment_methods[].acquirer.code`                                     | string  | Código del adquirente                                                  |
| `transaction.payment_methods[].acquirer.name`                                     | string  | Nombre del adquirente                                                  |
| `transaction.payment_methods[].card`                                              | object  | Información de tarjeta                                                 |
| `transaction.payment_methods[].card.mask`                                         | string  | Máscara de tarjeta                                                     |
| `transaction.payment_methods[].card.bin`                                          | string  | BIN de tarjeta                                                         |
| `transaction.payment_methods[].card.last_four_digits`                             | string  | Últimos cuatro dígitos                                                 |
| `transaction.payment_methods[].card.brand`                                        | string  | Marca de tarjeta                                                       |
| `transaction.payment_methods[].card.external_card_brand_id`                       | string  | ID externo de marca de tarjeta                                         |
| `transaction.payment_methods[].card.holder`                                       | string  | Titular de tarjeta                                                     |
| `transaction.payment_methods[].card.card_country`                                 | string  | País de tarjeta                                                        |
| `transaction.payment_methods[].transaction_date`                                  | object  | Fecha de transacción                                                   |
| `transaction.payment_methods[].transaction_date.date`                             | string  | Fecha                                                                  |
| `transaction.payment_methods[].transaction_date.time_zone_type`                   | number  | Tipo de zona horaria                                                   |
| `transaction.payment_methods[].transaction_date.time_zone_name`                   | string  | Nombre de zona horaria                                                 |
| `transaction.payment_methods[].additional_info_payment_methods`                   | object  | Información adicional de métodos de pago                               |
| `transaction.additional_data`                                                     | array   | Datos adicionales (opcional)                                           |
| `transaction.additional_data[].key`                                               | string  | Clave                                                                  |
| `transaction.additional_data[].value`                                             | string  | Valor                                                                  |

### Respuestas del Servidor

#### 400 Bad Request - Integración Incompleta

```json
{
  "code": 400,
  "status": "failed",
  "alert": "Integración imcompleta",
  "messages": ["falta campos x", "falta campos y"],
  "data": {}
}
```

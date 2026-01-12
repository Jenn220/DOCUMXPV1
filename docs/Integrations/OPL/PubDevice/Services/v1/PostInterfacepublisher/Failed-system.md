## Publicar Datos de Transacción

### Método HTTP

`POST`

### URL

```
{{serverPubDevice}}/api/v1/publisherData
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "type_publisher": "OPEN_CASH",
  "transaction": {
    "point_of_sale": {
      "cdn_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
      "restaurant_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
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
      "createdAt": "2024-09-11 12:14:40",
      "selected_shipping_method": "pickup",
      "accumulate_points": false,
      "redeem_points": false,
      "stock": false,
      "discount": false,
      "order_comment": "",
      "annulation_comment": "",
      "products": [
        {
          "plu_id": "401",
          "plu_name": "COMBO IDEAL",
          "plu_quantity": 1,
          "plu_comment": "",
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "taxes_percentage": 15,
              "tax_value": 0.85,
              "total": 6.5,
              "total_before_sale": 6.5,
              "suggested_price": 0
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": null,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "taxes_percentage": 15,
              "tax_value": 0.85,
              "total": 6.5,
              "total_before_sale": 6.5,
              "suggested_price": 0
            }
          },
          "modifier_groups": [
            {
              "suggested_question_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
              "description": "Es necesario elegir uno",
              "selected_modifiers": [
                {
                  "plu_id": "402",
                  "plu_name": "COMBO IDEAL",
                  "plu_quantity": 1,
                  "plu_comment": "",
                  "price": {
                    "total_per_plu": {
                      "currency_code": "USD",
                      "subtotal_without_taxes": 5.65,
                      "discount_percentage": 0,
                      "discounts_value": 0,
                      "subtotal_include_discounts": 5.65,
                      "taxes_percentage": 15,
                      "tax_value": 0.85,
                      "total": 6.5,
                      "total_before_sale": 6.5,
                      "suggested_price": 0
                    },
                    "total_price": {
                      "currency_code": "USD",
                      "subtotal_without_taxes": 5.65,
                      "discount_percentage": null,
                      "discounts_value": 0,
                      "subtotal_include_discounts": 5.65,
                      "taxes_percentage": 15,
                      "tax_value": 0.85,
                      "total": 6.5,
                      "total_before_sale": 6.5,
                      "suggested_price": 0
                    }
                  },
                  "modifier_groups": [],
                  "additional_info_modifier_groups": null
                }
              ]
            }
          ],
          "additional_info_order": null
        }
      ],
      "stock_details": null
    },
    "shipping_method": null,
    "payments": {
      "totals": [
        {
          "currency_code": "USD",
          "subtotal_without_taxes": 5.65,
          "discount_percentage": 0,
          "discounts_value": 0,
          "subtotal_include_discounts": 5.65,
          "taxes_percentage": 15,
          "tax_value": 0.85,
          "total_before_sale": 6.5,
          "total": 6.5
        },
        {
          "currency_code": "Points",
          "subtotal_without_taxes": 0,
          "discount_percentage": 0,
          "discounts_value": 0,
          "subtotal_include_discounts": 0,
          "taxes_percentage": 15,
          "tax_value": 0,
          "total_before_sale": 0,
          "total": 0
        }
      ],
      "shipping_cost": null,
      "extra_charges": null,
      "taxes": [
        {
          "name": "IVA 15%",
          "currency_code": "USD",
          "subtotal_without_taxes": 5.65,
          "percentage": 15,
          "total": 0.85
        }
      ],
      "discounts": [
        {
          "name": "OFF5APP",
          "percentage_discount": false,
          "amount_discount": true,
          "currency_code": "USD",
          "total_before_sale": 0,
          "subtotal_without_discounts": 4.65,
          "percentage": 0,
          "total": 4.3478,
          "total_with_taxes": 5
        }
      ],
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
      ]
    },
    "marketing": null,
    "additional_info_transaction": null
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                                                 | Tipo    | Descripción                                                            |
| ----------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `type_publisher`                                                                                      | string  | Tipo de impresión (catálogo de tipos de impresiones)                   |
| `transaction`                                                                                         | object  | Orden general con información de los puntos de venta                   |
| `transaction.point_of_sale`                                                                           | object  | Punto de venta con información física de quien y cómo realizó la venta |
| `transaction.point_of_sale.cdn_id`                                                                    | string  | Identificador de la franquicia                                         |
| `transaction.point_of_sale.restaurant_id`                                                             | string  | Identificador del restaurante                                          |
| `transaction.point_of_sale.cash_register_id`                                                          | string  | Identificador de caja                                                  |
| `transaction.point_of_sale.cash_register_name`                                                        | string  | Nombre o código de caja                                                |
| `transaction.point_of_sale.user_seller_id`                                                            | string  | Identificador de cajero o vendedor                                     |
| `transaction.point_of_sale.user_seller_name`                                                          | string  | Nombre de cajero/usuario                                               |
| `transaction.point_of_sale.device_os_name`                                                            | string  | Sistema operativo donde se está vendiendo                              |
| `transaction.point_of_sale.source_app_name`                                                           | string  | Origen de aplicativo                                                   |
| `transaction.point_of_sale.half_integration_id`                                                       | number  | ID de canal (medio de integración)                                     |
| `transaction.point_of_sale.half_integration_name`                                                     | string  | Nombre de canal                                                        |
| `transaction.client`                                                                                  | object  | Datos del cliente comprador y de facturación                           |
| `transaction.client.client_id`                                                                        | string  | Identificador del cliente                                              |
| `transaction.client.name`                                                                             | string  | Nombre del cliente                                                     |
| `transaction.client.last_name`                                                                        | string  | Apellido del cliente                                                   |
| `transaction.client.phone`                                                                            | string  | Teléfono del comprador                                                 |
| `transaction.client.email`                                                                            | string  | Correo del comprador                                                   |
| `transaction.client.gov_id_type`                                                                      | string  | Tipo de documento                                                      |
| `transaction.client.gov_id_number`                                                                    | string  | Identificación de gobierno del contribuyente                           |
| `transaction.client.external_id`                                                                      | string  | ID de referencia                                                       |
| `transaction.client.additional_info`                                                                  | object  | Información adicional del cliente                                      |
| `transaction.client.additional_info.birthdate`                                                        | string  | Fecha de cumpleaños                                                    |
| `transaction.order`                                                                                   | object  | Detalles de los PLUs, precios y modificadores utilizados               |
| `transaction.order.order_id`                                                                          | string  | ID de orden generada por el Punto de Venta                             |
| `transaction.order.createdAt`                                                                         | string  | Fecha de creación de orden de venta                                    |
| `transaction.order.selected_shipping_method`                                                          | string  | Método de envío                                                        |
| `transaction.order.accumulate_points`                                                                 | boolean | Si es una venta con temas de fidelización                              |
| `transaction.order.redeem_points`                                                                     | boolean | Si es una venta con redención de puntos                                |
| `transaction.order.stock`                                                                             | boolean | Si es una venta con temas de inventario                                |
| `transaction.order.discount`                                                                          | boolean | Si es una venta con descuentos                                         |
| `transaction.order.order_comment`                                                                     | string  | Comentario de la orden                                                 |
| `transaction.order.annulation_comment`                                                                | string  | Comentario de anulación/motivo                                         |
| `transaction.order.products`                                                                          | array   | Detalles de items                                                      |
| `transaction.order.products[].plu_id`                                                                 | string  | ID del PLU                                                             |
| `transaction.order.products[].plu_name`                                                               | string  | Nombre del PLU vendido                                                 |
| `transaction.order.products[].plu_quantity`                                                           | number  | Cantidad de PLU vendido                                                |
| `transaction.order.products[].plu_comment`                                                            | string  | Comentario del PLU vendido                                             |
| `transaction.order.products[].price`                                                                  | object  | Detalles de precios                                                    |
| `transaction.order.products[].price.total_per_plu`                                                    | object  | Detalle por unidad                                                     |
| `transaction.order.products[].price.total_per_plu.currency_code`                                      | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_per_plu.subtotal_without_taxes`                             | number  | Subtotal sin impuestos (PVP)                                           |
| `transaction.order.products[].price.total_per_plu.discount_percentage`                                | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_per_plu.discounts_value`                                    | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_per_plu.subtotal_include_discounts`                         | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_per_plu.taxes_percentage`                                   | number  | Porcentaje de impuestos                                                |
| `transaction.order.products[].price.total_per_plu.tax_value`                                          | number  | Valor del impuesto                                                     |
| `transaction.order.products[].price.total_per_plu.total`                                              | number  | Total                                                                  |
| `transaction.order.products[].price.total_per_plu.total_before_sale`                                  | number  | Total antes de venta                                                   |
| `transaction.order.products[].price.total_per_plu.suggested_price`                                    | number  | Precio sugerido                                                        |
| `transaction.order.products[].price.total_price`                                                      | object  | Detalles de totales por la cantidad de PLUs                            |
| `transaction.order.products[].price.total_price.currency_code`                                        | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_price.subtotal_without_taxes`                               | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_price.discount_percentage`                                  | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_price.discounts_value`                                      | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_price.subtotal_include_discounts`                           | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_price.taxes_percentage`                                     | number  | Porcentaje de impuestos                                                |
| `transaction.order.products[].price.total_price.tax_value`                                            | number  | Valor del impuesto                                                     |
| `transaction.order.products[].price.total_price.total`                                                | number  | Total                                                                  |
| `transaction.order.products[].price.total_price.total_before_sale`                                    | number  | Total antes de venta                                                   |
| `transaction.order.products[].price.total_price.suggested_price`                                      | number  | Precio sugerido                                                        |
| `transaction.order.products[].modifier_groups`                                                        | array   | Modificadores de PLUs                                                  |
| `transaction.order.products[].modifier_groups[].suggested_question_id`                                | string  | Identificador de la pregunta sugerida                                  |
| `transaction.order.products[].modifier_groups[].description`                                          | string  | Descripción de la pregunta sugerida                                    |
| `transaction.order.products[].modifier_groups[].selected_modifiers`                                   | array   | Modificadores seleccionados                                            |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].plu_id`                          | string  | ID del PLU modificador                                                 |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].plu_name`                        | string  | Nombre del PLU modificador                                             |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].plu_quantity`                    | number  | Cantidad del PLU modificador                                           |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].plu_comment`                     | string  | Comentario del PLU modificador                                         |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].price`                           | object  | Precios del modificador                                                |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].modifier_groups`                 | array   | Grupos de modificadores anidados                                       |
| `transaction.order.products[].modifier_groups[].selected_modifiers[].additional_info_modifier_groups` | null    | Información adicional para preguntas sugeridas                         |
| `transaction.order.products[].additional_info_order`                                                  | null    | Información adicional a nivel de detalle de orden                      |
| `transaction.order.stock_details`                                                                     | null    | Detalles de inventario de venta                                        |
| `transaction.shipping_method`                                                                         | null    | Información de método de entrega de la transacción                     |
| `transaction.payments`                                                                                | object  | Datos en relación a los pagos de la transacción                        |
| `transaction.payments.totals`                                                                         | array   | Totales por tipo de moneda                                             |
| `transaction.payments.totals[].currency_code`                                                         | string  | Código de moneda                                                       |
| `transaction.payments.totals[].subtotal_without_taxes`                                                | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.totals[].discount_percentage`                                                   | number  | Porcentaje de descuento                                                |
| `transaction.payments.totals[].discounts_value`                                                       | number  | Valor de descuentos                                                    |
| `transaction.payments.totals[].subtotal_include_discounts`                                            | number  | Subtotal incluyendo descuentos                                         |
| `transaction.payments.totals[].taxes_percentage`                                                      | number  | Porcentaje de impuestos                                                |
| `transaction.payments.totals[].tax_value`                                                             | number  | Valor del impuesto                                                     |
| `transaction.payments.totals[].total_before_sale`                                                     | number  | Total antes de venta                                                   |
| `transaction.payments.totals[].total`                                                                 | number  | Total                                                                  |
| `transaction.payments.shipping_cost`                                                                  | null    | Costos de envío                                                        |
| `transaction.payments.extra_charges`                                                                  | null    | Cargos extras                                                          |
| `transaction.payments.taxes`                                                                          | array   | Impuestos aplicados                                                    |
| `transaction.payments.taxes[].name`                                                                   | string  | Nombre del impuesto                                                    |
| `transaction.payments.taxes[].currency_code`                                                          | string  | Código de moneda                                                       |
| `transaction.payments.taxes[].subtotal_without_taxes`                                                 | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.taxes[].percentage`                                                             | number  | Porcentaje del impuesto                                                |
| `transaction.payments.taxes[].total`                                                                  | number  | Total del impuesto                                                     |
| `transaction.payments.discounts`                                                                      | array   | Descuentos aplicados                                                   |
| `transaction.payments.discounts[].name`                                                               | string  | Nombre del descuento                                                   |
| `transaction.payments.discounts[].percentage_discount`                                                | boolean | Si es descuento porcentual                                             |
| `transaction.payments.discounts[].amount_discount`                                                    | boolean | Si es descuento por monto                                              |
| `transaction.payments.discounts[].currency_code`                                                      | string  | Código de moneda                                                       |
| `transaction.payments.discounts[].total_before_sale`                                                  | number  | Total antes de venta                                                   |
| `transaction.payments.discounts[].subtotal_without_discounts`                                         | number  | Subtotal sin descuentos                                                |
| `transaction.payments.discounts[].percentage`                                                         | number  | Porcentaje de descuento                                                |
| `transaction.payments.discounts[].total`                                                              | number  | Total del descuento                                                    |
| `transaction.payments.discounts[].total_with_taxes`                                                   | number  | Total con impuestos                                                    |
| `transaction.payments.payment_methods`                                                                | array   | Tipos de pagos utilizados para la transacción                          |
| `transaction.payments.payment_methods[].payment_methods_id`                                           | string  | ID del método de pago                                                  |
| `transaction.payments.payment_methods[].processor`                                                    | string  | Procesador de pago                                                     |
| `transaction.payments.payment_methods[].currency_code`                                                | string  | Código de moneda                                                       |
| `transaction.payments.payment_methods[].payment_method_code`                                          | string  | Código del método de pago                                              |
| `transaction.payments.payment_methods[].transaction_type`                                             | string  | Tipo de transacción                                                    |
| `transaction.payments.payment_methods[].transaction_id`                                               | string  | Identificador de la orden                                              |
| `transaction.payments.payment_methods[].transaction_status`                                           | string  | Estado de la transacción                                               |
| `transaction.payments.payment_methods[].tid`                                                          | null    | Terminal ID                                                            |
| `transaction.payments.payment_methods[].mid`                                                          | null    | Merchant ID                                                            |
| `transaction.payments.payment_methods[].authorization_code`                                           | null    | Código de autorización                                                 |
| `transaction.payments.payment_methods[].voucher`                                                      | null    | Voucher                                                                |
| `transaction.payments.payment_methods[].reference_number`                                             | null    | Número de referencia                                                   |
| `transaction.payments.payment_methods[].exact_payment`                                                | boolean | Si es pago exacto                                                      |
| `transaction.payments.payment_methods[].customer_cash_amount`                                         | string  | Monto en efectivo del cliente                                          |
| `transaction.payments.payment_methods[].total_bill`                                                   | number  | Total de la factura                                                    |
| `transaction.payments.payment_methods[].acquirer`                                                     | object  | Información del adquirente                                             |
| `transaction.payments.payment_methods[].acquirer.code`                                                | string  | Código del adquirente                                                  |
| `transaction.payments.payment_methods[].acquirer.name`                                                | string  | Nombre del adquirente                                                  |
| `transaction.payments.payment_methods[].card`                                                         | object  | Información de la tarjeta                                              |
| `transaction.payments.payment_methods[].card.mask`                                                    | string  | Máscara de la tarjeta                                                  |
| `transaction.payments.payment_methods[].card.bin`                                                     | string  | BIN de la tarjeta                                                      |
| `transaction.payments.payment_methods[].card.last_four_digits`                                        | string  | Últimos 4 dígitos                                                      |
| `transaction.payments.payment_methods[].card.brand`                                                   | string  | Marca de la tarjeta                                                    |
| `transaction.payments.payment_methods[].card.external_card_brand_id`                                  | string  | ID externo de marca de tarjeta                                         |
| `transaction.payments.payment_methods[].card.holder`                                                  | string  | Titular de la tarjeta                                                  |
| `transaction.payments.payment_methods[].card.card_country`                                            | string  | País de la tarjeta                                                     |
| `transaction.payments.payment_methods[].transaction_date`                                             | object  | Fecha de transacción                                                   |
| `transaction.payments.payment_methods[].transaction_date.date`                                        | string  | Fecha y hora                                                           |
| `transaction.payments.payment_methods[].transaction_date.time_zone_type`                              | number  | Tipo de zona horaria                                                   |
| `transaction.payments.payment_methods[].transaction_date.time_zone_name`                              | string  | Nombre de zona horaria                                                 |
| `transaction.payments.payment_methods[].additional_info_payment_methods`                              | null    | Información adicional de métodos de pago                               |
| `transaction.marketing`                                                                               | null    | Información de marketing                                               |
| `transaction.additional_info_transaction`                                                             | null    | Información adicional de la transacción                                |

### Respuestas del Servidor

#### 500 Internal Server Error - Error al Imprimir

```json
{
  "code": 500,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["A non-empty request body is required."]
}
```

## Generar Nota de Crédito Electrónica Ecuador

### Método HTTP

`POST`

### URL

```
{{serverFeBuilder}}/api/v1/transaction/TX003
```

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "type_document": "NOTA_CREDITO-ECU",
  "transaction": {
    "transaction_date": "2025-07-17T15:33:20.123",
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
                  "tax_name": "IVA 10 %",
                  "tax_code": "iva23313",
                  "tax_percentage": 10,
                  "total_tax_vulue": 4.99,
                  "base_amount": 130
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
                  "tax_name": "IVA 10 %",
                  "tax_code": "iva23313",
                  "tax_percentage": 10,
                  "total_tax_vulue": 4.99,
                  "base_amount": 130
                }
              ]
            }
          }
        }
      ]
    },
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
          "tax_name": "IVA 15%",
          "tax_code": "iva23313",
          "tax_percentage": 15,
          "total_tax_vulue": 0.85,
          "base_amount": 5.65
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
          "transaction_type": "OTROS CON UTILIZACIÓN DEL SISTEMA FINANCIERO",
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
    "additional_data": [
      {
        "key": "MARCA",
        "value": "TOYOTA"
      }
    ],
    "invoice": {
      "companyTaxData": {
        "name": "INT FOOD SERVICES CORP SA",
        "identification_number": "1234567890001",
        "special_taxpayer": "GRAN CONTRIBUYENTE",
        "isSpecial_taxpayer": "Sí",
        "special_taxpayer_code": "RESOL. N°: NAC-GCFOIOC21-00000900-E",
        "type_tax": "3243fdw23",
        "obligatory_to_keep_accounts": "Sí",
        "resolution_code": "155",
        "company_address": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
        "restaurnt_address": "PICHINCHA / QUITO / AV. AMAZONAS 6121 Y EL INCA",
        "establishment_code": "001",
        "point_of_emission_code": "001"
      },
      "dataInvoice": {
        "sequential": "050-070-000470031",
        "transaction": "K024F001529034",
        "access_key": "YOUR_REDIS_OR_AZURE_KEY_HERE",
        "legend": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
        "link_label": "Para obtener su factura electrónica ingrese a:",
        "url_document": "https://facturacion.kfc.ec",
        "access_key_label": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
        "created_at": "2024-09-11 12:14:40",
        "document": {
          "client": {
            "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
            "name": "María José ",
            "last_name": "Hernández Zurita ",
            "phone": "+593986610329",
            "email": "mari_jhz@hotmail.com",
            "gov_id_type": "CI",
            "gov_id_number": "0929691038"
          },
          "orderInvoice": {
            "order_id": "0001292432-010103",
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
                    "taxes_percentage": 15,
                    "tax_value": 0.85,
                    "total": 6.5,
                    "total_before_sale": 6.5,
                    "suggested_price": 0,
                    "taxes": [
                      {
                        "name": "IVA 15%",
                        "currency_code": "USD",
                        "subtotal_without_taxes": 5.65,
                        "percentage": 15,
                        "total": 0.85
                      }
                    ]
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
                    "suggested_price": 0,
                    "taxes": [
                      {
                        "name": "IVA 15%",
                        "currency_code": "USD",
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
              "transaction_type": "OTROS METODOS UTILIZANDO EL SISTEMA FINANCIERO",
              "transaction_id": "",
              "transaction_status": "APPROVED",
              "reference_number": null,
              "exact_payment": true,
              "customer_cash_amount": "0.0000",
              "total_bill": 6.5,
              "acquirer": {
                "code": " ",
                "name": " "
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
      },
      "dataCredit": {}
    },
    "annulation_comment": "me equivoque!!"
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                         | Tipo    | Descripción                                                            |
| ----------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `type_document`                                                               | string  | Tipo de documento electrónico (NOTA_CREDITO-ECU)                       |
| `transaction`                                                                 | object  | Orden general con información de los puntos de venta                   |
| `transaction.transaction_date`                                                | string  | Fecha de la transacción (formato ISO 8601)                             |
| `transaction.point_of_sale`                                                   | object  | Punto de venta con información física de quien y cómo realizó la venta |
| `transaction.point_of_sale.cdn_id`                                            | string  | Identificador de la franquicia                                         |
| `transaction.point_of_sale.restaurant_id`                                     | string  | Identificador del restaurante                                          |
| `transaction.point_of_sale.cash_register_id`                                  | string  | Identificador de caja                                                  |
| `transaction.point_of_sale.cash_register_name`                                | string  | Nombre o código de caja                                                |
| `transaction.point_of_sale.user_seller_id`                                    | string  | Identificador de cajero o vendedor                                     |
| `transaction.point_of_sale.user_seller_name`                                  | string  | Nombre de cajero/usuario                                               |
| `transaction.point_of_sale.device_os_name`                                    | string  | Sistema operativo donde se está vendiendo                              |
| `transaction.point_of_sale.source_app_name`                                   | string  | Origen de aplicativo                                                   |
| `transaction.point_of_sale.half_integration_id`                               | number  | ID de canal (medio de integración)                                     |
| `transaction.point_of_sale.half_integration_name`                             | string  | Nombre de canal                                                        |
| `transaction.client`                                                          | object  | Datos del cliente comprador y de cliente de facturación                |
| `transaction.client.client_id`                                                | string  | Identificador del cliente                                              |
| `transaction.client.name`                                                     | string  | Nombre del cliente                                                     |
| `transaction.client.last_name`                                                | string  | Apellido del cliente                                                   |
| `transaction.client.phone`                                                    | string  | Teléfono del comprador                                                 |
| `transaction.client.email`                                                    | string  | Correo del comprador                                                   |
| `transaction.client.gov_id_type`                                              | string  | Tipo de documento                                                      |
| `transaction.client.gov_id_number`                                            | string  | Identificación de gobierno del contribuyente                           |
| `transaction.client.external_id`                                              | string  | ID de referencia                                                       |
| `transaction.client.additional_info`                                          | object  | Información adicional                                                  |
| `transaction.client.additional_info.birthdate`                                | string  | Cumpleaños                                                             |
| `transaction.order`                                                           | object  | Detalles de los productos, precios y modificadores utilizados          |
| `transaction.order.order_id`                                                  | string  | ID de orden generada por el Punto de Ventas                            |
| `transaction.order.createdAt`                                                 | string  | Fecha de creación de orden de venta                                    |
| `transaction.order.invoice_id`                                                | string  | ID de factura (cuando es una nota de crédito)                          |
| `transaction.order.invoice_key_aut`                                           | string  | Clave de autorización de factura (cuando es una nota de crédito)       |
| `transaction.order.products`                                                  | array   | Detalles de items                                                      |
| `transaction.order.products[].plu_id`                                         | string  | ID de producto                                                         |
| `transaction.order.products[].plu_name`                                       | string  | Nombre del producto vendido                                            |
| `transaction.order.products[].plu_quantity`                                   | number  | Cantidad de producto vendido                                           |
| `transaction.order.products[].plu_description`                                | string  | Comentario de producto vendido                                         |
| `transaction.order.products[].price`                                          | object  | Detalles de precios                                                    |
| `transaction.order.products[].price.total_per_plu`                            | object  | Detalle por unidad                                                     |
| `transaction.order.products[].price.total_per_plu.currency_code`              | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_per_plu.subtotal_without_taxes`     | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_per_plu.discount_percentage`        | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_per_plu.discounts_value`            | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_per_plu.subtotal_include_discounts` | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_per_plu.tax_value`                  | number  | Valor de impuesto                                                      |
| `transaction.order.products[].price.total_per_plu.total`                      | number  | Total                                                                  |
| `transaction.order.products[].price.total_per_plu.taxes`                      | array   | Detalles de impuestos                                                  |
| `transaction.order.products[].price.total_per_plu.taxes[].tax_name`           | string  | Nombre del impuesto                                                    |
| `transaction.order.products[].price.total_per_plu.taxes[].tax_code`           | string  | Código del impuesto                                                    |
| `transaction.order.products[].price.total_per_plu.taxes[].tax_percentage`     | number  | Porcentaje del impuesto                                                |
| `transaction.order.products[].price.total_per_plu.taxes[].total_tax_vulue`    | number  | Valor total del impuesto                                               |
| `transaction.order.products[].price.total_per_plu.taxes[].base_amount`        | number  | Base imponible                                                         |
| `transaction.order.products[].price.total_price`                              | object  | Detalles de totales por la cantidad de producto                        |
| `transaction.order.products[].price.total_price.currency_code`                | string  | Código de moneda                                                       |
| `transaction.order.products[].price.total_price.subtotal_without_taxes`       | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.total_price.discount_percentage`          | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.total_price.discounts_value`              | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.total_price.subtotal_include_discounts`   | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.total_price.tax_value`                    | number  | Valor de impuesto                                                      |
| `transaction.order.products[].price.total_price.total`                        | number  | Total                                                                  |
| `transaction.order.products[].price.total_price.taxes`                        | array   | Detalles de impuestos                                                  |
| `transaction.order.products[].price.total_price.taxes[].tax_name`             | string  | Nombre del impuesto                                                    |
| `transaction.order.products[].price.total_price.taxes[].tax_code`             | string  | Código del impuesto                                                    |
| `transaction.order.products[].price.total_price.taxes[].tax_percentage`       | number  | Porcentaje del impuesto                                                |
| `transaction.order.products[].price.total_price.taxes[].total_tax_vulue`      | number  | Valor total del impuesto                                               |
| `transaction.order.products[].price.total_price.taxes[].base_amount`          | number  | Base imponible                                                         |
| `transaction.payments`                                                        | object  | Datos en relación a los pagos utilizados para la transacción           |
| `transaction.payments.totals`                                                 | array   | Totales de pagos                                                       |
| `transaction.payments.totals[].currency_code`                                 | string  | Código de moneda                                                       |
| `transaction.payments.totals[].subtotal_without_taxes`                        | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.totals[].discount_percentage`                           | number  | Porcentaje de descuento                                                |
| `transaction.payments.totals[].discounts_value`                               | number  | Valor de descuentos                                                    |
| `transaction.payments.totals[].subtotal_include_discounts`                    | number  | Subtotal incluyendo descuentos                                         |
| `transaction.payments.totals[].taxes_percentage`                              | number  | Porcentaje de impuestos                                                |
| `transaction.payments.totals[].tax_value`                                     | number  | Valor de impuesto                                                      |
| `transaction.payments.totals[].total_before_sale`                             | number  | Total antes de venta                                                   |
| `transaction.payments.totals[].total`                                         | number  | Total                                                                  |
| `transaction.payments.shipping_cost`                                          | object  | Costos de envío                                                        |
| `transaction.payments.extra_charges`                                          | object  | Cargos extra                                                           |
| `transaction.payments.taxes`                                                  | array   | Impuestos                                                              |
| `transaction.payments.taxes[].tax_name`                                       | string  | Nombre del impuesto                                                    |
| `transaction.payments.taxes[].tax_code`                                       | string  | Código del impuesto                                                    |
| `transaction.payments.taxes[].tax_percentage`                                 | number  | Porcentaje del impuesto                                                |
| `transaction.payments.taxes[].total_tax_vulue`                                | number  | Valor total del impuesto                                               |
| `transaction.payments.taxes[].base_amount`                                    | number  | Base imponible                                                         |
| `transaction.payments.discounts`                                              | array   | Descuentos                                                             |
| `transaction.payments.discounts[].name`                                       | string  | Nombre del descuento                                                   |
| `transaction.payments.discounts[].percentage_discount`                        | boolean | Si es descuento porcentual                                             |
| `transaction.payments.discounts[].amount_discount`                            | boolean | Si es descuento por monto                                              |
| `transaction.payments.discounts[].currency_code`                              | string  | Código de moneda                                                       |
| `transaction.payments.discounts[].total_before_sale`                          | number  | Total antes de venta                                                   |
| `transaction.payments.discounts[].subtotal_without_discounts`                 | number  | Subtotal sin descuentos                                                |
| `transaction.payments.discounts[].percentage`                                 | number  | Porcentaje                                                             |
| `transaction.payments.discounts[].total`                                      | number  | Total                                                                  |
| `transaction.payments.discounts[].total_with_taxes`                           | number  | Total con impuestos                                                    |
| `transaction.payments.payment_methods`                                        | array   | Métodos de pago utilizados para la transacción                         |
| `transaction.payments.payment_methods[].payment_methods_id`                   | string  | ID del método de pago                                                  |
| `transaction.payments.payment_methods[].processor`                            | string  | Procesador de pago                                                     |
| `transaction.payments.payment_methods[].currency_code`                        | string  | Código de moneda                                                       |
| `transaction.payments.payment_methods[].payment_method_code`                  | string  | Código de método de pago                                               |
| `transaction.payments.payment_methods[].transaction_type`                     | string  | Tipo de transacción                                                    |
| `transaction.payments.payment_methods[].transaction_id`                       | string  | ID de transacción                                                      |
| `transaction.payments.payment_methods[].transaction_status`                   | string  | Estado de transacción                                                  |
| `transaction.payments.payment_methods[].tid`                                  | string  | TID                                                                    |
| `transaction.payments.payment_methods[].mid`                                  | string  | MID                                                                    |
| `transaction.payments.payment_methods[].authorization_code`                   | string  | Código de autorización                                                 |
| `transaction.payments.payment_methods[].voucher`                              | string  | Voucher                                                                |
| `transaction.payments.payment_methods[].reference_number`                     | string  | Número de referencia                                                   |
| `transaction.payments.payment_methods[].exact_payment`                        | boolean | Si es pago exacto                                                      |
| `transaction.payments.payment_methods[].customer_cash_amount`                 | string  | Monto en efectivo del cliente                                          |
| `transaction.payments.payment_methods[].total_bill`                           | number  | Total de la cuenta                                                     |
| `transaction.payments.payment_methods[].acquirer`                             | object  | Información del adquirente                                             |
| `transaction.payments.payment_methods[].acquirer.code`                        | string  | Código del adquirente                                                  |
| `transaction.payments.payment_methods[].acquirer.name`                        | string  | Nombre del adquirente                                                  |
| `transaction.payments.payment_methods[].card`                                 | object  | Información de tarjeta                                                 |
| `transaction.payments.payment_methods[].card.mask`                            | string  | Máscara de tarjeta                                                     |
| `transaction.payments.payment_methods[].card.bin`                             | string  | BIN de tarjeta                                                         |
| `transaction.payments.payment_methods[].card.last_four_digits`                | string  | Últimos cuatro dígitos                                                 |
| `transaction.payments.payment_methods[].card.brand`                           | string  | Marca de tarjeta                                                       |
| `transaction.payments.payment_methods[].card.external_card_brand_id`          | string  | ID externo de marca de tarjeta                                         |
| `transaction.payments.payment_methods[].card.holder`                          | string  | Titular de tarjeta                                                     |
| `transaction.payments.payment_methods[].card.card_country`                    | string  | País de tarjeta                                                        |
| `transaction.payments.payment_methods[].transaction_date`                     | object  | Fecha de transacción                                                   |
| `transaction.payments.payment_methods[].transaction_date.date`                | string  | Fecha                                                                  |
| `transaction.payments.payment_methods[].transaction_date.time_zone_type`      | number  | Tipo de zona horaria                                                   |
| `transaction.payments.payment_methods[].transaction_date.time_zone_name`      | string  | Nombre de zona horaria                                                 |
| `transaction.payments.payment_methods[].additional_info_payment_methods`      | object  | Información adicional de métodos de pago                               |
| `transaction.additional_data`                                                 | array   | Datos adicionales (opcional)                                           |
| `transaction.additional_data[].key`                                           | string  | Clave                                                                  |
| `transaction.additional_data[].value`                                         | string  | Valor                                                                  |
| `transaction.invoice`                                                         | object  | Datos de facturación (respuesta de fe.builder)                         |
| `transaction.invoice.companyTaxData`                                          | object  | Datos tributarios de la empresa                                        |
| `transaction.invoice.companyTaxData.name`                                     | string  | Nombre de la empresa                                                   |
| `transaction.invoice.companyTaxData.identification_number`                    | string  | Número de identificación                                               |
| `transaction.invoice.companyTaxData.special_taxpayer`                         | string  | Contribuyente especial                                                 |
| `transaction.invoice.companyTaxData.isSpecial_taxpayer`                       | string  | Si es contribuyente especial                                           |
| `transaction.invoice.companyTaxData.special_taxpayer_code`                    | string  | Código de contribuyente especial                                       |
| `transaction.invoice.companyTaxData.type_tax`                                 | string  | Tipo de impuesto                                                       |
| `transaction.invoice.companyTaxData.obligatory_to_keep_accounts`              | string  | Si está obligado a llevar contabilidad                                 |
| `transaction.invoice.companyTaxData.resolution_code`                          | string  | Código de resolución                                                   |
| `transaction.invoice.companyTaxData.company_address`                          | string  | Dirección de la empresa                                                |
| `transaction.invoice.companyTaxData.restaurnt_address`                        | string  | Dirección del restaurante                                              |
| `transaction.invoice.companyTaxData.establishment_code`                       | string  | Código de establecimiento                                              |
| `transaction.invoice.companyTaxData.point_of_emission_code`                   | string  | Código de punto de emisión                                             |
| `transaction.invoice.dataInvoice`                                             | object  | Datos devueltos por el sistema de facturación al crear factura         |
| `transaction.invoice.dataInvoice.sequential`                                  | string  | Secuencial de factura                                                  |
| `transaction.invoice.dataInvoice.transaction`                                 | string  | Código de transacción                                                  |
| `transaction.invoice.dataInvoice.access_key`                                  | string  | Clave de acceso                                                        |
| `transaction.invoice.dataInvoice.legend`                                      | string  | Leyenda                                                                |
| `transaction.invoice.dataInvoice.link_label`                                  | string  | Etiqueta de enlace                                                     |
| `transaction.invoice.dataInvoice.url_document`                                | string  | URL del documento                                                      |
| `transaction.invoice.dataInvoice.access_key_label`                            | string  | Etiqueta de clave de acceso                                            |
| `transaction.invoice.dataInvoice.created_at`                                  | string  | Fecha de creación                                                      |
| `transaction.invoice.dataInvoice.document`                                    | object  | Documento de factura                                                   |
| `transaction.invoice.dataInvoice.document.client`                             | object  | Datos del cliente                                                      |
| `transaction.invoice.dataInvoice.document.orderInvoice`                       | object  | Orden de factura                                                       |
| `transaction.invoice.dataInvoice.document.payment_methods`                    | array   | Métodos de pago                                                        |
| `transaction.invoice.dataInvoice.document.additional_data`                    | array   | Datos adicionales                                                      |
| `transaction.invoice.dataCredit`                                              | object  | Datos de nota de crédito                                               |
| `transaction.annulation_comment`                                              | string  | Comentario de anulación                                                |

### Respuestas del Servidor

#### 200 OK - Integración Completada Exitosamente

```json
{
  "code": 200,
  "status": "success",
  "alert": "Integración completada exitosamente",
  "message": ["Integración completada exitosamente"],
  "data": {
    "companyTaxData": {
      "name": "INT FOOD SERVICES CORP SA",
      "identificationNumber": "1791415132001",
      "specialTaxpayer": "GRAN CONTRIBUYENTE",
      "isSpecialTaxpayer": "Sí",
      "specialTaxpayerCode": "NAC-GCFOIOC21-00000900-E",
      "typeTax": "Especial",
      "obligatoryToKeepAccounts": "Sí",
      "resolutionCode": "RES-2024-00123",
      "companyAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
      "restaurantAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
      "issueType": "Emisión Normal"
    },
    "dataInvoice": {
      "sequential": "050-070-000470031",
      "transaction": "K024F001529034",
      "access_key": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "legend": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
      "link_label": "Para obtener su factura electrónica ingrese a:",
      "url_document": "https://facturacion.kfc.ec",
      "access_key_label": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
      "created_at": "2024-09-11 12:14:40",
      "document": {
        "client": {
          "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
          "name": "María José ",
          "last_name": "Hernández Zurita ",
          "phone": "+593986610329",
          "email": "mari_jhz@hotmail.com",
          "gov_id_type": "CI",
          "gov_id_number": "0929691038"
        },
        "orderInvoice": {
          "order_id": "0001292432-010103",
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
                  "taxes_percentage": 15,
                  "tax_value": 0.85,
                  "total": 6.5,
                  "total_before_sale": 6.5,
                  "suggested_price": 0,
                  "taxes": [
                    {
                      "name": "IVA 15%",
                      "currency_code": "USD",
                      "subtotal_without_taxes": 5.65,
                      "percentage": 15,
                      "total": 0.85
                    }
                  ]
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
                  "suggested_price": 0,
                  "taxes": [
                    {
                      "name": "IVA 15%",
                      "currency_code": "USD",
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
            "transaction_type": "OTROS METODOS UTILIZANDO EL SISTEMA FINANCIERO",
            "transaction_id": "",
            "transaction_status": "APPROVED",
            "reference_number": null,
            "exact_payment": true,
            "customer_cash_amount": "0.0000",
            "total_bill": 6.5,
            "acquirer": {
              "code": " ",
              "name": " "
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
    },
    "dataCredit": {
      "sequential": "005-052-000000082",
      "accessKey": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "transaction": "G001N000000087",
      "legend": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
      "linkLabel": "Para obtener su factura electrónica ingrese a:",
      "urlDocument": "https://facturacion.kfc.ec",
      "accessKeyLabel": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
      "environment": "Pruebas",
      "createdAt": "2025-07-17T15:33:20.123",
      "document": {
        "client": {
          "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
          "name": "María José ",
          "last_name": "Hernández Zurita ",
          "phone": "+593986610329",
          "email": "mari_jhz@hotmail.com",
          "gov_id_number": "0929691038",
          "gov_id_type": "CI"
        },
        "orderInvoice": {
          "order_id": "0001292432-010103",
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
                      "tax_name": "IVA 10 %",
                      "tax_code": "iva23313",
                      "tax_percentage": 10,
                      "total_tax_vulue": 4.99,
                      "base_amount": 130
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
                      "tax_name": "IVA 10 %",
                      "tax_code": "iva23313",
                      "tax_percentage": 10,
                      "total_tax_vulue": 4.99,
                      "base_amount": 130
                    }
                  ]
                }
              }
            }
          ]
        },
        "payment_methods": [
          {
            "processor": "DEUNA",
            "currency_code": "USD",
            "payment_methods_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
            "payment_method_code": "93",
            "transaction_id": "",
            "transaction_status": "APPROVED",
            "reference_number": null,
            "exact_payment": true,
            "customer_cash_amount": "0.0000",
            "total_bill": 6.5,
            "additional_info_payment_methods": null,
            "transaction_type": "",
            "acquirer": {
              "code": " ",
              "name": " "
            },
            "transaction_date": {
              "date": "2024-09-11 05:14:41",
              "time_zone_type": 3,
              "time_zone_name": "America/Guayaquil"
            },
            "payment_methods_printer_name": ""
          }
        ],
        "additional_data": [
          {
            "key": "MARCA",
            "value": "TOYOTA"
          }
        ]
      },
      "motivo": "me equivoque!!"
    },
    "document_code": "04"
  }
}
```

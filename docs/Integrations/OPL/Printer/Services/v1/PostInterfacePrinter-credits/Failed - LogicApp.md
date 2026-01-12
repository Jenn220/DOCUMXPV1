## Generar Impresión de Venta con Cupón

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/generatePrinter
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "typePrinter": "VENTA-CUPON",
  "transaction": {
    "pointOfSale": {
      "id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "code": "EC-CAJA001",
      "cashierId": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "cashierName": "pepito",
      "platform": "ios",
      "account": "KFC",
      "accountId": 1,
      "source": "App",
      "channelId": 3,
      "channelName": "App"
    },
    "client": {
      "uid": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "name": "María José ",
      "lastName": "Hernández Zurita ",
      "phone": "+593986610329",
      "email": "mari_jhz@hotmail.com",
      "govIdType": "CI",
      "govIdNumber": "0929691038",
      "externalId": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "billingInformation": {
        "fullName": "María José  Hernández Zurita ",
        "govIdType": "CI",
        "govIdNumber": "0929691038",
        "phone": "0986610329",
        "email": "mari_jhz@hotmail.com",
        "address": "Guayaquil",
        "externalId": "030B9503-85CF-E511-80C6-000D3A3261F3"
      },
      "additionalInfo": {
        "birthdate": "",
        "gender": ""
      }
    },
    "order": {
      "orderId": "0001292432-010103",
      "createdAt": "2024-09-11 12:14:40",
      "selectedShippingMethod": "pickup",
      "accumulatePoints": false,
      "redeemPoints": false,
      "stock": false,
      "discount": false,
      "orderComment": "",
      "annulationComment": "",
      "products": [
        {
          "productId": "401",
          "product": "COMBO IDEAL",
          "quantity": 1,
          "productComment": "",
          "price": {
            "unitPrice": {
              "currencyCode": "USD",
              "subtotalWithoutTaxes": 5.65,
              "discountPercentage": 0,
              "discountsValue": 0,
              "subtotalIncludeDiscounts": 5.65,
              "taxesPercentage": 15,
              "taxValue": 0.85,
              "total": 6.5,
              "totalBeforeSale": 6.5,
              "suggestedPrice": 0
            },
            "totalPrice": {
              "currencyCode": "USD",
              "subtotalWithoutTaxes": 5.65,
              "discountPercentage": null,
              "discountsValue": 0,
              "subtotalIncludeDiscounts": 5.65,
              "taxesPercentage": 15,
              "taxValue": 0.85,
              "total": 6.5,
              "totalBeforeSale": 6.5,
              "suggestedPrice": 0
            }
          },
          "modifierGroups": [
            {
              "id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
              "description": "Es necesario elegir uno",
              "selectedModifiers": [
                {
                  "productId": "33616",
                  "product": "CRISPY",
                  "quantity": 1,
                  "removedQuantity": null,
                  "price": {
                    "unitPrice": {
                      "currencyCode": "USD",
                      "subtotalWithoutTaxes": 0,
                      "discountPercentage": 0,
                      "discountsValue": 0,
                      "subtotalIncludeDiscounts": 0,
                      "taxesPercentage": 15,
                      "taxValue": 0,
                      "total": 0,
                      "totalBeforeSale": 0,
                      "suggestedPrice": 0
                    },
                    "totalPrice": {
                      "currencyCode": "USD",
                      "subtotalWithoutTaxes": 0,
                      "discountPercentage": null,
                      "discountsValue": 0,
                      "subtotalIncludeDiscounts": 0,
                      "taxesPercentage": 15,
                      "taxValue": 0,
                      "total": 0,
                      "totalBeforeSale": 0,
                      "suggestedPrice": 0
                    }
                  },
                  "modifierGroups": [],
                  "additionalInfo": {
                    "redeemed": false,
                    "referenceUnitPrice": {
                      "currencyCode": "USD",
                      "subtotalWithoutTaxes": 0,
                      "discountPercentage": 0,
                      "discountsValue": 0,
                      "subtotalIncludeDiscounts": 0,
                      "taxesPercentage": 15,
                      "taxValue": 15,
                      "totalBeforeSale": 0,
                      "total": 0,
                      "suggestedPrice": 0
                    },
                    "referenceTotalPrice": {
                      "currencyCode": "USD",
                      "subtotalWithoutTaxes": 0,
                      "discountPercentage": 0,
                      "discountsValue": 0,
                      "subtotalIncludeDiscounts": 0,
                      "taxesPercentage": 15,
                      "taxValue": 0,
                      "total": 0,
                      "totalBeforeSale": 0,
                      "suggestedPrice": 0
                    }
                  }
                }
              ]
            }
          ],
          "additionalInfo": {
            "strategy": " ",
            "relatedProductId": " ",
            "redeemed": false,
            "sort": 1,
            "referenceUnitPrice": {
              "currencyCode": "USD",
              "subtotalWithoutTaxes": 5.65,
              "discountPercentage": 0,
              "discountsValue": 0,
              "subtotalIncludeDiscounts": 5.65,
              "taxesPercentage": 15,
              "taxValue": 15,
              "total": 6.5,
              "totalBeforeSale": 6.5,
              "suggestedPrice": 0
            },
            "referenceTotalPrice": {
              "currencyCode": "USD",
              "subtotalWithoutTaxes": 5.65,
              "discountPercentage": 0,
              "discountsValue": 0,
              "subtotalIncludeDiscounts": 5.65,
              "taxesPercentage": 15,
              "taxValue": 15,
              "total": 6.5,
              "totalBeforeSale": 6.5,
              "suggestedPrice": 0
            }
          }
        }
      ],
      "stockDetails": [
        {
          "productId": 1890,
          "stock": 0
        }
      ]
    },
    "shippingMethod": {
      "store": {
        "id": 431,
        "name": "SHOPPING DAULE",
        "code": "K078",
        "vendorId": 10,
        "vendorName": "KENTUCKY FRIED CHICKEN",
        "latitude": -1.854157,
        "longitude": -79.975704
      },
      "delivery": {
        "deliveryDate": "2024-09-11 12:14:40",
        "latitude": "",
        "longitude": "",
        "country": "ECUADOR",
        "city": "DAULE",
        "mainStreet": "GUAYAS / DAULE / EMILIANO CAICEDO MARCOS / AV VICENTE PIEDRAHITA S/N",
        "secondaryStreet": "N/A",
        "reference": "Ref: payload.client.shippingInfo.reference",
        "propertyId": 1,
        "observationsAddress": "-",
        "numberContactAddress": "0986610329",
        "zipCode": "",
        "nickName": "",
        "externalId": ""
      },
      "pickup": {
        "pickupDate": "2024-09-11 12:19:40",
        "prepDate": "2024-09-11 12:19:40",
        "prepTimeUnit": "minute",
        "prepTime": 5,
        "propertyId": 1,
        "carryOutOptions": "PickUp-LLevar"
      }
    },
    "payments": {
      "totals": [
        {
          "currencyCode": "USD",
          "subtotalWithoutTaxes": 5.65,
          "discountPercentage": 0,
          "discountsValue": 0,
          "subtotalIncludeDiscounts": 5.65,
          "taxesPercentage": 15,
          "taxValue": 0.85,
          "totalBeforeSale": 6.5,
          "total": 6.5
        },
        {
          "currencyCode": "Points",
          "subtotalWithoutTaxes": 0,
          "discountPercentage": 0,
          "discountsValue": 0,
          "subtotalIncludeDiscounts": 0,
          "taxesPercentage": 15,
          "taxValue": 0,
          "totalBeforeSale": 0,
          "total": 0
        }
      ],
      "shippingCost": [
        {
          "quantity": 0,
          "productId": 43,
          "currencyCode": "USD",
          "subtotalWithoutTaxes": 0,
          "discountPercentage": 0,
          "discountsValue": 0,
          "subtotalIncludeDiscounts": 0,
          "taxesPercentage": null,
          "taxValue": 0,
          "total": 0
        }
      ],
      "extraCharges": [
        {
          "quantity": null,
          "productId": null,
          "description": null,
          "currencyCode": null,
          "subtotalWithoutTaxes": 0,
          "discountPercentage": 0,
          "discountsValue": 0,
          "subtotalIncludeDiscounts": 0,
          "taxesPercentage": 0,
          "taxValue": 0,
          "total": 0
        }
      ],
      "taxes": [
        {
          "name": "IVA 15%",
          "currencyCode": "USD",
          "subtotalWithoutTaxes": 5.65,
          "percentage": 15,
          "total": 0.85
        }
      ],
      "discounts": [
        {
          "externalId": null,
          "name": "OFF5APP",
          "percentageDiscount": false,
          "amountDiscount": true,
          "currencyCode": "USD",
          "totalBeforeSale": 0,
          "subtotalWithoutDiscounts": 4.65,
          "percentage": 0,
          "total": 4.3478,
          "totalWithTaxes": 5
        }
      ],
      "paymentMethods": [
        {
          "processor": "DEUNA",
          "currencyCode": "USD",
          "paymentMethodCode": "93",
          "transactionType": "credit",
          "transactionId": "",
          "transactionStatus": "APPROVED",
          "tid": null,
          "mid": null,
          "authorizationCode": null,
          "voucher": null,
          "referenceNumber": null,
          "exactPayment": true,
          "customerCashAmount": "0.0000",
          "totalBill": 6.5,
          "acquirer": {
            "code": " ",
            "name": " "
          },
          "card": {
            "mask": "360857XXXXXXX2001",
            "bin": "360857",
            "lastFourDigits": "2001",
            "brand": "diners_club",
            "externalCardBrandId": "D20A9503-85CF-E511-80C6-000D3A3261F3",
            "holder": " ",
            "cardCountry": " "
          },
          "transactionDate": {
            "date": "2024-09-11 05:14:41",
            "timeZoneType": 3,
            "timeZoneName": "America/Guayaquil"
          },
          "additionalInfo": {
            "externalPaymentMethodId": "D20A9503-85CF-E511-80C6-000D3A3261F3"
          }
        }
      ]
    },
    "marketing": {
      "loyalty": {
        "accumulation": {
          "storeCost": 0,
          "marketingCost": 0,
          "totalPoints": 0
        },
        "redemption": {
          "storeCost": 0,
          "marketingCost": 0,
          "totalPoints": 0
        },
        "accountBalancePoints": 0
      }
    },
    "additionalInfo": {
      "kiosk": {
        "ip": ""
      },
      "pickupPhase": "INITIAL_PICKUP"
    }
  },
  "feBuilder": {
    "companyTaxData": {
      "name": "",
      "isSpecialTaxpayer": "1",
      "specialTaxpayerCode": "3243fdw23",
      "typeTax": "3243fdw23",
      "obligatoryToKeepAccounts": 1,
      "resolutionCode": "3243fdw23",
      "companyAddress": "3243fdw23",
      "restaurntAddress": "3243fdw23"
    },
    "dataInvocie": {
      "sequential": "001-001-32443243",
      "accessKey": "3423423423423432432423432423",
      "legend": "erugeruiegruegr",
      "urlDocument": "https:/sdfdsfsdf.codhgd",
      "createdAt": "2024-09-11 12:14:40"
    },
    "dataCredit": {
      "sequential": "001-001-32443243",
      "accessKey": "3423423423423432432423432423",
      "legend": "erugeruiegruegr",
      "urlDocument": "https:/sdfdsfsdf.codhgd",
      "createdAt": "2024-09-11 12:14:40",
      "detailCredit": {}
    }
  },
  "pubDevice": {
    "turnero": {
      "codeQr": "dsfsdfsd",
      "typeQr": "type1"
    },
    "kds": {}
  },
  "promotions": {
    "cupones": {
      "codeQr": "dsfsdfsd",
      "typeQr": "type1",
      "text": ""
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                          | Tipo    | Descripción                                                     |
| ------------------------------------------------------------------------------ | ------- | --------------------------------------------------------------- |
| `typePrinter`                                                                  | string  | Tipo de impresión de cupones                                    |
| `transaction`                                                                  | object  | Orden general con información de los puntos de venta            |
| `transaction.pointOfSale`                                                      | object  | Punto de venta con información física de quien realizó la venta |
| `transaction.pointOfSale.id`                                                   | string  | Identificador de caja                                           |
| `transaction.pointOfSale.code`                                                 | string  | Nombre o código de caja                                         |
| `transaction.pointOfSale.cashierId`                                            | string  | Identificador de cajero o vendedor                              |
| `transaction.pointOfSale.cashierName`                                          | string  | Nombre de cajero/usuario                                        |
| `transaction.pointOfSale.platform`                                             | string  | Sistema operativo donde se está vendiendo                       |
| `transaction.pointOfSale.account`                                              | string  | Franchise cuenta autorizada                                     |
| `transaction.pointOfSale.accountId`                                            | number  | ID de cuenta autorizada                                         |
| `transaction.pointOfSale.source`                                               | string  | Origen de aplicativo                                            |
| `transaction.pointOfSale.channelId`                                            | number  | ID de canal                                                     |
| `transaction.pointOfSale.channelName`                                          | string  | Nombre de canal                                                 |
| `transaction.client`                                                           | object  | Datos del cliente comprador y de facturación                    |
| `transaction.client.uid`                                                       | string  | Identificador del cliente                                       |
| `transaction.client.name`                                                      | string  | Nombre del cliente                                              |
| `transaction.client.lastName`                                                  | string  | Apellido del cliente                                            |
| `transaction.client.phone`                                                     | string  | Teléfono de comprador                                           |
| `transaction.client.email`                                                     | string  | Correo del comprador                                            |
| `transaction.client.govIdType`                                                 | string  | Tipo de documento                                               |
| `transaction.client.govIdNumber`                                               | string  | Identificación de gobierno de contribuyente                     |
| `transaction.client.externalId`                                                | string  | ID de referencia                                                |
| `transaction.client.billingInformation`                                        | object  | Datos de facturación electrónica                                |
| `transaction.client.billingInformation.fullName`                               | string  | Nombre de contribuyente                                         |
| `transaction.client.billingInformation.govIdType`                              | string  | Tipo de documento                                               |
| `transaction.client.billingInformation.govIdNumber`                            | string  | Identificador de contribuyente                                  |
| `transaction.client.billingInformation.phone`                                  | string  | Teléfono                                                        |
| `transaction.client.billingInformation.email`                                  | string  | Correo electrónico                                              |
| `transaction.client.billingInformation.address`                                | string  | Dirección                                                       |
| `transaction.client.billingInformation.externalId`                             | string  | ID de referencia                                                |
| `transaction.client.additionalInfo`                                            | object  | Información adicional                                           |
| `transaction.client.additionalInfo.birthdate`                                  | string  | Cumpleaños                                                      |
| `transaction.client.additionalInfo.gender`                                     | string  | Género                                                          |
| `transaction.order`                                                            | object  | Detalles de los plus, precios y modificadores utilizados        |
| `transaction.order.orderId`                                                    | string  | ID de orden generada por el Punto de Ventas                     |
| `transaction.order.createdAt`                                                  | string  | Fecha de creación de orden de venta                             |
| `transaction.order.selectedShippingMethod`                                     | string  | Método de envío                                                 |
| `transaction.order.accumulatePoints`                                           | boolean | Si es una venta con temas de fidelización                       |
| `transaction.order.redeemPoints`                                               | boolean | Si es una venta con temas de fidelización                       |
| `transaction.order.stock`                                                      | boolean | Si es una venta con temas de inventario                         |
| `transaction.order.discount`                                                   | boolean | Si es una venta con descuentos                                  |
| `transaction.order.orderComment`                                               | string  | Comentario de la orden                                          |
| `transaction.order.annulationComment`                                          | string  | Comentario de la anulación motivo                               |
| `transaction.order.products`                                                   | array   | Detalles de items                                               |
| `transaction.order.products[].productId`                                       | string  | ID de plus                                                      |
| `transaction.order.products[].product`                                         | string  | Nombre del plus vendido                                         |
| `transaction.order.products[].quantity`                                        | number  | Cantidad de plus vendido                                        |
| `transaction.order.products[].productComment`                                  | string  | Comentario de plus vendido                                      |
| `transaction.order.products[].price`                                           | object  | Detalles de precios                                             |
| `transaction.order.products[].price.unitPrice`                                 | object  | Detalle por unidad                                              |
| `transaction.order.products[].price.unitPrice.currencyCode`                    | string  | Código de moneda                                                |
| `transaction.order.products[].price.unitPrice.subtotalWithoutTaxes`            | number  | Subtotal sin impuestos                                          |
| `transaction.order.products[].price.unitPrice.discountPercentage`              | number  | Porcentaje de descuento                                         |
| `transaction.order.products[].price.unitPrice.discountsValue`                  | number  | Valor de descuentos                                             |
| `transaction.order.products[].price.unitPrice.subtotalIncludeDiscounts`        | number  | Subtotal incluyendo descuentos                                  |
| `transaction.order.products[].price.unitPrice.taxesPercentage`                 | number  | Porcentaje de impuestos                                         |
| `transaction.order.products[].price.unitPrice.taxValue`                        | number  | Valor de impuesto                                               |
| `transaction.order.products[].price.unitPrice.total`                           | number  | Total                                                           |
| `transaction.order.products[].price.unitPrice.totalBeforeSale`                 | number  | Total antes de venta                                            |
| `transaction.order.products[].price.unitPrice.suggestedPrice`                  | number  | Precio sugerido                                                 |
| `transaction.order.products[].price.totalPrice`                                | object  | Detalles de totales por la cantidad de plus                     |
| `transaction.order.products[].modifierGroups`                                  | array   | Modificadores de plus                                           |
| `transaction.order.products[].modifierGroups[].id`                             | string  | ID del grupo de modificadores                                   |
| `transaction.order.products[].modifierGroups[].description`                    | string  | Descripción                                                     |
| `transaction.order.products[].modifierGroups[].selectedModifiers`              | array   | Modificadores seleccionados                                     |
| `transaction.order.products[].additionalInfo`                                  | object  | Información adicional a nivel de la orden detail                |
| `transaction.order.products[].additionalInfo.strategy`                         | string  | Estrategia                                                      |
| `transaction.order.products[].additionalInfo.relatedProductId`                 | string  | ID del producto relacionado                                     |
| `transaction.order.products[].additionalInfo.redeemed`                         | boolean | Si fue redimido                                                 |
| `transaction.order.products[].additionalInfo.sort`                             | number  | Orden                                                           |
| `transaction.order.stockDetails`                                               | array   | Cuando se realiza proceso de stock - inventario de venta        |
| `transaction.order.stockDetails[].productId`                                   | number  | ID artículos                                                    |
| `transaction.order.stockDetails[].stock`                                       | number  | Cantidad de inventario de venta                                 |
| `transaction.shippingMethod`                                                   | object  | Información de método de entrega de la transacción              |
| `transaction.shippingMethod.store`                                             | object  | Datos de la tienda                                              |
| `transaction.shippingMethod.store.id`                                          | number  | ID de la tienda                                                 |
| `transaction.shippingMethod.store.name`                                        | string  | Nombre de la tienda                                             |
| `transaction.shippingMethod.store.code`                                        | string  | Código de la tienda                                             |
| `transaction.shippingMethod.store.vendorId`                                    | number  | ID del vendedor                                                 |
| `transaction.shippingMethod.store.vendorName`                                  | string  | Nombre del vendedor                                             |
| `transaction.shippingMethod.store.latitude`                                    | number  | Latitud                                                         |
| `transaction.shippingMethod.store.longitude`                                   | number  | Longitud                                                        |
| `transaction.shippingMethod.delivery`                                          | object  | Datos de delivery                                               |
| `transaction.shippingMethod.delivery.deliveryDate`                             | string  | Fecha de entrega                                                |
| `transaction.shippingMethod.delivery.latitude`                                 | string  | Latitud                                                         |
| `transaction.shippingMethod.delivery.longitude`                                | string  | Longitud                                                        |
| `transaction.shippingMethod.delivery.country`                                  | string  | País                                                            |
| `transaction.shippingMethod.delivery.city`                                     | string  | Ciudad                                                          |
| `transaction.shippingMethod.delivery.mainStreet`                               | string  | Calle principal                                                 |
| `transaction.shippingMethod.delivery.secondaryStreet`                          | string  | Calle secundaria                                                |
| `transaction.shippingMethod.delivery.reference`                                | string  | Referencia                                                      |
| `transaction.shippingMethod.delivery.propertyId`                               | number  | ID de propiedad                                                 |
| `transaction.shippingMethod.delivery.observationsAddress`                      | string  | Observaciones de dirección                                      |
| `transaction.shippingMethod.delivery.numberContactAddress`                     | string  | Número de contacto de dirección                                 |
| `transaction.shippingMethod.delivery.zipCode`                                  | string  | Código postal                                                   |
| `transaction.shippingMethod.delivery.nickName`                                 | string  | Apodo                                                           |
| `transaction.shippingMethod.delivery.externalId`                               | string  | ID externo                                                      |
| `transaction.shippingMethod.pickup`                                            | object  | Datos de pickup                                                 |
| `transaction.shippingMethod.pickup.pickupDate`                                 | string  | Fecha de pickup                                                 |
| `transaction.shippingMethod.pickup.prepDate`                                   | string  | Fecha de preparación                                            |
| `transaction.shippingMethod.pickup.prepTimeUnit`                               | string  | Unidad de tiempo de preparación                                 |
| `transaction.shippingMethod.pickup.prepTime`                                   | number  | Tiempo de preparación                                           |
| `transaction.shippingMethod.pickup.propertyId`                                 | number  | ID de propiedad                                                 |
| `transaction.shippingMethod.pickup.carryOutOptions`                            | string  | Opciones de llevar                                              |
| `transaction.payments`                                                         | object  | Datos en relación a los pagos utilizados para la transacción    |
| `transaction.payments.totals`                                                  | array   | Totales                                                         |
| `transaction.payments.totals[].currencyCode`                                   | string  | Código de moneda                                                |
| `transaction.payments.totals[].subtotalWithoutTaxes`                           | number  | Subtotal sin impuestos                                          |
| `transaction.payments.totals[].discountPercentage`                             | number  | Porcentaje de descuento                                         |
| `transaction.payments.totals[].discountsValue`                                 | number  | Valor de descuentos                                             |
| `transaction.payments.totals[].subtotalIncludeDiscounts`                       | number  | Subtotal incluyendo descuentos                                  |
| `transaction.payments.totals[].taxesPercentage`                                | number  | Porcentaje de impuestos                                         |
| `transaction.payments.totals[].taxValue`                                       | number  | Valor de impuesto                                               |
| `transaction.payments.totals[].totalBeforeSale`                                | number  | Total antes de venta                                            |
| `transaction.payments.totals[].total`                                          | number  | Total                                                           |
| `transaction.payments.shippingCost`                                            | array   | Costo de envío                                                  |
| `transaction.payments.shippingCost[].quantity`                                 | number  | Cantidad                                                        |
| `transaction.payments.shippingCost[].productId`                                | number  | ID del producto                                                 |
| `transaction.payments.shippingCost[].currencyCode`                             | string  | Código de moneda                                                |
| `transaction.payments.shippingCost[].subtotalWithoutTaxes`                     | number  | Subtotal sin impuestos                                          |
| `transaction.payments.shippingCost[].discountPercentage`                       | number  | Porcentaje de descuento                                         |
| `transaction.payments.shippingCost[].discountsValue`                           | number  | Valor de descuentos                                             |
| `transaction.payments.shippingCost[].subtotalIncludeDiscounts`                 | number  | Subtotal incluyendo descuentos                                  |
| `transaction.payments.shippingCost[].taxesPercentage`                          | number  | Porcentaje de impuestos                                         |
| `transaction.payments.shippingCost[].taxValue`                                 | number  | Valor de impuesto                                               |
| `transaction.payments.shippingCost[].total`                                    | number  | Total                                                           |
| `transaction.payments.extraCharges`                                            | array   | Cargos extra                                                    |
| `transaction.payments.taxes`                                                   | array   | Impuestos                                                       |
| `transaction.payments.taxes[].name`                                            | string  | Nombre del impuesto                                             |
| `transaction.payments.taxes[].currencyCode`                                    | string  | Código de moneda                                                |
| `transaction.payments.taxes[].subtotalWithoutTaxes`                            | number  | Subtotal sin impuestos                                          |
| `transaction.payments.taxes[].percentage`                                      | number  | Porcentaje                                                      |
| `transaction.payments.taxes[].total`                                           | number  | Total                                                           |
| `transaction.payments.discounts`                                               | array   | Descuentos                                                      |
| `transaction.payments.discounts[].externalId`                                  | string  | ID externo                                                      |
| `transaction.payments.discounts[].name`                                        | string  | Nombre                                                          |
| `transaction.payments.discounts[].percentageDiscount`                          | boolean | Si es descuento porcentual                                      |
| `transaction.payments.discounts[].amountDiscount`                              | boolean | Si es descuento en monto                                        |
| `transaction.payments.discounts[].currencyCode`                                | string  | Código de moneda                                                |
| `transaction.payments.discounts[].totalBeforeSale`                             | number  | Total antes de venta                                            |
| `transaction.payments.discounts[].subtotalWithoutDiscounts`                    | number  | Subtotal sin descuentos                                         |
| `transaction.payments.discounts[].percentage`                                  | number  | Porcentaje                                                      |
| `transaction.payments.discounts[].total`                                       | number  | Total                                                           |
| `transaction.payments.discounts[].totalWithTaxes`                              | number  | Total con impuestos                                             |
| `transaction.payments.paymentMethods`                                          | array   | Tipo de pagos que se ocupó para la transacción                  |
| `transaction.payments.paymentMethods[].processor`                              | string  | Procesador                                                      |
| `transaction.payments.paymentMethods[].currencyCode`                           | string  | Código de moneda                                                |
| `transaction.payments.paymentMethods[].paymentMethodCode`                      | string  | Código del método de pago                                       |
| `transaction.payments.paymentMethods[].transactionType`                        | string  | Tipo de transacción                                             |
| `transaction.payments.paymentMethods[].transactionId`                          | string  | ID de transacción                                               |
| `transaction.payments.paymentMethods[].transactionStatus`                      | string  | Estado de transacción                                           |
| `transaction.payments.paymentMethods[].tid`                                    | string  | TID                                                             |
| `transaction.payments.paymentMethods[].mid`                                    | string  | MID                                                             |
| `transaction.payments.paymentMethods[].authorizationCode`                      | string  | Código de autorización                                          |
| `transaction.payments.paymentMethods[].voucher`                                | string  | Voucher                                                         |
| `transaction.payments.paymentMethods[].referenceNumber`                        | string  | Número de referencia                                            |
| `transaction.payments.paymentMethods[].exactPayment`                           | boolean | Si es pago exacto                                               |
| `transaction.payments.paymentMethods[].customerCashAmount`                     | string  | Monto en efectivo del cliente                                   |
| `transaction.payments.paymentMethods[].totalBill`                              | number  | Total de la cuenta                                              |
| `transaction.payments.paymentMethods[].acquirer`                               | object  | Adquiriente                                                     |
| `transaction.payments.paymentMethods[].acquirer.code`                          | string  | Código                                                          |
| `transaction.payments.paymentMethods[].acquirer.name`                          | string  | Nombre                                                          |
| `transaction.payments.paymentMethods[].card`                                   | object  | Datos de tarjeta                                                |
| `transaction.payments.paymentMethods[].card.mask`                              | string  | Máscara de tarjeta                                              |
| `transaction.payments.paymentMethods[].card.bin`                               | string  | BIN                                                             |
| `transaction.payments.paymentMethods[].card.lastFourDigits`                    | string  | Últimos cuatro dígitos                                          |
| `transaction.payments.paymentMethods[].card.brand`                             | string  | Marca de tarjeta                                                |
| `transaction.payments.paymentMethods[].card.externalCardBrandId`               | string  | ID externo de marca de tarjeta                                  |
| `transaction.payments.paymentMethods[].card.holder`                            | string  | Titular                                                         |
| `transaction.payments.paymentMethods[].card.cardCountry`                       | string  | País de tarjeta                                                 |
| `transaction.payments.paymentMethods[].transactionDate`                        | object  | Fecha de transacción                                            |
| `transaction.payments.paymentMethods[].transactionDate.date`                   | string  | Fecha                                                           |
| `transaction.payments.paymentMethods[].transactionDate.timeZoneType`           | number  | Tipo de zona horaria                                            |
| `transaction.payments.paymentMethods[].transactionDate.timeZoneName`           | string  | Nombre de zona horaria                                          |
| `transaction.payments.paymentMethods[].additionalInfo`                         | object  | Información adicional                                           |
| `transaction.payments.paymentMethods[].additionalInfo.externalPaymentMethodId` | string  | ID externo de método de pago                                    |
| `transaction.marketing`                                                        | object  | Información que se utiliza para marketing                       |
| `transaction.marketing.loyalty`                                                | object  | Lealtad                                                         |
| `transaction.marketing.loyalty.accumulation`                                   | object  | Acumulación                                                     |
| `transaction.marketing.loyalty.accumulation.storeCost`                         | number  | Costo de tienda                                                 |
| `transaction.marketing.loyalty.accumulation.marketingCost`                     | number  | Costo de marketing                                              |
| `transaction.marketing.loyalty.accumulation.totalPoints`                       | number  | Total de puntos                                                 |
| `transaction.marketing.loyalty.redemption`                                     | object  | Redención                                                       |
| `transaction.marketing.loyalty.redemption.storeCost`                           | number  | Costo de tienda                                                 |
| `transaction.marketing.loyalty.redemption.marketingCost`                       | number  | Costo de marketing                                              |
| `transaction.marketing.loyalty.redemption.totalPoints`                         | number  | Total de puntos                                                 |
| `transaction.marketing.loyalty.accountBalancePoints`                           | number  | Balance de puntos de cuenta                                     |
| `transaction.additionalInfo`                                                   | object  | Información adicional de la transacción en general              |
| `transaction.additionalInfo.kiosk`                                             | object  | Datos de kiosk                                                  |
| `transaction.additionalInfo.kiosk.ip`                                          | string  | IP                                                              |
| `transaction.additionalInfo.pickupPhase`                                       | string  | Fase de pickup                                                  |
| `feBuilder`                                                                    | object  | Datos de facturación lo responde fe.builder                     |
| `feBuilder.companyTaxData`                                                     | object  | Datos fiscales de la empresa                                    |
| `feBuilder.companyTaxData.name`                                                | string  | Nombre                                                          |
| `feBuilder.companyTaxData.isSpecialTaxpayer`                                   | string  | Es contribuyente especial                                       |
| `feBuilder.companyTaxData.specialTaxpayerCode`                                 | string  | Código de contribuyente especial                                |
| `feBuilder.companyTaxData.typeTax`                                             | string  | Tipo de impuesto                                                |
| `feBuilder.companyTaxData.obligatoryToKeepAccounts`                            | number  | Obligado a llevar contabilidad                                  |
| `feBuilder.companyTaxData.resolutionCode`                                      | string  | Código de resolución                                            |
| `feBuilder.companyTaxData.companyAddress`                                      | string  | Dirección de la empresa                                         |
| `feBuilder.companyTaxData.restaurntAddress`                                    | string  | Dirección del restaurante                                       |
| `feBuilder.dataInvocie`                                                        | object  | Datos que devuelve el sistema al crear la factura               |
| `feBuilder.dataInvocie.sequential`                                             | string  | Secuencial                                                      |
| `feBuilder.dataInvocie.accessKey`                                              | string  | Clave de acceso                                                 |
| `feBuilder.dataInvocie.legend`                                                 | string  | Leyenda                                                         |
| `feBuilder.dataInvocie.urlDocument`                                            | string  | URL del documento                                               |
| `feBuilder.dataInvocie.createdAt`                                              | string  | Fecha de creación                                               |
| `feBuilder.dataCredit`                                                         | object  | Datos que devuelve el sistema al crear una nota de crédito      |
| `feBuilder.dataCredit.sequential`                                              | string  | Secuencial                                                      |
| `feBuilder.dataCredit.accessKey`                                               | string  | Clave de acceso                                                 |
| `feBuilder.dataCredit.legend`                                                  | string  | Leyenda                                                         |
| `feBuilder.dataCredit.urlDocument`                                             | string  | URL del documento                                               |
| `feBuilder.dataCredit.createdAt`                                               | string  | Fecha de creación                                               |
| `feBuilder.dataCredit.detailCredit`                                            | object  | Detalle de crédito                                              |
| `pubDevice`                                                                    | object  | Datos de device lo responde pubDevice                           |
| `pubDevice.turnero`                                                            | object  | Información para impresión del QR turnero                       |
| `pubDevice.turnero.codeQr`                                                     | string  | Código QR                                                       |
| `pubDevice.turnero.typeQr`                                                     | string  | Tipo QR                                                         |
| `pubDevice.kds`                                                                | object  | KDS                                                             |
| `promotions`                                                                   | object  | Datos a imprimir en relación a promociones                      |
| `promotions.cupones`                                                           | object  | Cupones                                                         |
| `promotions.cupones.codeQr`                                                    | string  | Código QR                                                       |
| `promotions.cupones.typeQr`                                                    | string  | Tipo QR                                                         |
| `promotions.cupones.text`                                                      | string  | Texto                                                           |

### Respuestas del Servidor

#### 400 Bad Request - Error en la Impresión

```json
{
  "code": 400,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["Plantilla no cumple formato"]
}
```

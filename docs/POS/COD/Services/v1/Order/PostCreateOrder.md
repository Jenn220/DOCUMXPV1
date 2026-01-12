## Crear Orden COD

### Método HTTP

`POST`

### URL

```
{{server_cod}}/api/cod/order/create
```

### Headers

| Key           | Value            | Descripción                       |
| ------------- | ---------------- | --------------------------------- |
| Content-Type  | application/json | Tipo de contenido de la solicitud |
| Authorization | Bearer {{token}} | Token de autenticación            |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "orderId": "902499bf-284f-4f2e-80b7-60ef60c6bd9c",
  "accountId": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "account": "KFC Account",
  "source": "KIOSK",
  "platform": "WEB",
  "createdAt": "2025-12-08T10:30:00Z",
  "channelId": "568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d",
  "channelName": "KIOSK",
  "selectedShippingMethod": "PICKUP",
  "accumulatePoints": true,
  "redeemPoints": false,
  "discount": false,
  "orderComment": "Sin cebolla por favor",
  "client": {
    "name": "Juan",
    "lastName": "Pérez",
    "phone": "+525512345678",
    "email": "juan.perez@example.com",
    "govIdType": "RFC",
    "govIdNumber": "XAXX010101000",
    "billingInformation": {
      "rfc": "XAXX010101000",
      "businessName": "Empresa Demo SA de CV",
      "zipCode": "01000"
    },
    "additionalInfo": {
      "loyaltyId": "12345678",
      "membershipLevel": "GOLD"
    }
  },
  "store": {
    "id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
    "name": "KFC Reforma",
    "vendorId": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
    "vendorName": "KFC México",
    "latitude": "19.432608",
    "longitude": "-99.133209"
  },
  "order": {
    "products": [
      {
        "productId": "9bdeeb7f-136c-8f6a-489b-d9fc02db904a",
        "product": "Combo Coronel",
        "quantity": 2,
        "productComment": "Extra crujiente",
        "additionalInfo": {
          "pluId": "PLU001",
          "categoryId": "CAT001"
        },
        "price": {
          "unitPrice": 149.0,
          "totalPrice": 298.0,
          "currency": "MXN"
        },
        "modifierGroups": [
          {
            "id": "MOD001",
            "name": "Bebidas",
            "modifiers": [
              {
                "id": "BEB001",
                "name": "Coca Cola",
                "quantity": 1,
                "price": 0.0
              }
            ]
          }
        ]
      },
      {
        "productId": "7acddef8-245b-9e5c-6789-e8fd13ec915b",
        "product": "Papas Grandes",
        "quantity": 1,
        "productComment": "",
        "additionalInfo": {
          "pluId": "PLU002",
          "categoryId": "CAT002"
        },
        "price": {
          "unitPrice": 45.0,
          "totalPrice": 45.0,
          "currency": "MXN"
        },
        "modifierGroups": []
      }
    ]
  },
  "shippingMethod": {
    "delivery": null,
    "pickup": {
      "pickupTime": "2025-12-08T11:30:00Z",
      "pickupType": "COUNTER",
      "estimatedTime": 15
    }
  },
  "payments": {
    "totals": [
      {
        "subtotal": 343.0,
        "total": 398.28,
        "currency": "MXN"
      }
    ],
    "shippingCost": [
      {
        "amount": 0.0,
        "currency": "MXN"
      }
    ],
    "extraCharges": [
      {
        "name": "Servicio",
        "amount": 5.0,
        "currency": "MXN"
      }
    ],
    "taxes": [
      {
        "taxId": "568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d",
        "name": "IVA",
        "rate": 16,
        "amount": 50.28,
        "currency": "MXN"
      }
    ],
    "discounts": [
      {
        "discountId": "DISC001",
        "name": "Descuento Cliente Frecuente",
        "amount": 0.0,
        "percentage": 0,
        "currency": "MXN"
      }
    ],
    "paymentMethods": [
      {
        "methodId": "CARD001",
        "methodName": "Tarjeta de Crédito",
        "methodType": "CREDIT_CARD",
        "amount": 398.28,
        "currency": "MXN",
        "transactionId": "TRX123456789",
        "status": "APPROVED"
      }
    ]
  },
  "additionalInfo": {
    "kiosk": {
      "kioskId": "8028a2ff-c639-6df4-68e8-8982c0256be3",
      "kioskName": "Kiosco 1",
      "sessionId": "SESSION123"
    },
    "promotionalNotification": {
      "enabled": true,
      "smsNotification": true,
      "emailNotification": true
    },
    "membership": {
      "memberId": "MEM123456",
      "membershipType": "PREMIUM",
      "points": 1500
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                      | Tipo    | Descripción                            |
| ---------------------------------------------------------- | ------- | -------------------------------------- |
| `orderId`                                                  | string  | Identificador único de la orden        |
| `accountId`                                                | string  | Identificador de la cuenta             |
| `account`                                                  | string  | Nombre de la cuenta                    |
| `source`                                                   | string  | Origen de la orden                     |
| `platform`                                                 | string  | Plataforma de origen                   |
| `createdAt`                                                | string  | Fecha y hora de creación (formato ISO) |
| `channelId`                                                | string  | Identificador del canal                |
| `channelName`                                              | string  | Nombre del canal                       |
| `selectedShippingMethod`                                   | string  | Método de envío seleccionado           |
| `accumulatePoints`                                         | boolean | Indica si acumula puntos               |
| `redeemPoints`                                             | boolean | Indica si redime puntos                |
| `discount`                                                 | boolean | Indica si tiene descuento              |
| `orderComment`                                             | string  | Comentario de la orden                 |
| `client`                                                   | object  | Información del cliente                |
| `client.name`                                              | string  | Nombre del cliente                     |
| `client.lastName`                                          | string  | Apellido del cliente                   |
| `client.phone`                                             | string  | Teléfono del cliente                   |
| `client.email`                                             | string  | Correo electrónico del cliente         |
| `client.govIdType`                                         | string  | Tipo de documento de identidad         |
| `client.govIdNumber`                                       | string  | Número de documento de identidad       |
| `client.billingInformation`                                | object  | Información de facturación             |
| `client.billingInformation.rfc`                            | string  | RFC del cliente                        |
| `client.billingInformation.businessName`                   | string  | Razón social                           |
| `client.billingInformation.zipCode`                        | string  | Código postal                          |
| `client.additionalInfo`                                    | object  | Información adicional del cliente      |
| `client.additionalInfo.loyaltyId`                          | string  | Identificador de lealtad               |
| `client.additionalInfo.membershipLevel`                    | string  | Nivel de membresía                     |
| `store`                                                    | object  | Información de la tienda               |
| `store.id`                                                 | string  | Identificador de la tienda             |
| `store.name`                                               | string  | Nombre de la tienda                    |
| `store.vendorId`                                           | string  | Identificador del vendedor             |
| `store.vendorName`                                         | string  | Nombre del vendedor                    |
| `store.latitude`                                           | string  | Latitud de la ubicación                |
| `store.longitude`                                          | string  | Longitud de la ubicación               |
| `order`                                                    | object  | Información de la orden                |
| `order.products`                                           | array   | Lista de productos                     |
| `order.products[].productId`                               | string  | Identificador del producto             |
| `order.products[].product`                                 | string  | Nombre del producto                    |
| `order.products[].quantity`                                | number  | Cantidad del producto                  |
| `order.products[].productComment`                          | string  | Comentario del producto                |
| `order.products[].additionalInfo`                          | object  | Información adicional del producto     |
| `order.products[].additionalInfo.pluId`                    | string  | Identificador PLU                      |
| `order.products[].additionalInfo.categoryId`               | string  | Identificador de categoría             |
| `order.products[].price`                                   | object  | Información de precio                  |
| `order.products[].price.unitPrice`                         | number  | Precio unitario                        |
| `order.products[].price.totalPrice`                        | number  | Precio total                           |
| `order.products[].price.currency`                          | string  | Moneda                                 |
| `order.products[].modifierGroups`                          | array   | Grupos de modificadores                |
| `order.products[].modifierGroups[].id`                     | string  | Identificador del grupo                |
| `order.products[].modifierGroups[].name`                   | string  | Nombre del grupo                       |
| `order.products[].modifierGroups[].modifiers`              | array   | Lista de modificadores                 |
| `order.products[].modifierGroups[].modifiers[].id`         | string  | Identificador del modificador          |
| `order.products[].modifierGroups[].modifiers[].name`       | string  | Nombre del modificador                 |
| `order.products[].modifierGroups[].modifiers[].quantity`   | number  | Cantidad del modificador               |
| `order.products[].modifierGroups[].modifiers[].price`      | number  | Precio del modificador                 |
| `shippingMethod`                                           | object  | Método de envío                        |
| `shippingMethod.delivery`                                  | null    | Información de entrega                 |
| `shippingMethod.pickup`                                    | object  | Información de recogida                |
| `shippingMethod.pickup.pickupTime`                         | string  | Hora de recogida (formato ISO)         |
| `shippingMethod.pickup.pickupType`                         | string  | Tipo de recogida                       |
| `shippingMethod.pickup.estimatedTime`                      | number  | Tiempo estimado en minutos             |
| `payments`                                                 | object  | Información de pagos                   |
| `payments.totals`                                          | array   | Lista de totales                       |
| `payments.totals[].subtotal`                               | number  | Subtotal                               |
| `payments.totals[].total`                                  | number  | Total                                  |
| `payments.totals[].currency`                               | string  | Moneda                                 |
| `payments.shippingCost`                                    | array   | Costo de envío                         |
| `payments.shippingCost[].amount`                           | number  | Monto del envío                        |
| `payments.shippingCost[].currency`                         | string  | Moneda                                 |
| `payments.extraCharges`                                    | array   | Cargos adicionales                     |
| `payments.extraCharges[].name`                             | string  | Nombre del cargo                       |
| `payments.extraCharges[].amount`                           | number  | Monto del cargo                        |
| `payments.extraCharges[].currency`                         | string  | Moneda                                 |
| `payments.taxes`                                           | array   | Lista de impuestos                     |
| `payments.taxes[].taxId`                                   | string  | Identificador del impuesto             |
| `payments.taxes[].name`                                    | string  | Nombre del impuesto                    |
| `payments.taxes[].rate`                                    | number  | Tasa del impuesto                      |
| `payments.taxes[].amount`                                  | number  | Monto del impuesto                     |
| `payments.taxes[].currency`                                | string  | Moneda                                 |
| `payments.discounts`                                       | array   | Lista de descuentos                    |
| `payments.discounts[].discountId`                          | string  | Identificador del descuento            |
| `payments.discounts[].name`                                | string  | Nombre del descuento                   |
| `payments.discounts[].amount`                              | number  | Monto del descuento                    |
| `payments.discounts[].percentage`                          | number  | Porcentaje del descuento               |
| `payments.discounts[].currency`                            | string  | Moneda                                 |
| `payments.paymentMethods`                                  | array   | Métodos de pago                        |
| `payments.paymentMethods[].methodId`                       | string  | Identificador del método               |
| `payments.paymentMethods[].methodName`                     | string  | Nombre del método                      |
| `payments.paymentMethods[].methodType`                     | string  | Tipo de método                         |
| `payments.paymentMethods[].amount`                         | number  | Monto del pago                         |
| `payments.paymentMethods[].currency`                       | string  | Moneda                                 |
| `payments.paymentMethods[].transactionId`                  | string  | Identificador de transacción           |
| `payments.paymentMethods[].status`                         | string  | Estado del pago                        |
| `additionalInfo`                                           | object  | Información adicional                  |
| `additionalInfo.kiosk`                                     | object  | Información del kiosco                 |
| `additionalInfo.kiosk.kioskId`                             | string  | Identificador del kiosco               |
| `additionalInfo.kiosk.kioskName`                           | string  | Nombre del kiosco                      |
| `additionalInfo.kiosk.sessionId`                           | string  | Identificador de sesión                |
| `additionalInfo.promotionalNotification`                   | object  | Notificaciones promocionales           |
| `additionalInfo.promotionalNotification.enabled`           | boolean | Indica si está habilitado              |
| `additionalInfo.promotionalNotification.smsNotification`   | boolean | Notificación por SMS                   |
| `additionalInfo.promotionalNotification.emailNotification` | boolean | Notificación por correo                |
| `additionalInfo.membership`                                | object  | Información de membresía               |
| `additionalInfo.membership.memberId`                       | string  | Identificador de miembro               |
| `additionalInfo.membership.membershipType`                 | string  | Tipo de membresía                      |
| `additionalInfo.membership.points`                         | number  | Puntos acumulados                      |

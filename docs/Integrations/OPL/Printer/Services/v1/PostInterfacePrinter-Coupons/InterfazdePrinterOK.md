## Generar Impresión de Cupón

### Método HTTP

`POST`

### URL

{{serverPrinter}}/api/v1/transaction/TX014

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "type_printer": "CUPON",
  "transaction": {
    "transaction_date": "",
    "point_of_sale": {
      "cdn_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
      "restaurant_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
      "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "cash_register_name": "EC-CAJA001",
      "user_seller_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "user_seller_name": "Akiles Baesta",
      "device_os_name": "ios",
      "source_app_name": "Maxpoint 2.0",
      "half_integration_id": 3,
      "half_integration_name": "Local",
      "user_admin": "Carlos Zambrano",
      "restaurant_name": "G008 - EL INCA",
      "franchise_name": "GUS"
    },
    "coupons": {
      "code_coupon": "0002816S100389810000001EQLW19489",
      "code_detail": "CKFCA003804",
      "effective_date": "",
      "redemption_date": "",
      "type_coupon": "Credito"
    },
    "client": {
      "code": "ECUpas123456",
      "identification": "0503684920",
      "client": "ANGEL  AGUAIZA USHCO",
      "phone": "+593995707586",
      "email": "er@gmail.com.",
      "address": "Barrio Matilde de Alvarez",
      "additional_info": {
        "birthdate": "",
        "disclaimer": ""
      }
    },
    "order": {
      "order_id": "902499bf-284f-4f2e-80b7-60ef60c6bd9c",
      "createdAt": "2025-10-09T16:26:24.943Z",
      "order_comment": "",
      "products": [
        {
          "code_detail": "CKFCA003804",
          "plu_id": 4,
          "num_plu": 340,
          "plu_name": "1/2 POLLO + PAPAS FRITAS",
          "plu_quantity": 1,
          "plu_comment": "",
          "price": {
            "total": 7.99,
            "tax_value": 1.0422,
            "subtotal_without_taxes": 6.9478
          }
        },
        {
          "code_detail": "CKFCA003804",
          "plu_id": 21,
          "num_plu": 352,
          "plu_name": "1/4 POLLO + ENSALADA + COLA",
          "plu_quantity": 1,
          "plu_comment": "",
          "price": {
            "total": 4.99,
            "tax_value": 0.6509,
            "subtotal_without_taxes": 4.3391
          }
        }
      ]
    }
  }
}
```

| Campo                                             | Tipo   | Descripción                           |
| ------------------------------------------------- | ------ | ------------------------------------- |
| `type_printer`                                    | string | Tipo de impresión del cupón           |
| `transaction`                                     | object | Información general de la transacción |
| `transaction.transaction_date`                    | string | Fecha y hora de la transacción        |
| `transaction.point_of_sale`                       | object | Información del punto de venta        |
| `transaction.point_of_sale.cdn_id`                | string | Identificador de la franquicia        |
| `transaction.point_of_sale.restaurant_id`         | string | Identificador del restaurante         |
| `transaction.point_of_sale.cash_register_id`      | string | Identificador de la caja              |
| `transaction.point_of_sale.cash_register_name`    | string | Nombre o código de la caja            |
| `transaction.point_of_sale.user_seller_id`        | string | Identificador del vendedor            |
| `transaction.point_of_sale.user_seller_name`      | string | Nombre del vendedor                   |
| `transaction.point_of_sale.device_os_name`        | string | Sistema operativo del dispositivo     |
| `transaction.point_of_sale.source_app_name`       | string | Aplicación origen                     |
| `transaction.point_of_sale.half_integration_id`   | number | ID del canal de integración           |
| `transaction.point_of_sale.half_integration_name` | string | Nombre del canal de integración       |
| `transaction.point_of_sale.user_admin`            | string | Usuario administrador                 |
| `transaction.point_of_sale.restaurant_name`       | string | Código y nombre del restaurante       |
| `transaction.point_of_sale.franchise_name`        | string | Nombre de la franquicia               |
| `transaction.coupons`                             | object | Información del cupón                 |
| `transaction.coupons.code_coupon`                 | string | Código del cupón                      |
| `transaction.coupons.type_coupon`                 | string | Tipo de cupón                         |
| `transaction.client`                              | object | Información del cliente               |
| `transaction.order`                               | object | Información de la orden               |
| `transaction.order.products`                      | array  | Productos de la orden                 |

### Respuestas del Servidor

#### 200 OK - Impresión Generada Correctamente

```json
{
  "code": 200,
  "status": "success",
  "alert": "Impresión generada correctamente",
  "messages": ["Impresión de factura completada"]
}
```

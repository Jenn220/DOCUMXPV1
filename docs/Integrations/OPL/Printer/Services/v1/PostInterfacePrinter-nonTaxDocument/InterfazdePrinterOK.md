## Generar Impresión de Caja Chica

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX010
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
  "type_printer": "CAJA_CHICA",
  "transaction": {
    "transaction_date": "",
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
      "half_integration_name": "App",
      "user_admin": "Carlos Zambrano",
      "restaurant_name": "G008 - EL INCA",
      "franchise_name": "GUS"
    },
    "withdrawn_amount": 351.0,
    "description": "Egreso Caja Chica Local",
    "addition_message": "Retiro para compra de candado"
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                             | Tipo   | Descripción                                                            |
| ------------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| `type_printer`                                    | string | Tipo de impresión (CAJA_CHICA, FALTANTE_CXC)                           |
| `transaction`                                     | object | Orden general con información de los puntos de venta                   |
| `transaction.transaction_date`                    | string | Fecha y hora de la transacción                                         |
| `transaction.point_of_sale`                       | object | Punto de venta con información física de quien y cómo realizó la venta |
| `transaction.point_of_sale.cdn_id`                | string | Identificador de la franquicia                                         |
| `transaction.point_of_sale.restaurant_id`         | string | Identificador del restaurante                                          |
| `transaction.point_of_sale.cash_register_id`      | string | Identificador de caja                                                  |
| `transaction.point_of_sale.cash_register_name`    | string | Nombre o código de caja                                                |
| `transaction.point_of_sale.user_seller_id`        | string | Identificador de cajero o vendedor                                     |
| `transaction.point_of_sale.user_seller_name`      | string | Nombre de cajero/usuario                                               |
| `transaction.point_of_sale.device_os_name`        | string | Sistema operativo donde se está vendiendo                              |
| `transaction.point_of_sale.source_app_name`       | string | Origen de aplicativo                                                   |
| `transaction.point_of_sale.half_integration_id`   | number | ID de canal                                                            |
| `transaction.point_of_sale.half_integration_name` | string | Nombre de canal                                                        |
| `transaction.point_of_sale.user_admin`            | string | Usuario administrador                                                  |
| `transaction.point_of_sale.restaurant_name`       | string | Código y nombre del restaurante                                        |
| `transaction.point_of_sale.franchise_name`        | string | Nombre de la franquicia                                                |
| `transaction.withdrawn_amount`                    | number | Monto retirado                                                         |
| `transaction.description`                         | string | Descripción del retiro                                                 |
| `transaction.addition_message`                    | string | Mensaje adicional                                                      |

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

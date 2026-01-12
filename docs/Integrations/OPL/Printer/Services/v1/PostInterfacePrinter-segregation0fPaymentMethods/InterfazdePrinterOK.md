## Generar Impresión de Retiros por Formas de Pago

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX008
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
  "type_printer": "RETIROS_FORMASPAGO",
  "transaction": {
    "transaction_date": "2025-10-09T11:27:08.941",
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
    "total_segregation_payment_methods": {
      "value": 351.0
    },
    "segregation_payment_methods": [
      {
        "payment_method": "EFECTIVO",
        "value": 140.0
      },
      {
        "description": "TARJEAS",
        "value": 210.0
      },
      {
        "description": "CUPONES",
        "value": 1.0
      }
    ]
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                      | Tipo   | Descripción                          |
| ---------------------------------------------------------- | ------ | ------------------------------------ |
| `type_printer`                                             | string | Tipo de impresión                    |
| `transaction`                                              | object | Información de la transacción        |
| `transaction.transaction_date`                             | string | Fecha y hora de la transacción       |
| `transaction.point_of_sale`                                | object | Información del punto de venta       |
| `transaction.point_of_sale.cdn_id`                         | string | Identificador de la franquicia       |
| `transaction.point_of_sale.restaurant_id`                  | string | Identificador del restaurante        |
| `transaction.point_of_sale.cash_register_id`               | string | Identificador de caja                |
| `transaction.point_of_sale.cash_register_name`             | string | Nombre o código de caja              |
| `transaction.point_of_sale.user_seller_id`                 | string | Identificador de cajero o vendedor   |
| `transaction.point_of_sale.user_seller_name`               | string | Nombre de cajero/usuario             |
| `transaction.point_of_sale.device_os_name`                 | string | Sistema operativo del dispositivo    |
| `transaction.point_of_sale.source_app_name`                | string | Nombre de la aplicación origen       |
| `transaction.point_of_sale.half_integration_id`            | number | ID de canal de integración           |
| `transaction.point_of_sale.half_integration_name`          | string | Nombre del canal de integración      |
| `transaction.point_of_sale.user_admin`                     | string | Nombre del usuario administrador     |
| `transaction.point_of_sale.restaurant_name`                | string | Código y nombre del restaurante      |
| `transaction.point_of_sale.franchise_name`                 | string | Nombre de la franquicia              |
| `transaction.total_segregation_payment_methods`            | object | Total de la segregación              |
| `transaction.total_segregation_payment_methods.value`      | number | Valor total de retiros               |
| `transaction.segregation_payment_methods`                  | array  | Detalle de retiros por forma de pago |
| `transaction.segregation_payment_methods[].payment_method` | string | Método de pago                       |
| `transaction.segregation_payment_methods[].description`    | string | Descripción del método de pago       |
| `transaction.segregation_payment_methods[].value`          | number | Valor del retiro por método          |

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

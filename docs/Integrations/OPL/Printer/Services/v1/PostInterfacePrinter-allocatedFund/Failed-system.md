## Generar Impresión de Retiro de Fondo Asignado

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
  "type_printer": "RETIRO_FONDO_ASIGNADO",
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
    "allocated_fund": {
      "assigned": 30.0,
      "retired": 30.0,
      "difference": 0.0
    }
  },
  "pub_device": {
    "cash_drawer": {}
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                             | Tipo   | Descripción                                |
| ------------------------------------------------- | ------ | ------------------------------------------ |
| `type_printer`                                    | string | Tipo de impresión                          |
| `transaction`                                     | object | Información de la transacción              |
| `transaction.point_of_sale`                       | object | Información del punto de venta             |
| `transaction.point_of_sale.cdn_id`                | string | Identificador de la franquicia             |
| `transaction.point_of_sale.restaurant_id`         | string | Identificador del restaurante              |
| `transaction.point_of_sale.cash_register_id`      | string | Identificador de caja                      |
| `transaction.point_of_sale.cash_register_name`    | string | Nombre o código de caja                    |
| `transaction.point_of_sale.user_seller_id`        | string | Identificador de cajero o vendedor         |
| `transaction.point_of_sale.user_seller_name`      | string | Nombre de cajero/usuario                   |
| `transaction.point_of_sale.device_os_name`        | string | Sistema operativo del dispositivo          |
| `transaction.point_of_sale.source_app_name`       | string | Nombre de la aplicación origen             |
| `transaction.point_of_sale.half_integration_id`   | number | ID de canal de integración                 |
| `transaction.point_of_sale.half_integration_name` | string | Nombre del canal de integración            |
| `transaction.allocated_fund`                      | object | Información del fondo asignado             |
| `transaction.allocated_fund.assigned`             | number | Monto asignado                             |
| `transaction.allocated_fund.retired`              | number | Monto retirado                             |
| `transaction.allocated_fund.difference`           | number | Diferencia entre asignado y retirado       |
| `pub_device`                                      | object | Información del dispositivo de publicación |
| `pub_device.cash_drawer`                          | object | Información de la gaveta de efectivo       |

### Respuestas del Servidor

#### 400 Bad Request - Cuerpo de Solicitud Vacío

```json
{
  "code": 400,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["A non-empty request body is required."]
}
```

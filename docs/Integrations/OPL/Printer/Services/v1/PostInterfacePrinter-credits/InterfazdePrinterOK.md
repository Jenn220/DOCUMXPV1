## Generar Impresión de Crédito de Empleado

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX013
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
  "type_printer": "CREDITO_EMPLEADO",
  "transaction": {
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
      "user_admin": "Carlos Zambrano"
    },
    "company": {
      "name": "EMBUTSER S.A.",
      "identificationNumber": "1792351057001",
      "companyAddress": "COREA 126 Y AV AMAZONAS",
      "restaurantAddress": "PICHINCHA / QUITO / AV. AMAZONAS 6121 Y EL INCA"
    },
    "client": {
      "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "name": "ESTIVEN",
      "last_name": "ARRIAGA",
      "phone": "+593986610329",
      "email": "mari_jhz@hotmail.com",
      "gov_id_type": "CI",
      "gov_id_number": "1206302802",
      "additional_info": {
        "birthdate": ""
      }
    },
    "detail": {
      "creation_date": "10/01/2025 10:41AM",
      "transaction": "BD02F000177034",
      "method_of_payment": "EMPLEADO",
      "total": 54.21
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                             | Tipo   | Descripción                                                                              |
| ------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------- |
| `type_printer`                                    | string | Tipo de impresión (CREDITO_EMPLEADO, CREDITO_EXTERNO, CREDITO_EMPRESA, CREDITO_PRODUCTO) |
| `transaction`                                     | object | Orden general con información de los puntos de venta                                     |
| `transaction.point_of_sale`                       | object | Punto de venta con información física de quien y cómo realizó la venta                   |
| `transaction.point_of_sale.cdn_id`                | string | Identificador de la franquicia                                                           |
| `transaction.point_of_sale.restaurant_id`         | string | Identificador del restaurante                                                            |
| `transaction.point_of_sale.cash_register_id`      | string | Identificador de caja                                                                    |
| `transaction.point_of_sale.cash_register_name`    | string | Nombre o código de caja                                                                  |
| `transaction.point_of_sale.user_seller_id`        | string | Identificador de cajero o vendedor                                                       |
| `transaction.point_of_sale.user_seller_name`      | string | Nombre de cajero/usuario                                                                 |
| `transaction.point_of_sale.device_os_name`        | string | Sistema operativo donde se está vendiendo                                                |
| `transaction.point_of_sale.source_app_name`       | string | Origen de aplicativo                                                                     |
| `transaction.point_of_sale.half_integration_id`   | number | ID de canal                                                                              |
| `transaction.point_of_sale.half_integration_name` | string | Nombre de canal                                                                          |
| `transaction.point_of_sale.user_admin`            | string | Usuario administrador                                                                    |
| `transaction.company`                             | object | Datos de la empresa a la que se solicita el crédito                                      |
| `transaction.company.name`                        | string | Nombre de la empresa                                                                     |
| `transaction.company.identificationNumber`        | string | Número de identificación de la empresa                                                   |
| `transaction.company.companyAddress`              | string | Dirección de la empresa                                                                  |
| `transaction.company.restaurantAddress`           | string | Dirección del restaurante                                                                |
| `transaction.client`                              | object | Datos del empleado que solicitó el crédito                                               |
| `transaction.client.client_id`                    | string | Identificador del cliente                                                                |
| `transaction.client.name`                         | string | Nombre del cliente                                                                       |
| `transaction.client.last_name`                    | string | Apellido del cliente                                                                     |
| `transaction.client.phone`                        | string | Teléfono del comprador                                                                   |
| `transaction.client.email`                        | string | Correo del comprador                                                                     |
| `transaction.client.gov_id_type`                  | string | Tipo de documento                                                                        |
| `transaction.client.gov_id_number`                | string | Identificación de gobierno del contribuyente                                             |
| `transaction.client.additional_info`              | object | Información adicional                                                                    |
| `transaction.client.additional_info.birthdate`    | string | Cumpleaños                                                                               |
| `transaction.detail`                              | object | Detalle de la transacción de crédito                                                     |
| `transaction.detail.creation_date`                | string | Fecha de creación                                                                        |
| `transaction.detail.transaction`                  | string | Código de transacción                                                                    |
| `transaction.detail.method_of_payment`            | string | Método de pago                                                                           |
| `transaction.detail.total`                        | number | Total del crédito                                                                        |

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

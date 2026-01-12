## Generar Impresión de Fin de Día

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX011
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
  "type_printer": "FIN_DE_DIA",
  "transaction": {
    "point_of_sale": {
      "cdn_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
      "restaurant_id": "f2c13a02-3cb5-4781-9e10-d3f1519c51e2",
      "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "cash_register_name": "EC-CAJA001",
      "user_seller_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "user_seller_name": "pepito",
      "device_os_name": "ios",
      "source_app_name": "Maxpoint 2.0",
      "half_integration_id": 3,
      "half_integration_name": "App",
      "user_admin": "Carlos Zambrano"
    },
    "summaries": {
      "transacction_number": 23,
      "gross_sales": 234.53,
      "iva_base": 34.32,
      "gratuities": 46.9,
      "swaps": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "credits": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "courtesies": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "totalCCC": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "correctionOfErrors": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "creditNotes": {
        "quantity": 2,
        "total_talue": 23.56
      },
      "declaredValues": [
        {
          "paymentMethod": "DATAFONO",
          "quantity": 2,
          "total_talue": 23.56
        },
        {
          "paymentMethod": "FIDELIZACION",
          "quantity": 2,
          "total_talue": 23.56
        }
      ],
      "expenses": 0.0,
      "income": 45.9,
      "cash_fund": {}
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                  | Tipo   | Descripción                                                               |
| ------------------------------------------------------ | ------ | ------------------------------------------------------------------------- |
| `type_printer`                                         | string | Tipo de impresión (FIN_DE_DIA, DESASIGNAR_CAJERO, REPORTE_X, ARQUEO_CAJA) |
| `transaction`                                          | object | Orden general con información de los puntos de venta                      |
| `transaction.point_of_sale`                            | object | Punto de venta con información física de quien y cómo realizó la venta    |
| `transaction.point_of_sale.cdn_id`                     | string | Identificador de la franquicia                                            |
| `transaction.point_of_sale.restaurant_id`              | string | Identificador del restaurante                                             |
| `transaction.point_of_sale.cash_register_id`           | string | Identificador de caja                                                     |
| `transaction.point_of_sale.cash_register_name`         | string | Nombre o código de caja                                                   |
| `transaction.point_of_sale.user_seller_id`             | string | Identificador de cajero o vendedor                                        |
| `transaction.point_of_sale.user_seller_name`           | string | Nombre de cajero/usuario                                                  |
| `transaction.point_of_sale.device_os_name`             | string | Sistema operativo donde se está vendiendo                                 |
| `transaction.point_of_sale.source_app_name`            | string | Origen de aplicativo                                                      |
| `transaction.point_of_sale.half_integration_id`        | number | ID de canal                                                               |
| `transaction.point_of_sale.half_integration_name`      | string | Nombre de canal                                                           |
| `transaction.point_of_sale.user_admin`                 | string | Usuario administrador                                                     |
| `transaction.summaries`                                | object | Resúmenes del día                                                         |
| `transaction.summaries.transacction_number`            | number | Número de transacciones al momento de imprimir                            |
| `transaction.summaries.gross_sales`                    | number | Valor total de ventas                                                     |
| `transaction.summaries.iva_base`                       | number | Valor del IVA                                                             |
| `transaction.summaries.gratuities`                     | number | Propinas                                                                  |
| `transaction.summaries.swaps`                          | object | Canjes                                                                    |
| `transaction.summaries.swaps.quantity`                 | number | Cantidad de canjes                                                        |
| `transaction.summaries.swaps.total_talue`              | number | Valor total de canjes                                                     |
| `transaction.summaries.credits`                        | object | Créditos                                                                  |
| `transaction.summaries.credits.quantity`               | number | Cantidad de créditos                                                      |
| `transaction.summaries.credits.total_talue`            | number | Valor total de créditos                                                   |
| `transaction.summaries.courtesies`                     | object | Cortesías                                                                 |
| `transaction.summaries.courtesies.quantity`            | number | Cantidad de cortesías                                                     |
| `transaction.summaries.courtesies.total_talue`         | number | Valor total de cortesías                                                  |
| `transaction.summaries.totalCCC`                       | object | Total CCC                                                                 |
| `transaction.summaries.totalCCC.quantity`              | number | Cantidad                                                                  |
| `transaction.summaries.totalCCC.total_talue`           | number | Valor total                                                               |
| `transaction.summaries.correctionOfErrors`             | object | Corrección de errores                                                     |
| `transaction.summaries.correctionOfErrors.quantity`    | number | Cantidad de correcciones                                                  |
| `transaction.summaries.correctionOfErrors.total_talue` | number | Valor total de correcciones                                               |
| `transaction.summaries.creditNotes`                    | object | Notas de crédito                                                          |
| `transaction.summaries.creditNotes.quantity`           | number | Cantidad de notas de crédito                                              |
| `transaction.summaries.creditNotes.total_talue`        | number | Valor total de notas de crédito                                           |
| `transaction.summaries.declaredValues`                 | array  | Valores declarados (retiros)                                              |
| `transaction.summaries.declaredValues[].paymentMethod` | string | Método de pago                                                            |
| `transaction.summaries.declaredValues[].quantity`      | number | Cantidad                                                                  |
| `transaction.summaries.declaredValues[].total_talue`   | number | Valor total                                                               |
| `transaction.summaries.expenses`                       | number | Gastos                                                                    |
| `transaction.summaries.income`                         | number | Ingresos                                                                  |
| `transaction.summaries.cash_fund`                      | object | Fondo de caja                                                             |

### Respuestas del Servidor

#### 400 Bad Request - Error en Formato de Plantilla

```json
{
  "code": 400,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["Plantilla no cumple formato"]
}
```

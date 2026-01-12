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

El cuerpo es extenso debido a la estructura completa del reporte de fin de día. Ver JSON completo en la documentación.

### Descripción del Cuerpo de la Solicitud

| Campo                                                             | Tipo   | Descripción                                                            |
| ----------------------------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| `type_printer`                                                    | string | Tipo de impresión (FIN_DE_DIA, Arquero, Desasignar cajero, Corte en X) |
| `transaction`                                                     | object | Información de la transacción                                          |
| `transaction.transaction_date`                                    | string | Fecha y hora de la transacción                                         |
| `transaction.point_of_sale`                                       | object | Información del punto de venta                                         |
| `transaction.point_of_sale.cdn_id`                                | string | Identificador de la franquicia                                         |
| `transaction.point_of_sale.restaurant_id`                         | string | Identificador del restaurante                                          |
| `transaction.point_of_sale.cash_register_id`                      | string | Identificador de caja                                                  |
| `transaction.point_of_sale.cash_register_name`                    | string | Nombre o código de caja                                                |
| `transaction.point_of_sale.user_seller_id`                        | string | Identificador de cajero o vendedor                                     |
| `transaction.point_of_sale.user_seller_name`                      | string | Nombre de cajero/usuario                                               |
| `transaction.point_of_sale.device_os_name`                        | string | Sistema operativo del dispositivo                                      |
| `transaction.point_of_sale.source_app_name`                       | string | Nombre de la aplicación origen                                         |
| `transaction.point_of_sale.half_integration_id`                   | number | ID de canal de integración                                             |
| `transaction.point_of_sale.half_integration_name`                 | string | Nombre del canal de integración                                        |
| `transaction.point_of_sale.user_admin`                            | string | Usuario administrador                                                  |
| `transaction.point_of_sale.restaurant_name`                       | string | Código y nombre del restaurante                                        |
| `transaction.point_of_sale.franchise_name`                        | string | Nombre de la franquicia                                                |
| `transaction.summaries`                                           | object | Resúmenes del día                                                      |
| `transaction.summaries.transacction_number`                       | number | Número de transacciones                                                |
| `transaction.summaries.gross_sales`                               | number | Ventas brutas                                                          |
| `transaction.summaries.iva_base`                                  | number | Base imponible IVA                                                     |
| `transaction.summaries.not_iva_base`                              | number | Base no gravada                                                        |
| `transaction.summaries.iva`                                       | number | Valor IVA                                                              |
| `transaction.summaries.discount`                                  | number | Descuentos                                                             |
| `transaction.summaries.average_ticket`                            | number | Ticket promedio                                                        |
| `transaction.summaries.gratuities`                                | number | Propinas                                                               |
| `transaction.summaries.exchange`                                  | object | Información de cambios                                                 |
| `transaction.summaries.exchange.quantity`                         | number | Cantidad de cambios                                                    |
| `transaction.summaries.exchange.total_value`                      | number | Valor total de cambios                                                 |
| `transaction.summaries.credits`                                   | object | Información de créditos                                                |
| `transaction.summaries.credits.quantity`                          | number | Cantidad de créditos                                                   |
| `transaction.summaries.credits.total_value`                       | number | Valor total de créditos                                                |
| `transaction.summaries.courtesies`                                | object | Información de cortesías                                               |
| `transaction.summaries.courtesies.quantity`                       | number | Cantidad de cortesías                                                  |
| `transaction.summaries.courtesies.total_value`                    | number | Valor total de cortesías                                               |
| `transaction.summaries.totalCCC`                                  | object | Total CCC                                                              |
| `transaction.summaries.totalCCC.quantity`                         | number | Cantidad                                                               |
| `transaction.summaries.totalCCC.total_value`                      | number | Valor total                                                            |
| `transaction.summaries.correctionOfErrors`                        | object | Corrección de errores                                                  |
| `transaction.summaries.correctionOfErrors.quantity`               | number | Cantidad de correcciones                                               |
| `transaction.summaries.correctionOfErrors.total_value`            | number | Valor total de correcciones                                            |
| `transaction.summaries.creditNotes`                               | object | Notas de crédito                                                       |
| `transaction.summaries.creditNotes.quantity`                      | number | Cantidad de notas de crédito                                           |
| `transaction.summaries.creditNotes.total_value`                   | number | Valor total de notas de crédito                                        |
| `transaction.summaries.declaredValues`                            | object | Valores declarados                                                     |
| `transaction.summaries.declaredValues.total_withdrawals_declared` | number | Total de retiros declarados                                            |
| `transaction.summaries.declaredValues.total_withdrawals`          | number | Total de retiros                                                       |
| `transaction.summaries.declaredValues.total_declared`             | number | Total declarado                                                        |
| `transaction.summaries.declaredValues.detail`                     | array  | Detalle por forma de pago                                              |
| `transaction.summaries.declaredValues.detail[].paymentMethod`     | string | Método de pago                                                         |
| `transaction.summaries.declaredValues.detail[].withdrawals`       | number | Retiros                                                                |
| `transaction.summaries.declaredValues.detail[].declared`          | number | Declarado                                                              |
| `transaction.summaries.declaredValues.detail[].pos_calculated`    | number | Calculado por POS                                                      |
| `transaction.summaries.declaredValues.detail[].detail`            | array  | Detalle anidado de subcategorías                                       |
| `transaction.summaries.egress`                                    | null   | Egresos                                                                |
| `transaction.summaries.income`                                    | null   | Ingresos                                                               |
| `transaction.summaries.surplus_or_shortage`                       | number | Sobrante o faltante                                                    |
| `transaction.summaries.cash_fund`                                 | object | Fondo de caja                                                          |
| `transaction.summaries.cash_fund.assigned_value`                  | number | Valor asignado                                                         |
| `transaction.summaries.cash_fund.confirmed_value`                 | number | Valor confirmado                                                       |
| `transaction.summaries.cash_fund.withdrawn_value`                 | number | Valor retirado                                                         |
| `transaction.summaries.cash_fund.value_for_withdrawal`            | number | Valor para retiro                                                      |

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

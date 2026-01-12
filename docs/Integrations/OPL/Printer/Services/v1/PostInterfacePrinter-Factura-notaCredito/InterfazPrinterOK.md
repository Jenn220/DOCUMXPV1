## Generar Impresión de Orden de Pedido con Factura

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX004
```

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

El cuerpo es extenso debido a la estructura completa de la transacción con factura electrónica. Ver JSON completo en la documentación.

### Descripción del Cuerpo de la Solicitud

| Campo                                                        | Tipo    | Descripción                           |
| ------------------------------------------------------------ | ------- | ------------------------------------- |
| `type_printer`                                               | string  | Tipo de impresora/documento a generar |
| `transaction`                                                | object  | Datos completos de la transacción     |
| `transaction.transaction_date`                               | string  | Fecha y hora de la transacción        |
| `transaction.point_of_sale`                                  | object  | Información del punto de venta        |
| `transaction.point_of_sale.cdn_id`                           | string  | Identificador de la franquicia        |
| `transaction.point_of_sale.restaurant_id`                    | string  | Identificador del restaurante         |
| `transaction.point_of_sale.cash_register_id`                 | string  | Identificador de caja                 |
| `transaction.point_of_sale.cash_register_name`               | string  | Nombre o código de caja               |
| `transaction.point_of_sale.user_seller_id`                   | string  | Identificador de cajero/vendedor      |
| `transaction.point_of_sale.user_seller_name`                 | string  | Nombre de cajero/usuario              |
| `transaction.point_of_sale.device_os_name`                   | string  | Sistema operativo del dispositivo     |
| `transaction.point_of_sale.source_app_name`                  | string  | Nombre de la aplicación origen        |
| `transaction.point_of_sale.half_integration_name`            | string  | Nombre del canal de integración       |
| `transaction.point_of_sale.restaurant_name`                  | string  | Código y nombre del restaurante       |
| `transaction.point_of_sale.franchise_name`                   | string  | Nombre de la franquicia               |
| `transaction.client`                                         | object  | Información del cliente               |
| `transaction.client.client_id`                               | string  | Identificador del cliente             |
| `transaction.client.name`                                    | string  | Nombre del cliente                    |
| `transaction.client.last_name`                               | string  | Apellido del cliente                  |
| `transaction.client.phone`                                   | string  | Teléfono del cliente                  |
| `transaction.client.email`                                   | string  | Email del cliente                     |
| `transaction.client.gov_id_type`                             | string  | Tipo de documento de identidad        |
| `transaction.client.gov_id_number`                           | string  | Número de documento de identidad      |
| `transaction.client.external_id`                             | string  | ID de referencia externa              |
| `transaction.client.additional_info`                         | object  | Información adicional del cliente     |
| `transaction.client.additional_info.birthdate`               | string  | Fecha de nacimiento                   |
| `transaction.client.additional_info.disclaimer`              | string  | Descargo de responsabilidad           |
| `transaction.order`                                          | object  | Información de la orden               |
| `transaction.order.order_id`                                 | string  | Identificador de la orden             |
| `transaction.order.createdAt`                                | string  | Fecha de creación de la orden         |
| `transaction.order.selected_shipping_method`                 | string  | Método de envío seleccionado          |
| `transaction.order.accumulate_points`                        | boolean | Si acumula puntos de fidelización     |
| `transaction.order.redeem_points`                            | boolean | Si redime puntos                      |
| `transaction.order.invoice`                                  | object  | Información de facturación            |
| `transaction.order.stock`                                    | boolean | Si maneja inventario                  |
| `transaction.order.discount`                                 | boolean | Si tiene descuentos aplicados         |
| `transaction.order.order_comment`                            | string  | Comentarios de la orden               |
| `transaction.order.annulation_comment`                       | string  | Comentario de anulación               |
| `transaction.order.products`                                 | array   | Lista de productos de la orden        |
| `transaction.order.products[].plu_id`                        | number  | ID del PLU                            |
| `transaction.order.products[].cdn_plu_id`                    | number  | ID del PLU en CDN                     |
| `transaction.order.products[].plu_name`                      | string  | Nombre del producto                   |
| `transaction.order.products[].plu_quantity`                  | number  | Cantidad del producto                 |
| `transaction.order.products[].plu_comment`                   | string  | Comentario del producto               |
| `transaction.order.products[].price`                         | object  | Información de precios del producto   |
| `transaction.order.products[].modifier_groups`               | array   | Grupos de modificadores del producto  |
| `transaction.order.stock_details`                            | null    | Detalles de inventario                |
| `transaction.shipping_method`                                | null    | Método de envío                       |
| `transaction.payments`                                       | object  | Información de pagos                  |
| `transaction.payments.totals`                                | array   | Totales por moneda                    |
| `transaction.payments.totals[].currency_code`                | string  | Código de moneda                      |
| `transaction.payments.totals[].subtotal_without_taxes`       | number  | Subtotal sin impuestos                |
| `transaction.payments.totals[].discount_percentage`          | number  | Porcentaje de descuento               |
| `transaction.payments.totals[].discounts_value`              | number  | Valor de descuentos                   |
| `transaction.payments.totals[].subtotal_include_discounts`   | number  | Subtotal con descuentos               |
| `transaction.payments.totals[].taxes_percentage`             | number  | Porcentaje de impuestos               |
| `transaction.payments.totals[].tax_value`                    | number  | Valor de impuestos                    |
| `transaction.payments.totals[].total_before_sale`            | number  | Total antes de venta                  |
| `transaction.payments.totals[].total`                        | number  | Total final                           |
| `transaction.payments.totals[].taxes`                        | array   | Desglose de impuestos                 |
| `transaction.payments.shipping_cost`                         | null    | Costo de envío                        |
| `transaction.payments.extra_charges`                         | null    | Cargos extras                         |
| `transaction.payments.taxes`                                 | array   | Impuestos aplicados                   |
| `transaction.payments.discounts`                             | array   | Descuentos aplicados                  |
| `transaction.payments.payment_methods`                       | array   | Métodos de pago utilizados            |
| `transaction.payments.payment_methods[].payment_methods_id`  | string  | ID del método de pago                 |
| `transaction.payments.payment_methods[].payment_method_name` | string  | Nombre del método de pago             |
| `transaction.payments.payment_methods[].processor`           | string  | Procesador de pago                    |
| `transaction.payments.payment_methods[].currency_code`       | string  | Código de moneda                      |
| `transaction.payments.payment_methods[].payment_method_code` | string  | Código del método                     |
| `transaction.payments.payment_methods[].transaction_type`    | string  | Tipo de transacción                   |
| `transaction.payments.payment_methods[].transaction_status`  | string  | Estado de la transacción              |
| `transaction.payments.payment_methods[].transaction_id`      | string  | ID de transacción                     |
| `transaction.payments.payment_methods[].total_bill`          | number  | Total de la cuenta                    |
| `feBuilder`                                                  | object  | Constructor de factura electrónica    |
| `feBuilder.companyTaxData`                                   | object  | Datos fiscales de la empresa          |
| `feBuilder.companyTaxData.name`                              | string  | Nombre de la empresa                  |
| `feBuilder.companyTaxData.identificationNumber`              | string  | RUC de la empresa                     |
| `feBuilder.companyTaxData.specialTaxpayer`                   | string  | Tipo de contribuyente especial        |
| `feBuilder.companyTaxData.specialTaxpayerCode`               | string  | Código de contribuyente especial      |
| `feBuilder.companyTaxData.obligatoryToKeepAccounts`          | string  | Obligado a llevar contabilidad        |
| `feBuilder.companyTaxData.companyAddress`                    | string  | Dirección de la empresa               |
| `feBuilder.companyTaxData.restaurantAddress`                 | string  | Dirección del restaurante             |
| `feBuilder.dataInvoice`                                      | object  | Datos de la factura                   |
| `feBuilder.dataInvoice.sequential`                           | string  | Número secuencial de factura          |
| `feBuilder.dataInvoice.accessKey`                            | string  | Clave de acceso                       |
| `feBuilder.dataInvoice.transaction`                          | string  | Código de transacción                 |
| `feBuilder.dataInvoice.legend`                               | string  | Leyenda de la factura                 |
| `feBuilder.dataInvoice.urlDocument`                          | string  | URL del documento                     |
| `feBuilder.dataInvoice.environment`                          | string  | Ambiente (Pruebas/Producción)         |
| `feBuilder.dataInvoice.createdAt`                            | string  | Fecha de creación                     |
| `feBuilder.dataInvoice.document`                             | object  | Documento de factura                  |
| `feBuilder.dataCredit`                                       | object  | Datos de nota de crédito              |
| `feBuilder.document_code`                                    | string  | Código de tipo de documento           |
| `pubDevice`                                                  | null    | Dispositivo de publicación            |
| `promotions`                                                 | null    | Promociones aplicadas                 |

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

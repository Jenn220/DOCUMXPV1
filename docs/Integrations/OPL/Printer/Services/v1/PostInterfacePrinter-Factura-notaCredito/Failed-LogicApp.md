## Generar Impresión de Cupón de Venta

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/generatePrinter
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

El cuerpo es extenso debido a la estructura completa de la transacción con información de cupones y promociones. Ver JSON completo en la documentación.

### Descripción del Cuerpo de la Solicitud

| Campo                                                                               | Tipo    | Descripción                                                            |
| ----------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `typePrinter`                                                                       | string  | Tipo de impresión (catálogo de tipos de impresiones)                   |
| `transaction`                                                                       | object  | Orden general con información de los puntos de venta                   |
| `transaction.pointOfSale`                                                           | object  | Punto de venta con información física de quien y cómo realizó la venta |
| `transaction.pointOfSale.id`                                                        | string  | Identificador de caja                                                  |
| `transaction.pointOfSale.code`                                                      | string  | Nombre o código de caja                                                |
| `transaction.pointOfSale.cashierId`                                                 | string  | Identificador de cajero o vendedor                                     |
| `transaction.pointOfSale.cashierName`                                               | string  | Nombre de cajero/usuario                                               |
| `transaction.pointOfSale.platform`                                                  | string  | Sistema operativo donde se está vendiendo                              |
| `transaction.pointOfSale.account`                                                   | string  | Franchise cuenta autorizada                                            |
| `transaction.pointOfSale.accountId`                                                 | number  | ID de cuenta autorizada                                                |
| `transaction.pointOfSale.source`                                                    | string  | Origen de aplicativo                                                   |
| `transaction.pointOfSale.channelId`                                                 | number  | ID de canal                                                            |
| `transaction.pointOfSale.channelName`                                               | string  | Nombre de canal                                                        |
| `transaction.client`                                                                | object  | Datos del cliente comprador y de facturación                           |
| `transaction.client.uid`                                                            | string  | Identificador del cliente                                              |
| `transaction.client.name`                                                           | string  | Nombre del cliente                                                     |
| `transaction.client.lastName`                                                       | string  | Apellido del cliente                                                   |
| `transaction.client.phone`                                                          | string  | Teléfono del comprador                                                 |
| `transaction.client.email`                                                          | string  | Correo del comprador                                                   |
| `transaction.client.govIdType`                                                      | string  | Tipo de documento                                                      |
| `transaction.client.govIdNumber`                                                    | string  | Identificación de gobierno del contribuyente                           |
| `transaction.client.externalId`                                                     | string  | ID de referencia                                                       |
| `transaction.client.billingInformation`                                             | object  | Datos de facturación electrónica                                       |
| `transaction.client.billingInformation.fullName`                                    | string  | Nombre de contribuyente                                                |
| `transaction.client.billingInformation.govIdType`                                   | string  | Tipo de documento                                                      |
| `transaction.client.billingInformation.govIdNumber`                                 | string  | Identificador de contribuyente                                         |
| `transaction.client.billingInformation.phone`                                       | string  | Teléfono                                                               |
| `transaction.client.billingInformation.email`                                       | string  | Correo electrónico                                                     |
| `transaction.client.billingInformation.address`                                     | string  | Dirección                                                              |
| `transaction.client.billingInformation.externalId`                                  | string  | ID de referencia                                                       |
| `transaction.client.additionalInfo`                                                 | object  | Información adicional                                                  |
| `transaction.client.additionalInfo.birthdate`                                       | string  | Cumpleaños                                                             |
| `transaction.client.additionalInfo.gender`                                          | string  | Género                                                                 |
| `transaction.order`                                                                 | object  | Detalles de los PLUs, precios y modificadores utilizados               |
| `transaction.order.orderId`                                                         | string  | ID de orden generada por el Punto de Venta                             |
| `transaction.order.createdAt`                                                       | string  | Fecha de creación de orden de venta                                    |
| `transaction.order.selectedShippingMethod`                                          | string  | Método de envío                                                        |
| `transaction.order.accumulatePoints`                                                | boolean | Si es una venta con temas de fidelización                              |
| `transaction.order.redeemPoints`                                                    | boolean | Si es una venta con redención de puntos                                |
| `transaction.order.stock`                                                           | boolean | Si es una venta con temas de inventario                                |
| `transaction.order.discount`                                                        | boolean | Si es una venta con descuentos                                         |
| `transaction.order.orderComment`                                                    | string  | Comentario de la orden                                                 |
| `transaction.order.annulationComment`                                               | string  | Comentario de anulación/motivo                                         |
| `transaction.order.products`                                                        | array   | Detalles de items                                                      |
| `transaction.order.products[].productId`                                            | string  | ID del PLU                                                             |
| `transaction.order.products[].product`                                              | string  | Nombre del PLU vendido                                                 |
| `transaction.order.products[].quantity`                                             | number  | Cantidad de PLU vendido                                                |
| `transaction.order.products[].productComment`                                       | string  | Comentario del PLU vendido                                             |
| `transaction.order.products[].price`                                                | object  | Detalles de precios                                                    |
| `transaction.order.products[].price.unitPrice`                                      | object  | Detalle por unidad                                                     |
| `transaction.order.products[].price.unitPrice.currencyCode`                         | string  | Código de moneda                                                       |
| `transaction.order.products[].price.unitPrice.subtotalWithoutTaxes`                 | number  | Subtotal sin impuestos                                                 |
| `transaction.order.products[].price.unitPrice.discountPercentage`                   | number  | Porcentaje de descuento                                                |
| `transaction.order.products[].price.unitPrice.discountsValue`                       | number  | Valor de descuentos                                                    |
| `transaction.order.products[].price.unitPrice.subtotalIncludeDiscounts`             | number  | Subtotal incluyendo descuentos                                         |
| `transaction.order.products[].price.unitPrice.taxesPercentage`                      | number  | Porcentaje de impuestos                                                |
| `transaction.order.products[].price.unitPrice.taxValue`                             | number  | Valor del impuesto                                                     |
| `transaction.order.products[].price.unitPrice.total`                                | number  | Total                                                                  |
| `transaction.order.products[].price.unitPrice.totalBeforeSale`                      | number  | Total antes de venta                                                   |
| `transaction.order.products[].price.unitPrice.suggestedPrice`                       | number  | Precio sugerido                                                        |
| `transaction.order.products[].price.totalPrice`                                     | object  | Detalles de totales por la cantidad de PLUs                            |
| `transaction.order.products[].modifierGroups`                                       | array   | Modificadores de PLUs                                                  |
| `transaction.order.products[].modifierGroups[].id`                                  | string  | ID del grupo modificador                                               |
| `transaction.order.products[].modifierGroups[].description`                         | string  | Descripción del grupo                                                  |
| `transaction.order.products[].modifierGroups[].selectedModifiers`                   | array   | Modificadores seleccionados                                            |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].productId`       | string  | ID del producto modificador                                            |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].product`         | string  | Nombre del modificador                                                 |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].quantity`        | number  | Cantidad                                                               |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].removedQuantity` | null    | Cantidad removida                                                      |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].price`           | object  | Precios del modificador                                                |
| `transaction.order.products[].modifierGroups[].selectedModifiers[].additionalInfo`  | object  | Información adicional del modificador                                  |
| `transaction.order.products[].additionalInfo`                                       | object  | Información adicional a nivel de detalle de orden                      |
| `transaction.order.products[].additionalInfo.strategy`                              | string  | Estrategia                                                             |
| `transaction.order.products[].additionalInfo.relatedProductId`                      | string  | ID de producto relacionado                                             |
| `transaction.order.products[].additionalInfo.redeemed`                              | boolean | Si fue redimido                                                        |
| `transaction.order.products[].additionalInfo.sort`                                  | number  | Orden                                                                  |
| `transaction.order.products[].additionalInfo.referenceUnitPrice`                    | object  | Precio unitario de referencia                                          |
| `transaction.order.products[].additionalInfo.referenceTotalPrice`                   | object  | Precio total de referencia                                             |
| `transaction.order.stockDetails`                                                    | array   | Detalles de inventario de venta                                        |
| `transaction.order.stockDetails[].productId`                                        | number  | ID de artículo                                                         |
| `transaction.order.stockDetails[].stock`                                            | number  | Cantidad de inventario de venta                                        |
| `transaction.shippingMethod`                                                        | object  | Información de método de entrega de la transacción                     |
| `transaction.shippingMethod.store`                                                  | object  | Información de tienda                                                  |
| `transaction.shippingMethod.store.id`                                               | number  | ID de tienda                                                           |
| `transaction.shippingMethod.store.name`                                             | string  | Nombre de tienda                                                       |
| `transaction.shippingMethod.store.code`                                             | string  | Código de tienda                                                       |
| `transaction.shippingMethod.store.vendorId`                                         | number  | ID de vendedor                                                         |
| `transaction.shippingMethod.store.vendorName`                                       | string  | Nombre de vendedor                                                     |
| `transaction.shippingMethod.store.latitude`                                         | number  | Latitud                                                                |
| `transaction.shippingMethod.store.longitude`                                        | number  | Longitud                                                               |
| `transaction.shippingMethod.delivery`                                               | object  | Información de delivery                                                |
| `transaction.shippingMethod.delivery.deliveryDate`                                  | string  | Fecha de entrega                                                       |
| `transaction.shippingMethod.delivery.latitude`                                      | string  | Latitud                                                                |
| `transaction.shippingMethod.delivery.longitude`                                     | string  | Longitud                                                               |
| `transaction.shippingMethod.delivery.country`                                       | string  | País                                                                   |
| `transaction.shippingMethod.delivery.city`                                          | string  | Ciudad                                                                 |
| `transaction.shippingMethod.delivery.mainStreet`                                    | string  | Calle principal                                                        |
| `transaction.shippingMethod.delivery.secondaryStreet`                               | string  | Calle secundaria                                                       |
| `transaction.shippingMethod.delivery.reference`                                     | string  | Referencia                                                             |
| `transaction.shippingMethod.delivery.propertyId`                                    | number  | ID de propiedad                                                        |
| `transaction.shippingMethod.delivery.observationsAddress`                           | string  | Observaciones de dirección                                             |
| `transaction.shippingMethod.delivery.numberContactAddress`                          | string  | Número de contacto                                                     |
| `transaction.shippingMethod.delivery.zipCode`                                       | string  | Código postal                                                          |
| `transaction.shippingMethod.delivery.nickName`                                      | string  | Apodo                                                                  |
| `transaction.shippingMethod.delivery.externalId`                                    | string  | ID externo                                                             |
| `transaction.shippingMethod.pickup`                                                 | object  | Información de pickup                                                  |
| `transaction.shippingMethod.pickup.pickupDate`                                      | string  | Fecha de pickup                                                        |
| `transaction.shippingMethod.pickup.prepDate`                                        | string  | Fecha de preparación                                                   |
| `transaction.shippingMethod.pickup.prepTimeUnit`                                    | string  | Unidad de tiempo de preparación                                        |
| `transaction.shippingMethod.pickup.prepTime`                                        | number  | Tiempo de preparación                                                  |
| `transaction.shippingMethod.pickup.propertyId`                                      | number  | ID de propiedad                                                        |
| `transaction.shippingMethod.pickup.carryOutOptions`                                 | string  | Opciones de carry out                                                  |
| `transaction.payments`                                                              | object  | Datos en relación a los pagos de la transacción                        |
| `transaction.payments.totals`                                                       | array   | Totales por tipo de moneda                                             |
| `transaction.payments.totals[].currencyCode`                                        | string  | Código de moneda                                                       |
| `transaction.payments.totals[].subtotalWithoutTaxes`                                | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.totals[].discountPercentage`                                  | number  | Porcentaje de descuento                                                |
| `transaction.payments.totals[].discountsValue`                                      | number  | Valor de descuentos                                                    |
| `transaction.payments.totals[].subtotalIncludeDiscounts`                            | number  | Subtotal incluyendo descuentos                                         |
| `transaction.payments.totals[].taxesPercentage`                                     | number  | Porcentaje de impuestos                                                |
| `transaction.payments.totals[].taxValue`                                            | number  | Valor del impuesto                                                     |
| `transaction.payments.totals[].totalBeforeSale`                                     | number  | Total antes de venta                                                   |
| `transaction.payments.totals[].total`                                               | number  | Total                                                                  |
| `transaction.payments.shippingCost`                                                 | array   | Costos de envío                                                        |
| `transaction.payments.shippingCost[].quantity`                                      | number  | Cantidad                                                               |
| `transaction.payments.shippingCost[].productId`                                     | number  | ID de producto                                                         |
| `transaction.payments.shippingCost[].currencyCode`                                  | string  | Código de moneda                                                       |
| `transaction.payments.shippingCost[].subtotalWithoutTaxes`                          | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.shippingCost[].discountPercentage`                            | number  | Porcentaje de descuento                                                |
| `transaction.payments.shippingCost[].discountsValue`                                | number  | Valor de descuentos                                                    |
| `transaction.payments.shippingCost[].subtotalIncludeDiscounts`                      | number  | Subtotal incluyendo descuentos                                         |
| `transaction.payments.shippingCost[].taxesPercentage`                               | number  | Porcentaje de impuestos                                                |
| `transaction.payments.shippingCost[].taxValue`                                      | number  | Valor del impuesto                                                     |
| `transaction.payments.shippingCost[].total`                                         | number  | Total                                                                  |
| `transaction.payments.extraCharges`                                                 | array   | Cargos extras                                                          |
| `transaction.payments.extraCharges[].quantity`                                      | null    | Cantidad                                                               |
| `transaction.payments.extraCharges[].productId`                                     | null    | ID de producto                                                         |
| `transaction.payments.extraCharges[].description`                                   | null    | Descripción                                                            |
| `transaction.payments.extraCharges[].currencyCode`                                  | null    | Código de moneda                                                       |
| `transaction.payments.extraCharges[].subtotalWithoutTaxes`                          | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.extraCharges[].discountPercentage`                            | number  | Porcentaje de descuento                                                |
| `transaction.payments.extraCharges[].discountsValue`                                | number  | Valor de descuentos                                                    |
| `transaction.payments.extraCharges[].subtotalIncludeDiscounts`                      | number  | Subtotal incluyendo descuentos                                         |
| `transaction.payments.extraCharges[].taxesPercentage`                               | number  | Porcentaje de impuestos                                                |
| `transaction.payments.extraCharges[].taxValue`                                      | number  | Valor del impuesto                                                     |
| `transaction.payments.extraCharges[].total`                                         | number  | Total                                                                  |
| `transaction.payments.taxes`                                                        | array   | Impuestos aplicados                                                    |
| `transaction.payments.taxes[].name`                                                 | string  | Nombre del impuesto                                                    |
| `transaction.payments.taxes[].currencyCode`                                         | string  | Código de moneda                                                       |
| `transaction.payments.taxes[].subtotalWithoutTaxes`                                 | number  | Subtotal sin impuestos                                                 |
| `transaction.payments.taxes[].percentage`                                           | number  | Porcentaje del impuesto                                                |
| `transaction.payments.taxes[].total`                                                | number  | Total del impuesto                                                     |
| `transaction.payments.discounts`                                                    | array   | Descuentos aplicados                                                   |
| `transaction.payments.discounts[].externalId`                                       | null    | ID externo                                                             |
| `transaction.payments.discounts[].name`                                             | string  | Nombre del descuento                                                   |
| `transaction.payments.discounts[].percentageDiscount`                               | boolean | Si es descuento porcentual                                             |
| `transaction.payments.discounts[].amountDiscount`                                   | boolean | Si es descuento por monto                                              |
| `transaction.payments.discounts[].currencyCode`                                     | string  | Código de moneda                                                       |
| `transaction.payments.discounts[].totalBeforeSale`                                  | number  | Total antes de venta                                                   |
| `transaction.payments.discounts[].subtotalWithoutDiscounts`                         | number  | Subtotal sin descuentos                                                |
| `transaction.payments.discounts[].percentage`                                       | number  | Porcentaje de descuento                                                |
| `transaction.payments.discounts[].total`                                            | number  | Total del descuento                                                    |
| `transaction.payments.discounts[].totalWithTaxes`                                   | number  | Total con impuestos                                                    |
| `transaction.payments.paymentMethods`                                               | array   | Tipos de pagos utilizados para la transacción                          |
| `transaction.payments.paymentMethods[].processor`                                   | string  | Procesador de pago                                                     |
| `transaction.payments.paymentMethods[].currencyCode`                                | string  | Código de moneda                                                       |
| `transaction.payments.paymentMethods[].paymentMethodCode`                           | string  | Código del método de pago                                              |
| `transaction.payments.paymentMethods[].transactionType`                             | string  | Tipo de transacción                                                    |
| `transaction.payments.paymentMethods[].transactionId`                               | string  | ID de transacción                                                      |
| `transaction.payments.paymentMethods[].transactionStatus`                           | string  | Estado de la transacción                                               |
| `transaction.payments.paymentMethods[].tid`                                         | null    | Terminal ID                                                            |
| `transaction.payments.paymentMethods[].mid`                                         | null    | Merchant ID                                                            |
| `transaction.payments.paymentMethods[].authorizationCode`                           | null    | Código de autorización                                                 |
| `transaction.payments.paymentMethods[].voucher`                                     | null    | Voucher                                                                |
| `transaction.payments.paymentMethods[].referenceNumber`                             | null    | Número de referencia                                                   |
| `transaction.payments.paymentMethods[].exactPayment`                                | boolean | Si es pago exacto                                                      |
| `transaction.payments.paymentMethods[].customerCashAmount`                          | string  | Monto en efectivo del cliente                                          |
| `transaction.payments.paymentMethods[].totalBill`                                   | number  | Total de la factura                                                    |
| `transaction.payments.paymentMethods[].acquirer`                                    | object  | Información del adquirente                                             |
| `transaction.payments.paymentMethods[].acquirer.code`                               | string  | Código del adquirente                                                  |
| `transaction.payments.paymentMethods[].acquirer.name`                               | string  | Nombre del adquirente                                                  |
| `transaction.payments.paymentMethods[].card`                                        | object  | Información de la tarjeta                                              |
| `transaction.payments.paymentMethods[].card.mask`                                   | string  | Máscara de la tarjeta                                                  |
| `transaction.payments.paymentMethods[].card.bin`                                    | string  | BIN de la tarjeta                                                      |
| `transaction.payments.paymentMethods[].card.lastFourDigits`                         | string  | Últimos 4 dígitos                                                      |
| `transaction.payments.paymentMethods[].card.brand`                                  | string  | Marca de la tarjeta                                                    |
| `transaction.payments.paymentMethods[].card.externalCardBrandId`                    | string  | ID externo de marca de tarjeta                                         |
| `transaction.payments.paymentMethods[].card.holder`                                 | string  | Titular de la tarjeta                                                  |
| `transaction.payments.paymentMethods[].card.cardCountry`                            | string  | País de la tarjeta                                                     |
| `transaction.payments.paymentMethods[].transactionDate`                             | object  | Fecha de transacción                                                   |
| `transaction.payments.paymentMethods[].transactionDate.date`                        | string  | Fecha y hora                                                           |
| `transaction.payments.paymentMethods[].transactionDate.timeZoneType`                | number  | Tipo de zona horaria                                                   |
| `transaction.payments.paymentMethods[].transactionDate.timeZoneName`                | string  | Nombre de zona horaria                                                 |
| `transaction.payments.paymentMethods[].additionalInfo`                              | object  | Información adicional                                                  |
| `transaction.payments.paymentMethods[].additionalInfo.externalPaymentMethodId`      | string  | ID externo del método de pago                                          |
| `transaction.marketing`                                                             | object  | Información que se utiliza para marketing                              |
| `transaction.marketing.loyalty`                                                     | object  | Información de fidelización                                            |
| `transaction.marketing.loyalty.accumulation`                                        | object  | Acumulación de puntos                                                  |
| `transaction.marketing.loyalty.accumulation.storeCost`                              | number  | Costo tienda                                                           |
| `transaction.marketing.loyalty.accumulation.marketingCost`                          | number  | Costo marketing                                                        |
| `transaction.marketing.loyalty.accumulation.totalPoints`                            | number  | Total de puntos                                                        |
| `transaction.marketing.loyalty.redemption`                                          | object  | Redención de puntos                                                    |
| `transaction.marketing.loyalty.redemption.storeCost`                                | number  | Costo tienda                                                           |
| `transaction.marketing.loyalty.redemption.marketingCost`                            | number  | Costo marketing                                                        |
| `transaction.marketing.loyalty.redemption.totalPoints`                              | number  | Total de puntos                                                        |
| `transaction.marketing.loyalty.accountBalancePoints`                                | number  | Balance de puntos en cuenta                                            |
| `transaction.additionalInfo`                                                        | object  | Información adicional de la transacción                                |
| `transaction.additionalInfo.kiosk`                                                  | object  | Información de kiosk                                                   |
| `transaction.additionalInfo.kiosk.ip`                                               | string  | IP del kiosk                                                           |
| `transaction.additionalInfo.pickupPhase`                                            | string  | Fase de pickup                                                         |
| `feBuilder`                                                                         | object  | Datos de facturación (responde fe.builder)                             |
| `feBuilder.companyTaxData`                                                          | object  | Datos fiscales de la empresa                                           |
| `feBuilder.companyTaxData.name`                                                     | string  | Nombre de la empresa                                                   |
| `feBuilder.companyTaxData.isSpecialTaxpayer`                                        | string  | Si es contribuyente especial                                           |
| `feBuilder.companyTaxData.specialTaxpayerCode`                                      | string  | Código de contribuyente especial                                       |
| `feBuilder.companyTaxData.typeTax`                                                  | string  | Tipo de impuesto                                                       |
| `feBuilder.companyTaxData.obligatoryToKeepAccounts`                                 | number  | Obligado a llevar contabilidad                                         |
| `feBuilder.companyTaxData.resolutionCode`                                           | string  | Código de resolución                                                   |
| `feBuilder.companyTaxData.companyAddress`                                           | string  | Dirección de la empresa                                                |
| `feBuilder.companyTaxData.restaurntAddress`                                         | string  | Dirección del restaurante                                              |
| `feBuilder.dataInvocie`                                                             | object  | Datos que devuelve el sistema de facturación al crear factura          |
| `feBuilder.dataInvocie.sequential`                                                  | string  | Secuencial de factura                                                  |
| `feBuilder.dataInvocie.accessKey`                                                   | string  | Clave de acceso                                                        |
| `feBuilder.dataInvocie.legend`                                                      | string  | Leyenda                                                                |
| `feBuilder.dataInvocie.urlDocument`                                                 | string  | URL del documento                                                      |
| `feBuilder.dataInvocie.createdAt`                                                   | string  | Fecha de creación                                                      |
| `feBuilder.dataCredit`                                                              | object  | Datos que devuelve el sistema al crear nota de crédito                 |
| `feBuilder.dataCredit.sequential`                                                   | string  | Secuencial                                                             |
| `feBuilder.dataCredit.accessKey`                                                    | string  | Clave de acceso                                                        |
| `feBuilder.dataCredit.legend`                                                       | string  | Leyenda                                                                |
| `feBuilder.dataCredit.urlDocument`                                                  | string  | URL del documento                                                      |
| `feBuilder.dataCredit.createdAt`                                                    | string  | Fecha de creación                                                      |
| `feBuilder.dataCredit.detailCredit`                                                 | object  | Detalle de crédito                                                     |
| `pubDevice`                                                                         | object  | Datos de device (responde pubDevice)                                   |
| `pubDevice.turnero`                                                                 | object  | Información para impresión del QR turnero                              |
| `pubDevice.turnero.codeQr`                                                          | string  | Código QR                                                              |
| `pubDevice.turnero.typeQr`                                                          | string  | Tipo de QR                                                             |
| `pubDevice.kds`                                                                     | object  | Información de KDS                                                     |
| `promotions`                                                                        | object  | Datos a imprimir en relación a promociones                             |
| `promotions.cupones`                                                                | object  | Información de cupones                                                 |
| `promotions.cupones.codeQr`                                                         | string  | Código QR                                                              |
| `promotions.cupones.typeQr`                                                         | string  | Tipo de QR                                                             |
| `promotions.cupones.text`                                                           | string  | Texto del cupón                                                        |

### Respuestas del Servidor

#### 400 Bad Request - Error en Plantilla

```json
{
  "code": 400,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["Plantilla no cumple formato"]
}
```

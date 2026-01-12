## Generar Impresión de Voucher Aprobado

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX005
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
  "type_printer": "VOUCHER_APROBADO",
  "transaction": {
    "transaction_date": "2025-10-09T11:27:08.941",
    "point_of_sale": {
      "cdn_id": "533d60dc-c672-d14c-b9a9-29801c8ae01a",
      "restaurant_id": "84226b3d-e13b-cc41-b262-d55f324239d0",
      "cash_register_id": "d7a253d7-d95f-0a45-9b99-f823219a79b2",
      "cash_register_name": "Caja 1",
      "user_seller_id": "668d3b43-ab48-4fe0-ab01-ea4f21107be8",
      "user_seller_name": "ANA GOMEZ",
      "device_os_name": "web",
      "source_app_name": "Maxpoint 2.0",
      "half_integration_id": 3,
      "half_integration_name": "App",
      "franchise_name": "KENTUCKY FRIED CHICKEN"
    },
    "price": {
      "currency": "USD",
      "total": 141.99,
      "subsidy": 0,
      "discount": 0,
      "tax": 11.99,
      "base_amount": 130,
      "base_amountWithOutTax": 0,
      "taxes": [
        {
          "tax_name": "IVA 10 %",
          "tax_code": "iva23313",
          "tax_percentage": 10,
          "total_tax_vulue": 4.99,
          "base_amount": 130
        },
        {
          "tax_name": "ICE 10 %",
          "tax_code": "iva23313",
          "tax_percentage": 10,
          "total_tax_vulue": 4.99,
          "base_amount": 130
        }
      ]
    },
    "payer": {
      "gov_id_type": "Cedula",
      "gov_id_number": "1234567891",
      "name": "EDISON  FIGUEROA",
      "last_name": "",
      "phone": "992087877",
      "address": "",
      "city": "",
      "state": "",
      "country": "",
      "zip_code": ""
    },
    "order_detail": {
      "products": [
        {
          "plu_id": "a3a5830e-0385-424a-9e8c-785b305679e7",
          "cdn_plu_id": "Cajun - COMBO CHOP SUEY",
          "plu_quantity": 1,
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            }
          }
        },
        {
          "plu_id": "88813a38-abe7-457d-9de5-511bbdd2050f",
          "cdn_plu_id": "Cajun - PEPSI",
          "plu_quantity": 1,
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "tax_name": "IVA 10 %",
                  "tax_code": "iva23313",
                  "tax_percentage": 10,
                  "total_tax_vulue": 4.99,
                  "base_amount": 130
                },
                {
                  "tax_name": "IVA 10 %",
                  "tax_code": "iva23313",
                  "tax_percentage": 10,
                  "total_tax_vulue": 4.99,
                  "base_amount": 130
                }
              ]
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "tax_name": "IVA 10 %",
                  "tax_code": "iva23313",
                  "tax_percentage": 10,
                  "total_tax_vulue": 4.99,
                  "base_amount": 130
                }
              ]
            }
          }
        },
        {
          "plu_id": "aed25a39-941b-4775-abda-e0986cce1375",
          "cdn_plu_id": "Cajun - JUGO DE MORA",
          "plu_quantity": 1,
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "tax_value": 0.85,
              "total": 6.5,
              "taxes": [
                {
                  "name": "IVA 15%",
                  "code": "iva_12",
                  "subtotal_without_taxes": 5.65,
                  "percentage": 15,
                  "total": 0.85
                }
              ]
            }
          }
        }
      ]
    },
    "result_payment": {
      "error": false,
      "mensaje": "",
      "datosRespuesta": [
        {
          "tipoMensaje": 0,
          "tipoRespuesta": 0,
          "codigoAdquiriente": 2,
          "codigorespuestaAutorizador": "00",
          "mensajeRespuesta": "00 AUTORIZACION OK. ",
          "secuenciaTransaccion": "003635",
          "numeroLote": "000046",
          "horaTransaccion": "143441",
          "fechaTransaccion": "20250611",
          "numeroAutorizacion": "769974",
          "terminalID": "KFC07001",
          "merchantID": "000000832412   ",
          "valorInteres": "            ",
          "mensajeriaImpresion": "        ",
          "codigoBancoAdquiriente": "   ",
          "codigobancoemisor": "                              ",
          "nombreGrupoTarjeta": "VISA ELECT/DEB           ",
          "modoLectura": 7,
          "nombreTarjetaHabiente": "PAYWAVE/VISA                            ",
          "montoFijo": "            ",
          "idemv": "VISA DEBITO         ",
          "aidemv": "A0000000031010      ",
          "tipoemv": "80                    ",
          "verificaPin": "               ",
          "arqc": "6C84F48EC0C9082A",
          "tvr": "0000000000",
          "tsi": "0000",
          "numTarjTrunca": "41668300XXXX1426         ",
          "fechVencTrj": "3002",
          "numTarjEncri": "YOUR_REDIS_OR_AZURE_KEY_HERE",
          "filler": "                           ",
          "proveedorTarjeta": "MEDIANET"
        }
      ],
      "codigo": "",
      "datos": []
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                                | Tipo    | Descripción                                |
| ------------------------------------------------------------------------------------ | ------- | ------------------------------------------ |
| `type_printer`                                                                       | string  | Tipo de impresión de voucher               |
| `transaction`                                                                        | object  | Información de la transacción              |
| `transaction.transaction_date`                                                       | string  | Fecha y hora de la transacción             |
| `transaction.point_of_sale`                                                          | object  | Información del punto de venta             |
| `transaction.point_of_sale.cdn_id`                                                   | string  | ID de la franquicia                        |
| `transaction.point_of_sale.restaurant_id`                                            | string  | ID del restaurante                         |
| `transaction.point_of_sale.cash_register_id`                                         | string  | ID de caja                                 |
| `transaction.point_of_sale.cash_register_name`                                       | string  | Nombre de caja                             |
| `transaction.point_of_sale.user_seller_id`                                           | string  | ID del vendedor                            |
| `transaction.point_of_sale.user_seller_name`                                         | string  | Nombre del vendedor                        |
| `transaction.point_of_sale.device_os_name`                                           | string  | Sistema operativo del dispositivo          |
| `transaction.point_of_sale.source_app_name`                                          | string  | Nombre de la aplicación                    |
| `transaction.point_of_sale.half_integration_id`                                      | number  | ID de integración                          |
| `transaction.point_of_sale.half_integration_name`                                    | string  | Nombre de integración                      |
| `transaction.point_of_sale.franchise_name`                                           | string  | Nombre de la cadena                        |
| `transaction.price`                                                                  | object  | Información de precios                     |
| `transaction.price.currency`                                                         | string  | Código de moneda                           |
| `transaction.price.total`                                                            | number  | Total de la transacción                    |
| `transaction.price.subsidy`                                                          | number  | Subsidio aplicado                          |
| `transaction.price.discount`                                                         | number  | Descuento aplicado                         |
| `transaction.price.tax`                                                              | number  | Total de impuestos                         |
| `transaction.price.base_amount`                                                      | number  | Base imponible total                       |
| `transaction.price.base_amountWithOutTax`                                            | number  | Base sin impuestos                         |
| `transaction.price.taxes`                                                            | array   | Arreglo de impuestos                       |
| `transaction.price.taxes[].tax_name`                                                 | string  | Nombre del impuesto                        |
| `transaction.price.taxes[].tax_code`                                                 | string  | Código del impuesto                        |
| `transaction.price.taxes[].tax_percentage`                                           | number  | Porcentaje del impuesto                    |
| `transaction.price.taxes[].total_tax_vulue`                                          | number  | Valor del impuesto                         |
| `transaction.price.taxes[].base_amount`                                              | number  | Base imponible                             |
| `transaction.payer`                                                                  | object  | Información del pagador                    |
| `transaction.payer.gov_id_type`                                                      | string  | Tipo de identificación                     |
| `transaction.payer.gov_id_number`                                                    | string  | Número de identificación                   |
| `transaction.payer.name`                                                             | string  | Nombre del pagador                         |
| `transaction.payer.last_name`                                                        | string  | Apellido del pagador                       |
| `transaction.payer.phone`                                                            | string  | Teléfono                                   |
| `transaction.payer.address`                                                          | string  | Dirección                                  |
| `transaction.payer.city`                                                             | string  | Ciudad                                     |
| `transaction.payer.state`                                                            | string  | Estado/Provincia                           |
| `transaction.payer.country`                                                          | string  | País                                       |
| `transaction.payer.zip_code`                                                         | string  | Código postal                              |
| `transaction.order_detail`                                                           | object  | Detalle de la orden                        |
| `transaction.order_detail.products`                                                  | array   | Lista de productos                         |
| `transaction.order_detail.products[].plu_id`                                         | string  | ID del PLU                                 |
| `transaction.order_detail.products[].cdn_plu_id`                                     | string  | ID del PLU en CDN                          |
| `transaction.order_detail.products[].plu_quantity`                                   | number  | Cantidad del producto                      |
| `transaction.order_detail.products[].price`                                          | object  | Información de precios del producto        |
| `transaction.order_detail.products[].price.total_per_plu`                            | object  | Precio por unidad                          |
| `transaction.order_detail.products[].price.total_per_plu.currency_code`              | string  | Código de moneda                           |
| `transaction.order_detail.products[].price.total_per_plu.subtotal_without_taxes`     | number  | Subtotal sin impuestos                     |
| `transaction.order_detail.products[].price.total_per_plu.discount_percentage`        | number  | Porcentaje de descuento                    |
| `transaction.order_detail.products[].price.total_per_plu.discounts_value`            | number  | Valor de descuentos                        |
| `transaction.order_detail.products[].price.total_per_plu.subtotal_include_discounts` | number  | Subtotal con descuentos                    |
| `transaction.order_detail.products[].price.total_per_plu.tax_value`                  | number  | Valor del impuesto                         |
| `transaction.order_detail.products[].price.total_per_plu.total`                      | number  | Total                                      |
| `transaction.order_detail.products[].price.total_per_plu.taxes`                      | array   | Impuestos aplicados                        |
| `transaction.order_detail.products[].price.total_price`                              | object  | Precio total por cantidad                  |
| `transaction.result_payment`                                                         | object  | Resultado del pago                         |
| `transaction.result_payment.error`                                                   | boolean | Si hubo error en el pago                   |
| `transaction.result_payment.mensaje`                                                 | string  | Mensaje de resultado                       |
| `transaction.result_payment.datosRespuesta`                                          | array   | Datos de respuesta del procesador          |
| `transaction.result_payment.datosRespuesta[].tipoMensaje`                            | number  | Tipo de mensaje                            |
| `transaction.result_payment.datosRespuesta[].tipoRespuesta`                          | number  | Tipo de respuesta                          |
| `transaction.result_payment.datosRespuesta[].codigoAdquiriente`                      | number  | Código del adquiriente                     |
| `transaction.result_payment.datosRespuesta[].codigorespuestaAutorizador`             | string  | Código de respuesta del autorizador        |
| `transaction.result_payment.datosRespuesta[].mensajeRespuesta`                       | string  | Mensaje de respuesta                       |
| `transaction.result_payment.datosRespuesta[].secuenciaTransaccion`                   | string  | Secuencia de transacción                   |
| `transaction.result_payment.datosRespuesta[].numeroLote`                             | string  | Número de lote                             |
| `transaction.result_payment.datosRespuesta[].horaTransaccion`                        | string  | Hora de transacción                        |
| `transaction.result_payment.datosRespuesta[].fechaTransaccion`                       | string  | Fecha de transacción                       |
| `transaction.result_payment.datosRespuesta[].numeroAutorizacion`                     | string  | Número de autorización                     |
| `transaction.result_payment.datosRespuesta[].terminalID`                             | string  | ID de terminal                             |
| `transaction.result_payment.datosRespuesta[].merchantID`                             | string  | ID de comercio                             |
| `transaction.result_payment.datosRespuesta[].valorInteres`                           | string  | Valor de interés                           |
| `transaction.result_payment.datosRespuesta[].mensajeriaImpresion`                    | string  | Mensajería de impresión                    |
| `transaction.result_payment.datosRespuesta[].codigoBancoAdquiriente`                 | string  | Código del banco adquiriente               |
| `transaction.result_payment.datosRespuesta[].codigobancoemisor`                      | string  | Código del banco emisor                    |
| `transaction.result_payment.datosRespuesta[].nombreGrupoTarjeta`                     | string  | Nombre del grupo de tarjeta                |
| `transaction.result_payment.datosRespuesta[].modoLectura`                            | number  | Modo de lectura (Chip, Banda, Manual)      |
| `transaction.result_payment.datosRespuesta[].nombreTarjetaHabiente`                  | string  | Nombre del tarjetahabiente                 |
| `transaction.result_payment.datosRespuesta[].montoFijo`                              | string  | Monto fijo                                 |
| `transaction.result_payment.datosRespuesta[].idemv`                                  | string  | ID EMV                                     |
| `transaction.result_payment.datosRespuesta[].aidemv`                                 | string  | AID EMV                                    |
| `transaction.result_payment.datosRespuesta[].tipoemv`                                | string  | Tipo EMV                                   |
| `transaction.result_payment.datosRespuesta[].verificaPin`                            | string  | Verificación de PIN                        |
| `transaction.result_payment.datosRespuesta[].arqc`                                   | string  | ARQC                                       |
| `transaction.result_payment.datosRespuesta[].tvr`                                    | string  | TVR                                        |
| `transaction.result_payment.datosRespuesta[].tsi`                                    | string  | TSI                                        |
| `transaction.result_payment.datosRespuesta[].numTarjTrunca`                          | string  | Número de tarjeta truncado                 |
| `transaction.result_payment.datosRespuesta[].fechVencTrj`                            | string  | Fecha de vencimiento                       |
| `transaction.result_payment.datosRespuesta[].numTarjEncri`                           | string  | Número de tarjeta encriptado               |
| `transaction.result_payment.datosRespuesta[].filler`                                 | string  | Relleno                                    |
| `transaction.result_payment.datosRespuesta[].proveedorTarjeta`                       | string  | Proveedor de tarjeta (procesador/pasarela) |
| `transaction.result_payment.codigo`                                                  | string  | Código de respuesta                        |
| `transaction.result_payment.datos`                                                   | array   | Datos adicionales                          |

### Respuestas del Servidor

#### 200 OK - Impresión Generada Correctamente

```json
{
  "code": 200,
  "status": "success",
  "alert": "Impresión generada correctamente",
  "messages": ["Impresión de voucher completada"]
}
```

## Generar Impresión de Voucher de Pago

### Método HTTP

`POST`

### URL

```
{{serverPrinter}}/api/v1/transaction/TX005
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "type_printer": "VOUCHER_APROBADO",
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
    "price": {
      "currency": "USD",
      "total": 100,
      "subsidy": 0,
      "discount": 0,
      "tax": 20
    },
    "payer": {
      "documentType": "CC",
      "documentNumber": "1009283738",
      "firstName": "Joy",
      "lastName": "Lino",
      "phone": "+593988734644",
      "address": "Eloy Alfaro 139 y Catalina Aldaz",
      "city": "Quito",
      "state": "Pichincha",
      "country": "Ecuador",
      "zipCode": "170402"
    },
    "result_payment": {
      "error": false,
      "mensaje": "",
      "datosRespuesta": [
        {
          "tipoMensaje": 0,
          "tipoRespuesta": 0,
          "codigoAdquiriente": 2,
          "codigorespuestaAutorizador": "03",
          "mensajeRespuesta": "03 ESTAB NOAFILIADO ",
          "secuenciaTransaccion": "000004",
          "numeroLote": "000001",
          "horaTransaccion": "161501",
          "fechaTransaccion": "20251224",
          "numeroAutorizacion": "      ",
          "terminalID": "KFC02301",
          "merchantID": "000000KFC023   ",
          "valorInteres": "            ",
          "mensajeriaImpresion": "        ",
          "codigoBancoAdquiriente": "   ",
          "codigobancoemisor": "                              ",
          "nombreGrupoTarjeta": "MASTERCARD/MAES          ",
          "modoLectura": 7,
          "nombreTarjetaHabiente": "                                        ",
          "montoFijo": "            ",
          "idemv": "MASTERCARD          ",
          "aidemv": "A0000000041010      ",
          "tipoemv": "80                    ",
          "verificaPin": "               ",
          "arqc": "D290590025C51F93",
          "tvr": "0000008001",
          "tsi": "E000",
          "numTarjTrunca": "54225820XXXX1554         ",
          "fechVencTrj": "    ",
          "numTarjEncri": "YOUR_REDIS_OR_AZURE_KEY_HERE",
          "filler": "                           "
        }
      ],
      "codigo": "",
      "datos": []
    }
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                                    | Tipo    | Descripción                                                                                               |
| ------------------------------------------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------- |
| `type_printer`                                                           | string  | Tipo de voucher (VOUCHER_APROBADO, VOUCHER_NO_APROBADO, VOUCHER_CANCELADO_NO_APROBADO, VOUCHER_ANULACION) |
| `transaction`                                                            | object  | Orden general con información de los puntos de venta                                                      |
| `transaction.point_of_sale`                                              | object  | Punto de venta con información física de quien y cómo realizó la venta                                    |
| `transaction.point_of_sale.cdn_id`                                       | string  | Identificador de la franquicia                                                                            |
| `transaction.point_of_sale.restaurant_id`                                | string  | Identificador del restaurante                                                                             |
| `transaction.point_of_sale.cash_register_id`                             | string  | Identificador de caja                                                                                     |
| `transaction.point_of_sale.cash_register_name`                           | string  | Nombre o código de caja                                                                                   |
| `transaction.point_of_sale.user_seller_id`                               | string  | Identificador de cajero o vendedor                                                                        |
| `transaction.point_of_sale.user_seller_name`                             | string  | Nombre de cajero/usuario                                                                                  |
| `transaction.point_of_sale.device_os_name`                               | string  | Sistema operativo donde se está vendiendo                                                                 |
| `transaction.point_of_sale.source_app_name`                              | string  | Origen de aplicativo                                                                                      |
| `transaction.point_of_sale.half_integration_id`                          | number  | ID de canal                                                                                               |
| `transaction.point_of_sale.half_integration_name`                        | string  | Nombre de canal                                                                                           |
| `transaction.price`                                                      | object  | Información de precios                                                                                    |
| `transaction.price.currency`                                             | string  | Tipo de moneda                                                                                            |
| `transaction.price.total`                                                | number  | Total de la transacción                                                                                   |
| `transaction.price.subsidy`                                              | number  | Subsidio aplicado                                                                                         |
| `transaction.price.discount`                                             | number  | Descuento aplicado                                                                                        |
| `transaction.price.tax`                                                  | number  | Impuesto aplicado                                                                                         |
| `transaction.payer`                                                      | object  | Información del pagador                                                                                   |
| `transaction.payer.documentType`                                         | string  | Tipo de documento                                                                                         |
| `transaction.payer.documentNumber`                                       | string  | Número de documento                                                                                       |
| `transaction.payer.firstName`                                            | string  | Nombre                                                                                                    |
| `transaction.payer.lastName`                                             | string  | Apellido                                                                                                  |
| `transaction.payer.phone`                                                | string  | Teléfono                                                                                                  |
| `transaction.payer.address`                                              | string  | Dirección                                                                                                 |
| `transaction.payer.city`                                                 | string  | Ciudad                                                                                                    |
| `transaction.payer.state`                                                | string  | Estado/Provincia                                                                                          |
| `transaction.payer.country`                                              | string  | País                                                                                                      |
| `transaction.payer.zipCode`                                              | string  | Código postal                                                                                             |
| `transaction.result_payment`                                             | object  | Resultado del pago                                                                                        |
| `transaction.result_payment.error`                                       | boolean | Si hubo error en el pago                                                                                  |
| `transaction.result_payment.mensaje`                                     | string  | Mensaje de resultado                                                                                      |
| `transaction.result_payment.datosRespuesta`                              | array   | Datos de respuesta del procesador                                                                         |
| `transaction.result_payment.datosRespuesta[].tipoMensaje`                | number  | Tipo de mensaje                                                                                           |
| `transaction.result_payment.datosRespuesta[].tipoRespuesta`              | number  | Tipo de respuesta                                                                                         |
| `transaction.result_payment.datosRespuesta[].codigoAdquiriente`          | number  | Código del adquiriente                                                                                    |
| `transaction.result_payment.datosRespuesta[].codigorespuestaAutorizador` | string  | Código de respuesta del autorizador                                                                       |
| `transaction.result_payment.datosRespuesta[].mensajeRespuesta`           | string  | Mensaje de respuesta                                                                                      |
| `transaction.result_payment.datosRespuesta[].secuenciaTransaccion`       | string  | Secuencia de transacción                                                                                  |
| `transaction.result_payment.datosRespuesta[].numeroLote`                 | string  | Número de lote                                                                                            |
| `transaction.result_payment.datosRespuesta[].horaTransaccion`            | string  | Hora de transacción                                                                                       |
| `transaction.result_payment.datosRespuesta[].fechaTransaccion`           | string  | Fecha de transacción                                                                                      |
| `transaction.result_payment.datosRespuesta[].numeroAutorizacion`         | string  | Número de autorización                                                                                    |
| `transaction.result_payment.datosRespuesta[].terminalID`                 | string  | ID de terminal                                                                                            |
| `transaction.result_payment.datosRespuesta[].merchantID`                 | string  | ID de comercio                                                                                            |
| `transaction.result_payment.datosRespuesta[].valorInteres`               | string  | Valor de interés                                                                                          |
| `transaction.result_payment.datosRespuesta[].mensajeriaImpresion`        | string  | Mensajería de impresión                                                                                   |
| `transaction.result_payment.datosRespuesta[].codigoBancoAdquiriente`     | string  | Código del banco adquiriente                                                                              |
| `transaction.result_payment.datosRespuesta[].codigobancoemisor`          | string  | Código del banco emisor                                                                                   |
| `transaction.result_payment.datosRespuesta[].nombreGrupoTarjeta`         | string  | Nombre del grupo de tarjeta                                                                               |
| `transaction.result_payment.datosRespuesta[].modoLectura`                | number  | Modo de lectura                                                                                           |
| `transaction.result_payment.datosRespuesta[].nombreTarjetaHabiente`      | string  | Nombre del tarjetahabiente                                                                                |
| `transaction.result_payment.datosRespuesta[].montoFijo`                  | string  | Monto fijo                                                                                                |
| `transaction.result_payment.datosRespuesta[].idemv`                      | string  | ID EMV                                                                                                    |
| `transaction.result_payment.datosRespuesta[].aidemv`                     | string  | AID EMV                                                                                                   |
| `transaction.result_payment.datosRespuesta[].tipoemv`                    | string  | Tipo EMV                                                                                                  |
| `transaction.result_payment.datosRespuesta[].verificaPin`                | string  | Verificación de PIN                                                                                       |
| `transaction.result_payment.datosRespuesta[].arqc`                       | string  | ARQC                                                                                                      |
| `transaction.result_payment.datosRespuesta[].tvr`                        | string  | TVR                                                                                                       |
| `transaction.result_payment.datosRespuesta[].tsi`                        | string  | TSI                                                                                                       |
| `transaction.result_payment.datosRespuesta[].numTarjTrunca`              | string  | Número de tarjeta truncado                                                                                |
| `transaction.result_payment.datosRespuesta[].fechVencTrj`                | string  | Fecha de vencimiento                                                                                      |
| `transaction.result_payment.datosRespuesta[].numTarjEncri`               | string  | Número de tarjeta encriptado                                                                              |
| `transaction.result_payment.datosRespuesta[].filler`                     | string  | Relleno                                                                                                   |
| `transaction.result_payment.codigo`                                      | string  | Código de respuesta                                                                                       |
| `transaction.result_payment.datos`                                       | array   | Datos adicionales                                                                                         |

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

#### 500 Internal Server Error - Cuerpo de Solicitud Vacío

```json
{
  "code": 500,
  "status": "failed",
  "alert": "Ocurrio un error al imprimir",
  "messages": ["A non-empty request body is required."]
}
```

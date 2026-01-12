## Registrar Homologación de Tarjeta de Pago

### Método HTTP

`POST`

### URL

```
{{server_payments}}/api/v1/paymentcardhomologations/post_payment_card_homologation
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "country_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
  "data_transaction": {
    "tipoMensaje": 0,
    "tipoRespuesta": 0,
    "codigoAdquiriente": 2,
    "codigorespuestaAutorizador": "61",
    "mensajeRespuesta": "CUPO--EXCEDIDO      ",
    "secuenciaTransaccion": "012578",
    "numeroLote": "000064",
    "horaTransaccion": "102140",
    "fechaTransaccion": "20251208",
    "numeroAutorizacion": "      ",
    "terminalID": "JVZ03001",
    "merchantID": "000000JVZ030   ",
    "valorInteres": "            ",
    "mensajeriaImpresion": "        ",
    "codigoBancoAdquiriente": "   ",
    "codigobancoemisor": "                              ",
    "nombreGrupoTarjeta": "VISA ELECT DEB           ",
    "modoLectura": 7,
    "nombreTarjetaHabiente": "PAYWAVE/VISA                            ",
    "montoFijo": "            ",
    "idemv": "VISA DEBITO         ",
    "aidemv": "A0000000031010      ",
    "tipoemv": "80                    ",
    "verificaPin": "               ",
    "arqc": "CD0CC39D4F96043F",
    "tvr": "0000000000",
    "tsi": "0000",
    "numTarjTrunca": "42398800XXXX5636         ",
    "fechVencTrj": "    ",
    "numTarjEncri": "YOUR_REDIS_OR_AZURE_KEY_HERE",
    "filler": "                           "
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                         | Tipo   | Descripción                           |
| --------------------------------------------- | ------ | ------------------------------------- |
| `country_id`                                  | string | Identificador del país                |
| `data_transaction`                            | object | Datos de la transacción               |
| `data_transaction.tipoMensaje`                | number | Tipo de mensaje                       |
| `data_transaction.tipoRespuesta`              | number | Tipo de respuesta                     |
| `data_transaction.codigoAdquiriente`          | number | Código del adquiriente                |
| `data_transaction.codigorespuestaAutorizador` | string | Código de respuesta del autorizador   |
| `data_transaction.mensajeRespuesta`           | string | Mensaje de respuesta                  |
| `data_transaction.secuenciaTransaccion`       | string | Secuencia de la transacción           |
| `data_transaction.numeroLote`                 | string | Número de lote                        |
| `data_transaction.horaTransaccion`            | string | Hora de la transacción                |
| `data_transaction.fechaTransaccion`           | string | Fecha de la transacción               |
| `data_transaction.numeroAutorizacion`         | string | Número de autorización                |
| `data_transaction.terminalID`                 | string | Identificador de la terminal          |
| `data_transaction.merchantID`                 | string | Identificador del comerciante         |
| `data_transaction.valorInteres`               | string | Valor de interés                      |
| `data_transaction.mensajeriaImpresion`        | string | Mensajería de impresión               |
| `data_transaction.codigoBancoAdquiriente`     | string | Código del banco adquiriente          |
| `data_transaction.codigobancoemisor`          | string | Código del banco emisor               |
| `data_transaction.nombreGrupoTarjeta`         | string | Nombre del grupo de tarjeta           |
| `data_transaction.modoLectura`                | number | Modo de lectura de la tarjeta         |
| `data_transaction.nombreTarjetaHabiente`      | string | Nombre del tarjetahabiente            |
| `data_transaction.montoFijo`                  | string | Monto fijo                            |
| `data_transaction.idemv`                      | string | Identificador EMV                     |
| `data_transaction.aidemv`                     | string | AID EMV                               |
| `data_transaction.tipoemv`                    | string | Tipo EMV                              |
| `data_transaction.verificaPin`                | string | Verificación de PIN                   |
| `data_transaction.arqc`                       | string | ARQC (Application Request Cryptogram) |
| `data_transaction.tvr`                        | string | TVR (Terminal Verification Results)   |
| `data_transaction.tsi`                        | string | TSI (Transaction Status Information)  |
| `data_transaction.numTarjTrunca`              | string | Número de tarjeta truncado            |
| `data_transaction.fechVencTrj`                | string | Fecha de vencimiento de la tarjeta    |
| `data_transaction.numTarjEncri`               | string | Número de tarjeta encriptado          |
| `data_transaction.filler`                     | string | Relleno                               |

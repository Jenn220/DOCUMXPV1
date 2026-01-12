## Obtener Métodos de Pago y Restricciones de Tipos

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/payments/api/v1/paymenttype/get_payment_methods_and_types_restrictions
```

### Headers

| Key          | Value            | Descripción                       |
| ------------ | ---------------- | --------------------------------- |
| Content-Type | application/json | Tipo de contenido de la solicitud |
| is_download  | is_download      | Indicador de descarga             |

### Parámetros de Query

| Key           | Value                                | Descripción                           |
| ------------- | ------------------------------------ | ------------------------------------- |
| franchise     | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia        |
| device        | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador del dispositivo         |
| restaurant    | 18ab3836-3202-f6d4-1eef-a5b5de5a8e40 | Identificador del restaurante         |
| cash_register | aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0 | Identificador de la caja registradora |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

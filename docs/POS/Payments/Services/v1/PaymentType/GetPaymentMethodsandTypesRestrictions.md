## Obtener Métodos y Tipos de Pago con Restricciones

### Método HTTP

`GET`

### URL

```
{{server_payments}}/api/v1/paymenttype/get_payment_methods_and_types_restrictions
```

### Parámetros de Query

| Key           | Value                                | Descripción                           |
| ------------- | ------------------------------------ | ------------------------------------- |
| franchise     | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia        |
| device        | 668d3b43-ab48-4fe0-ab01-ea4f21107be8 | Identificador del dispositivo         |
| restaurant    | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante         |
| cash_register | aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0 | Identificador de la caja registradora |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

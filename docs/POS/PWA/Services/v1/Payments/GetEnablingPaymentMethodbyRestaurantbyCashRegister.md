## Obtener Métodos de Pago Habilitados por Restaurante y Caja Registradora

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/YOUR_REDIS_OR_AZURE_KEY_HEREget_enabling_payment_method_by_restaurant_by_cash_register
```

### Headers

| Key          | Value            | Descripción                       |
| ------------ | ---------------- | --------------------------------- |
| Content-Type | application/json | Tipo de contenido de la solicitud |
| is_download  | is_download      | Indicador de descarga             |

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

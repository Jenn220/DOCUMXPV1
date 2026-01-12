## Obtener Drive Thru por Restaurante

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/internalClients/api/v1/drivethru/get_drivethru_by_restaurant
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
| restaurant | 18ab3836-3202-f6d4-1eef-a5b5de5a8e40 | Identificador del restaurante  |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

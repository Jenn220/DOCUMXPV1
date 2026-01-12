## Obtener Fondos por Franquicia y Restaurante

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/internalClients/api/v1/fund/get_all_funds_by_franchise_and_restaurant
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

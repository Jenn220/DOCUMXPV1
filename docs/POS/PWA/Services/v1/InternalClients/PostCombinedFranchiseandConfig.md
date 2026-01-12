## Registrar Franquicia y Configuración Combinada

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/internalClients/api/v1/franchise/post_combined_franchise_and_config
```

### Headers

| Key          | Value            | Descripción                       |
| ------------ | ---------------- | --------------------------------- |
| Content-Type | application/json | Tipo de contenido de la solicitud |
| is_download  | is_download      | Indicador de descarga             |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchises": [
    {
      "franchise_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurants": [
        {
          "restaurant_id": "e17d03da-b8b6-f424-febc-3a767b6401bb"
        },
        {
          "restaurant_id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
        }
      ]
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                      | Tipo   | Descripción                     |
| ------------------------------------------ | ------ | ------------------------------- |
| `franchises`                               | array  | Lista de franquicias            |
| `franchises[].franchise_id`                | string | Identificador de la franquicia  |
| `franchises[].restaurants`                 | array  | Lista de restaurantes asociados |
| `franchises[].restaurants[].restaurant_id` | string | Identificador del restaurante   |

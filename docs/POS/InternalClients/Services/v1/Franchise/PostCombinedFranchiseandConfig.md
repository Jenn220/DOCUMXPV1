## Registrar Franquicia Combinada con Configuración

### Método HTTP

`POST`

### URL

```
{{server_internalClients}}/api/v1/franchise/post_combined_franchise_and_config
```

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
          "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1"
        }
      ]
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                      | Tipo   | Descripción                    |
| ------------------------------------------ | ------ | ------------------------------ |
| `franchises`                               | array  | Lista de franquicias           |
| `franchises[].franchise_id`                | string | Identificador de la franquicia |
| `franchises[].restaurants`                 | array  | Lista de restaurantes          |
| `franchises[].restaurants[].restaurant_id` | string | Identificador del restaurante  |

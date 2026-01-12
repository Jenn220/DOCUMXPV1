## Obtener Restaurantes por Franquicia

### Método HTTP

`GET`

### URL

```
{{server_BackOffice_InternalClients}}/api/v1/restaurants/getallbyfranchise
```

### Parámetros de Query

| Key            | Value                                  | Description         |
| -------------- | -------------------------------------- | ------------------- |
| `franchise_id` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | Franchise ID (UUID) |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Success",
  "data": [
    {
      "restaurant_id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
      "cdn_restaurant_id": "REST001",
      "restaurant_name": "KFC Centro",
      "province_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "city_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "city_name": "Bogotá",
      "province_name": "Cundinamarca"
    }
  ]
}
```

## Obtener Franquicias por País

### Método HTTP

`GET`

### URL

```
{{server_BackOffice_InternalClients}}/api/v1/franchise/getbycountry
```

### Parámetros de Query

| Key          | Value                                  | Description       |
| ------------ | -------------------------------------- | ----------------- |
| `country_id` | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | Country ID (UUID) |

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
      "id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "franchise_name": "KFC Colombia",
      "country_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f"
    }
  ]
}
```

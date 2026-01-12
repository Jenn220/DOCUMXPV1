## Obtener Moneda

### Método HTTP

`GET`

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
{
  "_id": {
    "$binary": {
      "base64": "PFQsd5np9MY/9waQJpgpVg==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
      "subType": "04"
    }
  },
  "currency_name": "DOLAR",
  "currency_code": "USD",
  "decimal_places": 2,
  "description": "Tipo de moneda USD",
  "created_at": {
    "$date": "2025-02-26T15:35:20.638Z"
  },
  "updated_at": {
    "$date": "2025-02-26T15:35:20.638Z"
  }
}
```

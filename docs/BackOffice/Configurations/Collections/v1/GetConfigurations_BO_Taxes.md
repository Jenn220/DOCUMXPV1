## Obtener Impuesto

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
      "base64": "0AxL6aVH9y24eyq668B/Sw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
      "subType": "04"
    }
  },
  "tax_name": "IVA 15%",
  "description": "Tasa de impuesto IVA 15%",
  "tax_rate": 15,
  "created_at": {
    "$date": "2025-11-26T17:59:11.835Z"
  },
  "updated_at": {
    "$date": "2025-11-26T17:59:11.835Z"
  }
}
```

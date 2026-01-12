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
      "base64": "7s66MbvFyerYJKpIYZlsJA==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
      "subType": "04"
    }
  },
  "tax_name": "IVA 8%",
  "description": "Tasa de impuesto IVA 8%",
  "tax_rate": 8,
  "created_at": {
    "$date": "2025-02-26T15:34:37.074Z"
  },
  "updated_at": {
    "$date": "2025-02-26T15:34:37.074Z"
  }
}
```

## Tipo de Servidor

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
      "base64": "I8yJLxUiDd2gV5OzI5ZPJQ==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "GKs4NjIC9tQe76W13lqOQA==",
      "subType": "04"
    }
  },
  "name": "Subsidio de UNA",
  "description": "Subsidio Banco Pichincha.",
  "image": "https://cdn.example.com/subsidios/energia2025.png",
  "start_date": {
    "$date": "2025-01-01T00:00:00.000Z"
  },
  "end_date": {
    "$date": "2025-12-31T23:59:59.000Z"
  },
  "value": 10000,
  "currency": "USD",
  "enabled": true,
  "limit_per_client": 10,
  "payment_methods": [
    {
      "$binary": {
        "base64": "Neh/fsV8eCLL2L97cI3g8Q==",
        "subType": "04"
      }
    }
  ],
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  }
}
```

## Obtener PLU de Subsidios Habilitados

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
      "base64": "NCymAvs+B0l1AJPellNETA==",
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
  "plu_id": {
    "$binary": {
      "base64": "qzcN2Thbm3cLzzjNUCmOlg==",
      "subType": "04"
    }
  },
  "campaign_id": {
    "$binary": {
      "base64": "I8yJLxUiDd2gV5OzI5ZPJQ==",
      "subType": "04"
    }
  },
  "subsidy_value": 300,
  "enabled": true,
  "limit_per_product": 50,
  "needs_approval": true,
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  }
}
```

## Obtener Campaña Anidada de Propagaciones

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
      "base64": "fSBWNKeSRb2mZ7NnDuuROw==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "t1GhLz1BRg2LNgEfVigjyQ==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "I8yJLxUiDd2gV5OzI5ZPJQ==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "ZIa9wf5QRW6m8EC0BpmysA==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-11-12T14:18:39.065Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "I8yJLxUiDd2gV5OzI5ZPJQ==",
          "subType": "04"
        }
      },
      "name": "Subsidio de UNA",
      "cdn_id": {
        "$binary": {
          "base64": "/CE6Ajy1R4GeENPxUZxR4g==",
          "subType": "04"
        }
      },
      "restaurant_id": {
        "$binary": {
          "base64": "VTDoQOKbQdSnFkRllEAAsA==",
          "subType": "04"
        }
      },
      "description": "Subsidio Banco Pichincha.",
      "image": "https://cdn.example.com/subsidios/energia2025.png",
      "start_date": {
        "$date": "2025-01-01T00:00:00.000Z"
      },
      "end_date": {
        "$date": "2025-12-31T23:59:59.000Z"
      },
      "value": 1000,
      "currency": "USD",
      "enabled": true,
      "limit_per_client": 2,
      "payment_methods": [],
      "created_at": {
        "$date": "2025-11-12T14:18:36.385Z"
      },
      "updated_at": {
        "$date": "2025-11-12T14:18:36.385Z"
      }
    }
  ]
}
```

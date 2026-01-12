## Restricciones de Pagos de Franquicia

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
      "base64": "rZkwZfhQF6595UteVkBbMw==",
      "subType": "04"
    }
  },
  "restriction_active": true,
  "franchises_restriction_active": true,
  "restaurants_restriction_active": true,
  "cash_registers_restriction_active": true,
  "payment_method_id": {
    "$binary": {
      "base64": "ab3Ak6v/hU+99sb6Bze4kg==",
      "subType": "04"
    }
  },
  "franchises": [
    {
      "$binary": {
        "base64": "vC2K2uJeG7dV/jLRIFrErw==",
        "subType": "04"
      }
    }
  ],
  "restaurants": [],
  "cash_registers": [],
  "created_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  }
}
```

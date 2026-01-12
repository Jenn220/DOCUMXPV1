## Obtener Restricciones de Pagos

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
      "base64": "bFqXJ5MDmbjjY1UtMgc4/w==",
      "subType": "04"
    }
  },
  "restriction_active": true,
  "franchises_restriction_active": true,
  "restaurants_restriction_active": true,
  "cash_registers_restriction_active": true,
  "franchises": [
    {
      "$binary": {
        "base64": "8sE6Ajy1R4GeENPxUZxR4g==",
        "subType": "04"
      }
    }
  ],
  "restaurants": [
    {
      "$binary": {
        "base64": "8sE6Ajy1R4GeENPxUZxR4g==",
        "subType": "04"
      }
    }
  ],
  "cash_registers": [
    {
      "$binary": {
        "base64": "bFqXJ5MDmbjjY1UtMgc4/w==",
        "subType": "04"
      }
    }
  ],
  "payment_method_id": {
    "$binary": {
      "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
      "subType": "04"
    }
  },
  "created_user": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-09T17:18:10.139Z"
  },
  "updated_at": {
    "$date": "2024-03-03T15:20:55.223Z"
  }
}
```

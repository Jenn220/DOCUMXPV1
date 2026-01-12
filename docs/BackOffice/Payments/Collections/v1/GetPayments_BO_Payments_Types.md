## Obtener Tipo de Pago

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
      "base64": "cai073gIR9S4NljXHS3Yrg==",
      "subType": "04"
    }
  },
  "country_id": {
    "$binary": {
      "base64": "8gePP3TSSc+uLJK4RRWtkA==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "rVXci9n3QUO5yzRTiOneaw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "2OSK0bJmQn66uCr2JnMQ7A==",
      "subType": "04"
    }
  },
  "payment_type_name": "Tipo de pago",
  "payment_methods": [
    {
      "_id": {
        "$binary": {
          "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
          "subType": "04"
        }
      },
      "order": 1
    },
    {
      "_id": {
        "$binary": {
          "base64": "o/+JPmv1LUmCDp33pCZCvw==",
          "subType": "04"
        }
      },
      "order": 2
    }
  ],
  "description": "descripción tipo de pago",
  "status_payment_type_id": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "order": 1,
  "created_at": {
    "$date": "2025-04-02T20:10:52.026Z"
  },
  "updated_at": {
    "$date": "2025-04-02T20:10:52.026Z"
  },
  "updated_user": "updated_user test"
}
```

## Métodos de Pago Habilitados de Franquicia

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
      "base64": "UTgBYD/yQ4yL2G/5RLTJYg==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "payment_enabling": ["abe9665d-4127-04ca-8e7e-6bc9912ca6f3"],
  "restaurants": [
    {
      "_id": {
        "$binary": {
          "base64": "JCYFefr4dj+qx14W+v+W0Q==",
          "subType": "04"
        }
      },
      "payment_enabling": ["35e87f7e-c57c-7822-cbd8-bf7b708de0f1"],
      "cash_register": [
        {
          "_id": {
            "$binary": {
              "base64": "qk7OfOxuqwEmp5XSwsgJwA==",
              "subType": "04"
            }
          },
          "payment_enabling": ["3be0126a-e739-3b40-6feb-f4aa92d73a7c"]
        }
      ]
    }
  ],
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
    "$date": "2025-09-24T17:18:10.139Z"
  },
  "updated_at": {
    "$date": "2025-09-24T15:20:55.223Z"
  }
}
```

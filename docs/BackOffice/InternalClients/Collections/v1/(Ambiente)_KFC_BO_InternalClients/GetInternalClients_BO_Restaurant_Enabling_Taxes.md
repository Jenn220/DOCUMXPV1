## Obtener Habilitación de Impuestos de Restaurante

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
      "base64": "2bPNHiXESh62NJ+J8m4U2w==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
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
      "base64": "4X0D2ri29CT+vDp2e2QBuw==",
      "subType": "04"
    }
  },
  "plus": [
    {
      "plu_id": {
        "$binary": {
          "base64": "LS7YA63k6tp/kCr0WiSrCg==",
          "subType": "04"
        }
      },
      "enabling_taxes": [
        {
          "tax_id": {
            "$binary": {
              "base64": "0AxL6aVH9y24eyq668B/Sw==",
              "subType": "04"
            }
          },
          "configuration": [
            {
              "start_date": {
                "$date": "2025-07-10T19:19:42.021Z"
              },
              "end_date": {
                "$date": "2025-07-14T19:19:42.021Z"
              },
              "tax_rate": 10
            }
          ]
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
    "$date": "2025-07-08T19:19:42.021Z"
  },
  "updated_at": {
    "$date": "2025-07-08T19:19:42.021Z"
  }
}
```

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
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
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
      "base64": "8sE6Ajy1R4GeENPxUZxR4g==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "VTDoQOKbQdSnFkRllUQACg==",
      "subType": "04"
    }
  },
  "plus": [
    {
      "plu_id": {
        "$binary": {
          "base64": "JWmJUKoLTCq5KaBArTEnCA==",
          "subType": "04"
        }
      },
      "enabling_taxes": [
        {
          "tax_id": {
            "$binary": {
              "base64": "awQO4//mrUWL3V4SjRdaDg==",
              "subType": "04"
            }
          },
          "configuration": [
            {
              "start_date": {
                "$date": "2025-08-01T15:48:05.919Z"
              },
              "end_date": {
                "$date": "2025-10-28T15:48:05.919Z"
              },
              "tax_rate": 0
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
    "$date": "2025-08-01T15:48:05.919Z"
  },
  "updated_at": {
    "$date": "2025-08-01T15:48:05.919Z"
  }
}
```

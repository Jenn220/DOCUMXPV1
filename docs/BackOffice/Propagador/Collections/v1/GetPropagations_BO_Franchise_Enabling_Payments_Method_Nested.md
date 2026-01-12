## Obtener Habilitación de Métodos de Pago de Franquicia Anidada de Propagaciones

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
      "base64": "CKY3H3DBQcqUdeMEx7YZyw==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "eCL4L0H1R9WR2j8QV6yEOg==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "2OSK0bJmQn66uCr2JnMQ7A==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "IEK5mXUgTKKaBUYInTQ89Q==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-10-13T17:18:49.854Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "cdn_id": {
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
      "payment_enabling": [
        {
          "$binary": {
            "base64": "P6hfZFcXRWKz/CyWP2avpg==",
            "subType": "04"
          }
        }
      ],
      "restaurants": [
        {
          "_id": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "payment_enabling": [
            {
              "$binary": {
                "base64": "P6hfZFcXRWKz/CyWP2avpg==",
                "subType": "04"
              }
            }
          ],
          "cash_register": [
            {
              "_id": {
                "$binary": {
                  "base64": "P6hfZFcXRWKz/CyWP2avpg==",
                  "subType": "04"
                }
              },
              "payment_enabling": [
                {
                  "$binary": {
                    "base64": "P6hfZFcXRWKz/CyWP2avpg==",
                    "subType": "04"
                  }
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
        "$date": "2025-09-28T17:57:04.572Z"
      },
      "updated_at": {
        "$date": "2025-09-28T17:57:04.572Z"
      }
    }
  ]
}
```

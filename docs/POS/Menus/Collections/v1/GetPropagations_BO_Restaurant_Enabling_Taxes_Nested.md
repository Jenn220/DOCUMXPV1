## Propagación de Impuestos Anidados Habilitados por Restaurante

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
      "base64": "hDRkQ6YwSXyqXuZ8yvyPtw==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "I2xQIrPnT0WjdzE9PLISFQ==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "BJrobHQ2Q06bDK3dCe0PqQ==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-07-11T21:18:31.557Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "3ig2KAwESi6e+rpBVwG0gQ==",
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
          "base64": "Nbcdnn6cj04lwEcs+7/3XA==",
          "subType": "04"
        }
      },
      "plus": [
        {
          "plu_id": {
            "$binary": {
              "base64": "B/BsYJmNJC6sq4yRwzm3BA==",
              "subType": "04"
            }
          },
          "enabling_taxes": [
            {
              "tax_id": {
                "$binary": {
                  "base64": "ibwHZpP+SmYmahgf+H30DQ==",
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
  ]
}
```

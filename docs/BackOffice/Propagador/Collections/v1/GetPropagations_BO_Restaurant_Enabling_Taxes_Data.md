## Obtener Datos de Habilitación de Impuestos de Restaurante de Propagaciones

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
      "base64": "IAtezeLbRWyEjSmDQhsYIg==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "rXGzpZd/TY6Tw/BVWlHl1w==",
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
      "base64": "WPFEzBc5StahVBfdi1eL/g==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-07-03T16:46:46.828Z"
  },
  "data_list": [
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
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "restaurant_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "plus": [
        {
          "plu_id": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "enabling_taxes": [
            {
              "tax_id": {
                "$binary": {
                  "base64": "P6hfZFcXRWKz/CyWP2avpg==",
                  "subType": "04"
                }
              },
              "configuration": [
                {
                  "start_date": {
                    "$date": "2025-07-03T16:45:52.552Z"
                  },
                  "start_hour": "string",
                  "end_date": {
                    "$date": "2025-07-03T16:45:52.552Z"
                  },
                  "end_hour": "string",
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
        "$date": "2025-07-03T16:45:52.552Z"
      },
      "updated_at": {
        "$date": "2025-07-03T16:45:52.552Z"
      }
    }
  ]
}
```

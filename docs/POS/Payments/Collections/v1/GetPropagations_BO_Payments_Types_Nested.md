## Tipos de Pagos Anidados

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
      "base64": "Ts/tr1k5TEqOxEKT98iv1Q==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "IkpnXCmRTsOwAuySnoAUHg==",
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
      "base64": "VKmp7xjTTf6SE8fd0QUhFQ==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-04-25T12:40:28.574Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "cai073gIR9S4NljXHS3Yrg==",
          "subType": "04"
        }
      },
      "cdn_id": {
        "$binary": {
          "base64": "JwvjHTgLTkaeiXt1dHsDYA==",
          "subType": "04"
        }
      },
      "user_id": {
        "$binary": {
          "base64": "2OSK0bJmQn66uCr2JnMQ7A==",
          "subType": "04"
        }
      },
      "payment_type_name": "payment_type_name test OK",
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
      "description": "description test OK",
      "status_payment_type": {
        "_id": {
          "$binary": {
            "base64": "P6hfZFcXRWKz/CyWP2avpg==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado para publicación restaurante",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2024-02-06T03:18:52.852Z"
        },
        "updated_at": {
          "$date": "2024-05-31T06:42:27.014Z"
        }
      },
      "order": 1,
      "created_user": "d8e48ad1-b266-427e-bab8-2af6267310ec",
      "created_at": {
        "$date": "2025-04-02T20:10:52.026Z"
      },
      "updated_at": {
        "$date": "2025-04-02T20:10:52.026Z"
      },
      "updated_user": "d8e48ad1-b266-427e-bab8-2af6267310ec"
    }
  ]
}
```

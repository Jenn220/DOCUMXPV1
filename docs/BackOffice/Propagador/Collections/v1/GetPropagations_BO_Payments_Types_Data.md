## Obtener Datos de Tipos de Pago de Propagaciones

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
      "base64": "E4J2BKe/T9eZqi8+8c/HjQ==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "qnzB+zEnRsiUChJzfjrxSw==",
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
      "base64": "dNYhL7GxSK2eJPCcTkGUvg==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-10-08T20:22:12.688Z"
  },
  "data_list": [
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
          "base64": "Uz1g3MZy0Uy5qSmAHIrgGg==",
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
  ]
}
```

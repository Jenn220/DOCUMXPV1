## Obtener Subsidios Habilitados de PLUs Anidados de Propagaciones

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
      "base64": "7y83IfbXR2OLlt3HGSfkqA==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "HRV+SFYjQS2OgKgT3LH2Gw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "8eLTxBERIiIzM0REVVVmZg==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "6AIE2+/aQcyUEVOU85TnjQ==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-12-02T19:54:56.689Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "8eLTxBERIiIzM0REVVVmZg==",
          "subType": "04"
        }
      },
      "subsidy_value": 10,
      "enabled": true,
      "limit_per_product": 1,
      "needs_approval": true,
      "cdn_id": {
        "$binary": {
          "base64": "8eLTxBERIiIzM0REVVVmZg==",
          "subType": "04"
        }
      },
      "restaurant_id": {
        "$binary": {
          "base64": "8eLTxBERIiIzM0REVVVmZg==",
          "subType": "04"
        }
      },
      "plu_id": {
        "$binary": {
          "base64": "9e8XrfK3lZCNij6/C2jc/g==",
          "subType": "04"
        }
      },
      "campaign_id": {
        "$binary": {
          "base64": "I8yJLxUiDd2gV5OzI5ZPJQ==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": "2025-12-02T19:54:54.695Z"
      },
      "updated_at": {
        "$date": "2025-12-02T19:54:54.695Z"
      }
    }
  ]
}
```

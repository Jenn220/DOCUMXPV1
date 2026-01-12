## Obtener Sincronización de Integración

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
      "base64": "HNYhCAqgQpy8tMsw4J+kVA==",
      "subType": "04"
    }
  },
  "synchronization_name": "Sincronización homologación de usuario administrador",
  "synchronization_code": "Z0001",
  "synchronization_observations": "",
  "synchronization_hour_to_execute": "2025-07-22T17:10:29.118Z",
  "synchronization_is_hour_and_date_Settings": false,
  "synchronization_is_recurrent_execution": false,
  "synchronization_recurring_execution": null,
  "synchronization_sync_run_state": [
    {
      "code": 200,
      "status": "success",
      "process": "I0001",
      "message": "Integración completada exitosamente",
      "syncId": "1cd62108-0aa0-429c-bcb4-cb30e09fa454",
      "data": {
        "EXTRACTS": [
          {
            "code": 200,
            "status": "success",
            "process": "E0001",
            "message": "Extracción completada exitosamente",
            "dateTime": {
              "$date": "2025-07-22T22:10:30.773Z"
            }
          }
        ],
        "TRANSFORMS": [
          {
            "code": 200,
            "status": "success",
            "process": "H001",
            "message": "Transformación completada exitosamente",
            "dateTime": {
              "$date": "2025-07-22T22:10:30.773Z"
            }
          }
        ],
        "LOADS": [
          {
            "code": 200,
            "status": "success",
            "process": "L0001",
            "message": "Carga completada exitosamente",
            "dateTime": {
              "$date": "2025-07-22T22:10:31.174Z"
            }
          }
        ]
      }
    }
  ],
  "integrations": [
    {
      "$binary": {
        "base64": "o62/LZW5TPyE5LeDLyg7Tg==",
        "subType": "04"
      }
    }
  ],
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "status_id": {
    "$binary": {
      "base64": "ky8sUNNtQKy6xQuV7I2/0g==",
      "subType": "04"
    }
  },
  "created_at": "2025-07-22T17:10:29.118Z",
  "updated_at": "2025-07-22T17:10:31.431Z",
  "country": [
    {
      "Country_id": {
        "$binary": {
          "base64": "hXrMw8WaS2yuhFlC9aFFgQ==",
          "subType": "04"
        }
      },
      "Country_name": "Ecuador",
      "Country_code": "ECU",
      "Country_description": "1"
    }
  ],
  "franchise": [],
  "enterprise": [
    {
      "Enterprise_id": {
        "$binary": {
          "base64": "FDQGgpL4SoKxVCOHSgCprA==",
          "subType": "04"
        }
      },
      "Enterprise_name": "INT FOOD SERVICES CORP SA",
      "Enterprise_code": "3"
    }
  ],
  "restaurant": []
}
```

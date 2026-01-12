## Obtener Almacén de Eventos de Subsidios Plus Habilitados

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
      "base64": "KU3ijrETSGaoO6XjR6mrgA==",
      "subType": "04"
    }
  },
  "eventUuid": {
    "$binary": {
      "base64": "HRV+SFYjQS2OgKgT3LH2Gw==",
      "subType": "04"
    }
  },
  "creationDate": {
    "$date": "2025-12-02T19:54:58.993Z"
  },
  "eventVersion": 1,
  "metadata": {
    "eventType": "SubsidysEnabledPerPlu",
    "source": "SubsidysEnabledPerPluService",
    "user": "f1e2d3c4-1111-2222-3333-444455556666",
    "correlationId": "1d157e48-5623-412d-8e80-a813dcb1f61b",
    "causationId": "8ac27d2f-58e3-4b96-b18a-558677bc8390"
  },
  "data": {
    "operation_id": {
      "$binary": {
        "base64": "HRV+SFYjQS2OgKgT3LH2Gw==",
        "subType": "04"
      }
    },
    "items_ids": [
      {
        "$binary": {
          "base64": "8eLTxBERIiIzM0REVVVmZg==",
          "subType": "04"
        }
      }
    ],
    "items_ids_with_errors": [],
    "service": "SubsidysEnabledPerPluService",
    "response_time": "",
    "service_status": "InProcess",
    "timestamp": {
      "$date": "2025-12-02T19:54:58.992Z"
    }
  }
}
```

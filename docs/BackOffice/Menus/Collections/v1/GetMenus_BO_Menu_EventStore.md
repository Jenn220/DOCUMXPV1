## Obtener Evento de Menú

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
      "base64": "LiFs0SrWTG6tsgFMtnqldw==",
      "subType": "04"
    }
  },
  "eventUuid": {
    "$binary": {
      "base64": "Sau48UW1Sl2EdgooX1cIdQ==",
      "subType": "04"
    }
  },
  "creationDate": {
    "$date": "2025-12-09T03:16:48.563Z"
  },
  "eventVersion": 1,
  "metadata": {
    "eventType": "MenuPropagatorToMenuProcessed",
    "source": "Propagator Microservice",
    "user": "9bf439f0-bde7-360c-ecba-fc3526bfa7b0",
    "correlationId": "49abb8f1-45b5-4a5d-8476-0a285f570875",
    "causationId": "6a570dca-972e-4c43-891e-41110ce7ed52"
  },
  "data": {
    "operation_id": {
      "$binary": {
        "base64": "Sau48UW1Sl2EdgooX1cIdQ==",
        "subType": "04"
      }
    },
    "items_ids": [],
    "items_ids_with_errors": [],
    "service": "MenuPropagatorToMenuProcessed",
    "response_time": "",
    "service_status": "InProcess",
    "timestamp": {
      "$date": "2025-12-09T03:16:48.563Z"
    }
  }
}
```

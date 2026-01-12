## Obtener Almacén de Eventos de Propagaciones

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
      "base64": "0x26XXMNRjOa/u4CZqW5hA==",
      "subType": "04"
    }
  },
  "eventUuid": {
    "$binary": {
      "base64": "qKaRGRcSSIyLBsHy9WaAtA==",
      "subType": "04"
    }
  },
  "creationDate": {
    "$date": "2025-11-26T16:48:19.227Z"
  },
  "eventVersion": 1,
  "metadata": {
    "eventType": "PluSentToMenuService",
    "source": "MicroServicePropagator",
    "user": "9bf439f0-bde7-360c-ecba-fc3526bfa7b0",
    "correlationId": "a8a69119-1712-488c-8b06-c1f2f56680b4",
    "causationId": "d31dba5d-730d-4633-9afe-ee0266a5b984"
  },
  "data": {
    "operation_id": {
      "$binary": {
        "base64": "qKaRGRcSSIyLBsHy9WaAtA==",
        "subType": "04"
      }
    },
    "items_ids": [],
    "items_ids_with_errors": [],
    "service": "MicroServicePropagator",
    "response_time": "",
    "service_status": "Completed",
    "timestamp": {
      "$date": "2025-11-26T16:48:18.931Z"
    }
  }
}
```

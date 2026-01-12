## Almacén de Eventos de PLU

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
      "base64": "hfcU0mNnSTaLypThHZ7Ubw==",
      "subType": "04"
    }
  },
  "eventUuid": {
    "$binary": {
      "base64": "mVI9mk7nQ/meVuqMrBcslw==",
      "subType": "04"
    }
  },
  "creationDate": {
    "$date": "2025-11-26T16:48:31.987Z"
  },
  "eventVersion": 1,
  "metadata": {
    "eventType": "Plu",
    "source": "PluService",
    "user": "9bf439f0-bde7-360c-ecba-fc3526bfa7b0",
    "correlationId": "99523d9a-4ee7-43f9-9e56-ea8cac172c97",
    "causationId": "ff770aa3-4ba3-4975-b984-39eb8a5279d7"
  },
  "data": {
    "operation_id": {
      "$binary": {
        "base64": "mVI9mk7nQ/meVuqMrBcslw==",
        "subType": "04"
      }
    },
    "items_ids": [],
    "items_ids_with_errors": [
      {
        "item_id": {
          "$binary": {
            "base64": "dakdxabBRwOzY8fqvx50Jw==",
            "subType": "04"
          }
        },
        "error_message": "El listado está vacío"
      }
    ],
    "service": "PluService",
    "response_time": "",
    "service_status": "WithErrors",
    "timestamp": {
      "$date": "2025-11-26T16:48:31.987Z"
    }
  }
}
```

## Obtener Catálogo de Eventos OPL de Configuraciones

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
      "base64": "gKyYwleX2kGp9RwK5xMn4Q==",
      "subType": "04"
    }
  },
  "country_id": {
    "$binary": {
      "base64": "1srIPWzl9i4mKB4umue1Hw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "event_code": "payment_reverse_card",
  "event_name": "Reverso de Pago con Tarjeta",
  "description": "Dispara el evento de reverso de pago con tarjeta",
  "type": "payment",
  "endpoint_url": "payments_orchestrator",
  "supports_retry": true,
  "max_payment_wait_time_seconds": 100,
  "retry_attempts": 0,
  "block_operations_on_failure": true,
  "created_user": {
    "$binary": {
      "base64": "l4tKP8nMRTaqJ6vk3pOjEw==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "l4tKP8nMRTaqJ6vk3pOjEw==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  }
}
```

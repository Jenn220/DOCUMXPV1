## Obtener Restricciones de Horarios de Restaurantes

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
      "base64": "9abx0Qx2QcuaWojSyn1Pjw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "9aax0Qx2QcuaWoopLX2Ujw==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "9abx0Qx2QcuaWojSyn1Pjw==",
      "subType": "04"
    }
  },
  "schedules": {
    "is_active": true,
    "is_every_days": false,
    "every_days": [
      {
        "start": "10:00:00",
        "end": "12:00:00"
      },
      {
        "start": "10:00:00",
        "end": "12:00:00"
      }
    ],
    "monday": [
      {
        "start": "10:00",
        "end": "15:00"
      },
      {
        "start": "18:00",
        "end": "22:00"
      }
    ],
    "tuesday": [
      {
        "start": "10:00",
        "end": "15:00"
      },
      {
        "start": "18:00",
        "end": "22:00"
      }
    ],
    "wednesday": [
      {
        "start": "10:00",
        "end": "15:00"
      }
    ],
    "thursday": [
      {
        "start": "10:00",
        "end": "15:00"
      },
      {
        "start": "18:00",
        "end": "22:00"
      }
    ],
    "friday": [
      {
        "start": "10:00",
        "end": "15:00"
      },
      {
        "start": "18:00",
        "end": "22:00"
      }
    ],
    "saturday": [
      {
        "start": "12:00",
        "end": "18:00"
      }
    ],
    "sunday": [
      {
        "start": "12:00",
        "end": "18:00"
      }
    ]
  },
  "created_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "created_at": "2024-02-06T03:18:52.852Z",
  "updated_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "updated_at": "2024-05-31T06:42:27.014Z"
}
```

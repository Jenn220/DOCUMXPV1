## Obtener Estados de Venta

### Método HTTP

`GET`

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
[
  {
    "_id": {
      "$binary": {
        "base64": "9QT72aau2UO7CH4Vw5rRmA==",
        "subType": "04"
      }
    },
    "status_name": "Pendiente",
    "description": "Estado periodo de venta pendiente por cerrar",
    "color": "#80ff80",
    "background_color": "#ff5733",
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  },
  {
    "_id": {
      "$binary": {
        "base64": "GmuwaXmK5EKsSXzc+7YS/A==",
        "subType": "04"
      }
    },
    "status_name": "Fin de día",
    "description": "Estado periodo de venta cerrado",
    "color": "#80ff80",
    "background_color": "#ffffff",
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  },
  {
    "_id": {
      "$binary": {
        "base64": "kmOPRFLNUUS9w6pjrXtAew==",
        "subType": "04"
      }
    },
    "status_name": "Asentado",
    "description": "Estado periodo de venta asentado",
    "color": "#80ff80",
    "background_color": "#ff5733",
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  },
  {
    "_id": {
      "$binary": {
        "base64": "Ys7ukAyO70akt1ZeFWkqrA==",
        "subType": "04"
      }
    },
    "status_name": "Abierto",
    "description": "Estado periodo de venta abierto para edición",
    "color": "#80ff80",
    "background_color": "#ffffff",
    "codeType": "SRZ",
    "user_id": {
      "$binary": {
        "base64": "oQtZE7/5zEmHAM4YZ/oEGQ==",
        "subType": "04"
      }
    },
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  }
]
```

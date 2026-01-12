## Obtener Período de Restaurante POS

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
      "base64": "JXdWHUhjTXOpYgh2SqtesA==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "4X0D2ri29CT+vDp2e2QBuw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "oQtZE7/5zEmHAM4YZ/oEGQ==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "restaurant_name": "Gus G001 - Nube - Centralizado",
  "cdn_restaurant_name": "Gus G001 - Nube - Centralizado",
  "start_date": {
    "$date": "2025-07-30T22:40:24.380Z"
  },
  "final_date": {
    "$date": {
      "$numberLong": "-2208971024000"
    }
  },
  "periodtype": "Manual",
  "status_Period": {
    "_id": {
      "$binary": {
        "base64": "dy3cSjRjTkOYI+dtK1lzhw==",
        "subType": "04"
      }
    },
    "status_name": "Iniciado",
    "description": "Estado de periodo Iniciado ",
    "color": "#000000",
    "background_color": "#E2F7E2",
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  }
}
```

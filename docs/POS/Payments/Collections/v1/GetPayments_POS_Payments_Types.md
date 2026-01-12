## Tipos de Pagos

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
      "base64": "KfZCr6cNTxy2Im1FmAgAdw==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "zETSrTA8pEaxiBPXa0vjjw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "payment_type_name": "Wallets",
  "payment_methods": [
    {
      "_id": {
        "$binary": {
          "base64": "XQ9dd0VUii0dDlPvFJUkkg==",
          "subType": "04"
        }
      },
      "order": 1
    },
    {
      "_id": {
        "$binary": {
          "base64": "dLgkavIQmzE3v0Jo2qXd/g==",
          "subType": "04"
        }
      },
      "order": 2
    },
    {
      "_id": {
        "$binary": {
          "base64": "Neh/fsV8eCLL2L97cI3g8Q==",
          "subType": "04"
        }
      },
      "order": 3
    },
    {
      "_id": {
        "$binary": {
          "base64": "MfH65Ttdlp6Z3fxFffWh7A==",
          "subType": "04"
        }
      },
      "order": 4
    }
  ],
  "description": "Tipo de pagos para wallets",
  "status_payment_type": {
    "_id": {
      "$binary": {
        "base64": "drC+MdArJgZpUw+FOaZFMg==",
        "subType": "04"
      }
    },
    "status_name": "Publicado",
    "description": "Estado publicado para categorías",
    "color": "#1B3E19",
    "background_color": "#E2F7E2",
    "created_at": {
      "$date": "2024-02-06T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-05-31T06:42:27.014Z"
    }
  },
  "order": 3,
  "created_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  }
}
```

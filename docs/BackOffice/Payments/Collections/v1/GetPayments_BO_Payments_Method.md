## Obtener Método de Pago

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
      "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnatvvuSk0ySTNrtr9sCA==",
      "subType": "04"
    }
  },
  "payment_method_name": "efectivo ecu",
  "description": "tipo de pagos para favoritos",
  "is_group_amount": true,
  "status_payment_method_id": {
    "$binary": {
      "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
      "subType": "04"
    }
  },
  "icon": {
    "icon_id": {
      "$binary": {
        "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
        "subType": "04"
      }
    },
    "color_id": {
      "$binary": {
        "base64": "HFaXJ5MDmbjjU1LTIHOP/w==",
        "subType": "04"
      }
    }
  },
  "images_payment_methods": [
    {
      "images_payment_method_id": {
        "$binary": {
          "base64": "Cz6k44QtBOnQg+KHP8q6Eg==",
          "subType": "04"
        }
      }
    },
    {
      "images_payment_method_id": {
        "$binary": {
          "base64": "Cz6k44QtBOnQg+KHP8q6Eg==",
          "subType": "04"
        }
      }
    }
  ],
  "created_user": {
    "$binary": {
      "base64": "GCnatvvuSk0ySTNrtr9sCA==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_user": {
    "$binary": {
      "base64": "GCnatvvuSk0ySTNrtr9sCA==",
      "subType": "04"
    }
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  }
}
```

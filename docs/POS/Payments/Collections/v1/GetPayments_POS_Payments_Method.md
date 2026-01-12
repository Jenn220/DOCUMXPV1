## Métodos de Pago

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
      "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "payment_method_name": "Efectivo",
  "description": "Tipo de pago efectivo",
  "is_group_amount": true,
  "authorization_required": false,
  "status_payment_method": {
    "_id": {
      "$binary": {
        "base64": "drC+MdArJgZpUw+FOaZFMg==",
        "subType": "04"
      }
    },
    "status_name": "Publicado",
    "description": "Estado publicado",
    "color": "#1B3E19",
    "background_color": "#E2F7E2",
    "created_at": {
      "$date": "2024-02-06T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-05-31T06:42:27.014Z"
    }
  },
  "icon": {
    "icon_id": {
      "$binary": {
        "base64": "NCymAvs+B0l1aJPellNETQ==",
        "subType": "04"
      }
    },
    "icon_name": "icon-cash",
    "icon_paths": 6,
    "icon_font": "Material or KFC1",
    "description": "Estado para publicación",
    "created_at": {
      "$date": "2024-02-06T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-05-31T06:42:27.014Z"
    },
    "color_id": {
      "$binary": {
        "base64": "klnuEWOWvhLOptjIJzjllw==",
        "subType": "04"
      }
    },
    "color_name": "distance",
    "color_hex": "#1B3E19",
    "background_color": "#1B3E19"
  },
  "images_payment_method": [
    {
      "_id": {
        "$binary": {
          "base64": "zUumPNOOQz2TFJHoxCXpLA==",
          "subType": "04"
        }
      },
      "extension": "jpg",
      "name": "Imagen2",
      "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d41797a1fb83_domicilio_4486_744x744_1678487100.png?d=400x400&format=webp%22",
      "description": "Descripción de la imagen",
      "size": {
        "width": 312,
        "height": 315
      },
      "device_image": {
        "_id": {
          "$binary": {
            "base64": "tGRXSHjCAWBWZ3kQWInB1w==",
            "subType": "04"
          }
        },
        "device_name": "Kiosco",
        "description": "Dispositivo para Kioscos",
        "created_at": {
          "$date": "2024-02-06T03:18:52.852Z"
        },
        "updated_at": {
          "$date": "2024-05-31T06:42:27.014Z"
        }
      },
      "path": "/accessStorage/kkcDev/imagen2.jpg",
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      }
    }
  ],
  "is_visible_invoices": true,
  "event_code_payment": "payment_cash",
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

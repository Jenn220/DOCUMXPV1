## Obtener Períodos de Restaurante de Clientes Internos

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
      "base64": "NhwUKRh5Scy40TpRJWtn1A==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefr4dj+qx14W+v+W0Q==",
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
  "restaurant_name": "UAT_Gus G008",
  "cdn_restaurant_name": "UAT_Gus G008",
  "start_date": {
    "$date": "2025-11-18T20:16:00.691Z"
  },
  "final_date": {
    "$date": "2025-11-18T20:29:24.486Z"
  },
  "periodtype": "Manual",
  "status_Period": {
    "_id": {
      "$binary": {
        "base64": "CkY5v4oGykq/CpGuLWqxew==",
        "subType": "04"
      }
    },
    "status_name": "Cerrado",
    "description": "Estado de periodo cerrado ",
    "color": "#000000",
    "background_color": "#FFF8D6",
    "created_at": {
      "$date": "2024-11-25T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-11-25T06:42:27.014Z"
    }
  }
}
```

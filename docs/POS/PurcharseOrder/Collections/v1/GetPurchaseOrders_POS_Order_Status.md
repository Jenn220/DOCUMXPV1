## Obtener Estados de Canal de Órdenes de Compra

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
      "base64": "pn9hGcPWTBCpbAAATI9DSA==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "status_name": "Entregada",
  "description": "Entregada",
  "color": "#0040b0",
  "background_color": "#ebf8ff",
  "codeType": "D",
  "channels": [
    {
      "_id": {
        "$binary": {
          "base64": "o/+JPmv1LUmCDp33pCZCvw==",
          "subType": "04"
        }
      },
      "name": "Kiosko"
    },
    {
      "_id": {
        "$binary": {
          "base64": "o/+JPmv1LUmCDp33pCZCvw==",
          "subType": "04"
        }
      },
      "name": "DriveThru"
    },
    {
      "_id": {
        "$binary": {
          "base64": "CppmFyMZTZK2qQAAxvPSSA==",
          "subType": "04"
        }
      },
      "name": "Caja"
    }
  ],
  "created_at": {
    "$date": "2024-11-27T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-11-27T03:18:52.852Z"
  },
  "updated_by": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  }
}
```

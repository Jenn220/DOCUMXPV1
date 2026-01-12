## Obtener Venta por Hora

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
      "base64": "pDSoorM6QeGyNACcUS/xgQ==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefr4dj+qx14W+v+W0Q==",
      "subType": "04"
    }
  },
  "period_id": {
    "$binary": {
      "base64": "CsYHGBSORFOiPMNkLS443g==",
      "subType": "04"
    }
  },
  "start_date": "07/09/2025",
  "final_date": "07/09/2025",
  "sales": [
    {
      "time": "19:00 - 19:59",
      "transactions": 3,
      "value": 21.23
    },
    {
      "time": "10:00 - 10:59",
      "transactions": 1,
      "value": 20.91
    },
    {
      "time": "15:00 - 15:59",
      "transactions": 2,
      "value": 7.24
    },
    {
      "time": "09:00 - 09:59",
      "transactions": 1,
      "value": 7.74
    },
    {
      "time": "13:00 - 13:59",
      "transactions": 1,
      "value": 6.24
    },
    {
      "time": "07:00 - 07:59",
      "transactions": 1,
      "value": 0.7
    },
    {
      "time": "11:00 - 11:59",
      "transactions": 1,
      "value": 38.17
    }
  ]
}
```

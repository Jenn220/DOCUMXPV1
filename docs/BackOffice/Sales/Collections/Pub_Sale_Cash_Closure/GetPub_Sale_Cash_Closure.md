## Obtener Cierre de Caja de Venta

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
      "base64": "WzsTDOklRdymo8SmYW/8Xw==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "cdn_name": "Cadena Ejemplo",
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefr4dj+qx14W+v+W0Q==",
      "subType": "04"
    }
  },
  "restaurant": "G001",
  "period_id": {
    "$binary": {
      "base64": "JmF7iDxETAuH12FuxjOf/Q==",
      "subType": "04"
    }
  },
  "final_date": {
    "$date": "2025-12-02T00:00:00.000Z"
  },
  "start_date": {
    "$date": "2025-12-02T00:00:00.000Z"
  },
  "sales": [
    {
      "gross_sales": 19.5,
      "net_sales": 16.95,
      "tax_sales": 2.55,
      "tax_percentages": [
        {
          "percentage": 8,
          "amount": 2.55
        }
      ],
      "zero_sale": 0,
      "discount": {
        "total_discount": 0,
        "tax_discount": 0,
        "zero_discount": 0
      },
      "service": 0,
      "transactions": 3,
      "means_of_sale": "local"
    }
  ],
  "total": {
    "gross_sales": 19.5,
    "net_sales": 16.95,
    "tax_sales": 2.55,
    "tax_percentages": [
      {
        "percentage": 8,
        "amount": 2.55
      }
    ],
    "zero_sale": 0,
    "discount": {
      "total_discount": 0,
      "tax_discount": 0,
      "zero_discount": 0
    },
    "service": 0,
    "transactions": 3
  },
  "status": {
    "status_id": {
      "$binary": {
        "base64": "GmuwaXmK5EKsSXzc+7YS/A==",
        "subType": "04"
      }
    },
    "status_name": "Pendiente",
    "description": "Estado periodo de venta pendiente",
    "color": "#ff8080",
    "background_color": "#ffffff"
  }
}
```

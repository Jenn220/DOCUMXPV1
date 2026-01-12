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
      "base64": "xZcpsx/0Qui+mbUJlFXGOQ==",
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
      "gross_sales": 29.4,
      "net_sales": 25.57,
      "vat_sales": 3.83,
      "zero_sale": 0,
      "discount": {
        "total_discount": 0,
        "vat_discount": 0,
        "zero_discount": 0
      },
      "service": 0,
      "transactions": 3,
      "means_of_sale": "Local"
    },
    {
      "gross_sales": 18.72,
      "net_sales": 16.28,
      "vat_sales": 2.44,
      "zero_sale": 0,
      "discount": {
        "total_discount": 0,
        "vat_discount": 0,
        "zero_discount": 0
      },
      "service": 0,
      "transactions": 2,
      "means_of_sale": "Drive"
    },
    {
      "gross_sales": 8.2,
      "net_sales": 7.13,
      "vat_sales": 1.07,
      "zero_sale": 0,
      "discount": {
        "total_discount": 0,
        "vat_discount": 0,
        "zero_discount": 0
      },
      "service": 0,
      "transactions": 3,
      "means_of_sale": "Llevar"
    },
    {
      "gross_sales": 45.91,
      "net_sales": 39.92,
      "vat_sales": 5.99,
      "zero_sale": 0,
      "discount": {
        "total_discount": 0,
        "vat_discount": 0,
        "zero_discount": 0
      },
      "service": 0,
      "transactions": 2,
      "means_of_sale": "Rappi"
    }
  ]
}
```

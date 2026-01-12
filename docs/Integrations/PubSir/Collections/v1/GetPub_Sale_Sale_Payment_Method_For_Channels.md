## Obtener Métodos de Pago de Venta por Canales

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
      "base64": "uOr9VVpLSz6sPMfZT0pbQg==",
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
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 2.5,
      "transactions": 1,
      "means_of_sale": "Local"
    },
    {
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 18.72,
      "transactions": 2,
      "means_of_sale": "Drive"
    },
    {
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 6.95,
      "transactions": 2,
      "means_of_sale": "Llevar"
    },
    {
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 38.17,
      "transactions": 1,
      "means_of_sale": "Rappi"
    },
    {
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "VISA",
      "value": 20.91,
      "transactions": 1,
      "means_of_sale": "Local"
    },
    {
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "VISA",
      "value": 1.25,
      "transactions": 1,
      "means_of_sale": "Llevar"
    },
    {
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "DINERS CLUB",
      "value": 5.99,
      "transactions": 1,
      "means_of_sale": "Local"
    },
    {
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "DINERS CLUB",
      "value": 7.74,
      "transactions": 1,
      "means_of_sale": "Rappi"
    }
  ]
}
```

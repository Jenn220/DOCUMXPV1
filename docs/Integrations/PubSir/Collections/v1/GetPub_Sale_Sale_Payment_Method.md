## Obtener Métodos de Pago de Venta

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
      "base64": "Bu+QF2XHSpKdtT3JDZ/5+w==",
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
      "cashier": "Daniel Llerena",
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 14.98,
      "transactions": 2
    },
    {
      "cashier": "Odalis Valencia",
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 45.12,
      "transactions": 3
    },
    {
      "cashier": "Odalis Valencia",
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "VISA",
      "value": 20.91,
      "transactions": 1
    },
    {
      "cashier": "Ariel Gavilanes",
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "DINERS CLUB",
      "value": 5.99,
      "transactions": 1
    },
    {
      "cashier": "Ariel Gavilanes",
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 6.24,
      "transactions": 1
    },
    {
      "cashier": "Daniel LLerena",
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "DINERS CLUB",
      "value": 7.74,
      "transactions": 1
    },
    {
      "cashier": "Daniel LLerena",
      "payment_method_id": "abe9665d-4127-04ca-8e7e-6bc9912ca6f3",
      "payment_method": "VISA",
      "value": 1.25,
      "transactions": 1
    }
  ]
}
```

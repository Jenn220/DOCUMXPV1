## Obtener Resumen de Conciliación de Restaurante

### Método HTTP

`GET`

````

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
{
  "_id": {
    "$binary": {
      "base64": "bhW8chDkTMKQB8EUu+MX8A==",
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
      "base64": "WxorBAwWTKu2Tu49CYAjJg==",
      "subType": "04"
    }
  },
  "data_conciliation": {
    "payment_methods": [],
    "totals": {
      "total_income": 0,
      "total_egress": 0,
      "total_withdrawn": 0,
      "total_transactions": 0,
      "total_pos_calculated": 0,
      "total_difference": 0,
      "total_declaredvalue": 0
    }
  },
  "data_summary_restaurant": {
    "total_transactions": 1,
    "average_ticket": 5.99,
    "invoice_count": 1,
    "invoice_total": 5.99,
    "credit_note_count": 0,
    "credit_note_total": 0,
    "pending_order_count": 0,
    "pending_order_total": 0,
    "surplus_missing": 0,
    "cashier_total": 1
  },
  "restaurant_summary_completed": false,
  "created_user": {
    "$binary": {
      "base64": "PJSYjE3bTB+0fHFvm2vfvg==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "PJSYjE3bTB+0fHFvm2vfvg==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2025-11-18T19:51:19.162Z"
  },
  "updated_at": {
    "$date": "2025-11-18T19:51:19.162Z"
  }
}
````

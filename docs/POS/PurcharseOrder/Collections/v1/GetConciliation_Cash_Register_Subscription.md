## Obtener Suscripción de Caja Registradora de Conciliación

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
      "base64": "LAgSv8XWTVGjNSrBvVNnZw==",
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
  "found_id": {
    "$binary": {
      "base64": "luaKxzKrRZeo1PVS5fQAlQ==",
      "subType": "04"
    }
  },
  "period_id": {
    "$binary": {
      "base64": "4fzQg5edSCWFQwVPXfORhA==",
      "subType": "04"
    }
  },
  "cash_register_subscription_id": {
    "$binary": {
      "base64": "qk7OfOxuqwEmp5XSwsgJwA==",
      "subType": "04"
    }
  },
  "conciliation_type": {
    "$binary": {
      "base64": "0oLC/Iff6EOjCDsRMpSMeQ==",
      "subType": "04"
    }
  },
  "seller": {
    "user_seller_id": {
      "$binary": {
        "base64": "wXtujYilnrUfRK7sFhSU2g==",
        "subType": "04"
      }
    },
    "user_seller_name": "CINTHYA BARRE VARGAS"
  },
  "data_conciliation": {
    "payment_methods": [
      {
        "_id": {
          "$binary": {
            "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
            "subType": "04"
          }
        },
        "method": "Efectivo",
        "transactions": 2,
        "income": 0,
        "income_details": [],
        "egress": 0,
        "egress_details": [],
        "declared_value": 12,
        "pos_calculated": 11.98,
        "difference": 0.019999999999999574,
        "details": []
      }
    ],
    "totals": {
      "total_income": 0,
      "total_egress": 0,
      "total_withdrawn": 0,
      "total_transactions": 2,
      "total_pos_calculated": 11.98,
      "total_difference": 0.019999999999999574,
      "total_declaredvalue": 12
    }
  },
  "data_summary_conciliation": {
    "total_transactions": 2,
    "average_ticket": 5.99,
    "invoice_count": 2,
    "invoice_total": 11.98,
    "credit_note_count": 0,
    "credit_note_total": 0,
    "pending_order_count": 0,
    "pending_order_total": 0,
    "surplus_missing": 0,
    "cashier_total": 1
  },
  "cash_conciliation_completed": true,
  "cash_conciliation_at": {
    "$date": "2025-11-12T16:50:43.927Z"
  },
  "cash_conciliation_by": {
    "$binary": {
      "base64": "PJSYjE3bTB+0fHFvm2vfvg==",
      "subType": "04"
    }
  },
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
    "$date": "2025-11-12T16:50:06.058Z"
  },
  "updated_at": {
    "$date": "2025-11-12T16:50:06.058Z"
  }
}
```

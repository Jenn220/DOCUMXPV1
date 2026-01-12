## Obtener Conciliación de Suscripción de Caja Registradora

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
      "base64": "F03PbuR2RQ+li1dGRLUrIg==",
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
      "base64": "GKs4NjIC9tQe76W13lqOQA==",
      "subType": "04"
    }
  },
  "found_id": {
    "$binary": {
      "base64": "mPnLUSrhRWasNmVenEcP6g==",
      "subType": "04"
    }
  },
  "period_id": {
    "$binary": {
      "base64": "6UeulHAWThuqHLZ+PsZZzw==",
      "subType": "04"
    }
  },
  "cash_register_subscription_id": {
    "$binary": {
      "base64": "zXc20Lsxw+fWN0BF/SkuSw==",
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
        "base64": "sBlGxlrIYUKRCk9PexeS8g==",
        "subType": "04"
      }
    },
    "user_seller_name": "GUARACA MALAN VICTOR GERARDO"
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
  "data_summary_conciliation": {
    "total_transactions": 0,
    "average_ticket": 0,
    "invoice_count": 0,
    "invoice_total": 0,
    "credit_note_count": 0,
    "credit_note_total": 0,
    "pending_order_count": 0,
    "pending_order_total": 0,
    "surplus_missing": 0,
    "cashier_total": 0
  },
  "cash_conciliation_completed": false,
  "cash_conciliation_at": {
    "$date": "2025-11-13T00:05:00.841Z"
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
    "$date": "2025-11-12T20:36:39.444Z"
  },
  "updated_at": {
    "$date": "2025-11-12T20:36:39.444Z"
  }
}
```

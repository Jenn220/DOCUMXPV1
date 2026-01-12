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
      "base64": "WzsTDOklRdymowxKZhb/Xw==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2IutoeTbdV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "cdn_name": "Cadena Ejemplo",
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefrfez+qx14W+v+W0Q==",
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
      "cashier": "CINTHYA BARRE VARGAS",
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 0,
      "pos_calculated": 11.74,
      "transactions": 2
    },
    {
      "cashier": "Daniel Llerena",
      "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
      "payment_method": "EFECTIVO",
      "value": 14.98,
      "transactions": 2
    }
  ],
  "total": [
    {
      "cashier": "CINTHYA BARRE VARGAS",
      "value": 5.74,
      "pos_calculated": 11.74,
      "transactions": 2,
      "cash_register_subscription_id": {
        "$binary": {
          "base64": "yMMAzBuCF0KehrKXElefEA==",
          "subType": "04"
        }
      },
      "cash_register_subscription_name": "caja001",
      "surplus_or_shortage": -6
    },
    {
      "cashier": "Daniel Llerena",
      "value": 14.98,
      "pos_calculated": 11.74,
      "transactions": 2,
      "cash_register_subscription_id": {
        "$binary": {
          "base64": "XMMAzBuCF0KehrKXElefEA==",
          "subType": "04"
        }
      },
      "cash_register_subscription_name": "caja002",
      "surplus_or_shortage": 3.74
    }
  ],
  "status": {
    "status_id": {
      "$binary": {
        "base64": "Gmu6CZeKREKsSXzc/LYS/A==",
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

## Obtener Configuración de Franquicia

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
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "franchise_name": "string",
  "country_id": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "menu_deep_level_nested": 0,
  "decimal_quantity": 0,
  "decimal_quantity_presentation": 0,
  "limit_time_remove_plu_from_order": 0,
  "limit_time_redirect_payments": 0,
  "limit_characters_comments": 0,
  "limit_max_size_batch_syncronize_orders": 0,
  "retries_period": 0,
  "theme_by_franchise": {
    "theme_id": {
      "$binary": {
        "base64": "tGRXSHjCABZWl3kQWInB1w==",
        "subType": "04"
      }
    },
    "is_active": true
  },
  "status_franchise": {
    "$binary": {
      "base64": "bFqXJ5MDmbjjY1UtMgc4/w==",
      "subType": "04"
    }
  },
  "restaurants": [
    {
      "_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "restaurant_name": "string",
      "company_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "description": "string",
      "address": "string",
      "cdn_restaurant_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "restaurant_code": "string",
      "restaurant_image": "string",
      "city_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "category_plu_default": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "active_sincronization_chouch_db": true,
      "type_period_default": "string",
      "active_cash_reconciliation": true,
      "couch_db": {
        "username": "probamos",
        "password": "string",
        "endpoint": "string",
        "alias": "string"
      },
      "opt_connection": {
        "username": "esta",
        "password": "string",
        "endpoint": "string",
        "alias": "string"
      },
      "sync_connection": {
        "username": "propagacion",
        "password": "string",
        "endpoint": "string",
        "alias": "string"
      },
      "limit_retry_get_all_menus_products_max": 0,
      "retry_time_get_all_menus_products": 0,
      "status_restaurant": {
        "$binary": {
          "base64": "bFqXJ5MDmbjjY1UtMgc4/w==",
          "subType": "04"
        }
      },
      "schedules": {
        "is_active": true,
        "is_every_days": true,
        "every_days": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "monday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "tuesday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "wednesday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "thursday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "friday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "saturday": [
          {
            "start": "string",
            "end": "string"
          }
        ],
        "sunday": [
          {
            "start": "string",
            "end": "string"
          }
        ]
      },
      "cash_registers_subscriptions": [
        {
          "_id": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "string",
          "description": "string",
          "payment_type_default": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "default_value_fund": "0",
          "type_fund_id": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "$binary": {
              "base64": "bFqXJ5MDmbjjY1UtMgc4/w==",
              "subType": "04"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-04-08T21:26:40.049Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "updated_at": {
            "$date": "2025-04-08T21:26:40.049Z"
          }
        }
      ],
      "created_at": {
        "$date": "2025-04-08T21:26:40.049Z"
      },
      "updated_at": {
        "$date": "2025-04-08T21:26:40.049Z"
      }
    }
  ],
  "tax_default": {
    "$binary": {
      "base64": "bFLplQPwOi9vX02mHBEs/Q==",
      "subType": "04"
    }
  },
  "administrators": [
    {
      "user_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      }
    }
  ],
  "information_block_images": [
    {
      "imagen_id": {
        "$binary": {
          "base64": "aldOAJEDQPej3jve/EuARw==",
          "subType": "04"
        }
      }
    }
  ],
  "created_user": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "P6hfZFcXRWKz/CyWP2avpg==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2025-04-08T21:26:40.049Z"
  },
  "updated_at": {
    "$date": "2025-04-08T21:26:40.049Z"
  },
  "limit_max_downloaded_restaurants": 0
}
```

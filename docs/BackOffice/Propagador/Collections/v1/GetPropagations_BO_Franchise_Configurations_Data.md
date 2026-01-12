## Obtener Datos de Configuraciones de Franquicia de Propagaciones

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
      "base64": "Sbjn3c5yQgunPJjFtiABkQ==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "R+oumBPCQNyao7R81CA6yw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "2OSK0bJmQn66uCr2JnMQ7A==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "37X6jdpvRl2DPhY5wWS3iA==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-10-13T17:15:32.791Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "l+b2B6jhQJC1XHRVApyrbw==",
          "subType": "04"
        }
      },
      "franchise_name": "Fanquicia fallida - exotic cuisine",
      "cdn_id": {
        "$binary": {
          "base64": "cBK7B/EqT9+kAp0BsmhQgA==",
          "subType": "04"
        }
      },
      "country_id": {
        "$binary": {
          "base64": "8sE6Ajy1R4GeENPxUZxR4g==",
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
      "is_enabled_departament_in_plu": true,
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
      "operation_policies_opl": [
        {
          "event_id": {
            "$binary": {
              "base64": "6riOdwVQD+zvQErsp8vyOA==",
              "subType": "04"
            }
          },
          "endpoint_url": "/api/v1/drawer/open/aqui2",
          "block_operations_on_failure": true
        },
        {
          "event_id": {
            "$binary": {
              "base64": "6riOdwVQD+zvQErsp8vyOA==",
              "subType": "04"
            }
          },
          "endpoint_url": "/api/v1/print/generic_printer_external0",
          "block_operations_on_failure": true
        }
      ],
      "restaurants": [
        {
          "_id": {
            "$binary": {
              "base64": "hCJrPeE7zEGyYtVfMkI50A==",
              "subType": "04"
            }
          },
          "restaurant_name": "El sason colombiano",
          "company_id": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "description": "comida llanera",
          "address": "castellana",
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
            "username": "prueba12",
            "password": "string",
            "endpoint": "string",
            "alias": "string"
          },
          "opl_connection": {
            "username": "esta2344444",
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
          "operation_policies_opl": [
            {
              "event_id": {
                "$binary": {
                  "base64": "6riOdwVQD+zvQErsp8vyOA==",
                  "subType": "04"
                }
              },
              "endpoint_url": "/api/v1/drawer/open",
              "block_operations_on_failure": true
            },
            {
              "event_id": {
                "$binary": {
                  "base64": "6riOdwVQD+zvQErsp8vyOA==",
                  "subType": "04"
                }
              },
              "endpoint_url": "/api/v1/print/generic_printer_external",
              "block_operations_on_failure": true
            }
          ],
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
              "default_value_fund": {
                "$numberDecimal": "0"
              },
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
              "operation_policies_opl": [
                {
                  "event_id": {
                    "$binary": {
                      "base64": "6riOdwVQD+zvQErsp8vyOA==",
                      "subType": "04"
                    }
                  },
                  "endpoint_url": "/api/v1/drawer/open",
                  "block_operations_on_failure": true
                },
                {
                  "event_id": {
                    "$binary": {
                      "base64": "6riOdwVQD+zvQErsp8vyOA==",
                      "subType": "04"
                    }
                  },
                  "endpoint_url": "/api/v1/print/generic_printer_external",
                  "block_operations_on_failure": true
                }
              ],
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
      "administrators": [],
      "information_block_images": [],
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
  ]
}
```

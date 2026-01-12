## Obtener Datos de Configuraciones de País

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
      "base64": "4PnkCaAAQ0yzw/FxPo0zGg==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "wrem1GKrQkWL+ZBrcY/G9w==",
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
      "base64": "8gePP3TSSc+uLJK4RRWtkA==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-04-28T16:34:44.155Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "P6hfZFcXRWKz/CyWP2avpg==",
          "subType": "04"
        }
      },
      "currencies": [
        {
          "currency_id": {
            "$binary": {
              "base64": "Yx79HqzVEfJHEKczjFM/Aw==",
              "subType": "04"
            }
          }
        }
      ],
      "max_amount_end_customer": 1,
      "session_expiration_time": 1,
      "api_base_url_customer": "api/test12",
      "client_id_api_customer": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "client_secret_api_customer": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "denominations": [
        {
          "denomination_id": {
            "$binary": {
              "base64": "+NGitdOFR6m4J+34kjRTIw==",
              "subType": "04"
            }
          }
        }
      ],
      "documents_identity": [
        {
          "document_id": {
            "$binary": {
              "base64": "P/36iHTbRB+UiTGkJyns4g==",
              "subType": "04"
            }
          }
        }
      ],
      "notification_push": [
        {
          "limit_time_minutes": 1,
          "retries": 1,
          "limit_time_minutes_block": 1
        }
      ],
      "notification_otp": [
        {
          "limit_time_minutes": 1,
          "retries": 1,
          "limit_time_minutes_block": 1
        }
      ],
      "transaction_lock_time": 1,
      "allows_client_change": true,
      "deleted_limit": 1,
      "legal_notes": "string",
      "images_login": [
        {
          "_id": {
            "$binary": {
              "base64": "BxuK6kBMSMqX0pNsw8kL7A==",
              "subType": "04"
            }
          },
          "user_id": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "extension": "jpg",
          "name": "Imagen2",
          "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d41797a1fb83_domicilio_4486_744x744_1678487100.png?d=400x400&format=webp%22",
          "description": "Descripción de la imagen",
          "size": {
            "width": 312,
            "height": 315
          },
          "path": "/accessStorage/kkcDev/imagen2.jpg",
          "device_image": {
            "$binary": {
              "base64": "tGRXSHjCAAZWl3kQWInB1w==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-05-31T06:42:27.014Z"
          }
        }
      ],
      "limit_failed_attempts": 1,
      "max_limit_fund": 1,
      "limit_time_block_user": 1,
      "payment_methods_config": [
        {
          "id_method": {
            "$binary": {
              "base64": "P6hfZFcXRWKz/CyWP2avpg==",
              "subType": "04"
            }
          },
          "declared_active": true,
          "payment_methods_config": true,
          "allow_withdrawal_value": true
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
        "$date": "2025-04-20T15:22:22.650Z"
      },
      "updated_at": {
        "$date": "2025-04-20T15:22:22.650Z"
      }
    }
  ]
}
```

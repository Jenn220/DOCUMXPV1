## Obtener Configuraciones de Franquicias de Clientes Internos

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
      "base64": "b/KdUIfzGJ34uaRtePGAbw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "franchise_name": "GUS",
  "country_id": {
    "$binary": {
      "base64": "1srIPWzl9i4mKB4umue1Hw==",
      "subType": "04"
    }
  },
  "menu_deep_level_nested": 3,
  "decimal_quantity": 6,
  "decimal_quantity_presentation": 2,
  "limit_time_remove_plu_from_order": 10,
  "limit_time_redirect_payments": 30,
  "limit_characters_comments": 100,
  "limit_max_size_batch_syncronize_orders": 100,
  "retries_period": 3,
  "status_franchise": {
    "_id": {
      "$binary": {
        "base64": "OX93DoPdGUKD02doBb6kyg==",
        "subType": "04"
      }
    },
    "status_name": "Publicado",
    "description": "Estado de publicado y activo",
    "color": "#FFF",
    "background_color": "#FDDF33",
    "created_at": {
      "$date": "2024-02-06T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-05-31T06:42:27.014Z"
    }
  },
  "restaurants": [
    {
      "_id": {
        "$binary": {
          "base64": "4X0D2ri29CT+vDp2e2QBuw==",
          "subType": "04"
        }
      },
      "restaurant_name": "UAT_Gus G001",
      "description": "Restaurante de G001",
      "address": "Av. de Mi casa y de su Casa",
      "cdn_restaurant_id": "EC-G001",
      "restaurant_image": "https://repositoryuatbo.azureedge.net/colombia/kfc/imagesCadena/GUS.png?sp=r&st=2025-03-31T19:52:31Z&se=2028-11-26T03:52:31Z&spr=https&sv=2024-11-04&sr=d&sig=7D7%2FHovilqDSP%2FhDwzTyrurlBR6%2FiMg99ERAturwmy4%3D&sdd=2",
      "city_id": {
        "$binary": {
          "base64": "D7cLlP+DRYe8rPzqXnGbXQ==",
          "subType": "04"
        }
      },
      "category_plu_default": {
        "$binary": {
          "base64": "m97rfxNsj2pIm9n8AtuQSg==",
          "subType": "04"
        }
      },
      "couch_db": {
        "username": "admin",
        "password": "PasswordKFC2025",
        "endpoint": "https://192.168.101.78:6984",
        "alias": "ECU_G001"
      },
      "active_sincronization_chouch_db": true,
      "type_period_default": "Manual",
      "status_restaurant": {
        "_id": {
          "$binary": {
            "base64": "VzUgWhB/x0yWPLBNZjdxKA==",
            "subType": "04"
          }
        },
        "status_name": "Active",
        "description": "Restaurant is currently open.",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2024-02-06T03:18:52.852Z"
        },
        "updated_at": {
          "$date": "2024-05-31T06:42:27.014Z"
        }
      },
      "schedules": {
        "is_active": true,
        "is_every_days": true,
        "every_days": [
          {
            "start": "06:00:00",
            "end": "23:00:00"
          }
        ],
        "monday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "tuesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "wednesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "thursday": [
          {
            "start": "10:00",
            "end": "23:00"
          }
        ],
        "friday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "saturday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ],
        "sunday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ]
      },
      "administrators": [
        {
          "_id": {
            "$binary": {
              "base64": "+d5HMIELH1c150Cp37R2EQ==",
              "subType": "04"
            }
          },
          "position": "Administrator k300",
          "email": "juan.gonzales@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Diego Gonzales",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "U0PrUELDeZmMWlKwLUCTHA==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "pe.casas@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Pedro Casas",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "twfGf/MsSb4c95kEbaN7AQ==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "luis.villalba@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Luis Villalba",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "C3P3cvqVoi5Bf52q5Fqomg==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "andres.alvarez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Andres Alvarez",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "6Igw5w+GZbb0oemG2rZh2w==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "amanda.ramirez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Amanda Ramirez",
          "phone": "+593112342213"
        }
      ],
      "cash_registers_subscriptions": [
        {
          "_id": {
            "$binary": {
              "base64": "t6cI61qtF0S7vakaIf65yg==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja-1-G001",
          "description": "UAT_Caja-1-G001",
          "payment_type_default": {
            "$binary": {
              "base64": "rTwq4TgnbUXIV6qR6OdZ3Q==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 0,
          "type_fund_id": {
            "$binary": {
              "base64": "vwJr+OAmckC2FkRtFLVsag==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "Lj23iJhfyUGPXIIg066jWA==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "CUAT_aja-2-G001",
          "description": "UAT_Caja-2-G001",
          "payment_type_default": {
            "$binary": {
              "base64": "rTwq4TgnbUXIV6qR6OdZ3Q==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 34,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "qLk2+PMU4EqNkwNQ6hDSqQ==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja-3-G001",
          "description": "UAT_Caja-3-G001",
          "payment_type_default": {
            "$binary": {
              "base64": "rTwq4TgnbUXIV6qR6OdZ3Q==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 23,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "SsRDXRvCYUuTj6KeSAuQMQ==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja-4-G001",
          "description": "UAT_Caja-4-G001",
          "payment_type_default": {
            "$binary": {
              "base64": "rTwq4TgnbUXIV6qR6OdZ3Q==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 23,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "PiLQL1Fvt0yfsmpqtDmtmQ==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja-5-G001",
          "description": "UAT_Caja-5-G001",
          "payment_type_default": {
            "$binary": {
              "base64": "rTwq4TgnbUXIV6qR6OdZ3Q==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 23,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        }
      ],
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      },
      "active_cash_reconciliation": true,
      "download_max_retry_attempts": 5,
      "download_retry_interval": 30,
      "opl_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.78",
        "alias": ""
      },
      "sync_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.78:8443",
        "alias": ""
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "GKs4NjIC9tQe76W13lqOQA==",
          "subType": "04"
        }
      },
      "restaurant_name": "UAT_Gus G002",
      "description": "GUS Carlos",
      "address": "6 DE DICIEMBRE Y COMERCIO",
      "cdn_restaurant_id": "UAT_ECU-G002",
      "restaurant_image": "https://repositoryUatBO.azureedge.YOUR_REDIS_OR_AZURE_KEY_HERE.png?sv=2022-11-02&ss=b&srt=co&sp=rx&se=2026-04-25T04:29:08Z&st=2024-04-24T20:29:08Z&spr=https&sig=smdg4im4sXLcBCURwNnwJOPs%2BztVlmwt8AOilDNwumE%3D",
      "city_id": {
        "$binary": {
          "base64": "D7cLlP+DRYe8rPzqXnGbXQ==",
          "subType": "04"
        }
      },
      "category_plu_default": {
        "$binary": {
          "base64": "m97rfxNsj2pIm9n8AtuQSg==",
          "subType": "04"
        }
      },
      "couch_db": {
        "username": "admin",
        "password": "PasswordKFC2025",
        "endpoint": "https://192.168.101.13:6984",
        "alias": "ECU-G002"
      },
      "active_sincronization_chouch_db": true,
      "type_period_default": "Manual",
      "status_restaurant": {
        "_id": {
          "$binary": {
            "base64": "VzUgWhB/x0yWPLBNZjdxKA==",
            "subType": "04"
          }
        },
        "status_name": "Active",
        "description": "Restaurant is currently open.",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2024-02-06T03:18:52.852Z"
        },
        "updated_at": {
          "$date": "2024-05-31T06:42:27.014Z"
        }
      },
      "schedules": {
        "is_active": true,
        "is_every_days": true,
        "every_days": [
          {
            "start": "06:00:00",
            "end": "23:00:00"
          }
        ],
        "monday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "tuesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "wednesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "thursday": [
          {
            "start": "10:00",
            "end": "23:00"
          }
        ],
        "friday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "saturday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ],
        "sunday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ]
      },
      "administrators": [
        {
          "_id": {
            "$binary": {
              "base64": "+d5HMIELH1c150Cp37R2EQ==",
              "subType": "04"
            }
          },
          "position": "Administrator k300",
          "email": "juan.gonzales@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Diego Gonzales",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "U0PrUELDeZmMWlKwLUCTHA==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "pe.casas@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Pedro Casas",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "twfGf/MsSb4c95kEbaN7AQ==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "luis.villalba@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Luis Villalba",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "C3P3cvqVoi5Bf52q5Fqomg==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "andres.alvarez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Andres Alvarez",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "6Igw5w+GZbb0oemG2rZh2w==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "amanda.ramirez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Amanda Ramirez",
          "phone": "+593112342213"
        }
      ],
      "cash_registers_subscriptions": [
        {
          "_id": {
            "$binary": {
              "base64": "zXc20Lsxw+fWN0BF/SkuSw==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja 1- G002",
          "description": "UAT_Caja Principal-G002",
          "payment_type_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 50,
          "type_fund_id": {
            "$binary": {
              "base64": "vwJr+OAmckC2FkRtFLVsag==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "SP",
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "nxa9DzX07EuUUQCsKCEhhg==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja 2 - G002",
          "description": "UAT_Caja Secundaria-G002",
          "payment_type_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 50,
          "type_fund_id": {
            "$binary": {
              "base64": "vwJr+OAmckC2FkRtFLVsag==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "codeType": "SP",
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        }
      ],
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      },
      "active_cash_reconciliation": true,
      "download_max_retry_attempts": 5,
      "download_retry_interval": 30,
      "opl_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.13",
        "alias": ""
      },
      "sync_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.13:8443",
        "alias": ""
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "JCYFefr4dj+qx14W+v+W0Q==",
          "subType": "04"
        }
      },
      "restaurant_name": "UAT_Gus G008",
      "description": "UAT_GUS ESTADIO",
      "address": "6 DE DICIEMBRE Y COMERCIO",
      "cdn_restaurant_id": "ECU-G008",
      "restaurant_image": "https://repositoryUatBO.azureedge.YOUR_REDIS_OR_AZURE_KEY_HERE.png?sv=2022-11-02&ss=b&srt=co&sp=rx&se=2026-04-25T04:29:08Z&st=2024-04-24T20:29:08Z&spr=https&sig=smdg4im4sXLcBCURwNnwJOPs%2BztVlmwt8AOilDNwumE%3D",
      "city_id": {
        "$binary": {
          "base64": "D7cLlP+DRYe8rPzqXnGbXQ==",
          "subType": "04"
        }
      },
      "category_plu_default": {
        "$binary": {
          "base64": "m97rfxNsj2pIm9n8AtuQSg==",
          "subType": "04"
        }
      },
      "couch_db": {
        "username": "admin",
        "password": "PasswordKFC2025",
        "endpoint": "https://192.168.101.13:6984",
        "alias": "ECU_GOO8"
      },
      "active_sincronization_chouch_db": true,
      "type_period_default": "Manual",
      "status_restaurant": {
        "_id": {
          "$binary": {
            "base64": "VzUgWhB/x0yWPLBNZjdxKA==",
            "subType": "04"
          }
        },
        "status_name": "Active",
        "description": "Restaurant is currently open.",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2024-02-06T03:18:52.852Z"
        },
        "updated_at": {
          "$date": "2024-05-31T06:42:27.014Z"
        }
      },
      "schedules": {
        "is_active": true,
        "is_every_days": true,
        "every_days": [
          {
            "start": "06:00:00",
            "end": "23:00:00"
          }
        ],
        "monday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "tuesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "wednesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "thursday": [
          {
            "start": "10:00",
            "end": "23:00"
          }
        ],
        "friday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "saturday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ],
        "sunday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ]
      },
      "administrators": [
        {
          "_id": {
            "$binary": {
              "base64": "+d5HMIELH1c150Cp37R2EQ==",
              "subType": "04"
            }
          },
          "position": "Administrator k300",
          "email": "juan.gonzales@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Diego Gonzales",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "U0PrUELDeZmMWlKwLUCTHA==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "pe.casas@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Pedro Casas",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "twfGf/MsSb4c95kEbaN7AQ==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "luis.villalba@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Luis Villalba",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "C3P3cvqVoi5Bf52q5Fqomg==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "andres.alvarez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Andres Alvarez",
          "phone": "+593112342213"
        },
        {
          "_id": {
            "$binary": {
              "base64": "6Igw5w+GZbb0oemG2rZh2w==",
              "subType": "04"
            }
          },
          "position": "Administrator",
          "email": "amanda.ramirez@kfc.com.ec",
          "status": {
            "_id": {
              "$binary": {
                "base64": "drC+MdArJgZpUw+FOaZFMg==",
                "subType": "04"
              }
            },
            "status_name": "Publicado",
            "description": "Estado publicado para caja",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "fullname": "Amanda Ramirez",
          "phone": "+593112342213"
        }
      ],
      "cash_registers_subscriptions": [
        {
          "_id": {
            "$binary": {
              "base64": "qk7OfOxuqwEmp5XSwsgJwA==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja 1- G008",
          "description": "UAT_Caja Principal-G008 ",
          "payment_type_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 0,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "iPgC0QluuLbTYa6+K54AuQ==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas ",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        },
        {
          "_id": {
            "$binary": {
              "base64": "QSohKC2op0KC1eXANrGNFw==",
              "subType": "04"
            }
          },
          "cash_registers_subscriptions_name": "UAT_Caja 2- G008",
          "description": "UAT_Caja Secundaria-G008 ",
          "payment_type_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "method_payment_default": {
            "$binary": {
              "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
              "subType": "04"
            }
          },
          "default_value_fund": 0,
          "type_fund_id": {
            "$binary": {
              "base64": "ogJNThjZck620k7YbbenWw==",
              "subType": "04"
            }
          },
          "status_cash_register": {
            "_id": {
              "$binary": {
                "base64": "iPgC0QluuLbTYa6+K54AuQ==",
                "subType": "04"
              }
            },
            "codeType": "AC",
            "status_name": "Activa",
            "description": "Estado de Activo de subcripcion de Cajas ",
            "color": "#1B3E19",
            "background_color": "#E2F7E2",
            "created_at": {
              "$date": "2024-02-06T03:18:52.852Z"
            },
            "updated_at": {
              "$date": "2024-05-31T06:42:27.014Z"
            }
          },
          "created_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_at": {
            "$date": "2024-02-06T03:18:52.852Z"
          },
          "updated_user": {
            "$binary": {
              "base64": "GCnanvu+SjvSSjNgtb9sCA==",
              "subType": "04"
            }
          }
        }
      ],
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      },
      "active_cash_reconciliation": true,
      "download_max_retry_attempts": 5,
      "download_retry_interval": 30,
      "opl_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.13",
        "alias": ""
      },
      "sync_connection": {
        "username": "",
        "password": "",
        "endpoint": "https://192.168.101.13:8443",
        "alias": ""
      }
    }
  ],
  "tax_default": {
    "_id": {
      "$binary": {
        "base64": "0AxL6aVH9y24eyq668B/Sw==",
        "subType": "04"
      }
    },
    "tax_name": "Impuesto 15%",
    "tax_rate": 15,
    "description": "tasa de impuesto 15%",
    "created_at": {
      "$date": "2024-02-06T03:18:52.852Z"
    },
    "updated_at": {
      "$date": "2024-05-31T06:42:27.014Z"
    }
  },
  "information_block_images": [
    {
      "_id": {
        "$binary": {
          "base64": "9abx0Qx2QcuaWojSyn1Pjw==",
          "subType": "04"
        }
      },
      "extension": "jpg",
      "name": "Imagen3",
      "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d4f0-f219-4f95-b113-355689353d94?sv=2019-12-12&ss=bfqt&srt=sco&sp=r&se=2024-03-10T00%3A00%3A00Z&st=2024-03-09T14%3A26%3A04Z&spr=https&sig=YOUR_REDIS_OR_AZURE_KEY_HERE%3D",
      "size": {
        "width": 312,
        "height": 315
      },
      "path": "/accessStorage/kkcDev/imagen2.jpg",
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "KWpYf0sG6E876UY53CYPZg==",
          "subType": "04"
        }
      },
      "extension": "jpg",
      "name": "Imagen2",
      "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d4f0-f219-4f95-b113-355689353d94?sv=2019-12-12&ss=bfqt&srt=sco&sp=r&se=2024-03-10T00%3A00%3A00Z&st=2024-03-09T14%3A26%3A04Z&spr=https&sig=YOUR_REDIS_OR_AZURE_KEY_HERE%3D",
      "size": {
        "width": 312,
        "height": 315
      },
      "path": "/accessStorage/kkcDev/imagen2.jpg",
      "created_at": {
        "$date": "2024-02-06T03:18:52.852Z"
      },
      "updated_at": {
        "$date": "2024-05-31T06:42:27.014Z"
      }
    }
  ],
  "created_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-02-06T03:18:52.852Z"
  },
  "updated_at": {
    "$date": "2024-05-31T06:42:27.014Z"
  },
  "limit_max_downloaded_restaurants": 3,
  "theme_by_franchise": {
    "codeType": "FRCS00102",
    "is_active": false,
    "image_logo": "https://repositoryuatbo.azureedge.net/colombia/kfc/imagesCadena/GUS.png?sp=r&st=2025-03-31T19:52:31Z&se=2028-11-26T03:52:31Z&spr=https&sv=2024-11-04&sr=d&sig=7D7%2FHovilqDSP%2FhDwzTyrurlBR6%2FiMg99ERAturwmy4%3D&sdd=2",
    "image_background": "https://repositoryuatbo.azureedge.net/colombia/kfc/imagesCadena/GUS.png?sp=r&st=2025-03-31T19:52:31Z&se=2028-11-26T03:52:31Z&spr=https&sv=2024-11-04&sr=d&sig=7D7%2FHovilqDSP%2FhDwzTyrurlBR6%2FiMg99ERAturwmy4%3D&sdd=2",
    "background_color_primary_hex": "#B22222",
    "background_color_dark_hex": "#D9EBD9",
    "background_color_light_hex": "#FBD5DC",
    "text_color_dark_hex": "#8B0000",
    "text_color_light_hex": "#D9EBD9",
    "optional_color_hex": "#E4002B",
    "icon": {
      "icon_name": "icon-franquicia-GUS",
      "icon_paths": 0,
      "icon_font": "mxp-icons-custom",
      "description": "Estado para publicación",
      "created_at": "2024-02-06T03:18:52.852Z",
      "updated_at": "2024-02-06T03:18:52.852Z",
      "color_name": "distance",
      "color_hex": "#FFF",
      "background_color_hex": "#FFF"
    },
    "created_at": "2024-02-06T03:18:52.852Z",
    "updated_at": "2024-02-06T03:18:52.852Z"
  },
  "categories_group_presentation": true,
  "operation_policies_opl": []
}
```

## Obtener Restricciones de Horarios de Restaurantes de Menú

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
      "base64": "n8JT2X/8Wu/9Y7lYPKENjw==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "time_restriction_active": false,
  "restaurants_restriction_active": false,
  "restaurants": [],
  "schedules": {
    "effective_active": false,
    "effective_start_date": {
      "$date": {
        "$numberLong": "-62135596800000"
      }
    },
    "effective_final_date": {
      "$date": {
        "$numberLong": "-62135596800000"
      }
    },
    "is_active_days": false,
    "is_every_days": false,
    "every_days": [],
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": [],
    "created_at": {
      "$date": {
        "$numberLong": "-62135596800000"
      }
    },
    "updated_at": {
      "$date": {
        "$numberLong": "-62135596800000"
      }
    }
  },
  "created_at": {
    "$date": {
      "$numberLong": "-62135596800000"
    }
  },
  "updated_at": {
    "$date": "2025-08-05T22:47:15.815Z"
  },
  "menu_id": {
    "$binary": {
      "base64": "MclvIZLcw43D9P9HDfQuIw==",
      "subType": "04"
    }
  },
  "categories": [
    {
      "_id": {
        "$binary": {
          "base64": "rER49M2buqhXRQcRCwZJ6g==",
          "subType": "04"
        }
      },
      "user_id": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "time_restriction_active": false,
      "restaurants_restriction_active": false,
      "restaurants": [],
      "schedules": {
        "effective_active": false,
        "effective_start_date": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "effective_final_date": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "is_active_days": false,
        "is_every_days": false,
        "every_days": [],
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
        "created_at": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "updated_at": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": "2025-08-05T22:47:15.904Z"
      },
      "menu_category_id": {
        "$binary": {
          "base64": "rER49M2buqhXRQcRCwZJ6g==",
          "subType": "04"
        }
      },
      "plus": [
        {
          "_id": {
            "$binary": {
              "base64": "DhTHuybUL9WiTlFciUJgmg==",
              "subType": "04"
            }
          },
          "user_id": {
            "$binary": {
              "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
              "subType": "04"
            }
          },
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "time_restriction_active": true,
          "restaurants_restriction_active": true,
          "restaurants": [
            {
              "$binary": {
                "base64": "UPau0venB6ESLs9fdBmzjA==",
                "subType": "04"
              }
            }
          ],
          "schedules": {
            "effective_active": false,
            "effective_start_date": {
              "$date": "2025-08-05T22:47:11.727Z"
            },
            "effective_final_date": {
              "$date": "2025-08-05T22:47:11.727Z"
            },
            "is_active_days": true,
            "is_every_days": false,
            "every_days": [],
            "monday": [],
            "tuesday": [],
            "wednesday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": [],
            "created_at": {
              "$date": "2025-08-05T22:47:12.238Z"
            },
            "updated_at": {
              "$date": "2025-08-05T22:47:12.238Z"
            }
          },
          "created_at": {
            "$date": {
              "$numberLong": "-62135596800000"
            }
          },
          "updated_at": {
            "$date": "2025-08-05T22:47:15.909Z"
          },
          "plu_id": {
            "$binary": {
              "base64": "DhTHuybUL9WiTlFciUJgmg==",
              "subType": "04"
            }
          }
        }
      ]
    },
    {
      "_id": {
        "$binary": {
          "base64": "ZNseQCwj9funAl/lSoESaQ==",
          "subType": "04"
        }
      },
      "user_id": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "time_restriction_active": false,
      "restaurants_restriction_active": false,
      "restaurants": [],
      "schedules": {
        "effective_active": false,
        "effective_start_date": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "effective_final_date": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "is_active_days": false,
        "is_every_days": false,
        "every_days": [],
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
        "created_at": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        },
        "updated_at": {
          "$date": {
            "$numberLong": "-62135596800000"
          }
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": "2025-08-05T22:47:15.910Z"
      },
      "menu_category_id": {
        "$binary": {
          "base64": "ZNseQCwj9funAl/lSoESaQ==",
          "subType": "04"
        }
      },
      "plus": [
        {
          "_id": {
            "$binary": {
              "base64": "ighv81XMNvtEb9eSNP5P/g==",
              "subType": "04"
            }
          },
          "user_id": {
            "$binary": {
              "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
              "subType": "04"
            }
          },
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "time_restriction_active": true,
          "restaurants_restriction_active": false,
          "restaurants": [],
          "schedules": {
            "effective_active": false,
            "effective_start_date": {
              "$date": "2025-08-05T22:47:11.727Z"
            },
            "effective_final_date": {
              "$date": "2025-08-05T22:47:11.727Z"
            },
            "is_active_days": true,
            "is_every_days": false,
            "every_days": [],
            "monday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "tuesday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "wednesday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "thursday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "friday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "saturday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "sunday": [
              {
                "start": "06:00:00",
                "end": "23:59:00"
              }
            ],
            "created_at": {
              "$date": "2025-08-05T22:47:12.269Z"
            },
            "updated_at": {
              "$date": "2025-08-05T22:47:12.269Z"
            }
          },
          "created_at": {
            "$date": {
              "$numberLong": "-62135596800000"
            }
          },
          "updated_at": {
            "$date": "2025-08-05T22:47:15.910Z"
          },
          "plu_id": {
            "$binary": {
              "base64": "ighv81XMNvtEb9eSNP5P/g==",
              "subType": "04"
            }
          }
        }
      ]
    }
  ]
}
```

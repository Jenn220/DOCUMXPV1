## Obtener Pregunta Sugerida Anidada de Propagaciones

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
      "base64": "9OdO9v2vTeCxtlAm6zn0Eg==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "8SfObWz8SrSOK3UcZERFmA==",
      "subType": "04"
    }
  },
  "user_id": {
    "$binary": {
      "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
      "subType": "04"
    }
  },
  "optional_id": {
    "$binary": {
      "base64": "hiWTd7NySMS7uoWyYb0exA==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-05-07T20:03:37.127Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "/sU8O++tz6dJH3PLgC8HFQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DE TU BEBIDA?",
      "sug_question_tittle": "APP SABOR DE BEBIDA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "KJtILSLFCRlvc+pBoAkU4g==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "kWV0aZTMiQtVDEklcYmpRw==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "Rwt/I8PlTkFifZJ0sxHIow==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 0,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS REALIZAR ALGÚN CAMBIO A SU COMBO?",
      "sug_question_tittle": "PCK CAMBIO COMBOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "kZHOlHmZm/B2WuPtIoQItQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "nmHbMbADBlbaJ5CKjlRlnQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO CONSOME X LOCRO",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "CUqL5ztRoLX5AFXdUb6+iQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "XIxa9FqkJIlYmzXUiw1pZw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA x JUGO GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "YXf7oJP8VVn4IBf35nR54A==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "s3FxC5DReOLntdnC+gVByA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA x JUGO NARANJILLA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "V7L3McsyX9vnjqLTRF3uug==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "pI2VJbg/zwKAUFfeNlS8Xg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA X JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "dNcZM7WPBT9+InRz8lH/eA==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "L4+u5wGlCGohpujZGp8wOA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO CONSOME X SANCOCHO",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "/WYDGBwGfcLSacSmiF4zaQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 10,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS COMPLEMENTAR TU PEDIDO?",
      "sug_question_tittle": "PCK AGREGA COMBOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "0gonV/V7FmNOWjrTqnK7jA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "thTJoz0AiBGCFPllK421rQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGREGA PAPA FRITA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+MR0eyO9GYj3g1w+6k0vYQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "HiGAEu3ED6M1bBGQuQdMNg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "3Uc698RNWgXyHYa3w9c5/Q==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "aT7NY2pp8sJC+WyvuSpHXw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "SCaXTekSCmMn9un9GlUVcg==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "4aNQn/4R3UolBn32q/uSCA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "IeYxBgfEwTkb9nslc2vJGg==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "dD2/aPE3/avc4AGUuVW0cg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO D NARANJILLA GUS",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+JSgOfvyL9xx9UMYEOa7SQ==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "xlGzjq9Gx1c74cJdPsilFQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "v6BsFn/j+oCXe+gHZs00+w==",
              "subType": "04"
            }
          },
          "order": 7,
          "plu_id": {
            "$binary": {
              "base64": "LzZWdHpwBqwdS9CHBFBtRQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "FRUTILLA JR",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "7sSIdtQ3AJg1gS+YA2gyCw==",
              "subType": "04"
            }
          },
          "order": 11,
          "plu_id": {
            "$binary": {
              "base64": "kLPaADz8ofim3vdqW7VsBw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LOCRO PEQUENO",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "miOp102obZ5t0zOs/eq+QQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DE TU BEBIDA?",
      "sug_question_tittle": "PCK SABOR DE BEBIDA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "7jU/xevrJy3NWSCDgApLdg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "Pf3YFmEepXmyaS0Dm11KcA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "VQZ0z4dfyOAXshTY0WjXOw==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "AfFyzl9+iVxwb8OSZnkDUQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "eQKk7mEemj3tMWS/f6Z5mA==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "HMvzDNVZLbtr9/gkDi7aqg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "FRESA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "aO94nOgmRNYHGDLnIkFtzg==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "C73vFU/43my0CRoGrqH48A==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MANZANA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "mn5aZi7L83ZM/8B2bpT6wA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 0,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS CAMBIAR TU PAPA FRITA POR PAPA CRIOLLA?",
      "sug_question_tittle": "PCK CAMBIO FAMILIARES",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "nPDZKFETuP/wRGmJ6oE3pA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "nPsksbgsm/W+LFqsuG+t1w==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO P FRITA X CRIOLLA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "2FB57EeYybh6Mibems9vxg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 10,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS COMPLEMENTAR TU PEDIDO?",
      "sug_question_tittle": "PCK AGREGA FAMILIARES",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "qhKJuwuy4FRqhtOOUkfFOA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "HiGAEu3ED6M1bBGQuQdMNg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "rUj/pkHTVJ/xwoL+++C0/Q==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "aT7NY2pp8sJC+WyvuSpHXw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "MaSFVcZGCHvaE7QhUfmZBw==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "4aNQn/4R3UolBn32q/uSCA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Y+GBOkNLGs2tXuNP8k7A8Q==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "dD2/aPE3/avc4AGUuVW0cg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO D NARANJILLA GUS",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Q5TxrzcRXFs6Y81WsTJCig==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "xlGzjq9Gx1c74cJdPsilFQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "yXddQr8Rw3pYSBOzzi+ZDA==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "LzZWdHpwBqwdS9CHBFBtRQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "FRUTILLA JR",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "bQAFvaJmvDHA/qTmWWpaTw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 2,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DE TU BEBIDA",
      "sug_question_tittle": "APP SABOR DE BEBIDA 2",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "hv9JluCvJTQMGLSIhCBc0g==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "cV+E0TLUu5WC2J7YAYXDdg==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "rrty6Rn0RDeac2PSLXcnzA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 0,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA AGREGAR UNA BEBIDA A SU ORDEN",
      "sug_question_tittle": "APP BEBIDAS PAGADAS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "QiYxFOSZQSvNzwyLKILIQA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "PmQV4iwwBLCO5kkDYYUZjw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 2 LTS",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "jNlhU0IuEKastK3qTk1xpg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DE SU BEBIDA?",
      "sug_question_tittle": "BEBIDA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "9AgQE8w2KofNtfqweJqvBg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "HVACneyd+pO7UDx07wxR9A==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "h2XLG658EeLsVGO/+WAUhg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "EqqbaGEfLwBhAn7PxUTDfA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "rvsTC7JZ0/TwYPzCBU6rPA==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "z7U6l1St2ze9D9KOvcf1hw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NARANJA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "7U2oD88/r0TR9RSh51lcLA==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "RjTqmK2TQIFyo4DLr8hAuw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "FRESA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "399I82+S8RioiLoh2t4VAQ==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "nQ8dm6XTnGUO7/O/23fqZw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MANZANA - Salon",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "WcDe74DOMerNm0se+rSYaA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DEL HELADO?",
      "sug_question_tittle": "HELADO NACIONAL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "S+NQMKeZs9q8CXXZVsAOFQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "DQQ5zWQIZkoVh0huGr+1bg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CHOCOLATE - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Acshr8kE3RTCZpzgKXEmHQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "lWgnMKZl9dVxXVUjRsQcpw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "VAINILLA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "5ufIlo0CB6LLvC1drEaQWQ==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "mjbqZ9WJQHJ7OPzUY+4EKw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "RON PASAS - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Rtx31kRmkASBT0CqmxCpWQ==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "OOsReJKSNWy2HpF9R8sC4w==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MORA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+RbdWhoF5SJoALyBardeTQ==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "CX1Ab226Omv4UXMnU3+wEA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CHICLE - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Fh7TDmoclHLLo4wUXW5fnw==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "slBIyvl959AKsK7JuFh0pQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MIXTO - Salon",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "xXQ4S2uHpZlYr7y8aYxlBw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA CAMBIAR SU CONSOME",
      "sug_question_tittle": "CONSOME",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "/6EUOsTF1ANaWIRVYGRySw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "VWEEIzMGy7DWwptFde00AA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO CONSOME X LOCRO                   - Salon",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "9EPyCvDw5iy1pTy/wnh6bQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 4,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "ANADIR O RETIRAR?",
      "sug_question_tittle": "COMBOS 2, 6 Y 1/4",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "j3fGi6Onu74OaE4PO4plOw==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "s/gXOodPS9D7sQv67AyCLQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ARROZ - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "C9DKSMSkGJHFEqSriOPIAQ==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "QKstYtzfWqID0r+V4DSk6Q==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MENESTRA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "gfTW7RElxncCBZEK2ZvOGQ==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "4biI334w594EpYZSoukLRg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LECHUGA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "FOqIGgR31FvRjFYAIacD5Q==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "fZaxjRzwlTaaIRJyKo+Tqg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "TOMATE - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "zUIwfz3aIkopgW8g1OSSCA==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "bFH+UDLanJtNXECDMBR4ug==",
              "subType": "04"
            }
          },
          "answer_pos_description": "SIN MENESTRA - Salon",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "DxAL1Jq9QsVupMUm0RaWag==",
              "subType": "04"
            }
          },
          "order": 7,
          "plu_id": {
            "$binary": {
              "base64": "NQnu2M5r9UtDkaBr4w1eIw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "SIN ARROZ - Salon",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "EVEoMujY3JmyAho8WphW1w==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 3,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "COMPLEMENTOS - SALON",
      "sug_question_tittle": "COMPLEMENTOS - SALON",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "VtLhDz1Ocdpa+p/hc0WjRQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 3,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIOS - SALON",
      "sug_question_tittle": "CAMBIOS - SALON",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "xWkGgSQplc9rn4JX8dzNmg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "VWEEIzMGy7DWwptFde00AA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO CONSOME X LOCRO",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "361Z1/uvwzYnhAZ36e54fA==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "tJRBab7sPo1vSOBde5pvvg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA POR JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "pfsF8yXaK555C5Uepg4oAg==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "teQQlzsEL5OmzTLGbvc6iA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA x JUGO GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "x/YX6qP4V6kBBwXrauOIPg==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "5CXgkTEmIjbE6IKiABDTrg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 4,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGRANDADOS - SALON",
      "sug_question_tittle": "AGRANDADOS - SALON",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "O0noAUFzacDd4xEsUnYGWQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "EgLHLZBMVBg8XZBCDyMxjQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA COLA 12 A 22 OZ",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "yKDkHTf7HeZOBsAJ/Ak8Jw==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "HbGavq2yzW73wLn2tqa4EA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA PAPA CRIOLLA + COLA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "KPwreEJwJAM+EnfnFGPxEQ==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "iUmxrZxX/X0jsugAaWowVw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA FESTIN",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "RannhWIEbUDCKUOeBI+ctg==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "9I6JHCJU7dkoYO2D8GXMqg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGREGA - SALON",
      "sug_question_tittle": "AGREGA - SALON",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "VknONStXnlMk28KphRKiTg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "ETZ/lk2DNlMX5dzKXaYvNg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGREGA PAPA FRITA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "m9xnEbQpbaaU2LyICQDWtw==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "QwM3oSyBpgI96fp3AKzFYQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "3LCJk3WZE4qpnTrdHkIuVg==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "/ZB3uETXv67/qYtz/8Bbbg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "jRSYhfNuwafYBuaj+YSTdw==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "huc604OcXiC2cCuuF0NlSg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA LECHUGA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "ZgKXgHhLMTf1nEzbfE2TPw==",
              "subType": "04"
            }
          },
          "order": 7,
          "plu_id": {
            "$binary": {
              "base64": "oeIhGVVvQkjg2w4h9US3IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "OxvELybadHvnt8wnjAyCFA==",
              "subType": "04"
            }
          },
          "order": 8,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "auy85JYGqEijCUaROXqq3A==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 4,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGRANDADOS - LLEVAR",
      "sug_question_tittle": "AGRANDADOS - LLEVAR",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "pdoAzRz0Qn1crXt1t4ol7Q==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "rmOZk/1d+NsMEzxK9qStrQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA FESTIN",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "ohfsKmYytFukaCxmaN00PQ==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "fSBJwbMVLka7MaKmz02dUw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA PAPA FRITA + COLA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+fWuj8UzFnpOjhEJ+0WsuQ==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "oe/H2lVMsMEngQIZpuzBzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA PAPA CRIOLLA + COLA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "phTSGhir9A9tCkopaluRCQ==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "9nxyEycrD5/S2cOu8EpCGg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGREGA - LLEVAR",
      "sug_question_tittle": "AGREGA - LLEVAR",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "8sN/5KtNBxfoPHC8goWxaA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "8TW9+i4e3hbF8TrTWySCwg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA LECHUGA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "h+vNrBzyLPamOoSEzvUxkA==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "aT7NY2pp8sJC+WyvuSpHXw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "xyzpg01iEmrD8QcCzlvMHw==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "4aNQn/4R3UolBn32q/uSCA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "JUGO DE GUANABANA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "aSg0WvBCpi3d04kWPruv6Q==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "xlGzjq9Gx1c74cJdPsilFQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "e0+PB2ebDSVCFbEC4Jym/w==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "thTJoz0AiBGCFPllK421rQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGREGA PAPA FRITA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "F3nvS39pVmaPUt9kiXpMbw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 3,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIOS - LLEVAR",
      "sug_question_tittle": "CAMBIOS - LLEVAR",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "O9jztxWsqFUMMZ449diHGQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "nmHbMbADBlbaJ5CKjlRlnQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO CONSOME X LOCRO",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "GLo+b2hZwB4ylCo/CNec4w==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "XIxa9FqkJIlYmzXUiw1pZw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA x JUGO GUANABANA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "gu9Z2eYnzxTTAsxF9eh1cg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA REALIZAR ALGUN CAMBIO A SU COMBO?",
      "sug_question_tittle": "AGR CAMBIO COMBOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "caGOtYuU1Gvu2VXSUzLIGQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "7ILGSepo69KJ2xz/1scg3A==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO DE COLA X AGUA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "cHXZ6PH3XoYsMoCxefL6Vw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS COMPLEMENTAR TU PEDIDO?",
      "sug_question_tittle": "AGR AGREGA EXTRA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "nM6Uo6dfLzD2pSxKMC5Xqw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "u+IhbGP0ytQlzEMt2T6z2g==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "U0q1yPqwBOBrXr4n7zMoTg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "gnGNwuBr9FNY9m+qs7tsSw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ARROZ GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "g3kVTo/ORbF5RCecbsxD4w==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "t+7FpI8zUTRjoPEaWbIbfg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MENESTRA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "MTX0z3lCzbzxtNjF/9SXLg==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "c110LU+ZXeHl6pfnXdkBSg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA LECHUGA TOMATE",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "tDu/DKYO5jgn331GdsU+zw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL",
      "sug_question_tittle": "CAMBIO 1/4 GRANDE A 1/4 NORMAL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "A1nR7g5FLRWnQHPk0RRozw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "dEjWbNf7fkRaHVE7puXQ0Q==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "oSca1qHsAIiiKnfAZ+LWDw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "nXpNYfxoDjsLaZS+LXziIg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL LL",
      "sug_question_tittle": "CAMBIO 1/4 GRANDE A 1/4 NORMAL LL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "0X9WIE/CpQbVDDiOpaxrTA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "HhXuyZUR4MY0BAKy8XAfrA==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "yvCdoubirJqkFVOCVYXymQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL LL",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "pmxEIRTym+gWJ826NuaXIg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL DV",
      "sug_question_tittle": "CAMBIO 1/4 GRANDE A 1/4 NORMAL DV",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "xhBqsyuuIgJnzyPNL4ebMg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "EsEDh6ukMJzc87JlQrV4wQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "kM3/nWBBW516FvPi9QJLHQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO 1/4 GRANDE A 1/4 NORMAL DV",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "AaMO4wOIOA2bbVcXQrIsEQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO 1/8 GRANDE A 1/8 NORMAL",
      "sug_question_tittle": "CAMBIO 1/8 GRANDE A 1/8 NORMAL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "z6MBCqqXKN9KOxRqxIkayQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "ENRg0TAXktUhYusKhLL9Qg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "CNo1QI3mMUYuYybvVKKSAw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO 1/8 GRANDE A 1/8 NORMAL",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "qVPpBYSaard8qRHowM9z7A==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO 1/8 GRANDE A 1/8 NORMAL LL",
      "sug_question_tittle": "CAMBIO 1/8 GRANDE A 1/8 NORMAL LL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "KuSe4MO/jpGLpNJtAZ/4Wg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "5Ck0pCfL5vG48s09SdjYNg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "ENOoD3wPBzpulsfnKBiqpg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO 1/8 GRANDE A 1/8 NORMAL LL",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "Vgh70nAe3bJ7dVLKrPrJCA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGRANDA PAPA FRITA",
      "sug_question_tittle": "AGRANDA PAPA FRITA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "YeEet16lDYrBty65B55ImQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "GHFI7kFkKXjErYMlHRb7zA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA PAPA FRITA 50G",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "IrE9AuudfAnH6tAfwrfABg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "nALSWX6Ib7Xj2rF2n1eMQQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO COLA POR JUGO DE MORA",
      "sug_question_tittle": "CAMBIO COLA POR JUGO DE MORA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "VxPdqhCUs7RfWpwljFMVTg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "tJRBab7sPo1vSOBde5pvvg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA POR JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+nvKrKI1NPUsRSSamtkbVQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "tLxdVBjKUwOhJDl4K8dCjQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGRANDA PAPA FRITA LL",
      "sug_question_tittle": "AGRANDA PAPA FRITA LL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "1xvZT1VDUSbRE+h96EN+GQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "DP2hfqqrbFBiNR347u4ieQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "AGRANDA PAPA FRITA LL 50G",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "RWGJMIFc0N3kjlWStx66dQ==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "GEO11P6hkmlNdH+mN1INEw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO COLA X JUGO DE MORA LL",
      "sug_question_tittle": "CAMBIO COLA X JUGO DE MORA LL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "m9+BrBufkU74ZOkdWxc+QQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "pI2VJbg/zwKAUFfeNlS8Xg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO COLA X JUGO DE MORA",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "+Q8hu6x+IkYmwY+XhdmcXw==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "AwKnFlPPCMciZneDtc9/IA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "NO APLICA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "296gZqDt2lbJwi71XpdDNQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "AGREGA EXTRA",
      "sug_question_tittle": "APP AGREGA EXTRA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "OGRZV6dO9Yy4KYMVQdW4hg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "+5YhJW+uRlquxeRjWGJi2w==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ARROZ GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "/6U8QCR6uu6k2x10/N8HCA==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "1F1/dDYsd5/z0ZUt1avPtw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "MENESTRA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "hwRNnkrXspFNZHSev2px8Q==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "oj/vI8VZCpzSh1RdGWmAZg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA CRIOLLA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "vGlD+pFtyCxwMnlGKMtQRg==",
              "subType": "04"
            }
          },
          "order": 4,
          "plu_id": {
            "$binary": {
              "base64": "gwluFJpAMy14CXrE+IsMPQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "2ty7VswtHVTA2c+Hfg80rA==",
              "subType": "04"
            }
          },
          "order": 5,
          "plu_id": {
            "$binary": {
              "base64": "CIrFSvpM66IXHFAUZ8ABOA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA LECHUGA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "1kBtJDYbveH5rag7rYa6gg==",
              "subType": "04"
            }
          },
          "order": 6,
          "plu_id": {
            "$binary": {
              "base64": "CVbQNihXZm9X/r9ELefqcg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA DE COL GRANDE",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "u1JZwIY92S5fcTC4S02MQA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "CAMBIO COMBOS",
      "sug_question_tittle": "APP CAMBIO COMBOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "URxXo3WnK1OM2++QZx8qyg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "7ILGSepo69KJ2xz/1scg3A==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CAMBIO DE COLA X AGUA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "9M2qoYR+nBXzdw6BdpfYXQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA AGREGAR GASEOSA",
      "sug_question_tittle": "APP AGREGA BEBIDA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "eYlukg7erQ1sneVPx0yO8Q==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "g1DodAYADimyNPEYJVsfDQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 400 ML",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "CjlGhHE/GwTZCoz6LtSAZw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA AGREGAR GASEOSA",
      "sug_question_tittle": "AGR AGREGA BEBIDA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "5BUB3pbYoJtEjHtNahmtmA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "g1DodAYADimyNPEYJVsfDQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 400 ML",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "MuMD3cuxfPcAcTxAK/5TEA==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "3LjtpnM5A13b40PLdyICRg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "1/4 P FRITA COLA DIF",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "g3sYcrIfkkIR9gfS3wq96w==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS AGREGAR JUGOS",
      "sug_question_tittle": "AGR AGREGA JUGOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "vvM/qHldRr3NvQ3uub2afg==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "w+tBv9KVtWA/1LZSuUVTzw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "lXfwrB2ewUPWuK9NH7Poag==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS AGREGAR SOPAS",
      "sug_question_tittle": "AGR AGREGA SOPAS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "Y46yDiJwaFsOgw9H064Lyw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "e57Zes6gRrgsw8aMMq9ocg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CONSOME",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "2NXvUBVwg7ggkYtg+bsyGQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS AGREGAR POSTRE",
      "sug_question_tittle": "AGR AGREGA TU POSTRE",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "TXRtblh54uDyM+R7U1gLXA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEA AGREGAR JUGOS",
      "sug_question_tittle": "APP AGREGA JUGOS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "BC7tj/h/l+dDfJflbAVkhA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "/UYF2WZ7OEOxOTiml9stRQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "bNdarhEuE8xlyCYvbRNL3Q==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS AGREGAR SOPAS",
      "sug_question_tittle": "APP AGREGA SOPAS",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "4niDfogJEYgxm5/l00fNug==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "2NNJAp0iLDjbgVRkeviTqQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CONSOME",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "sIKPMpS/Dj5WLvK4S+I0AQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "DESEAS AGREGAR POSTRE",
      "sug_question_tittle": "APP AGREGA POSTRES",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "1khSqz+iQJFmgz+ycBC+hg==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Complementa tu orden con :",
      "sug_question_tittle": "APP COMPLEMENTOS INDIVIDUALES NUEVO",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "9EzTVtbObux5/sdkW9uDXw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "XuuPRT1VG6uV7SWeRFCZaA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA REGULAR",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "xOCFjYD6ug9lqwAlTlh/mw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Complementa tu orden  con",
      "sug_question_tittle": "AGR COMPLEMENTOS INDIVIDUALES NUEVO",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "DMstpoFJXBBE7OfOzvfZWQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "XuuPRT1VG6uV7SWeRFCZaA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA REGULAR",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "R/bFQjzDQyhHFLgaCuuaNQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Agrega una bebida:",
      "sug_question_tittle": "APP AGREGAR BEBIDA INDIVIDUAL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "Pfnqt3I3KfjHe6GurwxKpg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "WyTtCeYCdRqtH2Sz7LWFOQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 400 ML",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "l1/f3WaxvpsxN93mwPTPIQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Agrega una bebida",
      "sug_question_tittle": "AGR AGREGAR BEBIDA INDIVIDUAL",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "dqGWm1WeVx7pCG71BkXtJg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "g1DodAYADimyNPEYJVsfDQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 400 ML",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "XyVGEqetIciMS8PwgErYBw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Agrega una bebida:",
      "sug_question_tittle": "AGR BEBIDA FAMILIAR NUEVO",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "OCKxXeeqn9Ufehcx++Kayg==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "c54JsW1s2MSwlQRFxQBlDA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 1 LT",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "fi7ypo2lKdBtmqLAF5pf1A==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Complementa tu orden con:",
      "sug_question_tittle": "AGR COMPLEMENTOS FAMILIARES NUEVO",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "iOlAOlevFPBijrN8aaIAwQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "e57Zes6gRrgsw8aMMq9ocg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CONSOME",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "cNJPfat0Sa8TWzq2UCcQXg==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "CVbQNihXZm9X/r9ELefqcg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA DE COL GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "jf31OvXGFOTewk0VgiuymQ==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "u+IhbGP0ytQlzEMt2T6z2g==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "d8EFj2aE/dutHdavLrbozw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 7,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Complementa tu orden con:",
      "sug_question_tittle": "APP COMPLEMENTOS FAMILIARES NUEVO",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "nRYr2VaIqXbxGtt7xsqahQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "gwluFJpAMy14CXrE+IsMPQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PAPA FRITA GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "oFwrTMlD0V/h3r71KLchYQ==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "CVbQNihXZm9X/r9ELefqcg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "ENSALADA DE COL GRANDE",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "yL8b3eKY46/IhndXScBIYg==",
              "subType": "04"
            }
          },
          "order": 7,
          "plu_id": {
            "$binary": {
              "base64": "2NNJAp0iLDjbgVRkeviTqQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "CONSOME",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "h3GmY9Kz4JS0ENiU/u2+OQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Agrega una bebida :",
      "sug_question_tittle": "APP BEBIDA FAMILIAR",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "Jb+RgMvsfiGVKGnUWhR3Uw==",
              "subType": "04"
            }
          },
          "order": 2,
          "plu_id": {
            "$binary": {
              "base64": "hGJUxjnRrJTQ6RAWkMF4kw==",
              "subType": "04"
            }
          },
          "answer_pos_description": "GASEOSA 1 LT",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "xQmFhF/969a4dPiiuQVbRA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 2,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Elije el sabor de tu bebida:",
      "sug_question_tittle": "APP SABOR BEBIDA 2",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "VFjMIJLNydipsrZO9n7ppA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "WSsVKjXaXWLabFgDoiT9NA==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "pfEwj19EkveKpK9kvzinBw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 2,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Elije el sabor de tu bebida:",
      "sug_question_tittle": "AGR SABOR BEBIDA 2",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "G8wKwcjx2G1VM3QuN/dkzw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "MPZfiBUpLjejMA5mq399Ig==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "8E/XBxwujWq7NHAW5GvqmA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Elije el sabor de tu bebida:",
      "sug_question_tittle": "APP SABOR BEBIDA 1",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "JAP0dml1xEZQ48MCBCmSPA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "Vp5mKlbVDknu3AHHMy4OLA==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "D5l7b5FIGBUFu2fJJQNb3g==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Elije el sabor de tu bebida:",
      "sug_question_tittle": "AGR SABOR BEBIDA 1",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "gsSxPU9EiH1aA4J66aNZbw==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "/ah2XvZbK46XWx+29E4cVA==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "di/6wt7YFPbCQlw9qR6ZEQ==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 2,
      "sug_question_max_responses": 2,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "SABOR DE TU BEBIDA",
      "sug_question_tittle": "AGR SABOR DE TU BEBIDA 2",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "dIjYgVDXsCK+02uT4e1cOw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Agregar limonada por 50 ctvs",
      "sug_question_tittle": "Limonada Extra",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "OIPRm0K9orEzuAKTJ98L9g==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "0ftOs/jDIXSupICEewZIUg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "LIMONADA MINI GUS",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "NhkmrfnMhFTWgFCR7wJC7w==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 1,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "¿Que sabor de bebida es de su gusto?",
      "sug_question_tittle": "AGR Sabor de bebida",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "OAwIOhU9TZR/NuohZC/GQw==",
            "subType": "04"
          }
        },
        "type_name": "Obligatoria",
        "description": "Tipo obligatoria para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "XoWEmM6vfvT66n+BCdsScQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "q9HLyl5e8w+MmtxYaPXAzA==",
              "subType": "04"
            }
          },
          "answer_pos_description": "PEPSI",
          "next_questions": []
        },
        {
          "answer_id": {
            "$binary": {
              "base64": "krkdtrtYz7syX+/+cIMuQg==",
              "subType": "04"
            }
          },
          "order": 3,
          "plu_id": {
            "$binary": {
              "base64": "IGR3rxvG0yetodKypzcrFg==",
              "subType": "04"
            }
          },
          "answer_pos_description": "7 UP",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "WrK/mD5oB4ELiUJOzCkWPw==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 5,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Desea agregar salsas",
      "sug_question_tittle": "AGR EXTRA SALSA NUEVA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "WyYOOaF01v6i1nfG2L/9vQ==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "xNZ6wXefENVEF6/TFmWStQ==",
              "subType": "04"
            }
          },
          "answer_pos_description": "EXTRA SALSA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    },
    {
      "_id": {
        "$binary": {
          "base64": "xOlDNJGJQsiGtSe+8BdZmA==",
          "subType": "04"
        }
      },
      "sug_question_min_responses": 0,
      "sug_question_max_responses": 5,
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "sug_question_pos_description": "Desea agregar salsa",
      "sug_question_tittle": "APP EXTRA SALSA NUEVA",
      "status_suggested_question": {
        "_id": {
          "$binary": {
            "base64": "sxz6NqAYYDOnVjPqmerljQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para preguntas Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:43:05.435Z"
        }
      },
      "type_question": {
        "_id": {
          "$binary": {
            "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
            "subType": "04"
          }
        },
        "type_name": "Opcional",
        "description": "Tipo opcional para preguntas sugeridas",
        "created_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:45:49.109Z"
        }
      },
      "answers": [
        {
          "answer_id": {
            "$binary": {
              "base64": "aSRLHuD2nl4VGHG2g6mYBA==",
              "subType": "04"
            }
          },
          "order": 1,
          "plu_id": {
            "$binary": {
              "base64": "3KF3qX7MTw0Qktg1Ajp9ww==",
              "subType": "04"
            }
          },
          "answer_pos_description": "EXTRA SALSA",
          "next_questions": []
        }
      ],
      "created_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "created_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      }
    }
  ]
}
```

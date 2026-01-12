## ## Obtener Preguntas Sugeridas del Menú

### Método HTTP

`GET`

### URL

```
https://example.com
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
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
}
```

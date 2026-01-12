## Obtener Menú Anidado de Propagaciones

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
      "base64": "fsSx3wRKStOguSjHh8e2XA==",
      "subType": "04"
    }
  },
  "operation_id": {
    "$binary": {
      "base64": "xhLibwdkRWCcbdZS/CJU+w==",
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
      "base64": "LMaX5uHaS262o1JqteU45g==",
      "subType": "04"
    }
  },
  "received_at": {
    "$date": "2025-05-07T17:55:12.660Z"
  },
  "data_list": [
    {
      "_id": {
        "$binary": {
          "base64": "MclvIZLcw43D9P9HDfQuIw==",
          "subType": "04"
        }
      },
      "cdn_id": {
        "$binary": {
          "base64": "vC2K2uJeG7dV/jLRIFrErw==",
          "subType": "04"
        }
      },
      "menu_name": "GUS SALON",
      "status_menu": {
        "_id": {
          "$binary": {
            "base64": "cAulkyRR7k+0OGjIXtw5MQ==",
            "subType": "04"
          }
        },
        "status_name": "Publicado",
        "description": "Estado inactivo para menú Publicado",
        "color": "#1B3E19",
        "background_color": "#E2F7E2",
        "created_at": {
          "$date": "2025-02-26T15:44:39.823Z"
        },
        "updated_at": {
          "$date": "2025-02-26T15:44:39.823Z"
        }
      },
      "classifications": [
        {
          "_id": {
            "$binary": {
              "base64": "E1J1fXGTczTMnKiIs3fKEw==",
              "subType": "04"
            }
          },
          "classification_name": "Salon",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "description": "Clasificación para Salon",
          "color": "",
          "background_color": "",
          "created_at": {
            "$date": "2025-02-26T15:40:20.747Z"
          },
          "updated_at": {
            "$date": "2025-02-26T15:40:20.747Z"
          }
        }
      ],
      "limit_columns_category": 6,
      "limit_rows_category": 15,
      "limit_columns_plu": 6,
      "limit_rows_plu": 15,
      "icon": {
        "icon_id": {
          "$binary": {
            "base64": "NCymAvs+B0l1aJPelLNETQ==",
            "subType": "04"
          }
        },
        "icon_name": "fastfood",
        "icon_font": "fastfood",
        "description": "Estado para publicación",
        "created_at": {
          "$date": "2024-11-28T20:36:44.912Z"
        },
        "updated_at": {
          "$date": "2024-11-28T20:36:44.912Z"
        },
        "color_id": {
          "$binary": {
            "base64": "gIYRrAybD2g4MKe1M1xbgQ==",
            "subType": "04"
          }
        },
        "color_name": "Rojo",
        "color_hex": "#A20825",
        "background_color": "#A20825"
      },
      "description": "GUS SALON",
      "images_menu": [],
      "categories": [
        {
          "category_id": {
            "$binary": {
              "base64": "6hNIGt6yISAKTWo3Iq++1A==",
              "subType": "04"
            }
          },
          "category_menu_name": "ABUNDANCIA",
          "description": "Categoría de menú ABUNDANCIA",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 3,
          "pos_x": 1,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "dBjo7D2MwtByvblwXja/2A==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "tDUHiT82Hlvm1CnMHtv+YQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "U+39ByQ6n/rLUoaB4PZP/w==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "0y+5xiE230CQGQndSr7YPA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "v/HsJxInakjbWoqpFBrNtA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "1o3hiCQOqU9bITPu07sMxg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "helULOC18lIiQNNcZcm2rw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "RaaMGhzlNKTty5PBorcOxg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "TgL1NNFSRf19/fwHe8y0lg==",
              "subType": "04"
            }
          },
          "category_menu_name": "BEBIDAS",
          "description": "Categoría de menú BEBIDAS",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 2,
          "pos_x": 1,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "EgLHLZBMVBg8XZBCDyMxjQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "jkKBF9IgE2LK1KmmQ6X4fQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "WUn673B4kOs6semqxgFIWQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "B/BsYJmNJC6sq4yRwzm3BA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "aqsGEowNmg/wagKLquVbdw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "QwM3oSyBpgI96fp3AKzFYQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "/ZB3uETXv67/qYtz/8Bbbg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "oeIhGVVvQkjg2w4h9US3IA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "qNxBoe4HT1Rjct5G17Ygug==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "c5hCDzDY3/Ku5MpgXF3pZw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "6sH6Wr+3KKi0/kxfDRJFYw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "pG+1Ra/a78jTGP6HU2Ydwg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "xtPJhk1+Ou3rCDcLfjzH8A==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "hF9FK919pA0dAZycfgiXNg==",
              "subType": "04"
            }
          },
          "category_menu_name": "COMBOS",
          "description": "Categoría de menú COMBOS",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 3,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "ihToZ40ibu2i5HdF8NI6/A==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "VYeU4DM3SGK6bNDOVOC3/g==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "5ts8V63Dj4ykF/pT8U25iQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "Zf8jDSllHQth7mJNiQvEJw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "yTwdN6u7+2sFkbGVqcVcYw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "K3ChE/6a5JCekYUqVtF+zA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "KAKnXSFPfm/BL9VfUqmyXQ==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "wX3L1L+P/Jl37VZsbVNHkQ==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "pB5K8zsD1g8uXDUQ2mNocg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "NZt+2CJSRc8YFOjT5rKo5Q==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "kfx72z6Wat6iGRlkT0wJWw==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "e/6czZC4Bzr7jyaoOByJVA==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "I0FyBPbMvGBxIAuBl3lTow==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "9uwDfSRWmZ/tlrNUyL0Crw==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "sXXq7IP8NTKGQVj9l5D9YA==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "qzcN2ThbnXcLzzjNUCmOlg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "LnSx88VN8qZi7dqI50K+CQ==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 4
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "OwCXGgP0B2h2kNLPbHb8dw==",
              "subType": "04"
            }
          },
          "category_menu_name": "COMBOS PARA COMPARTIR",
          "description": "Categoría de menú COMBOS PARA COMPARTIR",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 2,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "CQL+2fiC+xkjrR/iH7FfWA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "rBRZwtqvRuMftB2rm9X8XQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "D2O3rWhRwv/zIPlGeZBoKA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "FgE4sFzBjhr06DvMrjl+Jw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "/ik547N0HQrZedBBG7BTtw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "jxzw9pTZ05fv0RMItZMvZQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "xACbcN049Lj4B1C9zg0EMw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "rER49M2buqhXRQcRCwZJ6g==",
              "subType": "04"
            }
          },
          "category_menu_name": "COMPLEMENTOS",
          "description": "Categoría de menú COMPLEMENTOS",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 4,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "uGKtE3iLyZ3Io9YXhsHmqw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "5p1bJWBhTohDwy5BE9hG1w==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "Nx8JROXrucvgNiO7eFhzTQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "VaY6nFXEZg0/MAzrFWPR0Q==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "ETZ/lk2DNlMX5dzKXaYvNg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "0IwIXoT6UkzQ2HY9jJy0CA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "FDQXcBGI0TMEXyzXM7Kf8w==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "DhTHuybUL9WiTlFciUJgmg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "6Y87C4YPgiecM3eCxynbgw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "yuSHpoTSmq0yF6ltiRBo0A==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "bfJZ35xyNPIrknvviFWdUw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "Nb+I91MVfvB5SetD5fGLDA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 5
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "LpS3SgueoeuVBQWpJO8xnw==",
              "subType": "04"
            }
          },
          "category_menu_name": "DESAYUNOS / ENSALADAS",
          "description": "Categoría de menú DESAYUNOS / ENSALADAS",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 2,
          "pos_x": 2,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "nh/0oHLK85cetiISYWNojQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "huc604OcXiC2cCuuF0NlSg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "PLK/pceEnHOa+FuG3XvyTg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "V0FaSav1AuAgRKQzTQrSwA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "3uBP7Pu9AO8lJpdconnNnQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "kQgyUOWQ35gg1kAKD6zDqg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "PK+LfnX6rORJxUqTV/EaOw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "ZNseQCwj9funAl/lSoESaQ==",
              "subType": "04"
            }
          },
          "category_menu_name": "FAMILIARES",
          "description": "Categoría de menú FAMILIARES",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 1,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "8g0lIgOu2i9DZpJEkrsubw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "8fgbxuaYqllWgtCswr0aKQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "IaD0rnmpCeC6fgRd99yhug==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "B0cKTbi8T1hyO64ckCwYyA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "SAuttWJspROKRYvYnn2a/g==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "GDe823OW2YQBstj/yJZyJA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "ighv81XMNvtEb9eSNP5P/g==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "qUek4Jw2DzgwYzlqKvK9Kg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "I4O5I4wZaPXBSSY2ygUKww==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "oVa0pAAespZheeW0zfjDEQ==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "gU+G9DqJl3k+wjevBnN5MA==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "d5UlCnr6ICoiul9GqIcxlw==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "RI7zPNYhZNkQhaoIhwJDYw==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "W0A4HZ5cCVbPpyOMmb02ng==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "EFcu5vQabLOJvDU6s7JBag==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "/E1HkNjWOR4+8C8PQejZYQ==",
                  "subType": "04"
                }
              },
              "pos_y": 5,
              "pos_x": 3
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "kJIwnTnd7E47DezfFnrX+Q==",
              "subType": "04"
            }
          },
          "category_menu_name": "POSTRES",
          "description": "Categoría de menú POSTRES",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 5,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "oK/o1964FjOIMddIbkVzDg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "ptUBCBCtF6wyNuQcC8DSYw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "AvyYYM1LCkcrihgdnk2nag==",
              "subType": "04"
            }
          },
          "category_menu_name": "PROMOCIONES",
          "description": "Categoría de menú PROMOCIONES",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 1,
          "pos_x": 1,
          "plus": []
        },
        {
          "category_id": {
            "$binary": {
              "base64": "n0neFg9xl0kuhSXUinBrGw==",
              "subType": "04"
            }
          },
          "category_menu_name": "SANDUCHE",
          "description": "Categoría de menú SANDUCHE",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 2,
          "pos_x": 5,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "aaXeXv5KEvY2XQEtmrsHGA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "irRMF6diXkOqIjpdH5Ebaw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "xtGsUdbZoeSVSyzBJmGipA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "TsTa9uSbUOWfhE6MSAQCfw==",
              "subType": "04"
            }
          },
          "category_menu_name": "SNACKABLES",
          "description": "Categoría de menú SNACKABLES",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 2,
          "pos_x": 3,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "cOGV2PzOWo537lWCpeCjLg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "3+yQawnwnpNMJQXq3XtuXg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "dMWyozvJH3CJHyqwjBU+hQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "/3PpbGeIHeUdFrFQSWfs/Q==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "UWeRHG1dGhmI1LBQaKraKg==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "8sM0r6WSNJJVHtudV3kQsQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "/HBN+AyPGeAVnRlkkKxXZw==",
              "subType": "04"
            }
          },
          "category_menu_name": "SOPAS",
          "description": "Categoría de menú SOPAS",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 3,
          "pos_x": 1,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "qwItR+hWJel5SjInDgUCJA==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            }
          ]
        },
        {
          "category_id": {
            "$binary": {
              "base64": "30SmsGnnSnDBU+Q4Dg2kow==",
              "subType": "04"
            }
          },
          "category_menu_name": "VALOR",
          "description": "Categoría de menú VALOR",
          "cdn_id": {
            "$binary": {
              "base64": "vC2K2uJeG7dV/jLRIFrErw==",
              "subType": "04"
            }
          },
          "created_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "updated_at": {
            "$date": "2025-05-06T17:36:13.228Z"
          },
          "is_visible": true,
          "images_category_menu": [
            {
              "_id": {
                "$binary": {
                  "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
                  "subType": "04"
                }
              },
              "extension": "",
              "name": "",
              "sas_url": "",
              "description": "",
              "size": null,
              "device_image": null,
              "path": "",
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
            }
          ],
          "icon_image": {
            "icon": {
              "_id": {
                "$binary": {
                  "base64": "NCymAvs+B0l1aJPelLNETQ==",
                  "subType": "04"
                }
              },
              "icon_name": "fastfood",
              "icon_font": "fastfood",
              "description": "Estado para publicación",
              "created_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:36:44.912Z"
              }
            },
            "color": {
              "_id": {
                "$binary": {
                  "base64": "Q9GAnPClnLU1cS5KYts9lg==",
                  "subType": "04"
                }
              },
              "color_name": "Rojo Ruby ",
              "color_hex": "#A20825",
              "background_color": "#A20825",
              "description": "Rojo Ruby ",
              "created_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              },
              "updated_at": {
                "$date": "2024-11-28T20:13:43.304Z"
              }
            }
          },
          "pos_y": 2,
          "pos_x": 4,
          "plus": [
            {
              "plu_id": {
                "$binary": {
                  "base64": "i5aegi39O8XthVfAaYfaUQ==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "x+78ef29ieAWr+XaFPVH/w==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "ebh0znhO8vjkvv6vU8I+3g==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "7CerQnxqsCNe891pFgvy1w==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "5Qbm1GPnd+0JacULBzAG5A==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "vBrgwnaQsEuL514YhNFhTw==",
                  "subType": "04"
                }
              },
              "pos_y": 1,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "p4fTlAUoUYFAqisrpm7iXw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "KOCVL4yo6nYz8xK9j8dk0g==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "NUvFB0WFnAHDcJRQab6jwg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 2
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "IGIhweLthVGMDrX8ydRc1A==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 3
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "CeOIBZSpoj55mKS8sfypPw==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 4
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "Mi8mUQggnFDnrfDFOa6eMg==",
                  "subType": "04"
                }
              },
              "pos_y": 2,
              "pos_x": 5
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "yx/eDwjJzaS40aBfjq5ZfA==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 1
            },
            {
              "plu_id": {
                "$binary": {
                  "base64": "KrOZmGDAuJFaPcAse4f/Cw==",
                  "subType": "04"
                }
              },
              "pos_y": 3,
              "pos_x": 2
            }
          ]
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
      "updated_user": {
        "$binary": {
          "base64": "m/Q58L3nNgzsuvw1Jr+nsA==",
          "subType": "04"
        }
      },
      "updated_at": {
        "$date": {
          "$numberLong": "-62135596800000"
        }
      },
      "half_integration": {
        "_id": {
          "$binary": {
            "base64": "n8gXf8TD+d8M+SKMrFxPfQ==",
            "subType": "04"
          }
        },
        "cdn_id": {
          "$binary": {
            "base64": "vC2K2uJeG7dV/jLRIFrErw==",
            "subType": "04"
          }
        },
        "half_integration_name": "Local",
        "description": "Medio de venta Local",
        "created_at": {
          "$date": "2025-04-23T21:40:48.090Z"
        },
        "updated_at": {
          "$date": "2025-04-23T21:40:48.090Z"
        }
      }
    }
  ]
}
```

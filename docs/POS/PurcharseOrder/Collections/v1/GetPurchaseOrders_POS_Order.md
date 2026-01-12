## Obtener Órdenes de Compra POS

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
      "base64": "EzOHWUe+Qi6QJrPGY8D++w==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "channel": {
    "_id": {
      "$binary": {
        "base64": "CppmFyMZTZK2qQAAxvPSSA==",
        "subType": "04"
      }
    },
    "name": "Local",
    "status_channel": ""
  },
  "document_type": {
    "_id": {
      "$binary": {
        "base64": "m0Z8UPYB7EGWgJutjhKBzQ==",
        "subType": "04"
      }
    },
    "name": "Factura"
  },
  "invoice": {
    "companyTaxData": {
      "name": "INT FOOD SERVICES CORP SA",
      "identificationNumber": "1791415132001",
      "specialTaxpayer": "GRAN CONTRIBUYENTE",
      "isSpecialTaxpayer": "Sí",
      "specialTaxpayerCode": "NAC-GCFOIOC21-00000900-E",
      "typeTax": "Especial",
      "obligatoryToKeepAccounts": "SI",
      "resolutionCode": "RESOL. N: 155",
      "companyAddress": "PICHINCHA / QUITO / INAQUITO / COREA 126 Y AV.\nAMAZONAS",
      "restaurantAddress": "PICHINCHA / QUITO / JIPIJAPA / AV. 6 DE \nDICIEMBRE N37-157 Y EL COMERCIO",
      "issueType": "Emision Normal"
    },
    "dataInvoice": {
      "sequential": "097-100-000000197",
      "accessKey": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "transaction": "G008F000002756",
      "legend": "\nEstimado cliente: Por favor verifique los datos de su\nfactura, unicamente se aceptaran cambios el mismo dia\nde emision.",
      "linkLabel": "Para obtener su factura electronica ingrese a:",
      "urlDocument": "https://facturacion.kfc.ec",
      "accessKeyLabel": "(Usuario: CI/RUC, Clave: CI/RUC) o a la pagina web del \nSRI con la Clave de Acceso:",
      "environment": "Pruebas",
      "createdAt": "2025-11-18T14:43:39.196Z",
      "document": {
        "client": {
          "client_id": "e7a1c2b0-4d5f-4e8b-9c3a-2f6d7e8f9b0a",
          "name": "CONSUMIDOR FINAL",
          "last_name": "",
          "phone": "2222222",
          "email": "consumidor.final@kfc.com.ec",
          "gov_id_type": "CONSUMIDOR FINAL",
          "gov_id_number": "9999999999999"
        },
        "orderInvoice": {
          "order_id": "13338759-47be-422e-9026-b3c663c0fefb",
          "invoice_id": null,
          "invoice_key_aut": null,
          "products": [
            {
              "plu_id": 47360,
              "plu_name": "COMBO CHAULAFAN",
              "plu_quantity": 1,
              "plu_description": null,
              "price": {
                "total_per_plu": {
                  "currency_code": "USD",
                  "subtotal_without_taxes": {
                    "$numberDecimal": "5.434783"
                  },
                  "discount_percentage": 0,
                  "discounts_value": 0,
                  "subtotal_include_discounts": {
                    "$numberDecimal": "5.434783"
                  },
                  "tax_value": {
                    "$numberDecimal": "0.815217"
                  },
                  "total": {
                    "$numberDecimal": "6.25"
                  },
                  "taxes": [
                    {
                      "tax_name": "IVA 15%",
                      "tax_code": "d00c4be9-a547-f72d-b87b-2abaebc07f4b",
                      "tax_percentage": 15,
                      "total_tax_value": {
                        "$numberDecimal": "0.815217"
                      },
                      "base_amount": {
                        "$numberDecimal": "5.434783"
                      }
                    }
                  ]
                },
                "total_price": {
                  "currency_code": "USD",
                  "subtotal_without_taxes": {
                    "$numberDecimal": "5.434783"
                  },
                  "discount_percentage": 0,
                  "discounts_value": 0,
                  "subtotal_include_discounts": {
                    "$numberDecimal": "5.434783"
                  },
                  "tax_value": {
                    "$numberDecimal": "0.815217"
                  },
                  "total": {
                    "$numberDecimal": "6.25"
                  },
                  "taxes": [
                    {
                      "tax_name": "IVA 15%",
                      "tax_code": "d00c4be9-a547-f72d-b87b-2abaebc07f4b",
                      "tax_percentage": 15,
                      "total_tax_value": {
                        "$numberDecimal": "0.81521745"
                      },
                      "base_amount": {
                        "$numberDecimal": "5.434783"
                      }
                    }
                  ]
                }
              }
            }
          ]
        },
        "payment_methods": [
          {
            "payment_methods_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
            "processor": "",
            "currency_code": "USD",
            "payment_method_code": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
            "transaction_type": "Efectivo",
            "transaction_id": "",
            "transaction_status": "APPROVED",
            "reference_number": "",
            "exact_payment": true,
            "customer_cash_amount": "0.00",
            "total_bill": 6.25,
            "additional_info_payment_methods": {
              "external_reference": "",
              "method_name": "",
              "data_transaction": {
                "tipoMensaje": null,
                "tipoRespuesta": null,
                "codigoAdquiriente": null,
                "codigorespuestaAutorizador": null,
                "mensajeRespuesta": null,
                "secuenciaTransaccion": null,
                "numeroLote": null,
                "horaTransaccion": null,
                "fechaTransaccion": null,
                "numeroAutorizacion": null,
                "terminalID": null,
                "merchantID": null,
                "valorInteres": null,
                "mensajeriaImpresion": null,
                "codigoBancoAdquiriente": null,
                "codigobancoemisor": null,
                "nombreGrupoTarjeta": null,
                "modoLectura": null,
                "nombreTarjetaHabiente": null,
                "montoFijo": null,
                "idemv": null,
                "aidemv": null,
                "tipoemv": null,
                "verificaPin": null,
                "arqc": null,
                "tvr": null,
                "tsi": null,
                "numTarjTrunca": null,
                "fechVencTrj": null,
                "numTarjEncri": null,
                "filler": null
              }
            },
            "acquirer": {
              "code": "",
              "name": ""
            },
            "transaction_date": {
              "date": "2025-11-18T19:42:43.631Z",
              "time_zone_type": 3,
              "time_zone_name": "America/Guayaquil"
            }
          }
        ],
        "additional_data": []
      }
    },
    "dataCredit": {
      "sequential": "",
      "accessKey": "",
      "transaction": "",
      "legend": "",
      "linkLabel": "",
      "urlDocument": "",
      "accessKeyLabel": "",
      "environment": null,
      "createdAt": "Tue Nov 18 2025",
      "document": {
        "client": {
          "client_id": "",
          "name": "",
          "last_name": "",
          "phone": "",
          "email": "",
          "gov_id_type": "",
          "gov_id_number": ""
        },
        "orderInvoice": {
          "order_id": "",
          "invoice_id": "",
          "invoice_key_aut": "",
          "products": []
        },
        "payment_methods": [],
        "additional_data": []
      },
      "motivo": ""
    },
    "document_code": "01",
    "fe_authorization_status": {
      "codigo": "0",
      "mensaje": "COMPROBANTE AUTORIZADO",
      "estado": "A",
      "creation_date": "2025-11-18T14:46:19"
    }
  },
  "credit_note": null,
  "driveThru": null,
  "pickup": null,
  "orderParent": [],
  "last_eventUuid": null,
  "last_correlationId": null,
  "last_causationId": null,
  "cdn_name": "KFC",
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefr4dj+qx14W+v+W0Q==",
      "subType": "04"
    }
  },
  "restaurant_name": "G008",
  "cash_register_subscription": {
    "$binary": {
      "base64": "QSohKC2op0KC1eXANrGNFw==",
      "subType": "04"
    }
  },
  "cash_register_subscription_name": "412a2128-2da8-a742-82d5-e5c036b18d17",
  "seller": {
    "user_seller_id": {
      "$binary": {
        "base64": "wXtujYilnrUfRK7sFhSU2g==",
        "subType": "04"
      }
    },
    "user_seller_name": "CINTHYA BARRE VARGAS",
    "user_seller_rol": "Cajero",
    "user_seller_profile": "Cajero"
  },
  "status_order_id": {
    "$binary": {
      "base64": "6qWaJZCWBECjXFMZpa0IZA==",
      "subType": "04"
    }
  },
  "period_id": {
    "$binary": {
      "base64": "WxorBAwWTKu2Tu49CYAjJg==",
      "subType": "04"
    }
  },
  "status_order_description": "Entregada",
  "user_session": null,
  "conciliation_id": null,
  "order_id_call": "",
  "ui_reference_uuid": "001-C-20251118144243-O-34-A",
  "ui_started_at": {
    "$date": "2025-11-18T19:43:39.504Z"
  },
  "ui_finished_at": {
    "$date": "2025-11-18T19:42:43.631Z"
  },
  "totals": {
    "result_presentation": {
      "taxes": [
        {
          "_id": {
            "$binary": {
              "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
              "subType": "04"
            }
          },
          "tax_name": "IVA 15%",
          "value": {
            "$numberDecimal": "0.82"
          }
        }
      ],
      "subtotal_taxes": [
        {
          "tax": {
            "$numberDecimal": "15"
          },
          "value": {
            "$numberDecimal": "5.43"
          }
        }
      ],
      "subtotal_without_taxes": {
        "$numberDecimal": "5.43"
      },
      "total_discount": {
        "$numberDecimal": "0"
      },
      "tip": {
        "$numberDecimal": "0"
      },
      "total": {
        "$numberDecimal": "6.25"
      }
    },
    "result": {
      "taxes": [
        {
          "_id": {
            "$binary": {
              "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
              "subType": "04"
            }
          },
          "tax_name": "IVA 15%",
          "value": {
            "$numberDecimal": "0.815217"
          }
        }
      ],
      "subtotal_taxes": [
        {
          "tax": {
            "$numberDecimal": "15"
          },
          "value": {
            "$numberDecimal": "5.434783"
          }
        }
      ],
      "subtotal_without_taxes": {
        "$numberDecimal": "5.434783"
      },
      "total_discount": {
        "$numberDecimal": "0"
      },
      "tip": {
        "$numberDecimal": "0"
      },
      "total": {
        "$numberDecimal": "6.25"
      }
    },
    "result_per_plu": []
  },
  "items": [
    {
      "menu_id": {
        "$binary": {
          "base64": "xi8QxgQzSxpk/OJVaGDNew==",
          "subType": "04"
        }
      },
      "menu_description": "GUS LLEVAR",
      "category_id_plu": {
        "$binary": {
          "base64": "hF9FK919pA0dAZycfgiXNg==",
          "subType": "04"
        }
      },
      "category_description_plu": "",
      "classification_id": {
        "$binary": {
          "base64": "ZM0FBCWQQTKv7R28Iw4Kqw==",
          "subType": "04"
        }
      },
      "classification_description": "Llevar",
      "plu_parent_id": "",
      "plu_id": {
        "$binary": {
          "base64": "ZE4krWW+2ddPkUEkSxpq0w==",
          "subType": "04"
        }
      },
      "plu_name": "COMBO CHAULAFAN",
      "plu_description": "1/4 de pollo asado + 1  porción de chaulafan + 1 papa frita peq + 1 porción de ensalada de col + 1 gaseosa individual\n",
      "plu_pvp": {
        "$numberDecimal": "6.25"
      },
      "plu_quantity": 1,
      "is_plu_customization_group": false,
      "plu_customization": [
        {
          "comments": "",
          "suggest_questions": [
            {
              "suggested_question_id": {
                "$binary": {
                  "base64": "miOp102obZ5t0zOs/eq+QQ==",
                  "subType": "04"
                }
              },
              "sug_question_min_responses": 1,
              "sug_question_max_responses": 1,
              "sug_question_tittle": "PCK SABOR DE BEBIDA",
              "sug_question_pos_description": "SABOR DE TU BEBIDA?",
              "type_question_id": {
                "$binary": {
                  "base64": "OAwIOhU9TZR/NuohZC/GQw==",
                  "subType": "04"
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
                  "answer_pos_description": "PEPSI",
                  "order": 1,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "Pf3YFmEepXmyaS0Dm11KcA==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 39667,
                    "plu_name": "PEPSI",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0"
                    },
                    "plu_quantity": 1,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "VQZ0z4dfyOAXshTY0WjXOw==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "7 UP",
                  "order": 2,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "AfFyzl9+iVxwb8OSZnkDUQ==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 39669,
                    "plu_name": "7 UP",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "eQKk7mEemj3tMWS/f6Z5mA==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "FRESA",
                  "order": 3,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "HMvzDNVZLbtr9/gkDi7aqg==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 39672,
                    "plu_name": "FRESA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "aO94nOgmRNYHGDLnIkFtzg==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "MANZANA",
                  "order": 4,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "C73vFU/43my0CRoGrqH48A==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 39673,
                    "plu_name": "MANZANA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                }
              ]
            },
            {
              "suggested_question_id": {
                "$binary": {
                  "base64": "/WYDGBwGfcLSacSmiF4zaQ==",
                  "subType": "04"
                }
              },
              "sug_question_min_responses": 0,
              "sug_question_max_responses": 10,
              "sug_question_tittle": "PCK AGREGA COMBOS",
              "sug_question_pos_description": "DESEAS COMPLEMENTAR TU PEDIDO?",
              "type_question_id": {
                "$binary": {
                  "base64": "KJ0YfF20dTAzIN2ZEne9wg==",
                  "subType": "04"
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
                  "answer_pos_description": "AGREGA PAPA FRITA",
                  "order": 1,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "thTJoz0AiBGCFPllK421rQ==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 19205,
                    "plu_name": "AGREGA PAPA FRITA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0.65"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "+MR0eyO9GYj3g1w+6k0vYQ==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "PAPA FRITA GRANDE",
                  "order": 2,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "HiGAEu3ED6M1bBGQuQdMNg==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 4725,
                    "plu_name": "PAPA FRITA GRANDE",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "2.5"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "3Uc698RNWgXyHYa3w9c5/Q==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "JUGO DE MORA",
                  "order": 3,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "aT7NY2pp8sJC+WyvuSpHXw==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 12259,
                    "plu_name": "JUGO DE MORA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "1.99"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "SCaXTekSCmMn9un9GlUVcg==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "JUGO DE GUANABANA",
                  "order": 4,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "4aNQn/4R3UolBn32q/uSCA==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 15079,
                    "plu_name": "JUGO DE GUANABANA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "1.99"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "IeYxBgfEwTkb9nslc2vJGg==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "JUGO D NARANJILLA GUS",
                  "order": 5,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "dD2/aPE3/avc4AGUuVW0cg==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 27699,
                    "plu_name": "JUGO D NARANJILLA GUS",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "1.99"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "+JSgOfvyL9xx9UMYEOa7SQ==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "LIMONADA",
                  "order": 6,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "xlGzjq9Gx1c74cJdPsilFQ==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 17931,
                    "plu_name": "LIMONADA",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "2.25"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "v6BsFn/j+oCXe+gHZs00+w==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "FRUTILLA JR",
                  "order": 7,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "LzZWdHpwBqwdS9CHBFBtRQ==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 4992,
                    "plu_name": "FRUTILLA JR",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "0.99"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                },
                {
                  "answer_id": {
                    "$binary": {
                      "base64": "7sSIdtQ3AJg1gS+YA2gyCw==",
                      "subType": "04"
                    }
                  },
                  "answer_pos_description": "LOCRO PEQUENO",
                  "order": 11,
                  "plu": {
                    "_id": {
                      "$binary": {
                        "base64": "kLPaADz8ofim3vdqW7VsBw==",
                        "subType": "04"
                      }
                    },
                    "cdn_plu_id": 4702,
                    "plu_name": "LOCRO PEQUENO",
                    "plu_description": "",
                    "plu_pvp": {
                      "$numberDecimal": "1.99"
                    },
                    "plu_quantity": 0,
                    "tax": {
                      "_id": {
                        "$binary": {
                          "base64": "0AxL6aVH9y24eyq668B/Sw==",
                          "subType": "04"
                        }
                      },
                      "tax_name": "IVA 15%",
                      "value": {
                        "$numberDecimal": "15"
                      }
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "menu_id": {
        "$binary": {
          "base64": "xi8QxgQzSxpk/OJVaGDNew==",
          "subType": "04"
        }
      },
      "menu_description": "GUS LLEVAR",
      "category_id_plu": {
        "$binary": {
          "base64": "hF9FK919pA0dAZycfgiXNg==",
          "subType": "04"
        }
      },
      "category_description_plu": "",
      "classification_id": {
        "$binary": {
          "base64": "ZM0FBCWQQTKv7R28Iw4Kqw==",
          "subType": "04"
        }
      },
      "classification_description": "Llevar",
      "plu_parent_id": "5b6e3ace-9f3f-4c05-81bb-3adc1872777b",
      "plu_id": {
        "$binary": {
          "base64": "Pf3YFmEepXmyaS0Dm11KcA==",
          "subType": "04"
        }
      },
      "plu_name": "PEPSI",
      "plu_description": "",
      "plu_pvp": {
        "$numberDecimal": "0"
      },
      "plu_quantity": 1,
      "is_plu_customization_group": false,
      "plu_customization": []
    }
  ],
  "customer": {
    "_id": "e7a1c2b0-4d5f-4e8b-9c3a-2f6d7e8f9b0a",
    "id_user_external": "672a0a8d2d72b38d441e167f",
    "name": "CONSUMIDOR FINAL",
    "document_type": "Cedula",
    "document_number": "9999999999999",
    "email": "consumidor.final@kfc.com.ec",
    "contact_number": "2222222",
    "share_personal_data": false,
    "is_end_customer": true
  },
  "authorizations": [],
  "payments": [
    {
      "_id": {
        "$binary": {
          "base64": "RhHztVcjTIW2aCLYnHe9uw==",
          "subType": "04"
        }
      },
      "payment_method_id": {
        "$binary": {
          "base64": "O+ASauc5O0Bv6/Sqktc6fA==",
          "subType": "04"
        }
      },
      "payment_method_name": "Efectivo",
      "amount": {
        "$numberDecimal": "6.25"
      },
      "event_id": null,
      "event_code": null,
      "meta_data": {
        "external_reference": "",
        "method_name": "",
        "data_transaction": {
          "TipoMensaje": 0,
          "TipoRespuesta": 0,
          "CodigoAdquiriente": 0,
          "CodigoRespuestaAutorizador": "",
          "MensajeRespuesta": "",
          "SecuenciaTransaccion": "",
          "NumeroLote": "",
          "HoraTransaccion": "",
          "FechaTransaccion": "",
          "NumeroAutorizacion": "",
          "TerminalId": "",
          "MerchantId": "",
          "ValorInteres": "",
          "MensajeriaImpresion": "",
          "CodigoBancoAdquiriente": "",
          "CodigoBancoEmisor": "",
          "NombreGrupoTarjeta": "",
          "ModoLectura": 0,
          "NombreTarjetaHabiente": "",
          "MontoFijo": "",
          "IdEmv": "",
          "AidEmv": "",
          "TipoEmv": "",
          "VerificaPin": "",
          "Arqc": "",
          "Tvr": "",
          "Tsi": "",
          "NumTarjTrunca": "",
          "FechVencTrj": "",
          "NumTarjEncri": "",
          "Filler": ""
        }
      },
      "cash_register": null,
      "cash_register_name": "",
      "user_seller_id": {
        "$binary": {
          "base64": "AAAAAAAAAAAAAAAAAAAAAA==",
          "subType": "04"
        }
      },
      "user_seller_name": "",
      "created_at": {
        "$date": "2025-11-18T19:45:02.198Z"
      }
    }
  ],
  "deleted_order": null,
  "status_order_sync_id": "P",
  "status_order_sync": "Pendiente",
  "company_tax_data": null,
  "data_invoice": null,
  "order_comment": "",
  "created_user": {
    "$binary": {
      "base64": "wXtujYilnrUfRK7sFhSU2g==",
      "subType": "04"
    }
  },
  "updated_user": {
    "$binary": {
      "base64": "wXtujYilnrUfRK7sFhSU2g==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2025-11-18T19:45:02.379Z"
  },
  "updated_at": {
    "$date": "2025-11-18T19:45:02.379Z"
  }
}
```

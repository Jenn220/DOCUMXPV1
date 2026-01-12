## Obtener Programación de Precio de PLU

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
      "base64": "iVpjhUA7R4GBctnZgzMDzQ==",
      "subType": "04"
    }
  },
  "id_categories_selected": [
    {
      "$binary": {
        "base64": "+eREhtrn49Y+6U6N5vsEBQ==",
        "subType": "04"
      }
    },
    {
      "$binary": {
        "base64": "fPIsNZKaK7+Gic4DktetUA==",
        "subType": "04"
      }
    }
  ],
  "is_excel": true,
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "8sE6Ajy1R4GeENPxUZxR4g==",
      "subType": "04"
    }
  },
  "application_date": {
    "$date": "2024-07-03T23:57:12.839Z"
  },
  "status_progammation_prices_plu": {
    "$binary": {
      "base64": "gOa6T2mcTYqeNgAAiYqT5w==",
      "subType": "04"
    }
  },
  "plus": [
    {
      "plu_id": {
        "$binary": {
          "base64": "u8n6emhZSfOx0qOBIMvQIg==",
          "subType": "04"
        }
      },
      "is_changed": false,
      "categories": [
        {
          "category_id": {
            "$binary": {
              "base64": "+eREhtrn49Y+6U6N5vsEBQ==",
              "subType": "04"
            }
          },
          "classifications": [
            {
              "classification_id": {
                "$binary": {
                  "base64": "UlWMsy/bzWeOhr8q6covxg==",
                  "subType": "04"
                }
              },
              "price": {
                "net_value": {
                  "$numberDecimal": "0"
                },
                "retail_price": {
                  "$numberDecimal": "0"
                },
                "is_changed": false
              },
              "is_active": false
            }
          ]
        }
      ]
    }
  ],
  "updated_user": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "created_at": {
    "$date": "2024-07-03T23:57:12.839Z"
  },
  "updated_at": {
    "$date": "2024-07-08T12:16:28.532Z"
  }
}
```

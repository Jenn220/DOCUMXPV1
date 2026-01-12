## Ejecutar Flujo de Integración - Propagación de PLU de Menú (Facade)

### Método HTTP

`POST`

### URL

```
{{server_init}}/api/v1/facade
```

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "F101",
  "withResponse": false,
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "country": "{{country}}",
  "franchise_id": {{legacy_cdn_id}},
  "chunkLoad": 100,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E001",
        "withResponse": true,
        "withCache": false,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "{{server_legacy}}",
            "port": "",
            "user": "{{user_legacy}}",
            "password": "{{pass_legacy}}",
            "repository": "{{repository_legacy}}",
            "adapter": "SqlServerSP"
          },
          "entities": [
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_images"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_categories"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_questions"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_answers"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_taxes"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_classifications"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_departments"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Plus",
              "properties": [],
              "filters": [
                {
                  "name": "country",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "menu_name",
                  "operator": "equals",
                  "value": "{{menu_name}}"
                },
                {
                  "name": "plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "plus_for_franchise_tags"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E002",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": true,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "{{repository_mongo_hml}}",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "id_v2",
                  "operator": "equals",
                  "value": "9bf439f0-bde7-360c-ecba-fc3526bfa7b0"
                }
              ]
            },
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "in",
                  "value": [
                    "Cadena",
                    "Plus",
                    "PlusImages",
                    "Categoria",
                    "transformation_classifications",
                    "mxp_v2.Coleccion_Departamento_Plu",
                    "PlusTags",
                    "Pregunta_Sugerida",
                    "mxp_v2.View_Answer_For_Franchise"
                  ]
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": {{legacy_cdn_id}}
                }
              ]
            },
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "transformation_collection_plu"
                },
                {
                  "name": "id_v1",
                  "operator": "in",
                  "value": [
                    "PRODUCTO",
                    "MODIFICADOR",
                    "COMPLEMENTO"
                  ]
                }
              ]
            },
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "Impuestos"
                }
              ]
            },
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "mxp_v2.View_Status_PLU"
                }
              ]
            },
            {
              "name": "uuids",
              "properties": [
                {
                  "name": "id_v2",
                  "type": "base64"
                },
                {
                  "name": "country_code",
                  "type": "base64"
                },
                {
                  "name": "entity_name",
                  "type": "base64"
                },
                {
                  "name": "id_v1",
                  "type": "base64"
                },
                {
                  "name": "franchise_id",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "country_code",
                  "operator": "equals",
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "mxp_v2.View_Device_Images_PLU"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T001",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": true,
        "country": "{{country}}"
      }
    ],
    "LOADS": [
      {
        "code": "L001",
        "withCache": false,
        "withResponse": true,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "{{server_propagation}}",
            "port": "",
            "user": "",
            "password": "",
            "repository": "/YOUR_REDIS_OR_AZURE_KEY_HERE?user=9bf439f0-bde7-360c-ecba-fc3526bfa7b0&country_id=d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
            "adapter": "Rest"
          },
          "entities": [
            {
              "name": "plus",
              "toName": "plus",
              "properties": [
                {
                  "fromName": "_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "cdn_plu_id",
                  "fromType": "",
                  "toName": "cdn_plu_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "plu_name",
                  "fromType": "",
                  "toName": "plu_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "plu_description",
                  "fromType": "",
                  "toName": "plu_description",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "cdn_id",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "status_plu",
                  "fromType": "",
                  "toName": "status_plu",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "type_plu",
                  "fromType": "",
                  "toName": "type_plu",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "images_plu",
                  "fromType": "",
                  "toName": "images_plu",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "user_id",
                      "fromType": "",
                      "toName": "user_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "extension",
                      "fromType": "",
                      "toName": "extension",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "name",
                      "fromType": "",
                      "toName": "name",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "sas_url",
                      "fromType": "",
                      "toName": "sas_url",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "description",
                      "fromType": "",
                      "toName": "description",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "size",
                      "fromType": "",
                      "toName": "size",
                      "toType": "array",
                      "defaultValue": [
                        {
                          "fromName": "width",
                          "fromType": "",
                          "toName": "width",
                          "toType": "",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "height",
                          "fromType": "",
                          "toName": "height",
                          "toType": "",
                          "defaultValue": ""
                        }
                      ]
                    },
                    {
                      "fromName": "device_image",
                      "fromType": "",
                      "toName": "device_image",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "path",
                      "fromType": "",
                      "toName": "path",
                      "toType": "",
                      "defaultValue": ""
                    }
                  ]
                },
                {
                  "fromName": "categories",
                  "fromType": "",
                  "toName": "categories",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "category_id",
                      "fromType": "",
                      "toName": "category_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "classifications",
                      "fromType": "",
                      "toName": "classifications",
                      "toType": "array",
                      "defaultValue": [
                        {
                          "fromName": "classification_id",
                          "fromType": "",
                          "toName": "classification_id",
                          "toType": "uuid",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "price",
                          "fromType": "",
                          "toName": "price",
                          "toType": "array",
                          "defaultValue": [
                            {
                              "fromName": "user_id",
                              "fromType": "",
                              "toName": "user_id",
                              "toType": "uuid",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "net_value",
                              "fromType": "",
                              "toName": "net_value",
                              "toType": "",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "tax_value",
                              "fromType": "",
                              "toName": "tax_value",
                              "toType": "",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "retail_price",
                              "fromType": "",
                              "toName": "retail_price",
                              "toType": "",
                              "defaultValue": ""
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                {
                  "fromName": "suggested_questions",
                  "fromType": "",
                  "toName": "suggested_questions",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "suggested_question_id",
                      "fromType": "",
                      "toName": "suggested_question_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "order",
                      "fromType": "",
                      "toName": "order",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "answers",
                      "fromType": "",
                      "toName": "answers",
                      "toType": "array",
                      "defaultValue": [
                        {
                          "fromName": "answer_id",
                          "fromType": "",
                          "toName": "answer_id",
                          "toType": "uuid",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "order",
                          "fromType": "",
                          "toName": "order",
                          "toType": "",
                          "defaultValue": ""
                        }
                      ]
                    }
                  ]
                },
                {
                  "fromName": "taxes",
                  "fromType": "",
                  "toName": "taxes",
                  "toType": "array",
                  "defaultValue": "",
                  "hasUuids": "true"
                },
                {
                  "fromName": "tags",
                  "fromType": "",
                  "toName": "tags",
                  "toType": "array",
                  "defaultValue": ""
                },
                {
                  "fromName": "classifications",
                  "fromType": "",
                  "toName": "classifications",
                  "toType": "array",
                  "defaultValue": "",
                  "hasUuids": "true"
                },
                {
                  "fromName": "departments",
                  "fromType": "",
                  "toName": "departments",
                  "toType": "array",
                  "defaultValue": "",
                  "hasUuids": "true"
                }
              ]
            }
          ]
        },
        "dataInput": {}
      }
    ],
    "PUBLISHERS": []
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                           | Tipo    | Descripción                                          |
| ----------------------------------------------- | ------- | ---------------------------------------------------- |
| `code`                                          | string  | Código del flujo de integración                      |
| `withResponse`                                  | boolean | Indica si retorna respuesta                          |
| `syncId`                                        | string  | ID de sincronización                                 |
| `country`                                       | string  | Código del país                                      |
| `franchise_id`                                  | number  | ID de la franquicia en legacy                        |
| `chunkLoad`                                     | number  | Tamaño de lote para carga de datos                   |
| `processes`                                     | object  | Objeto con los procesos a ejecutar                   |
| `processes.EXTRACTS`                            | array   | Lista de procesos de extracción                      |
| `processes.EXTRACTS[].code`                     | string  | Código del proceso de extracción                     |
| `processes.EXTRACTS[].withResponse`             | boolean | Indica si retorna respuesta                          |
| `processes.EXTRACTS[].withCache`                | boolean | Indica si utiliza caché                              |
| `processes.EXTRACTS[].syncId`                   | string  | ID de sincronización                                 |
| `processes.EXTRACTS[].configuration`            | object  | Configuración del proceso                            |
| `processes.EXTRACTS[].configuration.connection` | object  | Configuración de conexión                            |
| `processes.EXTRACTS[].configuration.entities`   | array   | Lista de entidades a extraer                         |
| `processes.TRANSFORMS`                          | array   | Lista de procesos de transformación                  |
| `processes.TRANSFORMS[].code`                   | string  | Código del proceso de transformación                 |
| `processes.TRANSFORMS[].syncId`                 | string  | ID de sincronización                                 |
| `processes.TRANSFORMS[].withResponse`           | boolean | Indica si retorna respuesta                          |
| `processes.TRANSFORMS[].withCache`              | boolean | Indica si utiliza caché                              |
| `processes.TRANSFORMS[].country`                | string  | Código del país                                      |
| `processes.LOADS`                               | array   | Lista de procesos de carga                           |
| `processes.LOADS[].code`                        | string  | Código del proceso de carga                          |
| `processes.LOADS[].withCache`                   | boolean | Indica si utiliza caché                              |
| `processes.LOADS[].withResponse`                | boolean | Indica si retorna respuesta                          |
| `processes.LOADS[].syncId`                      | string  | ID de sincronización                                 |
| `processes.LOADS[].configuration`               | object  | Configuración del proceso de carga                   |
| `processes.LOADS[].configuration.connection`    | object  | Configuración de conexión al servicio de propagación |
| `processes.LOADS[].configuration.entities`      | array   | Lista de entidades de destino para la carga          |
| `processes.LOADS[].dataInput`                   | object  | Datos de entrada adicionales                         |
| `processes.PUBLISHERS`                          | array   | Lista de procesos de publicación                     |

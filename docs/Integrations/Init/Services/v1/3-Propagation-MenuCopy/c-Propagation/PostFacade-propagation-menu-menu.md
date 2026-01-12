## Ejecutar Flujo de Integración - Propagación de Menú (Facade)

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
              "name": "mxp_v2.USP_Propagate_Menu_Menu",
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
                  "value": "menu_for_franchise"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Menu",
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
                  "name": "´plu_id",
                  "operator": "equals",
                  "value": "{{plu_id}}"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "menu_for_franchise_categories"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Menu",
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
                  "value": "menu_for_franchise_categories_plu"
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
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "UAT_KFC_BO_Configurations",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "Configurations_BO_Enviroment_Variables",
              "properties": [
                {
                  "name": "limit_column_categories_menu",
                  "type": "base64"
                },
                {
                  "name": "limit_column_categories_product",
                  "type": "base64"
                },
                {
                  "name": "limit_row_categories_menu",
                  "type": "base64"
                },
                {
                  "name": "limit_row_categories_product",
                  "type": "base64"
                },
                {
                  "name": "principal_icon",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "domain",
                  "operator": "equals",
                  "value": "Menu"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E003",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
                  "value": "ECU"
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
                  "value": "ECU"
                },
                {
                  "name": "entity_name",
                  "operator": "in",
                  "value": [
                    "Cadena",
                    "Menu",
                    "Menu_Agrupacion",
                    "Plus",
                    "transformation_half_integration",
                    "transformation_classifications"
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
                  "value": "ECU"
                },
                {
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "mxp_v2.View_Status_Menu"
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
                  "value": "ECU"
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
        "code": "T002",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
            "repository": "/YOUR_REDIS_OR_AZURE_KEY_HERE?user=9bf439f0-bde7-360c-ecba-fc3526bfa7b0&country_id=8d1fb0d0-ff7a-4475-a7ec-2394361df3db",
            "adapter": "Rest"
          },
          "entities": [
            {
              "name": "menu",
              "toName": "menus",
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
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
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
                  "fromName": "status_menu",
                  "fromType": "",
                  "toName": "status_menu",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "half_integration_id",
                  "fromType": "",
                  "toName": "half_integration_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "menu_name",
                  "fromType": "",
                  "toName": "menu_name",
                  "toType": "",
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
                  "fromName": "limit_columns_category",
                  "fromType": "",
                  "toName": "limit_columns_category",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "limit_rows_category",
                  "fromType": "",
                  "toName": "limit_rows_category",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "limit_columns_plu",
                  "fromType": "",
                  "toName": "limit_columns_plu",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "limit_rows_plu",
                  "fromType": "",
                  "toName": "limit_rows_plu",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "icon",
                  "fromType": "",
                  "toName": "icon",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "icon_id",
                      "fromType": "",
                      "toName": "icon_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "color_id",
                      "fromType": "",
                      "toName": "color_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    }
                  ]
                },
                {
                  "fromName": "description",
                  "fromType": "",
                  "toName": "description",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "images_menu",
                  "fromType": "",
                  "toName": "images_menu",
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
                      "fromName": "pos_y",
                      "fromType": "",
                      "toName": "pos_y",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "pos_x",
                      "fromType": "",
                      "toName": "pos_x",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "plus",
                      "fromType": "",
                      "toName": "plus",
                      "toType": "array",
                      "defaultValue": [
                        {
                          "fromName": "plu_id",
                          "fromType": "",
                          "toName": "plu_id",
                          "toType": "uuid",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "pos_y",
                          "fromType": "",
                          "toName": "pos_y",
                          "toType": "",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "pos_x",
                          "fromType": "",
                          "toName": "pos_x",
                          "toType": "",
                          "defaultValue": ""
                        }
                      ]
                    }
                  ]
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

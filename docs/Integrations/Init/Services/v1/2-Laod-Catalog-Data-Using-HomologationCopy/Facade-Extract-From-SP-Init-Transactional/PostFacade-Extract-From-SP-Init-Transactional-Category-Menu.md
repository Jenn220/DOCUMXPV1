## Ejecutar Proceso ETL Facade para Categoría de Menú Transaccional

### Método HTTP

`POST`

### URL

```
{{server_init}}/api/v1/facade
```

### Autenticación

**Tipo:** Bearer Token

| Token       |
| ----------- |
| `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "F100",
  "withResponse": false,
  "withCache": false,
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
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
              "name": "mxp_v2.USP_Catalog_Data_MXPLegacy",
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
                  "name": "option",
                  "operator": "equals",
                  "value": "transactional_category_menu"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E002",
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
              "name": "mxp_v2.USP_Catalog_Data_MXPLegacy",
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
                  "name": "option",
                  "operator": "equals",
                  "value": "transactional_category_menu_image"
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
                  "value": "{{country}}"
                },
                {
                  "name": "entity_name",
                  "operator": "in",
                  "value": [
                    "Cadena",
                    "transformation_category_image",
                    "Menu_Agrupacion"
                  ]
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
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
                  "name": "id_v2",
                  "operator": "equals",
                  "value": "9bf439f0-bde7-360c-ecba-fc3526bfa7b0"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E006",
        "withResponse": true,
        "withCache": false,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
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
              "name": "Configurations_BO_Color",
              "properties": [
                {
                  "name": "color_name",
                  "type": "base64"
                },
                {
                  "name": "color_hex",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "_id",
                  "operator": "equals",
                  "value": "43d1809c-f0a5-9cb5-3571-2e4a62db3d96",
                  "datatype": "uuid"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E007",
        "withResponse": true,
        "withCache": false,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "UAT_KFC_BO_Menus",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "Menus_BO_Icon_Menu",
              "properties": [
                {
                  "name": "icon_name",
                  "type": "UUID"
                }
              ],
              "filters": [
                {
                  "name": "_id",
                  "operator": "equals",
                  "value": "342ca602-fb3e-0749-7568-93de94b3444d",
                  "datatype": "uuid"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T032",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "{{country}}"
      },
      {
        "code": "T031",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "{{country}}"
      }
    ],
    "LOADS": [
      {
        "code": "L001",
        "withResponse": true,
        "withCache": false,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "UAT_KFC_BO_Menus",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "transactional_category_menu",
              "toName": "Menus_BO_Category_Menu",
              "properties": [
                {
                  "fromName": "homologation_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "description",
                  "fromType": "",
                  "toName": "description",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "category_menu_name",
                  "fromType": "",
                  "toName": "category_menu_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "is_visible",
                  "fromType": "",
                  "toName": "is_visible",
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
                  "fromName": "cdn_id",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "uuid",
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
                  "fromName": "images_category_menu",
                  "fromType": "",
                  "toName": "images_category_menu",
                  "toType": "array",
                  "defaultValue": "",
                  "hasUuids": "true"
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "created_at",
                  "toType": "timestamp",
                  "defaultValue": "true"
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "updated_at",
                  "toType": "timestamp",
                  "defaultValue": "true"
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

## Ejecutar Flujo de Integración - Usuarios POS (Facade)

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
  "code": "F100",
  "withResponse": true,
  "withCache": false,
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
              "name": "mxp_v2.USP_UsuariosPos_JSON",
              "properties": [],
              "filters": [
                {
                  "name": "PerfilNombre",
                  "operator": "equals",
                  "value": "Administrador Local"
                },
                {
                  "name": "CadenaId",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "RestauranteId",
                  "operator": "equals",
                  "value": "0"
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
              "name": "mxp_v2.USP_UsuariosPos_JSON",
              "properties": [],
              "filters": [
                {
                  "name": "PerfilNombre",
                  "operator": "equals",
                  "value": "Cajero"
                },
                {
                  "name": "CadenaId",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "RestauranteId",
                  "operator": "equals",
                  "value": "0"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E003",
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
              "name": "mxp_v2.USP_UsuariosPos_JSON",
              "properties": [],
              "filters": [
                {
                  "name": "PerfilNombre",
                  "operator": "equals",
                  "value": "Mesero"
                },
                {
                  "name": "CadenaId",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                },
                {
                  "name": "RestauranteId",
                  "operator": "equals",
                  "value": "0"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E004",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "homologation_v1_v2",
            "adapter": "Mongo"
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
                  "value": ["Ciudad", "Perfil_Pos"]
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E005",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "homologation_v1_v2",
            "adapter": "Mongo"
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
                  "operator": "equals",
                  "value": "mxp_v2.View_User_POS"
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E006",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "homologation_v1_v2",
            "adapter": "Mongo"
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
                  "operator": "equals",
                  "value": "Restaurante"
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E007",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "homologation_v1_v2",
            "adapter": "Mongo"
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
                  "operator": "equals",
                  "value": "Cadena"
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E008",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "homologation_v1_v2",
            "adapter": "Mongo"
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
                  "operator": "equals",
                  "value": "Pais"
                },
                {
                  "name": "id_v1",
                  "operator": "equals",
                  "value": "{{legacy_country_id}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T120",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": true,
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
            "repository": "DEV_KFC_MXPi_Settings",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "users_pos",
              "toName": "Settings_BO_Users_Pos",
              "properties": [
                {
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "country",
                  "fromType": "",
                  "toName": "country",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "country_id",
                      "fromType": "",
                      "toName": "country_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "country",
                      "fromType": "",
                      "toName": "country",
                      "toType": "",
                      "defaultValue": ""
                    }
                  ]
                },
                {
                  "fromName": "country",
                  "fromType": "",
                  "toName": "country",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "user_pos",
                  "fromType": "",
                  "toName": "user_pos",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "first_name",
                      "fromType": "",
                      "toName": "first_name",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "last_name",
                      "fromType": "",
                      "toName": "last_name",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "email",
                      "fromType": "",
                      "toName": "email",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "phone",
                      "fromType": "",
                      "toName": "phone",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "address",
                      "fromType": "",
                      "toName": "address",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "birth_date",
                      "fromType": "",
                      "toName": "birth_date",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "user",
                      "fromType": "",
                      "toName": "user",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "password",
                      "fromType": "",
                      "toName": "password",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "identification",
                      "fromType": "",
                      "toName": "identification",
                      "toType": "",
                      "defaultValue": ""
                    }
                  ]
                },
                {
                  "fromName": "user_pos_profiles",
                  "fromType": "",
                  "toName": "user_pos_profiles",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "profile_id",
                      "fromType": "",
                      "toName": "profile_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "profile_name",
                      "fromType": "",
                      "toName": "profile_name",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "franchises",
                      "fromType": "",
                      "toName": "franchises",
                      "toType": "array",
                      "defaultValue": [
                        {
                          "fromName": "franchise_id",
                          "fromType": "",
                          "toName": "franchise_id",
                          "toType": "uuid",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "franchise_name",
                          "fromType": "",
                          "toName": "franchise_name",
                          "toType": "",
                          "defaultValue": ""
                        },
                        {
                          "fromName": "restaurants",
                          "fromType": "",
                          "toName": "restaurants",
                          "toType": "array",
                          "defaultValue": [
                            {
                              "fromName": "restaurant_id",
                              "fromType": "",
                              "toName": "restaurant_id",
                              "toType": "uuid",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "restaurant_name",
                              "fromType": "",
                              "toName": "restaurant_name",
                              "toType": "",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "address",
                              "fromType": "",
                              "toName": "address",
                              "toType": "",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "phone",
                              "fromType": "",
                              "toName": "phone",
                              "toType": "",
                              "defaultValue": ""
                            },
                            {
                              "fromName": "city_id",
                              "fromType": "",
                              "toName": "city_id",
                              "toType": "uuid",
                              "defaultValue": ""
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "IsActive",
                  "toType": "boolean",
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

### Descripción del Cuerpo de la Solicitud

| Campo                                           | Tipo    | Descripción                                 |
| ----------------------------------------------- | ------- | ------------------------------------------- |
| `code`                                          | string  | Código del flujo de integración             |
| `withResponse`                                  | boolean | Indica si retorna respuesta                 |
| `withCache`                                     | boolean | Indica si utiliza caché                     |
| `syncId`                                        | string  | ID de sincronización                        |
| `chunkLoad`                                     | number  | Tamaño de lote para carga de datos          |
| `processes`                                     | object  | Objeto con los procesos a ejecutar          |
| `processes.EXTRACTS`                            | array   | Lista de procesos de extracción             |
| `processes.EXTRACTS[].code`                     | string  | Código del proceso de extracción            |
| `processes.EXTRACTS[].withResponse`             | boolean | Indica si retorna respuesta                 |
| `processes.EXTRACTS[].withCache`                | boolean | Indica si utiliza caché                     |
| `processes.EXTRACTS[].syncId`                   | string  | ID de sincronización                        |
| `processes.EXTRACTS[].configuration`            | object  | Configuración del proceso                   |
| `processes.EXTRACTS[].configuration.connection` | object  | Configuración de conexión                   |
| `processes.EXTRACTS[].configuration.entities`   | array   | Lista de entidades a extraer                |
| `processes.TRANSFORMS`                          | array   | Lista de procesos de transformación         |
| `processes.TRANSFORMS[].code`                   | string  | Código del proceso de transformación        |
| `processes.TRANSFORMS[].syncId`                 | string  | ID de sincronización                        |
| `processes.TRANSFORMS[].withResponse`           | boolean | Indica si retorna respuesta                 |
| `processes.TRANSFORMS[].withCache`              | boolean | Indica si utiliza caché                     |
| `processes.TRANSFORMS[].country`                | string  | Código del país                             |
| `processes.LOADS`                               | array   | Lista de procesos de carga                  |
| `processes.LOADS[].code`                        | string  | Código del proceso de carga                 |
| `processes.LOADS[].withResponse`                | boolean | Indica si retorna respuesta                 |
| `processes.LOADS[].withCache`                   | boolean | Indica si utiliza caché                     |
| `processes.LOADS[].syncId`                      | string  | ID de sincronización                        |
| `processes.LOADS[].configuration`               | object  | Configuración del proceso de carga          |
| `processes.LOADS[].configuration.connection`    | object  | Configuración de conexión a base de datos   |
| `processes.LOADS[].configuration.entities`      | array   | Lista de entidades de destino para la carga |
| `processes.LOADS[].dataInput`                   | object  | Datos de entrada adicionales                |
| `processes.PUBLISHERS`                          | array   | Lista de procesos de publicación            |

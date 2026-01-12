## Ejecutar Flujo de Integración - Propagación de Preguntas Sugeridas de Menú (Facade)

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
  "withResponse": true,
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
              "name": "mxp_v2.USP_Propagate_Menu_Suggested_Question",
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
                  "value": "suggested_question_for_franchise"
                }
              ]
            },
            {
              "name": "mxp_v2.USP_Propagate_Menu_Suggested_Question",
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
                  "value": "suggested_question_for_franchise_answers"
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
                    "Pregunta_Sugerida",
                    "mxp_v2.View_Answer_For_Franchise",
                    "Plus"
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
                  "value": "mxp_v2.View_Status_Suggested_Question"
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
                  "value": "mxp_v2.View_Type_Question"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T003",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": true,
        "country": "{{country}}"
      }
    ],
    "LOADS": [
      {
        "code": "L001",
        "withCache": true,
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
              "name": "suggested_question",
              "toName": "suggestedQuestions",
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
                  "fromName": "sug_question_min_responses",
                  "fromType": "",
                  "toName": "sug_question_min_responses",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "sug_question_max_responses",
                  "fromType": "",
                  "toName": "sug_question_max_responses",
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
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "sug_question_pos_description",
                  "fromType": "",
                  "toName": "sug_question_pos_description",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "sug_question_tittle",
                  "fromType": "",
                  "toName": "sug_question_tittle",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "status_suggested_question_id",
                  "fromType": "",
                  "toName": "status_suggested_question_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "type_question_id",
                  "fromType": "",
                  "toName": "type_question_id",
                  "toType": "uuid",
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
                    },
                    {
                      "fromName": "plu_id",
                      "fromType": "",
                      "toName": "plu_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "answer_pos_description",
                      "fromType": "",
                      "toName": "answer_pos_description",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "next_questions",
                      "fromType": "",
                      "toName": "next_questions",
                      "toType": "",
                      "defaultValue": ""
                    }
                  ]
                },
                {
                  "fromName": "copy",
                  "fromType": "",
                  "toName": "copy",
                  "toType": "",
                  "defaultValue": ""
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

## Ejecutar Flujo de Integración - Propagación de UpSelling (Facade)

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
              "name": "mxp_v2.USP_Propagate_Menu_Up_Selling",
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
                  "value": "upselling_for_franchise"
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
                  "value": ["Plus", "transformation_collection_plu"]
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T004",
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
              "name": "upsellings",
              "toName": "UpSelling",
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
                  "fromName": "plu_references",
                  "fromType": "",
                  "toName": "plu_references",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "id_plu",
                      "fromType": "",
                      "toName": "id_plu",
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
                },
                {
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "plu_father",
                  "fromType": "",
                  "toName": "plu_father",
                  "toType": "uuid",
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
| `withCache`                                     | boolean | Indica si utiliza caché                              |
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

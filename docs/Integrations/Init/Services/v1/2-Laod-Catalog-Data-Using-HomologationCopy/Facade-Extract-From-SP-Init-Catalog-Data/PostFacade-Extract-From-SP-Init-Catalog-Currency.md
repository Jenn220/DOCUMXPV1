## Ejecutar Flujo de Integración - Catálogo de Monedas (Facade)

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
                  "value": "0"
                },
                {
                  "name": "option",
                  "operator": "equals",
                  "value": "catalog_currency"
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
                  "operator": "equals",
                  "value": "Pais"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T012",
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
            "repository": "UAT_KFC_BO_Configurations",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "catalog_currency",
              "toName": "Configurations_BO_Currency",
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
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "currency_name",
                  "fromType": "",
                  "toName": "currency_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "currency_code",
                  "fromType": "",
                  "toName": "currency_code",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "decimal_places",
                  "fromType": "",
                  "toName": "decimal_places",
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

### Descripción del Cuerpo de la Solicitud

| Campo                                           | Tipo    | Requerido | Descripción                          |
| ----------------------------------------------- | ------- | --------- | ------------------------------------ |
| `code`                                          | string  | Sí        | Código del flujo de integración      |
| `withResponse`                                  | boolean | No        | Indica si retorna respuesta          |
| `withCache`                                     | boolean | No        | Indica si utiliza caché              |
| `syncId`                                        | string  | Sí        | ID de sincronización                 |
| `processes`                                     | object  | Sí        | Objeto con los procesos a ejecutar   |
| `processes.EXTRACTS`                            | array   | No        | Lista de procesos de extracción      |
| `processes.EXTRACTS[].code`                     | string  | No        | Código del proceso de extracción     |
| `processes.EXTRACTS[].withResponse`             | boolean | No        | Indica si retorna respuesta          |
| `processes.EXTRACTS[].withCache`                | boolean | No        | Indica si utiliza caché              |
| `processes.EXTRACTS[].syncId`                   | string  | No        | ID de sincronización                 |
| `processes.EXTRACTS[].configuration`            | object  | No        | Configuración del proceso            |
| `processes.EXTRACTS[].configuration.connection` | object  | No        | Configuración de conexión            |
| `processes.EXTRACTS[].configuration.entities`   | array   | No        | Lista de entidades a extraer         |
| `processes.TRANSFORMS`                          | array   | No        | Lista de procesos de transformación  |
| `processes.TRANSFORMS[].code`                   | string  | No        | Código del proceso de transformación |
| `processes.TRANSFORMS[].syncId`                 | string  | No        | ID de sincronización                 |
| `processes.TRANSFORMS[].withResponse`           | boolean | No        | Indica si retorna respuesta          |
| `processes.TRANSFORMS[].withCache`              | boolean | No        | Indica si utiliza caché              |
| `processes.TRANSFORMS[].country`                | string  | No        | Código del país                      |
| `processes.LOADS`                               | array   | No        | Lista de procesos de carga           |
| `processes.LOADS[].code`                        | string  | No        | Código del proceso de carga          |
| `processes.LOADS[].withResponse`                | boolean | No        | Indica si retorna respuesta          |
| `processes.LOADS[].withCache`                   | boolean | No        | Indica si utiliza caché              |
| `processes.LOADS[].syncId`                      | string  | No        | ID de sincronización                 |
| `processes.LOADS[].configuration`               | object  | No        | Configuración del proceso de carga   |
| `processes.LOADS[].dataInput`                   | object  | No        | Datos de entrada adicionales         |
| `processes.PUBLISHERS`                          | array   | No        | Lista de procesos de publicación     |

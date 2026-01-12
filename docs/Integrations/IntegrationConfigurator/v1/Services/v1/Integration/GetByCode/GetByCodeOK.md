## Obtener Integración por Código

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/integrations/getById
```

### Parámetros de Query

| Key    | Value  | Description                          |
| ------ | ------ | ------------------------------------ |
| `code` | `I921` | Código de la integración a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": "F001",
  "withResponse": true,
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
            "server": "dbmaxpoint-ec-mi.132fe021d3ac.database.windows.net",
            "port": "",
            "user": "sis_mxpv2",
            "password": "mxp!v2*",
            "repository": "MAXPOINT_AZURE_102924",
            "adapter": "SqlServer"
          },
          "entities": [
            {
              "name": "Clasificacion",
              "properties": [
                {
                  "name": "IDClasificacion",
                  "type": "base64"
                },
                {
                  "name": "cla_nombre",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "IDStatus",
                  "operator": "equals",
                  "value": "5b039503-85cf-e511-80c6-000d3a3261f3"
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
            "server": "ec-mxpv2-dev.3hro7.mongodb.net",
            "port": "",
            "user": "dev_integration",
            "password": "rIJEUAk8WyynPhC4",
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
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "Cadena"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T008",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "ECU",
        "filter": [
          {
            "cacheName": "uuids",
            "nameObject": 0,
            "typeObject": "list"
          },
          {
            "cacheName": "Clasificacion",
            "nameObject": 0,
            "value_name": "cla_nombre",
            "entity_name": "Clasificacion",
            "fieldName": "combined_id",
            "combined_field": ["id_v1", "IDClasificacion"],
            "addFieldsFromCache": []
          }
        ]
      }
    ],
    "LOADS": [
      {
        "code": "{{code_load}}",
        "withCache": false,
        "withResponse": true,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "ec-mxpv2-dev.3hro7.mongodb.net",
            "port": "",
            "user": "dev_integration",
            "password": "rIJEUAk8WyynPhC4",
            "repository": "homologation_v1_v2",
            "adapter": "MongoMxpV2"
          },
          "entities": [
            {
              "name": 0,
              "toName": "transformation_classifications",
              "properties": [
                {
                  "fromName": "id_v1",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "entity",
                  "fromType": "",
                  "toName": "entity",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "value",
                  "fromType": "",
                  "toName": "value",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "IDClasificacion",
                  "fromType": "",
                  "toName": "legacy_classification_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "combined_id",
                  "fromType": "",
                  "toName": "combined_id",
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
    "TRANSACTIONS": [],
    "PUBLISHERS": []
  }
}
```

### Descripción de la Respuesta Exitosa

La respuesta contiene la configuración completa de la integración incluyendo sus procesos de extracción (EXTRACTS), transformación (TRANSFORMS), carga (LOADS), transacciones (TRANSACTIONS) y publicación (PUBLISHERS).

## Obtener Integración por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/integrations/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                            |
| ---- | -------------------------------------- | -------------------------------------- |
| `id` | `ac248fe2-2d7e-461f-b245-50557a4eeec1` | ID único de la integración a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": "I0137",
  "withResponse": true,
  "chunkLoad": 0,
  "syncId": "",
  "country": "ECU",
  "franchise_id": 0,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E0082",
        "withResponse": true,
        "withCache": true,
        "syncId": "",
        "configuration": {
          "connection": {
            "server": "192.168.1.70",
            "port": "",
            "user": "NAME",
            "password": "123456789",
            "repository": "USERNAME",
            "adapter": "CND ADAPTADOR"
          },
          "entities": [
            {
              "name": "CND_ENTITY",
              "properties": [
                {
                  "name": "cnd_properties",
                  "type": "string"
                }
              ],
              "filters": [
                {
                  "name": "cnd_properties",
                  "operator": "equal",
                  "value": "countryName"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T017",
        "syncId": "",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
      }
    ],
    "LOADS": [
      {
        "code": "L0003",
        "withCache": false,
        "withResponse": true,
        "syncId": "",
        "configuration": {
          "connection": {
            "server": "ec-mxpv2-qa.irplcko.mongodb.net",
            "port": "",
            "user": "app_uat_integration",
            "password": "2tg0tTzCxPMueq7I",
            "repository": "UAT_KFC_BO_InternalClients",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "catalog_for_franchise",
              "toName": "InternalClients_BO_Franchise",
              "properties": [
                {
                  "fromName": "homologation_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true",
                  "hasUuids": "false"
                },
                {
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "hasUuids": "false"
                },
                {
                  "fromName": "franchise_name",
                  "fromType": "",
                  "toName": "franchise_name",
                  "toType": "",
                  "defaultValue": "",
                  "hasUuids": "false"
                },
                {
                  "fromName": "description",
                  "fromType": "",
                  "toName": "description",
                  "toType": "",
                  "defaultValue": "",
                  "hasUuids": "false"
                },
                {
                  "fromName": "country_id",
                  "fromType": "",
                  "toName": "country_id",
                  "toType": "",
                  "defaultValue": "",
                  "hasUuids": "false"
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "created_at",
                  "toType": "timestamp",
                  "defaultValue": "true",
                  "hasUuids": "false"
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "updated_at",
                  "toType": "timestamp",
                  "defaultValue": "true",
                  "hasUuids": "false"
                }
              ]
            }
          ]
        },
        "dataInput": {}
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

La respuesta contiene la configuración completa de la integración incluyendo código, país, ID de franquicia y sus procesos de extracción (EXTRACTS), transformación (TRANSFORMS) y carga (LOADS).

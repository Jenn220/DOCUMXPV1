## Obtener Integración por ID y SyncId 2

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/integrations/getById
```

### Parámetros de Query

| Key      | Value                                  | Description                            |
| -------- | -------------------------------------- | -------------------------------------- |
| `id`     | `ac248fe2-2d7e-461f-b245-50557a4eeec1` | ID único de la integración a consultar |
| `syncId` | `caa3d39b-290a-4683-bcf5-e078b33c0974` | ID de sincronización                   |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": "I0137",
  "withResponse": true,
  "chunkLoad": 0,
  "syncId": "ac248fe2-2d7e-461f-b245-50557a4eeec1",
  "country": "ECU",
  "franchise_id": 0,
  "processes": {
    "LOADS": [
      {
        "code": "L0003",
        "withCache": false,
        "withResponse": true,
        "syncId": "ac248fe2-2d7e-461f-b245-50557a4eeec1",
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

La respuesta contiene la configuración de la integración enfocada en los procesos de carga (LOADS), mostrando la conexión a MongoDB y el mapeo de propiedades de las entidades.

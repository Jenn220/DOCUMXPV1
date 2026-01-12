## Ejecutar Flujo de Integración - Homologación de UUIDs Respuestas (Facade)

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
  "code": "H000",
  "withResponse": false,
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "country": "{{country}}",
  "franchise_id": "{{legacy_cdn_id}}",
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
            "adapter": "SqlServer"
          },
          "entities": [
            {
              "name": "mxp_v2.View_Answer_For_Franchise",
              "properties": [
                {
                  "name": "IDRespuestas",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "H001",
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
              "toName": "uuids",
              "properties": [
                {
                  "fromName": "id_v2",
                  "fromType": "",
                  "toName": "id_v2",
                  "toType": "string",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "country_code",
                  "fromType": "",
                  "toName": "country_code",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "franchise_id",
                  "fromType": "",
                  "toName": "franchise_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "entity_name",
                  "fromType": "",
                  "toName": "entity_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "id_v1",
                  "fromType": "",
                  "toName": "id_v1",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "",
                  "fromType": "",
                  "toName": "created_at",
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

| Campo                                           | Tipo    | Descripción                                 |
| ----------------------------------------------- | ------- | ------------------------------------------- |
| `code`                                          | string  | Código del flujo de integración             |
| `withResponse`                                  | boolean | Indica si retorna respuesta                 |
| `syncId`                                        | string  | ID de sincronización                        |
| `country`                                       | string  | Código del país                             |
| `franchise_id`                                  | string  | ID de la franquicia en legacy               |
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

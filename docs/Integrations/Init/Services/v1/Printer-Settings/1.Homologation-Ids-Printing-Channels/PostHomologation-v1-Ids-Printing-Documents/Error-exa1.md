## Ejecutar Flujo de Integración ETL (Facade)

### Método HTTP

`POST`

### URL

```
{{server_etlp_extract}}/api/v1/facade
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
  "withCache": false,
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "country": "{{country}}",
  "franchise_id": 0,
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
              "name": "Users_Pos",
              "properties": [
                {
                  "name": "IDUsersPos",
                  "type": "base64"
                }
              ],
              "filters": [
                {
                  "name": "IDPerfilPos",
                  "operator": "equals",
                  "value": "55059503-85cf-e511-80c6-000d3a3261f3"
                },
                {
                  "name": "usr_usuario",
                  "operator": "equals",
                  "value": "dllerena"
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
            "server": "ec-mxpv2-qa.irplcko.mongodb.net",
            "port": "",
            "user": "app_uat_integration",
            "password": "2tg0tTzCxPMueq7I",
            "repository": "UAT_KFC_MXP_Homologation_v1_v2",
            "adapter": "Mongo"
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

| Campo                                                                  | Tipo    | Descripción                                               |
| ---------------------------------------------------------------------- | ------- | --------------------------------------------------------- |
| `code`                                                                 | string  | Código de la homologación                                 |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta                 |
| `withCache`                                                            | boolean | Especifica si desea guardar la respuesta en caché (mongo) |
| `syncId`                                                               | string  | ID UUID de sincronización                                 |
| `country`                                                              | string  | Código de país (3 dígitos)                                |
| `franchise_id`                                                         | number  | ID de la cadena del MXP legacy                            |
| `processes`                                                            | object  | Objeto con los procesos a ejecutar                        |
| `processes.EXTRACTS`                                                   | array   | Lista de procesos de extracción                           |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                          |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Indica si retorna respuesta                               |
| `processes.EXTRACTS[].withCache`                                       | boolean | Indica si utiliza caché                                   |
| `processes.EXTRACTS[].syncId`                                          | string  | ID de sincronización                                      |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración del proceso                                 |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Configuración de conexión a base de datos                 |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                                 |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                        |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                       |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                                    |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos                                |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Tipo de adaptador de base de datos                        |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Lista de entidades a extraer                              |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la tabla/entidad a extraer                      |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Lista de propiedades a extraer                            |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                                    |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                              |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Lista de filtros para la extracción                       |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del campo a filtrar                                |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                                   |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del filtro                                          |
| `processes.TRANSFORMS`                                                 | array   | Lista de procesos de transformación                       |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación                      |
| `processes.TRANSFORMS[].syncId`                                        | string  | ID de sincronización                                      |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Indica si retorna respuesta                               |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Indica si utiliza caché                                   |
| `processes.TRANSFORMS[].country`                                       | string  | Código del país                                           |
| `processes.LOADS`                                                      | array   | Lista de procesos de carga                                |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                               |
| `processes.LOADS[].withCache`                                          | boolean | Indica si utiliza caché                                   |
| `processes.LOADS[].withResponse`                                       | boolean | Indica si retorna respuesta                               |
| `processes.LOADS[].syncId`                                             | string  | ID de sincronización                                      |
| `processes.LOADS[].configuration`                                      | object  | Configuración del proceso de carga                        |
| `processes.LOADS[].configuration.connection`                           | object  | Configuración de conexión a base de datos                 |
| `processes.LOADS[].configuration.connection.server`                    | string  | Servidor de base de datos                                 |
| `processes.LOADS[].configuration.connection.port`                      | string  | Puerto de conexión                                        |
| `processes.LOADS[].configuration.connection.user`                      | string  | Usuario de conexión                                       |
| `processes.LOADS[].configuration.connection.password`                  | string  | Contraseña de conexión                                    |
| `processes.LOADS[].configuration.connection.repository`                | string  | Nombre de la base de datos                                |
| `processes.LOADS[].configuration.connection.adapter`                   | string  | Tipo de adaptador de base de datos                        |
| `processes.LOADS[].configuration.entities`                             | array   | Lista de entidades de destino para la carga               |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad extraída                             |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad a cargar                             |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Lista de propiedades a mapear                             |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre de la propiedad extraída                           |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato de origen                                    |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre de la propiedad a cargar                           |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato de destino                                   |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto (vacío usa el valor de extracción)      |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Especifica si es valor único y valida duplicidad          |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                              |
| `processes.PUBLISHERS`                                                 | array   | Lista de procesos de publicación                          |

### Respuestas del Servidor

**500 Internal Server Error - Error en la Integración**

```json
{
  "code": 500,
  "status": "error",
  "process": "I001",
  "message": "Integración fallida",
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "data": {
    "EXTRACTS": [
      {
        "code": 500,
        "status": "error",
        "process": "E001",
        "message": "Error processing request: ('HYT00', '[HYT00] [Microsoft][ODBC Driver 18 for SQL Server]Login timeout expired (0) (SQLDriverConnect)')",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      }
    ],
    "TRANSFORMS": [],
    "LOAD": []
  }
}
```

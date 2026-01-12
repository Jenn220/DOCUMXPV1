## Ejecutar Proceso de Extracción ETL

### Método HTTP

`POST`

### URL

```
{{server_etlp_extract}}/api/v1/facade
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

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
        "withCache": true,
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
        "withCache": true,
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
        "code": "T008-1",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
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
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": 0,
              "toName": "transformation_classifications",
              "properties": [
                {
                  "fromName": "combined_id",
                  "fromType": "",
                  "toName": "combined_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
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

| Campo                                                                  | Tipo    | Descripción                                         |
| ---------------------------------------------------------------------- | ------- | --------------------------------------------------- |
| `code`                                                                 | string  | Código de la fachada de extracción                  |
| `withResponse`                                                         | boolean | Indica si debe retornar respuesta                   |
| `withCache`                                                            | boolean | Indica si debe usar caché                           |
| `syncId`                                                               | string  | Identificador único de sincronización               |
| `processes`                                                            | object  | Objeto contenedor de los procesos ETL               |
| `processes.EXTRACTS`                                                   | array   | Lista de procesos de extracción de datos            |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                    |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Indica si debe retornar respuesta                   |
| `processes.EXTRACTS[].withCache`                                       | boolean | Indica si debe usar caché                           |
| `processes.EXTRACTS[].syncId`                                          | string  | Identificador de sincronización del proceso         |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración del proceso de extracción             |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Información de conexión a la base de datos          |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                           |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                  |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                 |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                              |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos o repositorio            |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Adaptador de base de datos (SqlServer, Mongo, etc.) |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Lista de entidades a extraer                        |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la entidad                                |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Propiedades de la entidad a extraer                 |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                              |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                        |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Filtros aplicados a la entidad                      |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del campo a filtrar                          |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                             |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del filtro                                    |
| `processes.TRANSFORMS`                                                 | array   | Lista de procesos de transformación                 |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación                |
| `processes.TRANSFORMS[].syncId`                                        | string  | Identificador de sincronización del proceso         |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Indica si debe retornar respuesta                   |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Indica si debe usar caché                           |
| `processes.TRANSFORMS[].country`                                       | string  | Código del país para la transformación              |
| `processes.LOADS`                                                      | array   | Lista de procesos de carga de datos                 |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                         |
| `processes.LOADS[].withCache`                                          | boolean | Indica si debe usar caché                           |
| `processes.LOADS[].withResponse`                                       | boolean | Indica si debe retornar respuesta                   |
| `processes.LOADS[].syncId`                                             | string  | Identificador de sincronización del proceso         |
| `processes.LOADS[].configuration`                                      | object  | Configuración del proceso de carga                  |
| `processes.LOADS[].configuration.connection`                           | object  | Información de conexión a la base de datos destino  |
| `processes.LOADS[].configuration.connection.server`                    | string  | Servidor de base de datos destino                   |
| `processes.LOADS[].configuration.connection.port`                      | string  | Puerto de conexión                                  |
| `processes.LOADS[].configuration.connection.user`                      | string  | Usuario de conexión                                 |
| `processes.LOADS[].configuration.connection.password`                  | string  | Contraseña de conexión                              |
| `processes.LOADS[].configuration.connection.repository`                | string  | Nombre de la base de datos destino                  |
| `processes.LOADS[].configuration.connection.adapter`                   | string  | Adaptador de base de datos                          |
| `processes.LOADS[].configuration.entities`                             | array   | Lista de entidades a cargar                         |
| `processes.LOADS[].configuration.entities[].name`                      | number  | Índice de la entidad origen                         |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad destino                        |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Mapeo de propiedades entre origen y destino         |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre del campo origen                             |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato origen                                 |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre del campo destino                            |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato destino                                |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto del campo                         |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Indica si es clave primaria                         |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                        |
| `processes.PUBLISHERS`                                                 | array   | Lista de procesos de publicación                    |

### Respuestas del Servidor

#### 500 Internal Server Error

```html
<!DOCTYPE html>
<html lang="en">
  <title>500 Internal Server Error</title>
  <h1>Internal Server Error</h1>
  <p>
    The server encountered an internal error and was unable to complete your
    request. Either the server is overloaded or there is an error in the
    application.
  </p>
</html>
```

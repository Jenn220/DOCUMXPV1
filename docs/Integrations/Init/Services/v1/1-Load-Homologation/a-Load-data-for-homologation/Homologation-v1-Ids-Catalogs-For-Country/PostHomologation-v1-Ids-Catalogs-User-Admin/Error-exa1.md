## Ejecutar Proceso ETL Facade

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

### Descripción de Campos del Cuerpo

| Campo                                                                  | Tipo    | Description                                       |
| ---------------------------------------------------------------------- | ------- | ------------------------------------------------- |
| `code`                                                                 | string  | Código de la homologación                         |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta         |
| `withCache`                                                            | boolean | Especifica si desea guardar la respuesta en cache |
| `syncId`                                                               | string  | ID UUID de sincronización                         |
| `country`                                                              | string  | Código de país (3 dígitos)                        |
| `franchise_id`                                                         | number  | ID de la cadena del MXP legacy                    |
| `processes`                                                            | object  | Objeto con los procesos ETL                       |
| `processes.EXTRACTS`                                                   | array   | Array de procesos de extracción                   |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                  |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Devolver respuesta de extracción                  |
| `processes.EXTRACTS[].withCache`                                       | boolean | Guardar en cache                                  |
| `processes.EXTRACTS[].syncId`                                          | string  | ID de sincronización                              |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración de extracción                       |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Configuración de conexión                         |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                         |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                               |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                            |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos                        |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Tipo de adaptador (SqlServer/Mongo)               |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Array de entidades a extraer                      |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la entidad                              |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Propiedades de la entidad                         |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                            |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                      |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Filtros para la extracción                        |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del campo a filtrar                        |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                           |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del filtro                                  |
| `processes.TRANSFORMS`                                                 | array   | Array de procesos de transformación               |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación              |
| `processes.TRANSFORMS[].syncId`                                        | string  | ID de sincronización                              |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Devolver respuesta de transformación              |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Guardar en cache                                  |
| `processes.TRANSFORMS[].country`                                       | string  | Código de país                                    |
| `processes.LOADS`                                                      | array   | Array de procesos de carga                        |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                       |
| `processes.LOADS[].withCache`                                          | boolean | Guardar en cache                                  |
| `processes.LOADS[].withResponse`                                       | boolean | Devolver respuesta de carga                       |
| `processes.LOADS[].syncId`                                             | string  | ID de sincronización                              |
| `processes.LOADS[].configuration`                                      | object  | Configuración de carga                            |
| `processes.LOADS[].configuration.connection`                           | object  | Configuración de conexión destino                 |
| `processes.LOADS[].configuration.entities`                             | array   | Array de entidades a cargar                       |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad extraída                     |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad a cargar                     |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Mapeo de propiedades                              |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre de la propiedad origen                     |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato origen                               |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre de la propiedad destino                    |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato destino                              |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto                                 |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Indica si es clave primaria                       |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                      |
| `processes.PUBLISHERS`                                                 | array   | Array de procesos de publicación                  |

### Respuestas del Servidor

#### 200 OK - Proceso Exitoso

```json
{
  "code": 200,
  "status": "success",
  "process": "I001",
  "message": "Integración completada exitosamente",
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "data": {
    "EXTRACTS": [
      {
        "code": 200,
        "status": "success",
        "process": "E001",
        "message": "Extracción completada exitosamente",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      },
      {
        "code": 200,
        "status": "success",
        "process": "E002",
        "message": "Extracción completada exitosamente",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      },
      {
        "code": 200,
        "status": "success",
        "process": "E003",
        "message": "Extracción completada exitosamente",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      }
    ],
    "TRANSFORMS": [
      {
        "code": 200,
        "status": "success",
        "process": "T003",
        "message": "Transformación completada exitosamente",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      }
    ],
    "LOAD": [
      {
        "code": 200,
        "status": "success",
        "process": "L001",
        "message": "Carga completada exitosamente",
        "dateTime": "2025-02-04T17:32:05.740+00:00"
      }
    ]
  }
}
```

#### Descripción de la Respuesta Exitosa

| Campo                        | Description                              |
| ---------------------------- | ---------------------------------------- |
| `code`                       | Código de respuesta (200 = éxito)        |
| `status`                     | Estado del proceso                       |
| `process`                    | Código del proceso principal             |
| `message`                    | Mensaje descriptivo del resultado        |
| `syncId`                     | ID de sincronización                     |
| `data`                       | Objeto con los resultados de cada fase   |
| `data.EXTRACTS`              | Array con resultados de extracciones     |
| `data.EXTRACTS[].code`       | Código de respuesta de la extracción     |
| `data.EXTRACTS[].status`     | Estado de la extracción                  |
| `data.EXTRACTS[].process`    | Código del proceso de extracción         |
| `data.EXTRACTS[].message`    | Mensaje del resultado                    |
| `data.EXTRACTS[].dateTime`   | Fecha y hora de ejecución                |
| `data.TRANSFORMS`            | Array con resultados de transformaciones |
| `data.TRANSFORMS[].code`     | Código de respuesta de la transformación |
| `data.TRANSFORMS[].status`   | Estado de la transformación              |
| `data.TRANSFORMS[].process`  | Código del proceso de transformación     |
| `data.TRANSFORMS[].message`  | Mensaje del resultado                    |
| `data.TRANSFORMS[].dateTime` | Fecha y hora de ejecución                |
| `data.LOAD`                  | Array con resultados de cargas           |
| `data.LOAD[].code`           | Código de respuesta de la carga          |
| `data.LOAD[].status`         | Estado de la carga                       |
| `data.LOAD[].process`        | Código del proceso de carga              |
| `data.LOAD[].message`        | Mensaje del resultado                    |
| `data.LOAD[].dateTime`       | Fecha y hora de ejecución                |

#### 500 Internal Server Error - Error en el Proceso

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

#### Descripción de la Respuesta de Error

| Campo                      | Description                                      |
| -------------------------- | ------------------------------------------------ |
| `code`                     | Código de error (500 = error del servidor)       |
| `status`                   | Estado del proceso (error)                       |
| `process`                  | Código del proceso principal                     |
| `message`                  | Mensaje descriptivo del error                    |
| `syncId`                   | ID de sincronización                             |
| `data`                     | Objeto con los resultados de cada fase           |
| `data.EXTRACTS`            | Array con resultados de extracciones fallidas    |
| `data.EXTRACTS[].code`     | Código de error de la extracción                 |
| `data.EXTRACTS[].status`   | Estado de error                                  |
| `data.EXTRACTS[].process`  | Código del proceso de extracción                 |
| `data.EXTRACTS[].message`  | Mensaje de error detallado                       |
| `data.EXTRACTS[].dateTime` | Fecha y hora del error                           |
| `data.TRANSFORMS`          | Array vacío si no se ejecutaron transformaciones |
| `data.LOAD`                | Array vacío si no se ejecutaron cargas           |

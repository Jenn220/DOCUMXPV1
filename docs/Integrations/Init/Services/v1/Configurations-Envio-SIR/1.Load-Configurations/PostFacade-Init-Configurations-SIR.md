## Ejecutar Flujo de Integración - Configuración de Servicios SIR

### Método HTTP

`POST`

### URL

```
{{init}}/api/v1/facade
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
  "code": "I0010",
  "withResponse": true,
  "chunkLoad": 0,
  "syncId": "06ef59e7-eec7-4985-ba34-6afd70acae4f",
  "country": "ECU",
  "franchise_id": 9,
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
              "name": "mxp_v2.USP_InterfaceSIR_JSON",
              "properties": [],
              "filters": []
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
                  "name": "entity_name",
                  "operator": "equals",
                  "value": "Cadena"
                },
                {
                  "name": "franchise_id",
                  "operator": "equals",
                  "value": "{{legacy_cdn_id}}"
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
                  "value": "Pais"
                },
                {
                  "name": "id_v1",
                  "operator": "equals",
                  "value": "1"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T131",
        "syncId": "06ef59e7-eec7-4985-ba34-6afd70acae4f",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
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
            "repository": "DEV_KFC_MXPi_Settings",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "sir_service_configuration",
              "toName": "Settings_BO_SIR_Service_Configuration_test",
              "properties": [
                {
                  "fromName": "country_id",
                  "fromType": "",
                  "toName": "country_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "cdn_id",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "server",
                  "fromType": "",
                  "toName": "server",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "path",
                  "fromType": "",
                  "toName": "path",
                  "toType": "",
                  "defaultValue": ""
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

### Descripción del Cuerpo de la Solicitud

| Campo                                                                  | Tipo    | Descripción                                          |
| ---------------------------------------------------------------------- | ------- | ---------------------------------------------------- |
| `code`                                                                 | string  | Código del flujo de integración                      |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta            |
| `chunkLoad`                                                            | number  | Número de fragmento de carga                         |
| `syncId`                                                               | string  | ID UUID de sincronización                            |
| `country`                                                              | string  | Código del país                                      |
| `franchise_id`                                                         | number  | ID de la franquicia                                  |
| `processes`                                                            | object  | Objeto con los procesos a ejecutar                   |
| `processes.EXTRACTS`                                                   | array   | Lista de procesos de extracción                      |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                     |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Indica si retorna respuesta                          |
| `processes.EXTRACTS[].withCache`                                       | boolean | Indica si utiliza caché                              |
| `processes.EXTRACTS[].syncId`                                          | string  | ID de sincronización                                 |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración del proceso                            |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Configuración de conexión                            |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos o URL                      |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                   |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                  |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                               |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre del repositorio o base de datos               |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Tipo de adaptador de conexión                        |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Lista de entidades a extraer                         |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre del stored procedure o colección              |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Lista de propiedades a extraer                       |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                               |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                         |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Lista de filtros para la extracción                  |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del parámetro                                 |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                              |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del parámetro                                  |
| `processes.TRANSFORMS`                                                 | array   | Lista de procesos de transformación                  |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación                 |
| `processes.TRANSFORMS[].syncId`                                        | string  | ID de sincronización                                 |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Indica si retorna respuesta                          |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Indica si utiliza caché                              |
| `processes.TRANSFORMS[].country`                                       | string  | Código del país                                      |
| `processes.LOADS`                                                      | array   | Lista de procesos de carga                           |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                          |
| `processes.LOADS[].withResponse`                                       | boolean | Indica si retorna respuesta                          |
| `processes.LOADS[].withCache`                                          | boolean | Indica si utiliza caché                              |
| `processes.LOADS[].syncId`                                             | string  | ID de sincronización                                 |
| `processes.LOADS[].configuration`                                      | object  | Configuración del proceso de carga                   |
| `processes.LOADS[].configuration.connection`                           | object  | Configuración de conexión a base de datos            |
| `processes.LOADS[].configuration.connection.server`                    | string  | Servidor de base de datos                            |
| `processes.LOADS[].configuration.connection.port`                      | string  | Puerto de conexión                                   |
| `processes.LOADS[].configuration.connection.user`                      | string  | Usuario de conexión                                  |
| `processes.LOADS[].configuration.connection.password`                  | string  | Contraseña de conexión                               |
| `processes.LOADS[].configuration.connection.repository`                | string  | Nombre de la base de datos                           |
| `processes.LOADS[].configuration.connection.adapter`                   | string  | Tipo de adaptador de base de datos                   |
| `processes.LOADS[].configuration.entities`                             | array   | Lista de entidades de destino para la carga          |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad extraída                        |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad a cargar                        |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Lista de propiedades a mapear                        |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre de la propiedad extraída                      |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato de origen                               |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre de la propiedad a cargar                      |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato de destino                              |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto (vacío usa el valor de extracción) |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Especifica si es valor único y valida duplicidad     |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                         |

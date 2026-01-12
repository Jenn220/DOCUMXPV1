## Ejecutar Proceso ETL Facade para Catálogo de Dispositivos de Imágenes de PLU MXPv2

### Método HTTP

`POST`

### URL

```
{{server_init}}/api/v1/facade
```

### Autenticación

**Tipo:** Bearer Token

| Token       |
| ----------- |
| `{{token}}` |

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
                  "value": "catalog_mxpv2_device_images_plu"
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
                  "value": "mxp_v2.View_Device_Images_PLU"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T024",
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
            "repository": "UAT_KFC_BO_Menus",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "catalog_mxpv2_device_images_plu",
              "toName": "Menus_BO_Devices_Images_PLU",
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
                  "fromName": "device_name",
                  "fromType": "",
                  "toName": "device_name",
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
                  "fromName": "user_id",
                  "fromType": "",
                  "toName": "user_id",
                  "toType": "uuid",
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

### Descripción de Campos del Cuerpo

| Campo                                                                  | Tipo    | Description                                                    |
| ---------------------------------------------------------------------- | ------- | -------------------------------------------------------------- |
| `code`                                                                 | string  | Código del proceso facade (F100)                               |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta                      |
| `withCache`                                                            | boolean | Especifica si desea guardar la respuesta en cache              |
| `syncId`                                                               | string  | ID UUID de sincronización                                      |
| `processes`                                                            | object  | Objeto con los procesos ETL                                    |
| `processes.EXTRACTS`                                                   | array   | Array de procesos de extracción                                |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción (E001/E002)                   |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Devolver respuesta de extracción                               |
| `processes.EXTRACTS[].withCache`                                       | boolean | Guardar en cache                                               |
| `processes.EXTRACTS[].syncId`                                          | string  | ID de sincronización                                           |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración de extracción                                    |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Configuración de conexión                                      |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                                      |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                             |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                            |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                                         |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos                                     |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Tipo de adaptador (SqlServerSP/Mongo)                          |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Array de entidades a extraer                                   |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la entidad (mxp_v2.USP_Catalog_Data_MXPLegacy/uuids) |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Propiedades de la entidad                                      |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                                         |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                                   |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Filtros para la extracción                                     |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del campo a filtrar                                     |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                                        |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del filtro                                               |
| `processes.TRANSFORMS`                                                 | array   | Array de procesos de transformación                            |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación (T024)                    |
| `processes.TRANSFORMS[].syncId`                                        | string  | ID de sincronización                                           |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Devolver respuesta de transformación                           |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Guardar en cache                                               |
| `processes.TRANSFORMS[].country`                                       | string  | Código de país                                                 |
| `processes.LOADS`                                                      | array   | Array de procesos de carga                                     |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga (L001)                             |
| `processes.LOADS[].withCache`                                          | boolean | Guardar en cache                                               |
| `processes.LOADS[].withResponse`                                       | boolean | Devolver respuesta de carga                                    |
| `processes.LOADS[].syncId`                                             | string  | ID de sincronización                                           |
| `processes.LOADS[].configuration`                                      | object  | Configuración de carga                                         |
| `processes.LOADS[].configuration.connection`                           | object  | Configuración de conexión destino                              |
| `processes.LOADS[].configuration.entities`                             | array   | Array de entidades a cargar                                    |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad extraída                                  |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la colección destino                                 |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Mapeo de propiedades                                           |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre de la propiedad origen                                  |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato origen                                            |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre de la propiedad destino                                 |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato destino                                           |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto                                              |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Indica si es clave primaria                                    |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                                   |
| `processes.PUBLISHERS`                                                 | array   | Array de procesos de publicación                               |

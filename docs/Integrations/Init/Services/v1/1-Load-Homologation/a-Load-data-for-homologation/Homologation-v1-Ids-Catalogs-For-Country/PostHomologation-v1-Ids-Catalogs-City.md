## Ejecutar Proceso ETL Facade para Ciudades con Cache

### Método HTTP

`POST`

### URL

```
{{server_init}}/api/v1/facade
```

### Autenticación

**Tipo:** Bearer Token

**Header:**

```
Authorization: Bearer {{token}}
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "H000",
  "withResponse": false,
  "withCache": true,
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
            "server": "{{server_legacy}}",
            "port": "",
            "user": "{{user_legacy}}",
            "password": "{{pass_legacy}}",
            "repository": "{{repository_legacy}}",
            "adapter": "SqlServer"
          },
          "entities": [
            {
              "name": "Ciudad",
              "properties": [
                {
                  "name": "ciu_id",
                  "type": "base64"
                }
              ],
              "filters": []
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
        "code": "01",
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

### Descripción de Campos del Cuerpo

| Campo                                                                  | Tipo    | Description                                                           |
| ---------------------------------------------------------------------- | ------- | --------------------------------------------------------------------- |
| `code`                                                                 | string  | Código de la homologación                                             |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta                             |
| `withCache`                                                            | boolean | Especifica si desea guardar la respuesta en cache (true en este caso) |
| `syncId`                                                               | string  | ID UUID de sincronización                                             |
| `country`                                                              | string  | Código de país (3 dígitos)                                            |
| `franchise_id`                                                         | number  | ID de la cadena del MXP legacy                                        |
| `processes`                                                            | object  | Objeto con los procesos ETL                                           |
| `processes.EXTRACTS`                                                   | array   | Array de procesos de extracción                                       |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                                      |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Devolver respuesta de extracción                                      |
| `processes.EXTRACTS[].withCache`                                       | boolean | Guardar en cache                                                      |
| `processes.EXTRACTS[].syncId`                                          | string  | ID de sincronización                                                  |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración de extracción                                           |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Configuración de conexión                                             |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                                             |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                                    |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                                   |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                                                |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos                                            |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Tipo de adaptador (SqlServer/Mongo)                                   |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Array de entidades a extraer                                          |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la entidad (Ciudad)                                         |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Propiedades de la entidad                                             |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string  | Nombre de la propiedad                                                |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string  | Tipo de dato de la propiedad                                          |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Filtros para la extracción (vacío en este caso)                       |
| `processes.TRANSFORMS`                                                 | array   | Array de procesos de transformación                                   |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación                                  |
| `processes.TRANSFORMS[].syncId`                                        | string  | ID de sincronización                                                  |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Devolver respuesta de transformación                                  |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Guardar en cache                                                      |
| `processes.TRANSFORMS[].country`                                       | string  | Código de país                                                        |
| `processes.LOADS`                                                      | array   | Array de procesos de carga                                            |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                                           |
| `processes.LOADS[].withCache`                                          | boolean | Guardar en cache                                                      |
| `processes.LOADS[].withResponse`                                       | boolean | Devolver respuesta de carga                                           |
| `processes.LOADS[].syncId`                                             | string  | ID de sincronización                                                  |
| `processes.LOADS[].configuration`                                      | object  | Configuración de carga                                                |
| `processes.LOADS[].configuration.connection`                           | object  | Configuración de conexión destino                                     |
| `processes.LOADS[].configuration.entities`                             | array   | Array de entidades a cargar                                           |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad extraída                                         |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad a cargar                                         |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Mapeo de propiedades                                                  |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre de la propiedad origen                                         |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato origen                                                   |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre de la propiedad destino                                        |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato destino                                                  |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto                                                     |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Indica si es clave primaria                                           |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                                          |
| `processes.PUBLISHERS`                                                 | array   | Array de procesos de publicación                                      |

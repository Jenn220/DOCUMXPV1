## Ejecutar Flujo de Integración - Medios de Venta de Productos

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
  "code": "F100",
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
            "server": "{{server_legacy}}",
            "port": "",
            "user": "{{user_legacy}}",
            "password": "{{pass_legacy}}",
            "repository": "{{repository_legacy}}",
            "adapter": "SqlServer"
          },
          "entities": [
            {
              "name": "mxp_v2.Medio_Venta",
              "properties": [],
              "filters": []
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T129",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
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
            "repository": "DEV_KFC_MXPi_Settings",
            "adapter": "{{adapter_mongo}}"
          },
          "entities": [
            {
              "name": "plu_means_sale",
              "toName": "Pub_Sale_Sale_Product_Means",
              "properties": [
                {
                  "fromName": "legacy_medio_canal_menu_id",
                  "fromType": "",
                  "toName": "legacy_medio_canal_menu_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "legacy_medio_venta_id",
                  "fromType": "",
                  "toName": "legacy_medio_venta_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "half_integration_name",
                  "fromType": "",
                  "toName": "half_integration_name",
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

| Campo                                                                  | Tipo    | Descripción                                               |
| ---------------------------------------------------------------------- | ------- | --------------------------------------------------------- |
| `code`                                                                 | string  | Código del flujo de integración                           |
| `withResponse`                                                         | boolean | Especifica si desea devolver la respuesta                 |
| `withCache`                                                            | boolean | Especifica si desea guardar la respuesta en caché (mongo) |
| `syncId`                                                               | string  | ID UUID de sincronización                                 |
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
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la tabla/vista a extraer                        |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Lista de propiedades a extraer                            |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Lista de filtros para la extracción                       |
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
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                              |
| `processes.PUBLISHERS`                                                 | array   | Lista de procesos de publicación                          |

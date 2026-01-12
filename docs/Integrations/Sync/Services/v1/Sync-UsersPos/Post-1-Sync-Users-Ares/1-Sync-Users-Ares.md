## Ejecutar Sincronización de Datos con Filtros

### Método HTTP

`POST`

### URL

```
{{server_sync}}/api/v1/facade
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
  "code": "F008",
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "chunkLoad": 100,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E001",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo_qa}}",
            "port": "",
            "user": "{{user_mongo_qa}}",
            "password": "{{pass_mongo_qa}}",
            "repository": "QA_KFC_MXPi_Settings",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Settings_BO_Users_Pos",
              "properties": [],
              "filters": [
                {
                  "name": "user_pos_profiles.franchises.franchise_name",
                  "operator": "equals",
                  "value": "GUS"
                },
                {
                  "name": "user_pos_profiles.franchises.restaurants.restaurant_name",
                  "operator": "equals",
                  "value": "G002"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T121",
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
            "server": "192.168.101.13",
            "port": "27020",
            "user": "admin",
            "password": "admin123",
            "repository": "MXPi_ARES_Validate_Tenant",
            "adapter": "MongoLocal"
          },
          "entities": [
            {
              "name": "users_ares_for_restaurant",
              "toName": "Ares_Users_Pos",
              "properties": [
                {
                  "fromName": "_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "uuid",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "Account",
                  "fromType": "",
                  "toName": "Account",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "Password",
                  "fromType": "",
                  "toName": "Password",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "Resources",
                  "fromType": "",
                  "toName": "Resources",
                  "toType": "array",
                  "defaultValue": ""
                },
                {
                  "fromName": "IsActive",
                  "fromType": "",
                  "toName": "IsActive",
                  "toType": "",
                  "defaultValue": ""
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

| Campo                                                                  | Tipo    | Descripción                                          |
| ---------------------------------------------------------------------- | ------- | ---------------------------------------------------- |
| `code`                                                                 | string  | Código de la fachada de sincronización               |
| `syncId`                                                               | string  | Identificador único de sincronización                |
| `chunkLoad`                                                            | number  | Tamaño de lote para carga de datos                   |
| `processes`                                                            | object  | Objeto contenedor de los procesos ETL                |
| `processes.EXTRACTS`                                                   | array   | Lista de procesos de extracción de datos             |
| `processes.EXTRACTS[].code`                                            | string  | Código del proceso de extracción                     |
| `processes.EXTRACTS[].syncId`                                          | string  | Identificador de sincronización del proceso          |
| `processes.EXTRACTS[].withResponse`                                    | boolean | Indica si debe retornar respuesta                    |
| `processes.EXTRACTS[].withCache`                                       | boolean | Indica si debe usar caché                            |
| `processes.EXTRACTS[].configuration`                                   | object  | Configuración del proceso de extracción              |
| `processes.EXTRACTS[].configuration.connection`                        | object  | Información de conexión a la base de datos           |
| `processes.EXTRACTS[].configuration.connection.server`                 | string  | Servidor de base de datos                            |
| `processes.EXTRACTS[].configuration.connection.port`                   | string  | Puerto de conexión                                   |
| `processes.EXTRACTS[].configuration.connection.user`                   | string  | Usuario de conexión                                  |
| `processes.EXTRACTS[].configuration.connection.password`               | string  | Contraseña de conexión                               |
| `processes.EXTRACTS[].configuration.connection.repository`             | string  | Nombre de la base de datos o repositorio             |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string  | Adaptador de base de datos (Mongo, MongoLocal, etc.) |
| `processes.EXTRACTS[].configuration.entities`                          | array   | Lista de entidades a extraer                         |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string  | Nombre de la entidad                                 |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array   | Propiedades de la entidad                            |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array   | Filtros aplicados a la entidad                       |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string  | Nombre del campo a filtrar                           |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string  | Operador de comparación                              |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string  | Valor del filtro                                     |
| `processes.TRANSFORMS`                                                 | array   | Lista de procesos de transformación                  |
| `processes.TRANSFORMS[].code`                                          | string  | Código del proceso de transformación                 |
| `processes.TRANSFORMS[].syncId`                                        | string  | Identificador de sincronización del proceso          |
| `processes.TRANSFORMS[].withResponse`                                  | boolean | Indica si debe retornar respuesta                    |
| `processes.TRANSFORMS[].withCache`                                     | boolean | Indica si debe usar caché                            |
| `processes.TRANSFORMS[].country`                                       | string  | Código del país para la transformación               |
| `processes.LOADS`                                                      | array   | Lista de procesos de carga de datos                  |
| `processes.LOADS[].code`                                               | string  | Código del proceso de carga                          |
| `processes.LOADS[].withCache`                                          | boolean | Indica si debe usar caché                            |
| `processes.LOADS[].withResponse`                                       | boolean | Indica si debe retornar respuesta                    |
| `processes.LOADS[].syncId`                                             | string  | Identificador de sincronización del proceso          |
| `processes.LOADS[].configuration`                                      | object  | Configuración del proceso de carga                   |
| `processes.LOADS[].configuration.connection`                           | object  | Información de conexión a la base de datos destino   |
| `processes.LOADS[].configuration.connection.server`                    | string  | Servidor de base de datos destino                    |
| `processes.LOADS[].configuration.connection.port`                      | string  | Puerto de conexión                                   |
| `processes.LOADS[].configuration.connection.user`                      | string  | Usuario de conexión                                  |
| `processes.LOADS[].configuration.connection.password`                  | string  | Contraseña de conexión                               |
| `processes.LOADS[].configuration.connection.repository`                | string  | Nombre de la base de datos destino                   |
| `processes.LOADS[].configuration.connection.adapter`                   | string  | Adaptador de base de datos                           |
| `processes.LOADS[].configuration.entities`                             | array   | Lista de entidades a cargar                          |
| `processes.LOADS[].configuration.entities[].name`                      | string  | Nombre de la entidad origen                          |
| `processes.LOADS[].configuration.entities[].toName`                    | string  | Nombre de la entidad destino                         |
| `processes.LOADS[].configuration.entities[].properties`                | array   | Mapeo de propiedades entre origen y destino          |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string  | Nombre del campo origen                              |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string  | Tipo de dato origen                                  |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string  | Nombre del campo destino                             |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string  | Tipo de dato destino                                 |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string  | Valor por defecto del campo                          |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string  | Indica si es clave primaria                          |
| `processes.LOADS[].dataInput`                                          | object  | Datos de entrada adicionales                         |
| `processes.PUBLISHERS`                                                 | array   | Lista de procesos de publicación                     |

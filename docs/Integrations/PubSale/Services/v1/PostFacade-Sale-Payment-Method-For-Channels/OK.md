## Ejecutar Flujo de Integración - Métodos de Pago por Canales

### Método HTTP

`POST`

### URL

```
{{server_pub_sale}}/api/v1/facade
```

### Autenticación

| Tipo         | Token              |
| ------------ | ------------------ |
| Bearer Token | `{{token_legacy}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "F100",
  "withResponse": false,
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
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "DEV_KFC_POS_PurchaseOrders",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "PurchaseOrders_POS_Order",
              "properties": [],
              "filters": []
            }
          ]
        }
      },
      {
        "code": "E002",
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
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Settings_BO_Method_Payment_SIR",
              "properties": [],
              "filters": []
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T087",
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
            "repository": "QA_KFC_MXPi_PubSale",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "sale_method_for_channels",
              "toName": "Pub_Sale_Sale_Payment_Method_For_Channels",
              "properties": [
                {
                  "fromName": "cdn_id",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "restaurant_id",
                  "fromType": "",
                  "toName": "restaurant_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "period_id",
                  "fromType": "",
                  "toName": "period_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "start_date",
                  "fromType": "",
                  "toName": "start_date",
                  "toType": "string",
                  "defaultValue": ""
                },
                {
                  "fromName": "final_date",
                  "fromType": "",
                  "toName": "final_date",
                  "toType": "string",
                  "defaultValue": ""
                },
                {
                  "fromName": "sales",
                  "fromType": "",
                  "toName": "sales",
                  "toType": "array",
                  "defaultValue": [
                    {
                      "fromName": "means_of_sale",
                      "fromType": "",
                      "toName": "means_of_sale",
                      "toType": "",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "payment_method_id",
                      "fromType": "",
                      "toName": "payment_method_id",
                      "toType": "uuid",
                      "defaultValue": ""
                    },
                    {
                      "fromName": "payment_method",
                      "fromType": "",
                      "toName": "payment_method",
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
                      "fromName": "transactions",
                      "fromType": "",
                      "toName": "transactions",
                      "toType": "",
                      "defaultValue": ""
                    }
                  ]
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

| Campo                                                                  | Tipo         | Descripción                                                               |
| ---------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------- |
| `code`                                                                 | string       | Código del flujo de integración                                           |
| `withResponse`                                                         | boolean      | Especifica si desea devolver la respuesta                                 |
| `syncId`                                                               | string       | ID UUID de sincronización                                                 |
| `processes`                                                            | object       | Objeto con los procesos a ejecutar                                        |
| `processes.EXTRACTS`                                                   | array        | Lista de procesos de extracción                                           |
| `processes.EXTRACTS[].code`                                            | string       | Código del proceso de extracción                                          |
| `processes.EXTRACTS[].withResponse`                                    | boolean      | Indica si retorna respuesta                                               |
| `processes.EXTRACTS[].withCache`                                       | boolean      | Indica si utiliza caché                                                   |
| `processes.EXTRACTS[].syncId`                                          | string       | ID de sincronización                                                      |
| `processes.EXTRACTS[].configuration`                                   | object       | Configuración del proceso                                                 |
| `processes.EXTRACTS[].configuration.connection`                        | object       | Configuración de conexión                                                 |
| `processes.EXTRACTS[].configuration.connection.server`                 | string       | Servidor de base de datos                                                 |
| `processes.EXTRACTS[].configuration.connection.port`                   | string       | Puerto de conexión                                                        |
| `processes.EXTRACTS[].configuration.connection.user`                   | string       | Usuario de conexión                                                       |
| `processes.EXTRACTS[].configuration.connection.password`               | string       | Contraseña de conexión                                                    |
| `processes.EXTRACTS[].configuration.connection.repository`             | string       | Nombre de la base de datos                                                |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string       | Tipo de adaptador de conexión                                             |
| `processes.EXTRACTS[].configuration.entities`                          | array        | Lista de entidades a extraer                                              |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string       | Nombre de la colección                                                    |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array        | Lista de propiedades a extraer                                            |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array        | Lista de filtros para la extracción                                       |
| `processes.TRANSFORMS`                                                 | array        | Lista de procesos de transformación                                       |
| `processes.TRANSFORMS[].code`                                          | string       | Código del proceso de transformación                                      |
| `processes.TRANSFORMS[].syncId`                                        | string       | ID de sincronización                                                      |
| `processes.TRANSFORMS[].withResponse`                                  | boolean      | Indica si retorna respuesta                                               |
| `processes.TRANSFORMS[].withCache`                                     | boolean      | Indica si utiliza caché                                                   |
| `processes.TRANSFORMS[].country`                                       | string       | Código del país                                                           |
| `processes.LOADS`                                                      | array        | Lista de procesos de carga                                                |
| `processes.LOADS[].code`                                               | string       | Código del proceso de carga                                               |
| `processes.LOADS[].withCache`                                          | boolean      | Indica si utiliza caché                                                   |
| `processes.LOADS[].withResponse`                                       | boolean      | Indica si retorna respuesta                                               |
| `processes.LOADS[].syncId`                                             | string       | ID de sincronización                                                      |
| `processes.LOADS[].configuration`                                      | object       | Configuración del proceso de carga                                        |
| `processes.LOADS[].configuration.connection`                           | object       | Configuración de conexión a base de datos                                 |
| `processes.LOADS[].configuration.connection.server`                    | string       | Servidor de base de datos                                                 |
| `processes.LOADS[].configuration.connection.port`                      | string       | Puerto de conexión                                                        |
| `processes.LOADS[].configuration.connection.user`                      | string       | Usuario de conexión                                                       |
| `processes.LOADS[].configuration.connection.password`                  | string       | Contraseña de conexión                                                    |
| `processes.LOADS[].configuration.connection.repository`                | string       | Nombre de la base de datos                                                |
| `processes.LOADS[].configuration.connection.adapter`                   | string       | Tipo de adaptador de base de datos                                        |
| `processes.LOADS[].configuration.entities`                             | array        | Lista de entidades de destino para la carga                               |
| `processes.LOADS[].configuration.entities[].name`                      | string       | Nombre de la entidad extraída                                             |
| `processes.LOADS[].configuration.entities[].toName`                    | string       | Nombre de la entidad a cargar                                             |
| `processes.LOADS[].configuration.entities[].properties`                | array        | Lista de propiedades a mapear                                             |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string       | Nombre de la propiedad extraída                                           |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string       | Tipo de dato de origen                                                    |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string       | Nombre de la propiedad a cargar                                           |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string       | Tipo de dato de destino                                                   |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string/array | Valor por defecto (vacío usa el valor de extracción) o estructura anidada |
| `processes.LOADS[].dataInput`                                          | object       | Datos de entrada adicionales                                              |
| `processes.PUBLISHERS`                                                 | array        | Lista de procesos de publicación                                          |

### Respuestas del Servidor

#### 200 OK - Integración Exitosa

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

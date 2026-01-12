## Ejecutar Flujo de Integración - Facturación Electrónica

### Método HTTP

`POST`

### URL

```
{{server_pub}}/api/v1/facade
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
  "code": "F008",
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "chunkLoad": 1,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E001",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "QA_KFC_POS_PurchaseOrders",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "PurchaseOrders_POS_Order",
              "properties": [],
              "filters": [
                {
                  "name": "invoice.fe_authorization_status.estado",
                  "operator": "not_in",
                  "value": ["A", "RC", "XA", "DR", "ERROR ENVIO", "ENVIADO"]
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E0122",
        "withResponse": true,
        "withCache": false,
        "syncId": "00000000-0000-0000-0000-000000000000",
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "UAT_KFC_MXP_Integrations",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Integration_Catalog",
              "properties": [],
              "filters": [
                {
                  "name": "father_code",
                  "operator": "in",
                  "value": [350, 351, 352, 353, 354, 355, 356]
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T081",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
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
            "server": "https://testapi.seedbilling.cl",
            "port": "9701",
            "user": "",
            "password": "",
            "repository": "/api/kfc/ingresarComprobante",
            "adapter": "RestSingleDev"
          },
          "entities": [
            {
              "name": "documents",
              "toName": "documents",
              "properties": [
                {
                  "fromName": "pSuscriptor",
                  "fromType": "",
                  "toName": "pSuscriptor",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pToken",
                  "fromType": "",
                  "toName": "pToken",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pEmpresa",
                  "fromType": "",
                  "toName": "pEmpresa",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pEstablecimiento",
                  "fromType": "",
                  "toName": "pEstablecimiento",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pPuntoEmision",
                  "fromType": "",
                  "toName": "pPuntoEmision",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pTipoDocumento",
                  "fromType": "",
                  "toName": "pTipoDocumento",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pDocumento",
                  "fromType": "",
                  "toName": "pDocumento",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "pPaisOrigen",
                  "fromType": "",
                  "toName": "pPaisOrigen",
                  "toType": "",
                  "defaultValue": ""
                }
              ]
            }
          ]
        },
        "dataInput": {}
      },
      {
        "code": "L002",
        "withCache": false,
        "withResponse": true,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "QA_KFC_POS_PurchaseOrders",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "update",
              "toName": "PurchaseOrders_POS_Order",
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
                  "fromName": "invoice",
                  "fromType": "",
                  "toName": "invoice",
                  "toType": "array",
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

| Campo                                                                  | Tipo         | Descripción                                          |
| ---------------------------------------------------------------------- | ------------ | ---------------------------------------------------- |
| `code`                                                                 | string       | Código del flujo de integración                      |
| `syncId`                                                               | string       | ID UUID de sincronización                            |
| `chunkLoad`                                                            | number       | Número de fragmento de carga                         |
| `processes`                                                            | object       | Objeto con los procesos a ejecutar                   |
| `processes.EXTRACTS`                                                   | array        | Lista de procesos de extracción                      |
| `processes.EXTRACTS[].code`                                            | string       | Código del proceso de extracción                     |
| `processes.EXTRACTS[].syncId`                                          | string       | ID de sincronización                                 |
| `processes.EXTRACTS[].withResponse`                                    | boolean      | Indica si retorna respuesta                          |
| `processes.EXTRACTS[].withCache`                                       | boolean      | Indica si utiliza caché                              |
| `processes.EXTRACTS[].configuration`                                   | object       | Configuración del proceso                            |
| `processes.EXTRACTS[].configuration.connection`                        | object       | Configuración de conexión                            |
| `processes.EXTRACTS[].configuration.connection.server`                 | string       | Servidor de base de datos                            |
| `processes.EXTRACTS[].configuration.connection.port`                   | string       | Puerto de conexión                                   |
| `processes.EXTRACTS[].configuration.connection.user`                   | string       | Usuario de conexión                                  |
| `processes.EXTRACTS[].configuration.connection.password`               | string       | Contraseña de conexión                               |
| `processes.EXTRACTS[].configuration.connection.repository`             | string       | Nombre de la base de datos                           |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string       | Tipo de adaptador de conexión                        |
| `processes.EXTRACTS[].configuration.entities`                          | array        | Lista de entidades a extraer                         |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string       | Nombre de la colección                               |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array        | Lista de propiedades a extraer                       |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array        | Lista de filtros para la extracción                  |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string       | Nombre del parámetro                                 |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string       | Operador de comparación                              |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | array/number | Valor o lista de valores del parámetro               |
| `processes.TRANSFORMS`                                                 | array        | Lista de procesos de transformación                  |
| `processes.TRANSFORMS[].code`                                          | string       | Código del proceso de transformación                 |
| `processes.TRANSFORMS[].syncId`                                        | string       | ID de sincronización                                 |
| `processes.TRANSFORMS[].withResponse`                                  | boolean      | Indica si retorna respuesta                          |
| `processes.TRANSFORMS[].withCache`                                     | boolean      | Indica si utiliza caché                              |
| `processes.TRANSFORMS[].country`                                       | string       | Código del país                                      |
| `processes.LOADS`                                                      | array        | Lista de procesos de carga                           |
| `processes.LOADS[].code`                                               | string       | Código del proceso de carga                          |
| `processes.LOADS[].withCache`                                          | boolean      | Indica si utiliza caché                              |
| `processes.LOADS[].withResponse`                                       | boolean      | Indica si retorna respuesta                          |
| `processes.LOADS[].syncId`                                             | string       | ID de sincronización                                 |
| `processes.LOADS[].configuration`                                      | object       | Configuración del proceso de carga                   |
| `processes.LOADS[].configuration.connection`                           | object       | Configuración de conexión                            |
| `processes.LOADS[].configuration.connection.server`                    | string       | URL del servidor                                     |
| `processes.LOADS[].configuration.connection.port`                      | string       | Puerto de conexión                                   |
| `processes.LOADS[].configuration.connection.user`                      | string       | Usuario de conexión                                  |
| `processes.LOADS[].configuration.connection.password`                  | string       | Contraseña de conexión                               |
| `processes.LOADS[].configuration.connection.repository`                | string       | Ruta del endpoint o nombre de base de datos          |
| `processes.LOADS[].configuration.connection.adapter`                   | string       | Tipo de adaptador de conexión                        |
| `processes.LOADS[].configuration.entities`                             | array        | Lista de entidades de destino para la carga          |
| `processes.LOADS[].configuration.entities[].name`                      | string       | Nombre de la entidad extraída                        |
| `processes.LOADS[].configuration.entities[].toName`                    | string       | Nombre de la entidad a cargar                        |
| `processes.LOADS[].configuration.entities[].properties`                | array        | Lista de propiedades a mapear                        |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string       | Nombre de la propiedad extraída                      |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string       | Tipo de dato de origen                               |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string       | Nombre de la propiedad a cargar                      |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string       | Tipo de dato de destino                              |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string       | Valor por defecto (vacío usa el valor de extracción) |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string       | Especifica si es valor único y valida duplicidad     |
| `processes.LOADS[].dataInput`                                          | object       | Datos de entrada adicionales                         |
| `processes.PUBLISHERS`                                                 | array        | Lista de procesos de publicación                     |

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

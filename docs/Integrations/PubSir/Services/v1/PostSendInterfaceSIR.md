## Ejecutar Flujo de Integración - Procesamiento de Ventas SIR

### Método HTTP

`POST`

### URL

```
{{server_pub_sir}}/api/v1/facade
```

### Autenticación

No requiere autenticación.

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "F100",
  "withResponse": true,
  "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "country": "ECU",
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
            "repository": "{{repository_mongo_hml}}",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "uuids",
              "properties": [],
              "filters": [
                {
                  "name": "id_v2",
                  "operator": "equals",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
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
            "repository": "QA_KFC_MXPi_PubSale",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Pub_Sale_Cash_Closure",
              "properties": [],
              "filters": [
                {
                  "name": "period_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "8bda8c52-e2fb-44ff-9a2c-97c630f3f14c"
                },
                {
                  "name": "restaurant_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
                },
                {
                  "name": "start_date",
                  "operator": "equals",
                  "value": "29/08/2025"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E003",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
              "name": "Pub_Sale_Hourly_Sale",
              "properties": [],
              "filters": [
                {
                  "name": "period_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "8bda8c52-e2fb-44ff-9a2c-97c630f3f14c"
                },
                {
                  "name": "restaurant_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
                },
                {
                  "name": "start_date",
                  "operator": "equals",
                  "value": "29/08/2025"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E004",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
              "name": "Pub_Sale_Sale_Payment_Method",
              "properties": [],
              "filters": [
                {
                  "name": "period_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "8bda8c52-e2fb-44ff-9a2c-97c630f3f14c"
                },
                {
                  "name": "restaurant_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
                },
                {
                  "name": "start_date",
                  "operator": "equals",
                  "value": "29/08/2025"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E005",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
              "name": "Pub_Sale_Sale_Product",
              "properties": [],
              "filters": [
                {
                  "name": "period_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "8bda8c52-e2fb-44ff-9a2c-97c630f3f14c"
                },
                {
                  "name": "restaurant_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
                },
                {
                  "name": "start_date",
                  "operator": "equals",
                  "value": "29/08/2025"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E006",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
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
              "name": "Pub_Sale_Sale_Payment_Method_For_Channels",
              "properties": [],
              "filters": [
                {
                  "name": "period_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "8bda8c52-e2fb-44ff-9a2c-97c630f3f14c"
                },
                {
                  "name": "restaurant_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40"
                },
                {
                  "name": "start_date",
                  "operator": "equals",
                  "value": "29/08/2025"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E007",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "QA_KFC_MXPi_Settings",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Pub_Sale_Sale_Product_Means",
              "properties": [],
              "filters": []
            }
          ]
        }
      },
      {
        "code": "E008",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "QA_KFC_MXPi_Settings",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Pub_Sale_Sale_Product_Num",
              "properties": [],
              "filters": [
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af"
                }
              ]
            }
          ]
        }
      },
      {
        "code": "E009",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "{{server_mongo}}",
            "port": "",
            "user": "{{user_mongo}}",
            "password": "{{pass_mongo}}",
            "repository": "QA_KFC_MXPi_Settings",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "Settings_BO_Method_Payment_SIR",
              "properties": [],
              "filters": [
                {
                  "name": "method_payment",
                  "operator": "in",
                  "value": [
                    "ALIA",
                    "AMERICAN EXPRES",
                    "CAJA CHICA OTROS",
                    "CAMPAÑA SOLIDARIA",
                    "CHEQUES",
                    "CORTESIAS",
                    "CREDITO SC",
                    "CUENTAS COBRAR",
                    "CUMPLEANIOS",
                    "CUPON EFECTIVO",
                    "CUPON PREPAGADO",
                    "DATAFONO",
                    "DESCUENTOS",
                    "DINERS CLUB",
                    "DISCOVER",
                    "D-UNAPICHI",
                    "EFECTIVO",
                    "FALTANTE",
                    "GLOVO",
                    "KFC CLUB",
                    "MASTER CARD",
                    "NOTAS CREDITO",
                    "NOTAS DEBITO",
                    "PedidosYa",
                    "POSMANUAL",
                    "RAPPI",
                    "RETENCION",
                    "RETENCION_IVA",
                    "TARJETAS",
                    "TARJETAS DE DEBITO",
                    "TOTAL",
                    "UBER",
                    "UNIONPAY",
                    "VISA"
                  ]
                },
                {
                  "name": "cdn_id",
                  "operator": "equals",
                  "datatype": "uuid",
                  "value": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af"
                }
              ]
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T083",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
      },
      {
        "code": "T084",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
      },
      {
        "code": "T085",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
      },
      {
        "code": "T086",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
      },
      {
        "code": "T087",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
      },
      {
        "code": "T101",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "withData": "true"
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
            "server": "https://sirqa.grupokfc.com",
            "port": "",
            "user": "",
            "password": "",
            "repository": "/serviciosweb/interface/servicio.php",
            "adapter": "Rest"
          },
          "entities": []
        },
        "dataInput": {}
      }
    ]
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                              | Tipo         | Descripción                                 |
| ------------------------------------------------------------------ | ------------ | ------------------------------------------- |
| `code`                                                             | string       | Código del flujo de integración             |
| `withResponse`                                                     | boolean      | Especifica si desea devolver la respuesta   |
| `syncId`                                                           | string       | ID UUID de sincronización                   |
| `country`                                                          | string       | Código del país                             |
| `processes`                                                        | object       | Objeto con los procesos a ejecutar          |
| `processes.EXTRACTS`                                               | array        | Lista de procesos de extracción             |
| `processes.EXTRACTS[].code`                                        | string       | Código del proceso de extracción            |
| `processes.EXTRACTS[].syncId`                                      | string       | ID de sincronización                        |
| `processes.EXTRACTS[].withResponse`                                | boolean      | Indica si retorna respuesta                 |
| `processes.EXTRACTS[].withCache`                                   | boolean      | Indica si utiliza caché                     |
| `processes.EXTRACTS[].configuration`                               | object       | Configuración del proceso                   |
| `processes.EXTRACTS[].configuration.connection`                    | object       | Configuración de conexión                   |
| `processes.EXTRACTS[].configuration.connection.server`             | string       | Servidor de base de datos                   |
| `processes.EXTRACTS[].configuration.connection.port`               | string       | Puerto de conexión                          |
| `processes.EXTRACTS[].configuration.connection.user`               | string       | Usuario de conexión                         |
| `processes.EXTRACTS[].configuration.connection.password`           | string       | Contraseña de conexión                      |
| `processes.EXTRACTS[].configuration.connection.repository`         | string       | Nombre de la base de datos                  |
| `processes.EXTRACTS[].configuration.connection.adapter`            | string       | Tipo de adaptador de conexión               |
| `processes.EXTRACTS[].configuration.entities`                      | array        | Lista de entidades a extraer                |
| `processes.EXTRACTS[].configuration.entities[].name`               | string       | Nombre de la colección                      |
| `processes.EXTRACTS[].configuration.entities[].properties`         | array        | Lista de propiedades a extraer              |
| `processes.EXTRACTS[].configuration.entities[].filters`            | array        | Lista de filtros para la extracción         |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`     | string       | Nombre del parámetro                        |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator` | string       | Operador de comparación                     |
| `processes.EXTRACTS[].configuration.entities[].filters[].datatype` | string       | Tipo de dato del parámetro                  |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`    | string/array | Valor del parámetro o lista de valores      |
| `processes.TRANSFORMS`                                             | array        | Lista de procesos de transformación         |
| `processes.TRANSFORMS[].code`                                      | string       | Código del proceso de transformación        |
| `processes.TRANSFORMS[].syncId`                                    | string       | ID de sincronización                        |
| `processes.TRANSFORMS[].withResponse`                              | boolean      | Indica si retorna respuesta                 |
| `processes.TRANSFORMS[].withCache`                                 | boolean      | Indica si utiliza caché                     |
| `processes.TRANSFORMS[].withData`                                  | string       | Indica si incluye datos                     |
| `processes.LOADS`                                                  | array        | Lista de procesos de carga                  |
| `processes.LOADS[].code`                                           | string       | Código del proceso de carga                 |
| `processes.LOADS[].withCache`                                      | boolean      | Indica si utiliza caché                     |
| `processes.LOADS[].withResponse`                                   | boolean      | Indica si retorna respuesta                 |
| `processes.LOADS[].syncId`                                         | string       | ID de sincronización                        |
| `processes.LOADS[].configuration`                                  | object       | Configuración del proceso de carga          |
| `processes.LOADS[].configuration.connection`                       | object       | Configuración de conexión a servicio REST   |
| `processes.LOADS[].configuration.connection.server`                | string       | URL del servidor REST                       |
| `processes.LOADS[].configuration.connection.port`                  | string       | Puerto de conexión                          |
| `processes.LOADS[].configuration.connection.user`                  | string       | Usuario de conexión                         |
| `processes.LOADS[].configuration.connection.password`              | string       | Contraseña de conexión                      |
| `processes.LOADS[].configuration.connection.repository`            | string       | Ruta del endpoint                           |
| `processes.LOADS[].configuration.connection.adapter`               | string       | Tipo de adaptador de conexión               |
| `processes.LOADS[].configuration.entities`                         | array        | Lista de entidades de destino para la carga |
| `processes.LOADS[].dataInput`                                      | object       | Datos de entrada adicionales                |

## Ejecutar Flujo de Integración - Canales de Impresión con Documentos

### Método HTTP

`POST`

### URL

```
{{server_init}}/api/v1/facade
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
    "withResponse": false,
    "withCache": false,
    "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "country": "{{country}}",
    "franchise_id": {{legacy_cdn_id}},
    "processes": {
        "EXTRACTS": [
            {
                "code": "E001",
                "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "withResponse": true,
                "withCache": true,
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
                            "name": "Settings_BO_Printing_Channels",
                            "properties": [],
                            "filters": [
                                {
                                    "name": "channel_name",
                                    "operator": "equals",
                                    "value": "VOUCHER"
                                },
                                {
                                    "name": "cdn_id",
                                    "operator": "equals",
                                    "datatype": "uuid",
                                    "value": "{{franchise_id}}"
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
                        "repository": "DEV_KFC_MXPi_Settings",
                        "adapter": "{{adapter_mongo}}"
                    },
                    "entities": [
                        {
                            "name": "Settings_BO_Printing_Documents",
                            "properties": [
                                {
                                    "name": "document_key",
                                    "type": "string"
                                }
                            ],
                            "filters": [
                                {
                                    "name": "document_key",
                                    "operator": "in",
                                    "value": [
                                        "ARQUEO",
                                        "CORTE_XX",
                                        "DESASIGNADO_CAJERO",
                                        "DESASIGNADO_CAJERO_DEN",
                                        "FIN_DE_DIA",
                                        "RETIRO_FONDO_ASIGNADO",
                                        "RETIRO_EFECTIVO",
                                        "RETIROS_FORMASPAGO",
                                        "VOUCHER_CANCELADO_NO_APROBADO",
                                        "VOUCHER_APROBADO",
                                        "VOUCHER_ANULACION",
                                        "VOUCHER_NO_APROBADO"
                                    ]
                                },
                                {
                                    "name": "cdn_id",
                                    "operator": "equals",
                                    "datatype": "uuid",
                                    "value": "{{franchise_id}}"
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
                                    "value": "Pais"
                                },
                                {
                                    "name": "id_v1",
                                    "operator": "equals",
                                    "value": "{{legacy_country_id}}"
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "TRANSFORMS": [
            {
                "code": "T126",
                "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "withResponse": true,
                "withCache": false,
                "country": "{{country}}",
                "withData": "true"
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
                            "name": "printing_channels_with_documents",
                            "toName": "Settings_BO_Printing_Channels",
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
                                    "defaultValue": ""
                                },
                                {
                                    "fromName": "channel_name",
                                    "fromType": "",
                                    "toName": "channel_name",
                                    "toType": "",
                                    "defaultValue": ""
                                },
                                {
                                    "fromName": "documents_to_print",
                                    "fromType": "",
                                    "toName": "documents_to_print",
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

| Campo                                                                  | Tipo         | Descripción                                               |
| ---------------------------------------------------------------------- | ------------ | --------------------------------------------------------- |
| `code`                                                                 | string       | Código del flujo de integración                           |
| `withResponse`                                                         | boolean      | Especifica si desea devolver la respuesta                 |
| `withCache`                                                            | boolean      | Especifica si desea guardar la respuesta en caché (mongo) |
| `syncId`                                                               | string       | ID UUID de sincronización                                 |
| `country`                                                              | string       | Código de país (3 dígitos)                                |
| `franchise_id`                                                         | number       | ID de la cadena del MXP legacy                            |
| `processes`                                                            | object       | Objeto con los procesos a ejecutar                        |
| `processes.EXTRACTS`                                                   | array        | Lista de procesos de extracción                           |
| `processes.EXTRACTS[].code`                                            | string       | Código del proceso de extracción                          |
| `processes.EXTRACTS[].syncId`                                          | string       | ID de sincronización                                      |
| `processes.EXTRACTS[].withResponse`                                    | boolean      | Indica si retorna respuesta                               |
| `processes.EXTRACTS[].withCache`                                       | boolean      | Indica si utiliza caché                                   |
| `processes.EXTRACTS[].configuration`                                   | object       | Configuración del proceso                                 |
| `processes.EXTRACTS[].configuration.connection`                        | object       | Configuración de conexión a base de datos                 |
| `processes.EXTRACTS[].configuration.connection.server`                 | string       | Servidor de base de datos                                 |
| `processes.EXTRACTS[].configuration.connection.port`                   | string       | Puerto de conexión                                        |
| `processes.EXTRACTS[].configuration.connection.user`                   | string       | Usuario de conexión                                       |
| `processes.EXTRACTS[].configuration.connection.password`               | string       | Contraseña de conexión                                    |
| `processes.EXTRACTS[].configuration.connection.repository`             | string       | Nombre de la base de datos                                |
| `processes.EXTRACTS[].configuration.connection.adapter`                | string       | Tipo de adaptador de base de datos                        |
| `processes.EXTRACTS[].configuration.entities`                          | array        | Lista de entidades a extraer                              |
| `processes.EXTRACTS[].configuration.entities[].name`                   | string       | Nombre de la colección/tabla a extraer                    |
| `processes.EXTRACTS[].configuration.entities[].properties`             | array        | Lista de propiedades a extraer                            |
| `processes.EXTRACTS[].configuration.entities[].properties[].name`      | string       | Nombre de la propiedad                                    |
| `processes.EXTRACTS[].configuration.entities[].properties[].type`      | string       | Tipo de dato de la propiedad                              |
| `processes.EXTRACTS[].configuration.entities[].filters`                | array        | Lista de filtros para la extracción                       |
| `processes.EXTRACTS[].configuration.entities[].filters[].name`         | string       | Nombre del campo a filtrar                                |
| `processes.EXTRACTS[].configuration.entities[].filters[].operator`     | string       | Operador de comparación                                   |
| `processes.EXTRACTS[].configuration.entities[].filters[].datatype`     | string       | Tipo de dato del valor a filtrar                          |
| `processes.EXTRACTS[].configuration.entities[].filters[].value`        | string/array | Valor o lista de valores del filtro                       |
| `processes.TRANSFORMS`                                                 | array        | Lista de procesos de transformación                       |
| `processes.TRANSFORMS[].code`                                          | string       | Código del proceso de transformación                      |
| `processes.TRANSFORMS[].syncId`                                        | string       | ID de sincronización                                      |
| `processes.TRANSFORMS[].withResponse`                                  | boolean      | Indica si retorna respuesta                               |
| `processes.TRANSFORMS[].withCache`                                     | boolean      | Indica si utiliza caché                                   |
| `processes.TRANSFORMS[].country`                                       | string       | Código del país                                           |
| `processes.TRANSFORMS[].withData`                                      | string       | Indica si incluye datos en la transformación              |
| `processes.LOADS`                                                      | array        | Lista de procesos de carga                                |
| `processes.LOADS[].code`                                               | string       | Código del proceso de carga                               |
| `processes.LOADS[].withResponse`                                       | boolean      | Indica si retorna respuesta                               |
| `processes.LOADS[].withCache`                                          | boolean      | Indica si utiliza caché                                   |
| `processes.LOADS[].syncId`                                             | string       | ID de sincronización                                      |
| `processes.LOADS[].configuration`                                      | object       | Configuración del proceso de carga                        |
| `processes.LOADS[].configuration.connection`                           | object       | Configuración de conexión a base de datos                 |
| `processes.LOADS[].configuration.connection.server`                    | string       | Servidor de base de datos                                 |
| `processes.LOADS[].configuration.connection.port`                      | string       | Puerto de conexión                                        |
| `processes.LOADS[].configuration.connection.user`                      | string       | Usuario de conexión                                       |
| `processes.LOADS[].configuration.connection.password`                  | string       | Contraseña de conexión                                    |
| `processes.LOADS[].configuration.connection.repository`                | string       | Nombre de la base de datos                                |
| `processes.LOADS[].configuration.connection.adapter`                   | string       | Tipo de adaptador de base de datos                        |
| `processes.LOADS[].configuration.entities`                             | array        | Lista de entidades de destino para la carga               |
| `processes.LOADS[].configuration.entities[].name`                      | string       | Nombre de la entidad extraída                             |
| `processes.LOADS[].configuration.entities[].toName`                    | string       | Nombre de la entidad a cargar                             |
| `processes.LOADS[].configuration.entities[].properties`                | array        | Lista de propiedades a mapear                             |
| `processes.LOADS[].configuration.entities[].properties[].fromName`     | string       | Nombre de la propiedad extraída                           |
| `processes.LOADS[].configuration.entities[].properties[].fromType`     | string       | Tipo de dato de origen                                    |
| `processes.LOADS[].configuration.entities[].properties[].toName`       | string       | Nombre de la propiedad a cargar                           |
| `processes.LOADS[].configuration.entities[].properties[].toType`       | string       | Tipo de dato de destino                                   |
| `processes.LOADS[].configuration.entities[].properties[].defaultValue` | string       | Valor por defecto (vacío usa el valor de extracción)      |
| `processes.LOADS[].configuration.entities[].properties[].isPrimaryKey` | string       | Especifica si es valor único y valida duplicidad          |
| `processes.LOADS[].dataInput`                                          | object       | Datos de entrada adicionales                              |
| `processes.PUBLISHERS`                                                 | array        | Lista de procesos de publicación                          |

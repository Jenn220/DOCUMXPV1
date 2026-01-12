## Ejecutar Sincronización de Datos

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
  "chunkLoad": 10,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E001",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "configuration": {
          "connection": {
            "server": "ec-mxpv2-dev.3hro7.mongodb.net",
            "port": "",
            "user": "dev_integration",
            "password": "rIJEUAk8WyynPhC4",
            "repository": "MXP_integrations",
            "adapter": "Mongo"
          },
          "entities": [
            {
              "name": "billing_information",
              "properties": [],
              "filters": []
            },
            {
              "name": "number_sequence",
              "properties": [],
              "filters": []
            }
          ]
        }
      }
    ],
    "TRANSFORMS": [
      {
        "code": "T080",
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "withResponse": true,
        "withCache": false,
        "country": "ECU"
      }
    ],
    "LOADS": [
      {
        "code": "01",
        "withCache": true,
        "withResponse": true,
        "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "configuration": {
          "connection": {
            "server": "192.168.101.13",
            "port": "27020",
            "user": "admin",
            "password": "admin123",
            "repository": "KFC_MXPi_FeBuild",
            "adapter": "MongoLocal"
          },
          "entities": [
            {
              "name": "billing_information",
              "toName": "billing_information",
              "properties": [
                {
                  "fromName": "_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "",
                  "defaultValue": "",
                  "isPrimaryKey": "true"
                },
                {
                  "fromName": "cdn_id",
                  "fromType": "",
                  "toName": "cdn_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "company_id",
                  "fromType": "",
                  "toName": "company_id",
                  "toType": "uuid",
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
                  "fromName": "business_name",
                  "fromType": "",
                  "toName": "business_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "document_identity_type_id",
                  "fromType": "",
                  "toName": "document_identity_type_id",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "tax_identification_number",
                  "fromType": "",
                  "toName": "tax_identification_number",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "resolution_number",
                  "fromType": "",
                  "toName": "resolution_number",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "headquarters_address",
                  "fromType": "",
                  "toName": "headquarters_address",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "restaurant_address",
                  "fromType": "",
                  "toName": "restaurant_address",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "required_to_keep_accounting",
                  "fromType": "",
                  "toName": "required_to_keep_accounting",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "full_name",
                  "fromType": "",
                  "toName": "full_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "phone",
                  "fromType": "",
                  "toName": "phone",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "email",
                  "fromType": "",
                  "toName": "email",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "address",
                  "fromType": "",
                  "toName": "address",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "tax_payer",
                  "fromType": "",
                  "toName": "tax_payer",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "tax_payer_type",
                  "fromType": "",
                  "toName": "tax_payer_type",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "issue_type_name",
                  "fromType": "",
                  "toName": "issue_type_name",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "issue_type_code",
                  "fromType": "",
                  "toName": "issue_type_code",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "issue_date",
                  "fromType": "",
                  "toName": "issue_date",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "billing_label",
                  "fromType": "",
                  "toName": "billing_label",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "billing_link_label",
                  "fromType": "",
                  "toName": "billing_link_label",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "billing_link",
                  "fromType": "",
                  "toName": "billing_link",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "billing_access_key_label",
                  "fromType": "",
                  "toName": "billing_access_key_label",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "document_type",
                  "fromType": "",
                  "toName": "document_type",
                  "toType": "array",
                  "defaultValue": ""
                },
                {
                  "fromName": "branche_office",
                  "fromType": "",
                  "toName": "branche_office",
                  "toType": "array",
                  "defaultValue": ""
                },
                {
                  "fromName": "fe_build_code_number",
                  "fromType": "",
                  "toName": "fe_build_code_number",
                  "toType": "",
                  "defaultValue": ""
                }
              ]
            },
            {
              "name": "number_sequence",
              "toName": "number_sequence",
              "properties": [
                {
                  "fromName": "_id",
                  "fromType": "",
                  "toName": "_id",
                  "toType": "",
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
                  "fromName": "type_document_id",
                  "fromType": "",
                  "toName": "type_document_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "cash_id",
                  "fromType": "",
                  "toName": "cash_id",
                  "toType": "uuid",
                  "defaultValue": ""
                },
                {
                  "fromName": "sequential",
                  "fromType": "",
                  "toName": "sequential",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "document_code",
                  "fromType": "",
                  "toName": "document_code",
                  "toType": "",
                  "defaultValue": ""
                },
                {
                  "fromName": "created_at",
                  "fromType": "",
                  "toName": "created_at",
                  "toType": "timestamp",
                  "defaultValue": ""
                },
                {
                  "fromName": "updated_at",
                  "fromType": "",
                  "toName": "updated_at",
                  "toType": "timestamp",
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

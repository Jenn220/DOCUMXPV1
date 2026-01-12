## Actualizar Sincronización

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/update
```

### Parámetros de Query

| Key  | Value                                  | Description                          |
| ---- | -------------------------------------- | ------------------------------------ |
| `id` | `7654cb16-e955-4605-8579-b891a67f94c7` | ID de la sincronización a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "Sincronizacion de Menu v3 - Actualizado v2",
  "franchiseId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
  "status": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "observations": "observation",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "isHourAndDateSettings": true,
  "hourToExecute": "2024-05-22T20:20:01",
  "isRecurrentExecution": false,
  "recurringExecution": null,
  "integrations": [
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    },
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    }
  ],
  "sync_run_state": [
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
    },
    {
      "code": 500,
      "status": "error",
      "process": "I002",
      "message": "Integración fallida",
      "syncId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "data": {
        "EXTRACTS": [
          {
            "code": 500,
            "status": "error",
            "process": "E001",
            "message": "Error processing request: ('HYT00', '[HYT00] [Microsoft][ODBC Driver 18 for SQL Server]Login timeout expired (0) (SQLDriverConnect)')",
            "dateTime": "2025-02-04T17:32:05.740+00:00"
          }
        ],
        "TRANSFORMS": [],
        "LOAD": []
      }
    }
  ],
  "country": [
    {
      "countryId": "857accc3-c59a-4b6c-ae84-5942f5a14581",
      "countryName": "ECU",
      "countryDescription": "ECUADOR",
      "countryCode": "1"
    }
  ],
  "enterprise": [
    {
      "enterpriseId": "857accc3-c59a-4b6c-ae84-5942f5a14581",
      "enterpriseName": "INT IN FOOD SERVICE",
      "enterpriseCode": "1"
    }
  ],
  "franchise": [
    {
      "franchiseId": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "franchiseName": "GUS",
      "franchiseCode": "9"
    }
  ],
  "restaurant": [
    {
      "restaurantId": "957accc3-c59a-4b6c-ae84-5942f5a14587",
      "restaurantName": "G005",
      "restaurantDescription": "Labrador",
      "restaurantCode": "124"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                         | Tipo    | Requerido | Descripción                                    |
| --------------------------------------------- | ------- | --------- | ---------------------------------------------- |
| `name`                                        | string  | Sí        | Nombre de la sincronización (máx: 100)         |
| `franchiseId`                                 | string  | No        | ID de la franquicia (máx: 255)                 |
| `status`                                      | string  | Sí        | Estado de la sincronización (máx: 25)          |
| `observations`                                | string  | No        | Observaciones (máx: 300)                       |
| `userId`                                      | string  | Sí        | ID del usuario (máx: 255)                      |
| `isHourAndDateSettings`                       | boolean | No        | Indica si tiene configuración de hora y fecha  |
| `hourToExecute`                               | string  | No        | Fecha y hora programada de ejecución (máx: 50) |
| `isRecurrentExecution`                        | boolean | No        | Indica si es una ejecución recurrente          |
| `recurringExecution`                          | object  | No        | Configuración de ejecución recurrente          |
| `integrations`                                | array   | Sí        | Lista de integraciones (mínimo 1 elemento)     |
| `integrations[].id`                           | string  | Sí        | ID de la integración (máx: 100)                |
| `sync_run_state`                              | array   | No        | Estado de ejecución de la sincronización       |
| `sync_run_state[].code`                       | integer | No        | Código de estado de la integración             |
| `sync_run_state[].status`                     | string  | No        | Estado de la integración (success/error)       |
| `sync_run_state[].process`                    | string  | No        | Código del proceso de integración              |
| `sync_run_state[].message`                    | string  | No        | Mensaje descriptivo del resultado              |
| `sync_run_state[].syncId`                     | string  | No        | ID de la sincronización asociada               |
| `sync_run_state[].data`                       | object  | No        | Datos detallados de ejecución                  |
| `sync_run_state[].data.EXTRACTS`              | array   | No        | Array con resultados de extracciones           |
| `sync_run_state[].data.EXTRACTS[].code`       | integer | No        | Código de estado de la extracción              |
| `sync_run_state[].data.EXTRACTS[].status`     | string  | No        | Estado de la extracción                        |
| `sync_run_state[].data.EXTRACTS[].process`    | string  | No        | Código del proceso de extracción               |
| `sync_run_state[].data.EXTRACTS[].message`    | string  | No        | Mensaje descriptivo de la extracción           |
| `sync_run_state[].data.EXTRACTS[].dateTime`   | string  | No        | Fecha y hora de la extracción                  |
| `sync_run_state[].data.TRANSFORMS`            | array   | No        | Array con resultados de transformaciones       |
| `sync_run_state[].data.TRANSFORMS[].code`     | integer | No        | Código de estado de la transformación          |
| `sync_run_state[].data.TRANSFORMS[].status`   | string  | No        | Estado de la transformación                    |
| `sync_run_state[].data.TRANSFORMS[].process`  | string  | No        | Código del proceso de transformación           |
| `sync_run_state[].data.TRANSFORMS[].message`  | string  | No        | Mensaje descriptivo de la transformación       |
| `sync_run_state[].data.TRANSFORMS[].dateTime` | string  | No        | Fecha y hora de la transformación              |
| `sync_run_state[].data.LOAD`                  | array   | No        | Array con resultados de cargas                 |
| `sync_run_state[].data.LOAD[].code`           | integer | No        | Código de estado de la carga                   |
| `sync_run_state[].data.LOAD[].status`         | string  | No        | Estado de la carga                             |
| `sync_run_state[].data.LOAD[].process`        | string  | No        | Código del proceso de carga                    |
| `sync_run_state[].data.LOAD[].message`        | string  | No        | Mensaje descriptivo de la carga                |
| `sync_run_state[].data.LOAD[].dateTime`       | string  | No        | Fecha y hora de la carga                       |
| `country`                                     | array   | Sí        | Lista de países asociados                      |
| `country[].countryId`                         | string  | Sí        | ID del país                                    |
| `country[].countryName`                       | string  | Sí        | Nombre corto del país                          |
| `country[].countryDescription`                | string  | Sí        | Descripción del país                           |
| `country[].countryCode`                       | string  | Sí        | Código del país                                |
| `enterprise`                                  | array   | Sí        | Lista de empresas asociadas                    |
| `enterprise[].enterpriseId`                   | string  | Sí        | ID de la empresa                               |
| `enterprise[].enterpriseName`                 | string  | Sí        | Nombre de la empresa                           |
| `enterprise[].enterpriseCode`                 | string  | Sí        | Código de la empresa                           |
| `franchise`                                   | array   | No        | Lista de franquicias asociadas                 |
| `franchise[].franchiseId`                     | string  | No        | ID de la franquicia                            |
| `franchise[].franchiseName`                   | string  | No        | Nombre de la franquicia                        |
| `franchise[].franchiseCode`                   | string  | No        | Código de la franquicia                        |
| `restaurant`                                  | array   | No        | Lista de restaurantes asociados                |
| `restaurant[].restaurantId`                   | string  | No        | ID del restaurante                             |
| `restaurant[].restaurantName`                 | string  | No        | Nombre del restaurante                         |
| `restaurant[].restaurantDescription`          | string  | No        | Descripción del restaurante                    |
| `restaurant[].restaurantCode`                 | string  | No        | Código del restaurante                         |

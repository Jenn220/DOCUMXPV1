## Obtener Sincronizaciones por ID de Franquicia

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/getByFranchiseId
```

### Parámetros de Query

| Key           | Value                                  | Description                                       |
| ------------- | -------------------------------------- | ------------------------------------------------- |
| `franchiseId` | `69503d8f-fa70-2196-f0a0-e3a85fa10aec` | ID de la franquicia para filtrar sincronizaciones |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
[
  {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "status": "A",
    "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
    "userId": "sdfsdfhsdjkfhsdg",
    "isHourAndDateSettings": true,
    "hourToExecute": "",
    "isRecurrentExecution": false,
    "recurringExecution": null,
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
  },
  {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "status": "A",
    "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
    "userId": "sdfsdfhsdjkfhsdg",
    "isHourAndDateSettings": true,
    "hourToExecute": "",
    "isRecurrentExecution": false,
    "recurringExecution": null,
    "sync_run_state": null,
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
]
```

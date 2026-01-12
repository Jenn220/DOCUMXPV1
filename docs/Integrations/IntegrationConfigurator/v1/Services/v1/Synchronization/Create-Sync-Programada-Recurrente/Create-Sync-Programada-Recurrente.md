## Crear Sincronización

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "Sincronizacion de Menu v3",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "isHourAndDateSettings": false,
  "hourToExecute": null,
  "isRecurrentExecution": true,
  "recurringExecution": 5,
  "integrations": [
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    },
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    }
  ],
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
```

### Descripción de Campos

| Campo                   | Tipo        | Restricciones                                       | Descripción                                     |
| ----------------------- | ----------- | --------------------------------------------------- | ----------------------------------------------- |
| `name`                  | string      | Máximo: 100 caracteres, **Obligatorio**             | Nombre de la sincronización                     |
| `userId`                | string      | Máximo: 255 caracteres, **Obligatorio**             | ID del usuario                                  |
| `isHourAndDateSettings` | boolean     | -                                                   | Indica si tiene configuración de hora y fecha   |
| `hourToExecute`         | string/null | Máximo: 50 caracteres, null cuando no es programado | Hora de ejecución programada                    |
| `isRecurrentExecution`  | boolean     | -                                                   | Indica si es ejecución recurrente               |
| `recurringExecution`    | integer     | -                                                   | Intervalo de ejecución recurrente (en segundos) |
| `integrations`          | array       | Mínimo: 1 elemento                                  | Lista de integraciones asociadas                |
| `integrations[].id`     | string      | Máximo: 100 caracteres                              | ID de cada integración                          |
| `sync_run_state`        | string/null | -                                                   | Estado de ejecución de sincronización           |
| `country`               | array       | **Obligatorio**                                     | Lista de países                                 |
| `enterprise`            | array       | **Obligatorio**                                     | Lista de empresas                               |
| `franchise`             | array       | Opcional                                            | Lista de franquicias                            |
| `restaurant`            | array       | Opcional                                            | Lista de restaurantes                           |

## Obtener Procesos por Tipo

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/processes/getByType
```

### Parámetros de Query

| Key      | Value                                  | Description                        |
| -------- | -------------------------------------- | ---------------------------------- |
| `typeId` | `fc1e4f86-a544-4d8f-95c1-870b7f1a6dd1` | ID del tipo de proceso a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Encontrado Correctamente",
  "data": {
    "total_rows": 100,
    "rows": [
      {
        "id": "a627d86f-1092-4341-a9ad-21e6efc5f8c1",
        "code": "T001",
        "name": "my name",
        "description": "",
        "typeId": "fc1e4f86-a544-4d8f-95c1-870b7f1a6dd1",
        "connectionId": "712feaea-8228-4f03-9457-3ce36e618c56",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "entities": [
          {
            "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
            "properties": [
              {
                "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
                "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
              },
              {
                "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
              }
            ],
            "filters": [
              {
                "propertyId": "06b8588c-4cef-4f9e-b3ae-2283508be599",
                "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "isGlobalVariable": false,
                "value": "KFC"
              },
              {
                "propertyId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "isGlobalVariable": true,
                "value": [
                  {
                    "globalVariableId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e0",
                    "globalVariableName": "country",
                    "globalVariableValue": [
                      {
                        "globalVariableValueId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e2",
                        "globalVariableValueName": "countryName"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "id": "0e020c5d-ee6d-4a9c-9edf-23da26010f98",
        "code": "T002",
        "name": "my name",
        "description": "",
        "typeId": "fc1e4f86-a544-4d8f-95c1-870b7f1a6dd1",
        "connectionId": "712feaea-8228-4f03-9457-3ce36e618c56",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "entities": [
          {
            "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
            "properties": [
              {
                "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
                "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
              },
              {
                "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
              }
            ],
            "filters": [
              {
                "propertyId": "06b8588c-4cef-4f9e-b3ae-2283508be599",
                "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "value": "KFC"
              },
              {
                "propertyId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
                "value": "combo mix"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                      | Descripción                                      |
| -------------------------- | ------------------------------------------------ |
| `code`                     | Código de respuesta interno (20 = éxito)         |
| `description`              | Descripción del resultado                        |
| `data`                     | Objeto con los datos                             |
| `data.total_rows`          | Número total de registros disponibles            |
| `data.rows`                | Array con los procesos del tipo consultado       |
| `data.rows[].id`           | ID único de cada proceso                         |
| `data.rows[].code`         | Código del proceso                               |
| `data.rows[].name`         | Nombre del proceso                               |
| `data.rows[].description`  | Descripción del proceso                          |
| `data.rows[].typeId`       | ID del tipo de proceso                           |
| `data.rows[].connectionId` | ID de la conexión                                |
| `data.rows[].statusId`     | ID del estado del proceso                        |
| `data.rows[].entities`     | Array de entidades con sus propiedades y filtros |

## Obtener Sincronizaciones Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/getAllPaginated
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "string",
  "sort_order": 0,
  "sort_field": "string",
  "rows": 20,
  "first": 1,
  "activeOnly": true
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo    | Requerido | Descripción                                           |
| ------------ | ------- | --------- | ----------------------------------------------------- |
| `search`     | string  | No        | Texto de búsqueda                                     |
| `sort_order` | integer | No        | Orden de clasificación (1 ascendente, -1 descendente) |
| `sort_field` | string  | No        | Campo por el cual ordenar                             |
| `rows`       | integer | No        | Cantidad de registros por página                      |
| `first`      | integer | No        | Índice del primer registro a obtener                  |
| `activeOnly` | boolean | No        | Filtra solo registros en estado activo                |

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Data returned succesfully",
  "data": {
    "total_rows": 100,
    "rows": [
      {
        "id": "69503d8f-fa70-2196-f0a0-e3a85fa17aec",
        "name": "Sync test",
        "status": {
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "key": "success",
          "text": "Exitoso",
          "color": "#1B3E19",
          "background": "#E2F7E2"
        },
        "observations": "Lorem ipsum Lorem ipsum",
        "userId": "User test",
        "isHourAndDateSettings": true,
        "hourToExecute": "14/06/2024 23:00:00",
        "isRecurrentExecution": false,
        "recurringExecution": null
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e4a85fa18aec",
        "name": "Integración inicial",
        "status": {
          "id": "fd61c187-3ecc-4114-b83f-d10af3bc3256",
          "key": "error",
          "text": "Error",
          "color": "#810C22",
          "background": "#FBD5DC"
        },
        "observations": "Lorem ipsum Lorem ipsum",
        "userId": "User test",
        "isHourAndDateSettings": true,
        "hourToExecute": "14/06/2024 24:00:00",
        "isRecurrentExecution": false,
        "recurringExecution": null
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e3a85fa19aec",
        "name": "Sincronizacion mxp legacy a mxp v2",
        "status": {
          "id": "f285b374-252c-49df-a67f-a7eb6bd02a76",
          "key": "canceled",
          "text": "Cancelado",
          "color": "#810C22",
          "background": "#FBECD5"
        },
        "observations": "Lorem ipsum Lorem ipsum",
        "userId": "User test",
        "isHourAndDateSettings": true,
        "hourToExecute": "14/06/2024 23:00:00",
        "isRecurrentExecution": false,
        "recurringExecution": null
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e8a85fa11aec",
        "name": "Sincronizacion mxp v2 a mxp legacy",
        "status": {
          "id": "f316a140-f62e-493e-b00e-7fbc19d9bbb5",
          "key": "running",
          "text": "Ejecutando",
          "color": "#1D1819",
          "background": "#DFDEDE"
        },
        "observations": "Lorem ipsum Lorem ipsum",
        "userId": "User test",
        "isHourAndDateSettings": true,
        "hourToExecute": "14/06/2024 01:00:00",
        "isRecurrentExecution": false,
        "recurringExecution": null
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e8a85fa71aec",
        "name": "Sincronizacion mxp v2",
        "status": {
          "id": "e2a3cc14-211c-4539-8b1e-72bc3a8c001f",
          "key": "programmed",
          "text": "Programado",
          "color": "#0040B0",
          "background": "#EBF8FF"
        },
        "observations": "Lorem ipsum Lorem ipsum",
        "userId": "User test",
        "isHourAndDateSettings": true,
        "hourToExecute": "14/06/2024 01:00:00",
        "isRecurrentExecution": false,
        "recurringExecution": null
      }
    ]
  }
}
```

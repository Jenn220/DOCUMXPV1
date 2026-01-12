## Obtener Catálogos Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "",
  "sort_order": 0,
  "sort_field": "",
  "rows": 20,
  "first": 1
}
```

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Encontrado Correctamente",
  "data": {
    "total_rows": 10,
    "rows": [
      {
        "id": "51faf974-5c9e-4936-b234-91a173356dea",
        "code": 1,
        "name": "Tipo proceso",
        "value": "process_type",
        "fatherId": null,
        "isFather": true,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "aba246fc-76a2-48ea-968d-17a51702861f",
        "code": 2,
        "name": "Extracción",
        "value": "extract",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "623acd2c-b882-41ac-8182-16b9293ebb08",
        "code": 2,
        "name": "Transformación",
        "value": "transform",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "764ca591-9a83-48e0-b1f7-b6d43e0e2267",
        "code": 4,
        "name": "Carga",
        "value": "load",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "764ca591-9a83-48e0-b1f7-b6d43e0e2267",
        "code": 5,
        "name": "Publicación",
        "value": "publish",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                  | Descripción                                 |
| ---------------------- | ------------------------------------------- |
| `code`                 | Código de respuesta interno (20 = éxito)    |
| `description`          | Descripción del resultado                   |
| `data`                 | Objeto con los datos paginados              |
| `data.total_rows`      | Número total de registros disponibles       |
| `data.rows`            | Array con los registros de la página actual |
| `data.rows[].id`       | ID único de cada catálogo                   |
| `data.rows[].code`     | Código numérico del catálogo                |
| `data.rows[].name`     | Nombre del catálogo                         |
| `data.rows[].value`    | Valor del catálogo                          |
| `data.rows[].fatherId` | ID del padre (null si es padre)             |
| `data.rows[].isFather` | Indica si es un catálogo padre              |
| `data.rows[].detail`   | Detalle adicional del catálogo              |
| `data.rows[].statusId` | ID del estado del catálogo                  |

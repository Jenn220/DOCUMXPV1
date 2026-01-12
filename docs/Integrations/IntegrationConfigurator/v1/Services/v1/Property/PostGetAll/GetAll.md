## Obtener Propiedades Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/properties/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "",
  "sort_order": 0,
  "sort_field": "",
  "rows": 20,
  "first": 1,
  "activeOnly": true
}
```

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Encontrado Correctamente",
  "data": {
    "total_rows": 1,
    "rows": [
      {
        "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
        "code": "P001",
        "name": "description",
        "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
        "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "8f4c76a0-0779-40df-9fd6-5acba2e57333",
        "code": "P002",
        "name": "name",
        "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
        "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
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
| `data.rows[].id`       | ID único de cada propiedad                  |
| `data.rows[].code`     | Código de la propiedad                      |
| `data.rows[].name`     | Nombre de la propiedad                      |
| `data.rows[].typeId`   | ID del tipo de propiedad                    |
| `data.rows[].entityId` | ID de la entidad asociada                   |
| `data.rows[].statusId` | ID del estado de la propiedad               |

## Obtener Entidades Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/entities/getAllPaginated
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
        "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "code": "E001",
        "name": "plu",
        "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
        "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
        "repositoryDescription": "Reposirorio para mxp legacy",
        "repositoryName": "mxp-dev",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                               | Descripción                                 |
| ----------------------------------- | ------------------------------------------- |
| `code`                              | Código de respuesta interno (20 = éxito)    |
| `description`                       | Descripción del resultado                   |
| `data`                              | Objeto con los datos paginados              |
| `data.total_rows`                   | Número total de registros disponibles       |
| `data.rows`                         | Array con los registros de la página actual |
| `data.rows[].id`                    | ID único de cada entidad                    |
| `data.rows[].code`                  | Código de la entidad                        |
| `data.rows[].name`                  | Nombre de la entidad                        |
| `data.rows[].typeId`                | ID del tipo de entidad                      |
| `data.rows[].repositoryId`          | ID del repositorio                          |
| `data.rows[].repositoryDescription` | Descripción del repositorio                 |
| `data.rows[].repositoryName`        | Nombre del repositorio                      |
| `data.rows[].statusId`              | ID del estado de la entidad                 |

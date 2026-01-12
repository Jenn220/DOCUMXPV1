## Obtener Servidores Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/servers/getAllPaginated
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
  "description": "Data returned succesfully",
  "data": {
    "total_rows": 1,
    "rows": [
      {
        "id": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
        "code": "S001",
        "name": "server_centos",
        "typeServerId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
        "url": "https://server.com",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                      | Descripción                                 |
| -------------------------- | ------------------------------------------- |
| `code`                     | Código de respuesta interno (20 = éxito)    |
| `description`              | Descripción del resultado                   |
| `data`                     | Objeto con los datos paginados              |
| `data.total_rows`          | Número total de registros disponibles       |
| `data.rows`                | Array con los registros de la página actual |
| `data.rows[].id`           | ID único de cada servidor                   |
| `data.rows[].code`         | Código del servidor                         |
| `data.rows[].name`         | Nombre del servidor                         |
| `data.rows[].typeServerId` | ID del tipo de servidor                     |
| `data.rows[].url`          | URL del servidor                            |
| `data.rows[].statusId`     | ID del estado del servidor                  |

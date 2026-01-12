## Obtener Estados Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/status/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "string",
  "sort_order": 0,
  "sort_field": "string",
  "rows": 20,
  "first": 1
}
```

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
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "key": "active",
        "text": "Activo",
        "color": "#1B3E19",
        "background": "#E2F7E2"
      },
      {
        "id": "fd61c187-3ecc-4114-b83f-d10af3bc3256",
        "key": "inactive",
        "text": "Inactivo",
        "color": "#810C22",
        "background": "#FBD5DC"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                    | Descripción                                 |
| ------------------------ | ------------------------------------------- |
| `code`                   | Código de respuesta interno (20 = éxito)    |
| `description`            | Descripción del resultado                   |
| `data`                   | Objeto con los datos paginados              |
| `data.total_rows`        | Número total de registros disponibles       |
| `data.rows`              | Array con los registros de la página actual |
| `data.rows[].id`         | ID único de cada estado                     |
| `data.rows[].key`        | Clave del estado                            |
| `data.rows[].text`       | Texto del estado                            |
| `data.rows[].color`      | Color del texto                             |
| `data.rows[].background` | Color de fondo                              |

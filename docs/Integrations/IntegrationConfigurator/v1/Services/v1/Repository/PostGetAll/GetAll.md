## Obtener Repositorios Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/repositories/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "",
  "sort_order": 1,
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
        "id": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
        "code": "R001",
        "port": 9562,
        "username": "admin",
        "password": "admin123",
        "databaseName": "mxp-dev",
        "authTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "url": "https://apim-hera.azure-api.net/mxpi-init-prepro1",
        "repositoryDescription": "Repostirorio para mxp legacy"
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
| `data.rows[].id`                    | ID único de cada repositorio                |
| `data.rows[].code`                  | Código del repositorio                      |
| `data.rows[].port`                  | Puerto del repositorio                      |
| `data.rows[].username`              | Nombre de usuario                           |
| `data.rows[].password`              | Contraseña                                  |
| `data.rows[].databaseName`          | Nombre de la base de datos                  |
| `data.rows[].authTypeId`            | ID del tipo de autenticación                |
| `data.rows[].statusId`              | ID del estado del repositorio               |
| `data.rows[].url`                   | URL del repositorio                         |
| `data.rows[].repositoryDescription` | Descripción del repositorio                 |

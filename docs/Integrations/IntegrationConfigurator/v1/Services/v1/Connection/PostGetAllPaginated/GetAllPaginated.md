## Obtener Conexiones Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/connections/getAllPaginated
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
    "total_rows": 100,
    "rows": [
      {
        "id": "712feaea-8228-4f03-9457-3ce36e618c56",
        "code": "C001",
        "serverId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
        "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
        "adapterId": "6f5672e8-32fc-4195-b1f0-326f9e2ac82f",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "Conexión database maxpoint legacy",
        "description": "alguna descripción"
      },
      {
        "id": "c1845420-1f76-477d-b1f4-e1922c64a058",
        "code": "C002",
        "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
        "adapterId": "8d9c0ccb-27aa-4559-b533-ddf4b120c661",
        "statusId": "fd61c187-3ecc-4114-b83f-d10af3bc3256",
        "name": "Conexión database maxpoint v2",
        "description": "Descripción"
      },
      {
        "id": "06e4838d-e254-4585-a57b-e22c2d35e13c",
        "code": "C003",
        "serverId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "adapterId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
        "statusId": "fd61c187-3ecc-4114-b83f-d10af3bc3256",
        "name": "Conexión database maxpoint legacy",
        "description": "Descripción ..."
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
| `data.rows[].id`           | ID único de cada conexión                   |
| `data.rows[].code`         | Código de la conexión                       |
| `data.rows[].serverId`     | ID del servidor                             |
| `data.rows[].repositoryId` | ID del repositorio                          |
| `data.rows[].adapterId`    | ID del adaptador                            |
| `data.rows[].statusId`     | ID del estado de la conexión                |
| `data.rows[].name`         | Nombre de la conexión                       |
| `data.rows[].description`  | Descripción de la conexión                  |

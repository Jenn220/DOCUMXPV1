## Actualizar Repositorio

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/repositories/update
```

### Parámetros de Query

| Key  | Value                                  | Description                           |
| ---- | -------------------------------------- | ------------------------------------- |
| `id` | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID único del repositorio a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
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
```

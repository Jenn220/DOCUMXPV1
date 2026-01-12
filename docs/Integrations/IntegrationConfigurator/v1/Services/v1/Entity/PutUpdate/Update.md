## Actualizar Entidad

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/entities/update
```

### Parámetros de Query

| Key  | Value                                  | Description                         |
| ---- | -------------------------------------- | ----------------------------------- |
| `id` | `059bb531-5b34-4435-bdad-21c81b41cac1` | ID único de la entidad a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "plu",
  "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
  "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
  "repositoryDescription": "Reposirorio para mxp legacy",
  "repositoryName": "mxp-dev",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

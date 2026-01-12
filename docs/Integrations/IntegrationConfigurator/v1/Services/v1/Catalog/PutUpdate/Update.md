## Actualizar Catálogo

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/update
```

### Parámetros de Query

| Key  | Value                                  | Description                        |
| ---- | -------------------------------------- | ---------------------------------- |
| `id` | `51faf974-5c9e-4936-b234-91a173356dea` | ID único del catálogo a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "Tipo proceso",
  "code": 1,
  "value": "process_type",
  "fatherId": null,
  "isFather": true,
  "detail": "",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

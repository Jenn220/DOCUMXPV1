## Iniciar Propagación de Staging

### Método HTTP

`POST`

### URL

```
{{server_propagation}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key          | Value                                  | Description                       |
| ------------ | -------------------------------------- | --------------------------------- |
| `user`       | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |
| `country_id` | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "OperationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Descripción de Campos del Cuerpo

| Campo         | Tipo   | Description                   |
| ------------- | ------ | ----------------------------- |
| `OperationId` | string | ID de la operación de staging |

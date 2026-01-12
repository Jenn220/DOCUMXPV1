## Establecer Temporizador de Horario de Programación

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `country`   | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "programmation_price_id": "string",
  "application_date": "2024-01-01T00:00:00Z"
}
```

### Descripción de Campos del Cuerpo

| Campo                    | Tipo   | Description                                   |
| ------------------------ | ------ | --------------------------------------------- |
| `programmation_price_id` | string | ID de la programación de precio               |
| `application_date`       | string | Fecha y hora de aplicación (formato ISO 8601) |

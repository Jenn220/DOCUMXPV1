## Procesar Lote de Fondos por Suscripción de Caja Registradora

### Método HTTP

`POST`

### URL

```
{{server_internalClients}}/api/v1/fund/batch_funds_by_cash_register_subscriptions
```

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "funds": [
    {
      "_id": "00000000-0000-0000-0000-000000000000",
      "type_fund_id": "00000000-0000-0000-0000-000000000000",
      "cdn_id": "00000000-0000-0000-0000-000000000000",
      "restaurant_id": "00000000-0000-0000-0000-000000000000",
      "value_fund": 5000,
      "user_id": "00000000-0000-0000-0000-000000000000",
      "cash_register_subscription_id": "00000000-0000-0000-0000-000000000000",
      "reason_rejection_id": "rejection-uuid",
      "txt_reason_rejection": "Reason text",
      "is_active": true,
      "status_fund_id": "00000000-0000-0000-0000-000000000000",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                   | Tipo    | Descripción                                          |
| --------------------------------------- | ------- | ---------------------------------------------------- |
| `funds`                                 | array   | Lista de fondos                                      |
| `funds[]._id`                           | string  | Identificador del fondo                              |
| `funds[].type_fund_id`                  | string  | Identificador del tipo de fondo                      |
| `funds[].cdn_id`                        | string  | Identificador de la cadena                           |
| `funds[].restaurant_id`                 | string  | Identificador del restaurante                        |
| `funds[].value_fund`                    | number  | Valor del fondo                                      |
| `funds[].user_id`                       | string  | Identificador del usuario                            |
| `funds[].cash_register_subscription_id` | string  | Identificador de la suscripción de caja registradora |
| `funds[].reason_rejection_id`           | string  | Identificador de razón de rechazo                    |
| `funds[].txt_reason_rejection`          | string  | Texto de razón de rechazo                            |
| `funds[].is_active`                     | boolean | Indica si está activo                                |
| `funds[].status_fund_id`                | string  | Identificador del estado del fondo                   |
| `funds[].created_at`                    | string  | Fecha de creación (formato ISO)                      |
| `funds[].updated_at`                    | string  | Fecha de actualización (formato ISO)                 |

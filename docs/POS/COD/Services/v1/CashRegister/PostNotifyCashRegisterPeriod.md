## Notificar Caja Registradora

### Método HTTP

`POST`

### URL

```
{{server_cod}}/api/cod/cashier-register/notify
```

### Headers

| Key           | Value            | Descripción                       |
| ------------- | ---------------- | --------------------------------- |
| Content-Type  | application/json | Tipo de contenido de la solicitud |
| Authorization | Bearer {{token}} | Token de autenticación            |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "restaurant_id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
  "cash_register_id": "aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0",
  "period_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
  "channel_id": "568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d",
  "status": true
}
```

### Descripción del Cuerpo de la Solicitud

| Campo              | Tipo    | Descripción                           |
| ------------------ | ------- | ------------------------------------- |
| `restaurant_id`    | string  | Identificador del restaurante         |
| `cash_register_id` | string  | Identificador de la caja registradora |
| `period_id`        | string  | Identificador del período             |
| `channel_id`       | string  | Identificador del canal               |
| `status`           | boolean | Estado de la notificación             |

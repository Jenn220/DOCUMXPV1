## Registrar Dispositivo

### Método HTTP

`POST`

### URL

```
{{server_localSync}}/api/registerDevice
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "restaurantId": "24260579-faf8-763f-aac7-5e16faff96d1",
  "deviceId": "8028a2ff-c639-6df4-68e8-8982c0256be3",
  "cash_register_id": "aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0",
  "user_id": "c17b6e8d-88a5-9eb5-1f44-aeec161494da"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo              | Tipo   | Descripción                           |
| ------------------ | ------ | ------------------------------------- |
| `restaurantId`     | string | Identificador del restaurante         |
| `deviceId`         | string | Identificador del dispositivo         |
| `cash_register_id` | string | Identificador de la caja registradora |
| `user_id`          | string | Identificador del usuario             |

## Actualizar Transacción - TX016

### Método HTTP

`PUT`

### URL

```
{{server_pub_sir}}/api/v1/transaction/TX016
```

### Autenticación

No requiere autenticación.

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "transaction_id": "24260579-faf8-763f-aac7-5e16faff96d1",
  "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
  "cash_register_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "seller_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "adminitrastor_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "start_date": "12-09-2025",
  "end_date": "12-09-2025",
  "amount": 12.32
}
```

### Descripción del Cuerpo de la Solicitud

| Campo              | Tipo   | Descripción                           |
| ------------------ | ------ | ------------------------------------- |
| `transaction_id`   | string | ID UUID de la transacción             |
| `restaurant_id`    | string | ID UUID del restaurante               |
| `cash_register_id` | string | ID UUID de la caja registradora       |
| `seller_id`        | string | ID UUID del vendedor                  |
| `adminitrastor_id` | string | ID UUID del administrador             |
| `start_date`       | string | Fecha de inicio en formato DD-MM-YYYY |
| `end_date`         | string | Fecha de fin en formato DD-MM-YYYY    |
| `amount`           | number | Monto de la transacción               |

## Iniciar Propagación de Habilitación de Métodos de Pago de Franquicia

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
  "enabling_payments_methods": [
    {
      "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "cdn_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "payment_enabling": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
      "restaurants": [
        {
          "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "payment_enabling": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
          "cash_register": [
            {
              "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
              "payment_enabling": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"]
            }
          ]
        }
      ],
      "created_user": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "updated_user": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                                                        | Tipo     | Description                                       |
| ---------------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| `enabling_payments_methods`                                                  | array    | Array de métodos de pago habilitados              |
| `enabling_payments_methods[]._id`                                            | string   | Identificador único de la configuración           |
| `enabling_payments_methods[].user_id`                                        | string   | ID del usuario                                    |
| `enabling_payments_methods[].cdn_id`                                         | string   | ID del CDN                                        |
| `enabling_payments_methods[].payment_enabling`                               | string[] | Array de IDs de pagos habilitados                 |
| `enabling_payments_methods[].restaurants`                                    | array    | Array de restaurantes con pagos habilitados       |
| `enabling_payments_methods[].restaurants[]._id`                              | string   | ID del restaurante                                |
| `enabling_payments_methods[].restaurants[].payment_enabling`                 | string[] | Array de IDs de pagos habilitados del restaurante |
| `enabling_payments_methods[].restaurants[].cash_register`                    | array    | Array de cajas registradoras                      |
| `enabling_payments_methods[].restaurants[].cash_register[]._id`              | string   | ID de la caja registradora                        |
| `enabling_payments_methods[].restaurants[].cash_register[].payment_enabling` | string[] | Array de IDs de pagos habilitados de la caja      |
| `enabling_payments_methods[].created_user`                                   | string   | Usuario creador                                   |
| `enabling_payments_methods[].updated_user`                                   | string   | Usuario actualizador                              |
| `enabling_payments_methods[].created_at`                                     | string   | Fecha de creación (formato ISO 8601)              |
| `enabling_payments_methods[].updated_at`                                     | string   | Fecha de actualización (formato ISO 8601)         |

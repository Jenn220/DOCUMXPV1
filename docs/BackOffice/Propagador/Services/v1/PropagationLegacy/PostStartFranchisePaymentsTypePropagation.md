## Iniciar Propagación de Tipos de Pago de Franquicia

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
  "payments_types": [
    {
      "_id": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
      "country_id": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
      "cdn_id": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c10')",
      "user_id": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
      "payment_type_name": "Favoritos",
      "payment_methods": [
        {
          "_id": "UUID('343434-fbbe-4a3b-d24a-3360b5bf6c08')",
          "order": 1
        }
      ],
      "description": "Tipo de pagos para favoritos",
      "status_payment_type_id": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
      "order": 1,
      "created_at": "2024-02-09T17:18:10.139Z",
      "updated_at": "2024-03-03T15:20:55.223Z",
      "updated_user": "H9TaTQbOSNOoRwaJB4E9HQ"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                      | Tipo   | Description                               |
| ------------------------------------------ | ------ | ----------------------------------------- |
| `payments_types`                           | array  | Array de tipos de pago a propagar         |
| `payments_types[]._id`                     | string | Identificador único del tipo de pago      |
| `payments_types[].country_id`              | string | ID del país                               |
| `payments_types[].cdn_id`                  | string | ID del CDN                                |
| `payments_types[].user_id`                 | string | ID del usuario                            |
| `payments_types[].payment_type_name`       | string | Nombre del tipo de pago                   |
| `payments_types[].payment_methods`         | array  | Array de métodos de pago asociados        |
| `payments_types[].payment_methods[]._id`   | string | ID del método de pago                     |
| `payments_types[].payment_methods[].order` | number | Orden del método de pago                  |
| `payments_types[].description`             | string | Descripción del tipo de pago              |
| `payments_types[].status_payment_type_id`  | string | ID del estado del tipo de pago            |
| `payments_types[].order`                   | number | Orden del tipo de pago                    |
| `payments_types[].created_at`              | string | Fecha de creación (formato ISO 8601)      |
| `payments_types[].updated_at`              | string | Fecha de actualización (formato ISO 8601) |
| `payments_types[].updated_user`            | string | Identificador del usuario que actualizó   |

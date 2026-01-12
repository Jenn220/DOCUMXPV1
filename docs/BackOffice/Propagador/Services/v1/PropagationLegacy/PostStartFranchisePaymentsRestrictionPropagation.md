## Iniciar Propagación de Restricciones de Pago de Franquicia

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
  "restrictions": [
    {
      "_id": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
      "restriction_active": true,
      "franchises_restriction_active": true,
      "restaurants_restriction_active": true,
      "cash_registers_restriction_active": true,
      "payment_method_id": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
      "franchises": ["UUID('6c5a9727-9303-99b8-e363-552d320738ff')"],
      "restaurants": ["UUID('6c5a9727-9303-99b8-e363-552d320738ff')"],
      "cash_registers_suscriptions": [
        "UUID('6c5a9727-9303-99b8-e363-552d320738ff')"
      ],
      "created_user": "H9TaTQbOSNOoRwaJB4E9HQ",
      "created_at": "2024-02-09T17:18:10.139Z",
      "updated_at": "2024-03-03T15:20:55.223Z",
      "updated_user": "H9TaTQbOSNOoRwaJB4E9HQ"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                              | Tipo     | Description                                          |
| -------------------------------------------------- | -------- | ---------------------------------------------------- |
| `restrictions`                                     | array    | Array de restricciones de pago a propagar            |
| `restrictions[]._id`                               | string   | Identificador único de la restricción                |
| `restrictions[].restriction_active`                | boolean  | Indica si la restricción está activa                 |
| `restrictions[].franchises_restriction_active`     | boolean  | Indica si la restricción de franquicias está activa  |
| `restrictions[].restaurants_restriction_active`    | boolean  | Indica si la restricción de restaurantes está activa |
| `restrictions[].cash_registers_restriction_active` | boolean  | Indica si la restricción de cajas está activa        |
| `restrictions[].payment_method_id`                 | string   | ID del método de pago restringido                    |
| `restrictions[].franchises`                        | string[] | Array de IDs de franquicias restringidas             |
| `restrictions[].restaurants`                       | string[] | Array de IDs de restaurantes restringidos            |
| `restrictions[].cash_registers_suscriptions`       | string[] | Array de IDs de cajas registradoras restringidas     |
| `restrictions[].created_user`                      | string   | Identificador del usuario creador                    |
| `restrictions[].created_at`                        | string   | Fecha de creación (formato ISO 8601)                 |
| `restrictions[].updated_at`                        | string   | Fecha de actualización (formato ISO 8601)            |
| `restrictions[].updated_user`                      | string   | Identificador del usuario actualizador               |

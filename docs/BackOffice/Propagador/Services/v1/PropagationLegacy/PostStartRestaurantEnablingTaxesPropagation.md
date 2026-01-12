## Iniciar Propagación de Habilitación de Impuestos por Restaurante

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
  "restaurantEnablingTaxes": [
    {
      "_id": "d9b3cd1e-25c4-4a1e-b634-9f89f26e14db",
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurant_id": "e17d03da-b8b6-f424-febc-3a767b6401bb",
      "plus": [
        {
          "plu_id": "2d2ed803-ade4-eada-7f90-2af45a24ab0a",
          "enabling_taxes": [
            {
              "tax_id": "d00c4be9-a547-f72d-b87b-2abaebc07f4b",
              "configuration": [
                {
                  "start_date": "2025-07-10T19:19:42.021Z",
                  "end_date": "2025-07-14T19:19:42.021Z",
                  "tax_rate": 10
                }
              ]
            }
          ]
        }
      ],
      "created_user": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "updated_user": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "created_at": "2025-07-08T19:19:42.021Z",
      "updated_at": "2025-07-08T19:19:42.021Z"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                                                          | Tipo   | Description                             |
| ------------------------------------------------------------------------------ | ------ | --------------------------------------- |
| `restaurantEnablingTaxes`                                                      | array  | Array de configuraciones de impuestos   |
| `restaurantEnablingTaxes[]._id`                                                | string | Identificador único de la configuración |
| `restaurantEnablingTaxes[].user_id`                                            | string | ID del usuario                          |
| `restaurantEnablingTaxes[].cdn_id`                                             | string | ID del CDN                              |
| `restaurantEnablingTaxes[].restaurant_id`                                      | string | ID del restaurante                      |
| `restaurantEnablingTaxes[].plus`                                               | array  | Array de PLUs con impuestos habilitados |
| `restaurantEnablingTaxes[].plus[].plu_id`                                      | string | ID del PLU                              |
| `restaurantEnablingTaxes[].plus[].enabling_taxes`                              | array  | Array de impuestos habilitados          |
| `restaurantEnablingTaxes[].plus[].enabling_taxes[].tax_id`                     | string | ID del impuesto                         |
| `restaurantEnablingTaxes[].plus[].enabling_taxes[].configuration`              | array  | Array de configuraciones del impuesto   |
| `restaurantEnablingTaxes[].plus[].enabling_taxes[].configuration[].start_date` | string | Fecha de inicio (ISO 8601)              |
| `restaurantEnablingTaxes[].plus[].enabling_taxes[].configuration[].end_date`   | string | Fecha de fin (ISO 8601)                 |
| `restaurantEnablingTaxes[].plus[].enabling_taxes[].configuration[].tax_rate`   | number | Tasa del impuesto                       |
| `restaurantEnablingTaxes[].created_user`                                       | string | Usuario creador                         |
| `restaurantEnablingTaxes[].updated_user`                                       | string | Usuario actualizador                    |
| `restaurantEnablingTaxes[].created_at`                                         | string | Fecha de creación (ISO 8601)            |
| `restaurantEnablingTaxes[].updated_at`                                         | string | Fecha de actualización (ISO 8601)       |

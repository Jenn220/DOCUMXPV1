## Iniciar Propagación de Campañas de Subsidio

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
  "Campaigns": [
    {
      "_id": "campaign_001",
      "cdn_id": "cdn_001",
      "restuarant_id": "restaurant_001",
      "name": "Summer Promotion",
      "description": "Special discount for summer season",
      "image": "https://example.com/campaign.jpg",
      "start_date": "2024-06-01T00:00:00Z",
      "end_date": "2024-08-31T23:59:59Z",
      "value": 10,
      "currency": "USD",
      "enabled": true,
      "limit_per_client": 1,
      "payment_methods": ["credit_card", "debit_card"]
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                          | Tipo     | Description                          |
| ------------------------------ | -------- | ------------------------------------ |
| `Campaigns`                    | array    | Array de campañas a propagar         |
| `Campaigns[]._id`              | string   | Identificador único de la campaña    |
| `Campaigns[].cdn_id`           | string   | ID del CDN                           |
| `Campaigns[].restuarant_id`    | string   | ID del restaurante                   |
| `Campaigns[].name`             | string   | Nombre de la campaña                 |
| `Campaigns[].description`      | string   | Descripción de la campaña            |
| `Campaigns[].image`            | string   | URL de la imagen de la campaña       |
| `Campaigns[].start_date`       | string   | Fecha de inicio (formato ISO 8601)   |
| `Campaigns[].end_date`         | string   | Fecha de fin (formato ISO 8601)      |
| `Campaigns[].value`            | number   | Valor del subsidio o descuento       |
| `Campaigns[].currency`         | string   | Moneda del valor                     |
| `Campaigns[].enabled`          | boolean  | Indica si la campaña está habilitada |
| `Campaigns[].limit_per_client` | number   | Límite de uso por cliente            |
| `Campaigns[].payment_methods`  | string[] | Array de métodos de pago aplicables  |

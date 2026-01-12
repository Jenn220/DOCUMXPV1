## Insertar o Actualizar Orden

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/purchaseorders/api/v1/order/upsert_order
```

### Parámetros de Query

| Key                | Value                                | Descripción                           |
| ------------------ | ------------------------------------ | ------------------------------------- |
| franchise          | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia        |
| franchise_name     | KFC                                  | Nombre de la franquicia               |
| restaurant         | 18ab3836-3202-f6d4-1eef-a5b5de5a8e40 | Identificador del restaurante         |
| restaurant_name    | Restaurant Centro                    | Nombre del restaurante                |
| cash_register      | aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0 | Identificador de la caja registradora |
| cash_register_name | Caja 2                               | Nombre de la caja registradora        |
| user_seller        | c17b6e8d-88a5-9eb5-1f44-aeec161494da | Identificador del usuario vendedor    |
| user_seller_name   | Juan Perez                           | Nombre del usuario vendedor           |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "order_id": "902499bf-284f-4f2e-80b7-60ef60c6bd9c",
  "franchise_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
  "cash_register_id": "aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0",
  "user_seller_id": "c17b6e8d-88a5-9eb5-1f44-aeec161494da",
  "order_type": "DINE_IN",
  "order_status": "PENDING",
  "total_amount": 25.5,
  "items": [
    {
      "product_id": "9bdeeb7f-136c-8f6a-489b-d9fc02db904a",
      "product_name": "Chicken Bucket",
      "quantity": 2,
      "unit_price": 12.75
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                  | Tipo   | Descripción                           |
| ---------------------- | ------ | ------------------------------------- |
| `order_id`             | string | Identificador único de la orden       |
| `franchise_id`         | string | Identificador de la franquicia        |
| `restaurant_id`        | string | Identificador del restaurante         |
| `cash_register_id`     | string | Identificador de la caja registradora |
| `user_seller_id`       | string | Identificador del usuario vendedor    |
| `order_type`           | string | Tipo de orden                         |
| `order_status`         | string | Estado de la orden                    |
| `total_amount`         | number | Monto total de la orden               |
| `items`                | array  | Lista de productos en la orden        |
| `items[].product_id`   | string | Identificador del producto            |
| `items[].product_name` | string | Nombre del producto                   |
| `items[].quantity`     | number | Cantidad del producto                 |
| `items[].unit_price`   | number | Precio unitario del producto          |

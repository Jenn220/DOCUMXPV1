## Crear y Asociar Producto a Programación

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |
| `country`   | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "string",
  "description": "string",
  "products": [
    {
      "plu_id": "string",
      "price": 0
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo               | Tipo   | Description                            |
| ------------------- | ------ | -------------------------------------- |
| `name`              | string | Nombre de la programación              |
| `description`       | string | Descripción de la programación         |
| `products`          | array  | Array de productos a asociar           |
| `products[].plu_id` | string | ID del PLU del producto                |
| `products[].price`  | number | Precio del producto en la programación |

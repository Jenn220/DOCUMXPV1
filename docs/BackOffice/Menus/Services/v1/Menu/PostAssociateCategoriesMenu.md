## Asociar Categorías al Menú

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/menu/associate_categories_menu
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "menu_id": "string",
  "categories": [
    {
      "category_id": "string",
      "order": 0,
      "products": [
        {
          "plu_id": "string",
          "order": 0
        }
      ]
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                            | Tipo   | Description                                  |
| -------------------------------- | ------ | -------------------------------------------- |
| `menu_id`                        | string | ID del menú al que se asocian las categorías |
| `categories`                     | array  | Array de categorías a asociar                |
| `categories[].category_id`       | string | ID de la categoría                           |
| `categories[].order`             | number | Orden de la categoría en el menú             |
| `categories[].products`          | array  | Array de productos de la categoría           |
| `categories[].products[].plu_id` | string | ID del PLU del producto                      |
| `categories[].products[].order`  | number | Orden del producto dentro de la categoría    |

## Iniciar Propagación de Restricciones

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
  "Restrictions": [
    {
      "menu_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "categories": [
        {
          "menu_category_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "plus": [
            {
              "plu_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
          ]
        }
      ]
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                          | Tipo   | Description                           |
| ---------------------------------------------- | ------ | ------------------------------------- |
| `Restrictions`                                 | array  | Array de restricciones a propagar     |
| `Restrictions[].menu_id`                       | string | ID del menú con restricciones         |
| `Restrictions[].categories`                    | array  | Array de categorías con restricciones |
| `Restrictions[].categories[].menu_category_id` | string | ID de la categoría del menú           |
| `Restrictions[].categories[].plus`             | array  | Array de PLUs con restricciones       |
| `Restrictions[].categories[].plus[].plu_id`    | string | ID del PLU con restricción            |

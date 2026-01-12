## Iniciar Propagación de Menú

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
  "menus": [
    {
      "_id": "8d1571c9-9f1e-42a8-b1c2-6c29c38efb0e",
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "cdn_id": "c8c170f7-ea82-4197-a3fe-ea10b0dd95cc",
      "status_menu": "17452f45-a332-3b37-183f-8bd42b23151a",
      "half_integration_id": "cdcf691e-5dbe-fcae-99a9-3b04a5dd54a6",
      "menu_name": "Menu 1 - propagador",
      "classifications": ["aea9ed0d-938b-461a-ab1b-609fb945a0d7"],
      "limit_columns_category": 6,
      "limit_rows_category": 15,
      "limit_columns_plu": 6,
      "limit_rows_plu": 15,
      "icon": {
        "icon_id": null,
        "color_id": "47e46868-4f64-74b6-80d0-951815d826cc"
      },
      "description": "Descripcion menu 1 - propagador",
      "images_menu": [
        {
          "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "extension": "jpg",
          "name": "imagen1",
          "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d41797a1fb83_domicilio_4486_744x744_1678487100.png?d=400x400&format=webp%22",
          "description": "",
          "size": {
            "width": 100,
            "height": 1000
          },
          "device_image": "b4645748-78c2-0160-5667-79105889c1d7",
          "path": "string"
        }
      ],
      "categories": [
        {
          "category_id": "0394a625-6e7f-3914-d2a1-54c67e47369f",
          "pos_y": 0,
          "pos_x": 0,
          "plus": [
            {
              "plu_id": "755e02cc-712a-4dab-ab0b-948e8252e24b",
              "pos_y": 0,
              "pos_x": 0
            }
          ]
        }
      ],
      "created_at": "2024-11-19T21:37:24.819Z",
      "updated_at": "2024-11-19T21:37:24.820Z"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                | Tipo     | Description                               |
| ------------------------------------ | -------- | ----------------------------------------- |
| `menus`                              | array    | Array de menús a propagar                 |
| `menus[]._id`                        | string   | Identificador único del menú              |
| `menus[].user_id`                    | string   | ID del usuario                            |
| `menus[].cdn_id`                     | string   | ID del CDN                                |
| `menus[].status_menu`                | string   | ID del estado del menú                    |
| `menus[].half_integration_id`        | string   | ID de integración parcial                 |
| `menus[].menu_name`                  | string   | Nombre del menú                           |
| `menus[].classifications`            | string[] | Array de IDs de clasificaciones           |
| `menus[].limit_columns_category`     | number   | Límite de columnas para categorías        |
| `menus[].limit_rows_category`        | number   | Límite de filas para categorías           |
| `menus[].limit_columns_plu`          | number   | Límite de columnas para PLUs              |
| `menus[].limit_rows_plu`             | number   | Límite de filas para PLUs                 |
| `menus[].icon`                       | object   | Objeto de icono del menú                  |
| `menus[].icon.icon_id`               | string   | ID del icono (puede ser null)             |
| `menus[].icon.color_id`              | string   | ID del color del icono                    |
| `menus[].description`                | string   | Descripción del menú                      |
| `menus[].images_menu`                | array    | Array de imágenes del menú                |
| `menus[].images_menu[].user_id`      | string   | ID del usuario                            |
| `menus[].images_menu[].extension`    | string   | Extensión del archivo de imagen           |
| `menus[].images_menu[].name`         | string   | Nombre de la imagen                       |
| `menus[].images_menu[].sas_url`      | string   | URL SAS de la imagen                      |
| `menus[].images_menu[].description`  | string   | Descripción de la imagen                  |
| `menus[].images_menu[].size`         | object   | Dimensiones de la imagen                  |
| `menus[].images_menu[].size.width`   | number   | Ancho de la imagen                        |
| `menus[].images_menu[].size.height`  | number   | Alto de la imagen                         |
| `menus[].images_menu[].device_image` | string   | ID del dispositivo de imagen              |
| `menus[].images_menu[].path`         | string   | Ruta de almacenamiento de la imagen       |
| `menus[].categories`                 | array    | Array de categorías del menú              |
| `menus[].categories[].category_id`   | string   | ID de la categoría                        |
| `menus[].categories[].pos_y`         | number   | Posición Y de la categoría                |
| `menus[].categories[].pos_x`         | number   | Posición X de la categoría                |
| `menus[].categories[].plus`          | array    | Array de PLUs en la categoría             |
| `menus[].categories[].plus[].plu_id` | string   | ID del PLU                                |
| `menus[].categories[].plus[].pos_y`  | number   | Posición Y del PLU                        |
| `menus[].categories[].plus[].pos_x`  | number   | Posición X del PLU                        |
| `menus[].created_at`                 | string   | Fecha de creación (formato ISO 8601)      |
| `menus[].updated_at`                 | string   | Fecha de actualización (formato ISO 8601) |

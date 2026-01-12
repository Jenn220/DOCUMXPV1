## Iniciar Propagación de PLU

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
  "plus": [
    {
      "_id": "755e02cc-712a-4dab-ab0b-948e8252e24b",
      "cdn_plu_id": 1,
      "user_id": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c08",
      "plu_name": "plu 1 - propagador",
      "plu_description": "desc plu 1 propagador",
      "cdn_id": "c8c170f7-ea82-4197-a3fe-ea10b0dd95cc",
      "status_plu": "298db0ef-6a0d-4ac6-961c-a5fd9319e272",
      "type_plu": "b5b152bc-27df-479f-ba70-d6d061cd3a88",
      "images_plu": [
        {
          "user_id": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c08",
          "extension": "jpg",
          "name": "Imagen2",
          "sas_url": "https://images.getduna.com/5fe6067e-0e11-4869-9118-ad3dcc8765c2/6c64d41797a1fb83_domicilio_4486_744x744_1678487100.png?d=400x400&format=webp%22",
          "description": "Descripción de la imagen",
          "size": {
            "width": 312,
            "height": 315
          },
          "device_image": "9d6bfa70-fe9f-4545-af90-b3bbf381cd73",
          "path": "/accessStorage/kkcDev/imagen2.jpg"
        }
      ],
      "categories": [
        {
          "category_id": "bd88a6d6-95e7-4c39-abad-47dbafda1edc",
          "classifications": [
            {
              "classification_id": "7a3cf64c-3a21-4336-a452-dd93370fc5c8",
              "price": {
                "user_id": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c08",
                "net_value": 0,
                "tax_value": 0,
                "retail_price": 0
              }
            }
          ]
        }
      ],
      "suggested_questions": [
        {
          "suggested_question_id": "a39c9b2d-2f91-4f60-925b-fd89b02e873f",
          "order": 0,
          "answers": [
            {
              "answer_id": "4f9e7d5a-704f-4c79-9d1e-a463384d313c",
              "order": 0
            }
          ]
        }
      ],
      "taxes": [
        "1f179ca5-ea83-4379-8b29-5a9b0469f7db",
        "61bc0ebe-a720-4427-b4f6-64da271797b3"
      ],
      "classifications": ["aea9ed0d-938b-461a-ab1b-609fb945a0d7"],
      "departments": ["7a1ce210-1593-4646-9c1a-664b6d53e21f"],
      "tags": ["pollos"]
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                                      | Tipo     | Description                         |
| ---------------------------------------------------------- | -------- | ----------------------------------- |
| `plus`                                                     | array    | Array de PLUs a propagar            |
| `plus[]._id`                                               | string   | Identificador único del PLU         |
| `plus[].cdn_plu_id`                                        | number   | ID del PLU en CDN                   |
| `plus[].user_id`                                           | string   | ID del usuario                      |
| `plus[].plu_name`                                          | string   | Nombre del PLU                      |
| `plus[].plu_description`                                   | string   | Descripción del PLU                 |
| `plus[].cdn_id`                                            | string   | ID del CDN                          |
| `plus[].status_plu`                                        | string   | ID del estado del PLU               |
| `plus[].type_plu`                                          | string   | ID del tipo de PLU                  |
| `plus[].images_plu`                                        | array    | Array de imágenes del PLU           |
| `plus[].images_plu[].user_id`                              | string   | ID del usuario                      |
| `plus[].images_plu[].extension`                            | string   | Extensión del archivo de imagen     |
| `plus[].images_plu[].name`                                 | string   | Nombre de la imagen                 |
| `plus[].images_plu[].sas_url`                              | string   | URL SAS de la imagen                |
| `plus[].images_plu[].description`                          | string   | Descripción de la imagen            |
| `plus[].images_plu[].size`                                 | object   | Dimensiones de la imagen            |
| `plus[].images_plu[].size.width`                           | number   | Ancho de la imagen                  |
| `plus[].images_plu[].size.height`                          | number   | Alto de la imagen                   |
| `plus[].images_plu[].device_image`                         | string   | ID del dispositivo de imagen        |
| `plus[].images_plu[].path`                                 | string   | Ruta de almacenamiento de la imagen |
| `plus[].categories`                                        | array    | Array de categorías asociadas       |
| `plus[].categories[].category_id`                          | string   | ID de la categoría                  |
| `plus[].categories[].classifications`                      | array    | Array de clasificaciones            |
| `plus[].categories[].classifications[].classification_id`  | string   | ID de la clasificación              |
| `plus[].categories[].classifications[].price`              | object   | Objeto de precio                    |
| `plus[].categories[].classifications[].price.user_id`      | string   | ID del usuario                      |
| `plus[].categories[].classifications[].price.net_value`    | number   | Valor neto                          |
| `plus[].categories[].classifications[].price.tax_value`    | number   | Valor del impuesto                  |
| `plus[].categories[].classifications[].price.retail_price` | number   | Precio de venta al público          |
| `plus[].suggested_questions`                               | array    | Array de preguntas sugeridas        |
| `plus[].suggested_questions[].suggested_question_id`       | string   | ID de la pregunta sugerida          |
| `plus[].suggested_questions[].order`                       | number   | Orden de la pregunta                |
| `plus[].suggested_questions[].answers`                     | array    | Array de respuestas                 |
| `plus[].suggested_questions[].answers[].answer_id`         | string   | ID de la respuesta                  |
| `plus[].suggested_questions[].answers[].order`             | number   | Orden de la respuesta               |
| `plus[].taxes`                                             | string[] | Array de IDs de impuestos           |
| `plus[].classifications`                                   | string[] | Array de IDs de clasificaciones     |
| `plus[].departments`                                       | string[] | Array de IDs de departamentos       |
| `plus[].tags`                                              | string[] | Array de etiquetas                  |

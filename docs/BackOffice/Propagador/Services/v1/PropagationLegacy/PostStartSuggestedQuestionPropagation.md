## Iniciar Propagación de Preguntas Sugeridas

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
  "suggestedQuestions": [
    {
      "_id": "a39c9b2d-2f91-4f60-925b-fd89b02e873f",
      "sug_question_min_responses": 1,
      "sug_question_max_responses": 5,
      "cdn_id": "c8c170f7-ea82-4197-a3fe-ea10b0dd95cc",
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "sug_question_pos_description": "Suggested Question propagator 1",
      "sug_question_tittle": "Title sug Question Propag",
      "status_suggested_question_id": "23d7656e-1a9f-3f31-e826-3b734a832dfe",
      "type_question_id": "348d77b3-ccf9-4f2d-8664-3051a64e2b33",
      "answers": [
        {
          "answer_id": "3fa85f64-5717-4562-b3fc-2c963f66afa5",
          "order": 0,
          "plu_id": "755e02cc-712a-4dab-ab0b-948e8252e24b",
          "answer_pos_description": "Respuesta Propagador 1",
          "next_questions": []
        }
      ],
      "created_at": "2024-12-05T13:48:13.402Z",
      "updated_at": "2024-12-05T13:48:13.402Z",
      "copy": 0
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                                   | Tipo   | Description                                 |
| ------------------------------------------------------- | ------ | ------------------------------------------- |
| `suggestedQuestions`                                    | array  | Array de preguntas sugeridas a propagar     |
| `suggestedQuestions[]._id`                              | string | Identificador único de la pregunta sugerida |
| `suggestedQuestions[].sug_question_min_responses`       | number | Número mínimo de respuestas requeridas      |
| `suggestedQuestions[].sug_question_max_responses`       | number | Número máximo de respuestas permitidas      |
| `suggestedQuestions[].cdn_id`                           | string | ID del CDN                                  |
| `suggestedQuestions[].user_id`                          | string | ID del usuario                              |
| `suggestedQuestions[].sug_question_pos_description`     | string | Descripción de la pregunta sugerida         |
| `suggestedQuestions[].sug_question_tittle`              | string | Título de la pregunta sugerida              |
| `suggestedQuestions[].status_suggested_question_id`     | string | ID del estado de la pregunta sugerida       |
| `suggestedQuestions[].type_question_id`                 | string | ID del tipo de pregunta                     |
| `suggestedQuestions[].answers`                          | array  | Array de respuestas asociadas               |
| `suggestedQuestions[].answers[].answer_id`              | string | ID de la respuesta                          |
| `suggestedQuestions[].answers[].order`                  | number | Orden de la respuesta                       |
| `suggestedQuestions[].answers[].plu_id`                 | string | ID del PLU asociado a la respuesta          |
| `suggestedQuestions[].answers[].answer_pos_description` | string | Descripción de la respuesta                 |
| `suggestedQuestions[].answers[].next_questions`         | array  | Array de preguntas siguientes               |
| `suggestedQuestions[].created_at`                       | string | Fecha de creación (formato ISO 8601)        |
| `suggestedQuestions[].updated_at`                       | string | Fecha de actualización (formato ISO 8601)   |
| `suggestedQuestions[].copy`                             | number | Indicador de copia                          |

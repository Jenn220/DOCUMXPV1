## Actualizar Pregunta Sugerida

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/suggestedquestion/update
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `c17b6e8d-88a5-9eb5-1f44-aeec161494da` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "question": "string",
  "answers": [
    {
      "id": "string",
      "answer": "string",
      "order": 0
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo              | Tipo   | Description                             |
| ------------------ | ------ | --------------------------------------- |
| `id`               | string | ID de la pregunta sugerida a actualizar |
| `question`         | string | Texto de la pregunta                    |
| `answers`          | array  | Array de respuestas                     |
| `answers[].id`     | string | ID de la respuesta                      |
| `answers[].answer` | string | Texto de la respuesta                   |
| `answers[].order`  | number | Orden de la respuesta                   |

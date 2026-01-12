## Crear Pregunta Sugerida

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/suggestedquestion/create
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "question": "string",
  "answers": [
    {
      "answer": "string",
      "order": 0
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo              | Tipo   | Description           |
| ------------------ | ------ | --------------------- |
| `question`         | string | Texto de la pregunta  |
| `answers`          | array  | Array de respuestas   |
| `answers[].answer` | string | Texto de la respuesta |
| `answers[].order`  | number | Orden de la respuesta |

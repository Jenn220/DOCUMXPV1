## Asociar Productos a Pregunta Sugerida

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/suggestedquestion/associate_products_to_suggested_question
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `c17b6e8d-88a5-9eb5-1f44-aeec161494da` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "suggested_question_id": "string",
  "plus": ["string"]
}
```

### Descripción de Campos del Cuerpo

| Campo                   | Tipo     | Description                    |
| ----------------------- | -------- | ------------------------------ |
| `suggested_question_id` | string   | ID de la pregunta sugerida     |
| `plus`                  | string[] | Array de IDs de PLUs a asociar |

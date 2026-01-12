## Desasociar Pregunta Sugerida de PLUs

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/product/disassociate_suggestedquestion_for_plus
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "suggested_question_id": "string",
  "plus": ["string"]
}
```

### Descripción de Campos del Cuerpo

| Campo                   | Tipo     | Description                             |
| ----------------------- | -------- | --------------------------------------- |
| `suggested_question_id` | string   | ID de la pregunta sugerida a desasociar |
| `plus`                  | string[] | Array de IDs de PLUs a desasociar       |

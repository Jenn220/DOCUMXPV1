## Obtener Categorías por Clasificación y Franquicia

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

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "classification_ids": ["string"],
  "search": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo                | Tipo     | Description                                 |
| -------------------- | -------- | ------------------------------------------- |
| `classification_ids` | string[] | Array de IDs de clasificaciones a filtrar   |
| `search`             | string   | Término de búsqueda para filtrar categorías |

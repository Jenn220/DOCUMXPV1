## Actualizar Categoría con Información Básica

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/category/updatewithbasicinfo
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `country`   | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "short_name": "string",
  "status_id": "string",
  "parent_category_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo                | Tipo   | Description                          |
| -------------------- | ------ | ------------------------------------ |
| `id`                 | string | ID de la categoría a actualizar      |
| `name`               | string | Nombre de la categoría               |
| `description`        | string | Descripción de la categoría          |
| `short_name`         | string | Nombre corto de la categoría         |
| `status_id`          | string | ID del estado de la categoría        |
| `parent_category_id` | string | ID de la categoría padre (si aplica) |

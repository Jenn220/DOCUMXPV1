## Actualizar Categoría de Menú

### Método HTTP

`PUT`

### URL

```
{{server_BO_Menus}}/api/v1/menucategory/update_category
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "short_name": "string",
  "icon_id": "string",
  "image_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo         | Tipo   | Description                     |
| ------------- | ------ | ------------------------------- |
| `id`          | string | ID de la categoría a actualizar |
| `name`        | string | Nombre de la categoría          |
| `description` | string | Descripción de la categoría     |
| `short_name`  | string | Nombre corto de la categoría    |
| `icon_id`     | string | ID del icono de la categoría    |
| `image_id`    | string | ID de la imagen de la categoría |

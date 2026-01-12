## Actualizar Información Básica del Menú

### Método HTTP

`PUT`

### URL

```
{{server_BO_Menus}}/api/v1/menu/updatebasicinfo
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "menu_id": "string",
  "name": "string",
  "description": "string",
  "icon_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo         | Tipo   | Description              |
| ------------- | ------ | ------------------------ |
| `menu_id`     | string | ID del menú a actualizar |
| `name`        | string | Nombre del menú          |
| `description` | string | Descripción del menú     |
| `icon_id`     | string | ID del icono del menú    |

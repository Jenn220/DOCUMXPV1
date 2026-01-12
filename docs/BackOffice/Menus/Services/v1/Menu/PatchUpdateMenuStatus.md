## Actualizar Estado del Menú

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/menu/update_menu_status
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "menu_id": "string",
  "status_id": "string",
  "user_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo       | Tipo   | Description                          |
| ----------- | ------ | ------------------------------------ |
| `menu_id`   | string | ID del menú a actualizar             |
| `status_id` | string | ID del nuevo estado del menú         |
| `user_id`   | string | ID del usuario que realiza la acción |

## Eliminar Upselling

### Método HTTP

`DELETE`

### URL

```
{{server_BO_Menus}}/api/v1/upselling/delete
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "user_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo     | Tipo   | Description                          |
| --------- | ------ | ------------------------------------ |
| `id`      | string | ID del upselling a eliminar          |
| `user_id` | string | ID del usuario que realiza la acción |

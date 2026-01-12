## Actualizar Estado del Producto

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/product/updateproductstatus
```

### Parámetros de Query

| Key            | Value                                  | Description         |
| -------------- | -------------------------------------- | ------------------- |
| `franchise_id` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "plu_id": "string",
  "status_id": "string",
  "user_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo       | Tipo   | Description                          |
| ----------- | ------ | ------------------------------------ | --------------------------------- |
| `plu_id`    | string | ID del PLU del producto              |
| `status_id` | string | ID del nuevo estado del producto     |
| `user_id`   | string | ID del usuario que realiza la acción | ## Actualizar Estado del Producto |

### Método HTTP

`PATCH`

### URL

```
{{server_BO_Menus}}/api/v1/product/updateproductstatus
```

### Parámetros de Query

| Key            | Value                                  | Description         |
| -------------- | -------------------------------------- | ------------------- |
| `franchise_id` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "plu_id": "string",
  "status_id": "string",
  "user_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo       | Tipo   | Description                          |
| ----------- | ------ | ------------------------------------ |
| `plu_id`    | string | ID del PLU del producto              |
| `status_id` | string | ID del nuevo estado del producto     |
| `user_id`   | string | ID del usuario que realiza la acción |

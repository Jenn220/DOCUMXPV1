## Actualizar Upselling

### Método HTTP

`PUT`

### URL

```
{{server_BO_Menus}}/api/v1/upselling/update
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "user_id": "string",
  "plu_father": "string",
  "plu_references": [
    {
      "plu_id": "string",
      "order": 0
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                     | Tipo   | Description                   |
| ------------------------- | ------ | ----------------------------- |
| `id`                      | string | ID del upselling a actualizar |
| `user_id`                 | string | ID del usuario que actualiza  |
| `plu_father`              | string | ID del PLU padre              |
| `plu_references`          | array  | Array de referencias de PLUs  |
| `plu_references[].plu_id` | string | ID del PLU referenciado       |
| `plu_references[].order`  | number | Orden del PLU en el upselling |

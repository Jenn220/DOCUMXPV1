## Iniciar Propagación de Upselling

### Método HTTP

`POST`

### URL

```
{{server_propagation}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key          | Value                                  | Description                       |
| ------------ | -------------------------------------- | --------------------------------- |
| `user`       | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |
| `country_id` | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "upsellings": [
    {
      "_id": "4bbd9f64-5717-4562-b3fc-2c963f66afa6",
      "plu_references": [
        {
          "id_plu": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c07",
          "order": 0
        }
      ],
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "plu_father": "755e02cc-712a-4dab-ab0b-948e8252e24b",
      "created_at": "2024-12-08T03:41:28.065Z",
      "updated_at": "2024-12-08T03:41:28.065Z"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo                                  | Tipo   | Description                               |
| -------------------------------------- | ------ | ----------------------------------------- |
| `upsellings`                           | array  | Array de upsellings a propagar            |
| `upsellings[]._id`                     | string | Identificador único del upselling         |
| `upsellings[].plu_references`          | array  | Array de referencias de PLUs              |
| `upsellings[].plu_references[].id_plu` | string | ID del PLU referenciado                   |
| `upsellings[].plu_references[].order`  | number | Orden del PLU en el upselling             |
| `upsellings[].user_id`                 | string | ID del usuario                            |
| `upsellings[].plu_father`              | string | ID del PLU padre                          |
| `upsellings[].created_at`              | string | Fecha de creación (formato ISO 8601)      |
| `upsellings[].updated_at`              | string | Fecha de actualización (formato ISO 8601) |

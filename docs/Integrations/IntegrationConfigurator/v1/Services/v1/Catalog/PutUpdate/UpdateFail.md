## Actualizar Catálogo (con Error)

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/update
```

### Parámetros de Query

| Key  | Value                                  | Description                        |
| ---- | -------------------------------------- | ---------------------------------- |
| `id` | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID único del catálogo a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "prueba",
  "value": "prueba",
  "fatherId": "0",
  "detail": "",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Error - No Actualizado

```json
{
  "code": "21",
  "messages": ["no Actualizado correctamente"],
  "data": {}
}
```

### Descripción de la Respuesta de Error

| Campo      | Descripción                                |
| ---------- | ------------------------------------------ |
| `code`     | Código de respuesta interno ("21" = error) |
| `messages` | Array con mensajes de error                |
| `data`     | Objeto vacío                               |

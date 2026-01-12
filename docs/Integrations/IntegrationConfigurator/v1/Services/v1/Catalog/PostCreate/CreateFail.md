## Crear Catálogo (con Error)

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/catalogs
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "prueba",
  "value": "prueba",
  "fatherId": "0",
  "detail": "",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Error - No Creado

```json
{
  "code": "11",
  "messgaes": ["no creado correctamente"],
  "data": {}
}
```

### Descripción de la Respuesta de Error

| Campo      | Descripción                                |
| ---------- | ------------------------------------------ |
| `code`     | Código de respuesta interno ("11" = error) |
| `messgaes` | Array con mensajes de error                |
| `data`     | Objeto vacío                               |

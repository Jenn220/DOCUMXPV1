## Obtener Asignaciones de Integraciones Paginadas (con Error)

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "string",
  "sort_order": 0,
  "sort_field": "string",
  "rows": 20,
  "first": 1,
  "activeOnly": true
}
```

### 400 Bad Request / 500 Internal Server Error

```json
{
  "code": 400,
  "status": "error",
  "message": "Invalid date format",
  "errors": {}
}
```

### Descripción de la Respuesta de Error

| Campo     | Descripción                               |
| --------- | ----------------------------------------- |
| `code`    | Código de estado HTTP (400 o 500)         |
| `status`  | Estado de la respuesta ("error")          |
| `message` | Mensaje descriptivo del error             |
| `errors`  | Objeto con detalles adicionales del error |

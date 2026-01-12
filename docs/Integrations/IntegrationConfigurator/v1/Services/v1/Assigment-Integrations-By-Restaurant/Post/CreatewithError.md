## Crear Integración (con Error)

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/integrations/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchiseId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "status": "A",
  "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
  "userId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "hourToExecute": ""
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

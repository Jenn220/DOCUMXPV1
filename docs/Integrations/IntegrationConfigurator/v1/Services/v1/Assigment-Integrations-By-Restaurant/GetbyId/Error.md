## Obtener Asignación de Integraciones por ID (con Error)

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key  | Value                                  | Description                           |
| ---- | -------------------------------------- | ------------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID único de la asignación a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

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

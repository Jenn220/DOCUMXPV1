## Eliminar Servidor

### Método HTTP

`DELETE`

### URL

```
{{server_orchestrator}}/api/v1/servers/delete
```

### Parámetros de Query

| Key  | Value                                  | Description                      |
| ---- | -------------------------------------- | -------------------------------- |
| `id` | `7654cb16-e955-4605-8579-b891a67f94c7` | ID único del servidor a eliminar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Eliminación Exitosa

```json
{
  "code": 10,
  "messages": ["deleted succefully"],
  "data": {
    "id": "7654cb16-e955-4605-8579-b891a67f94c7"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo      | Descripción                                      |
| ---------- | ------------------------------------------------ |
| `code`     | Código de respuesta interno (10 = éxito)         |
| `messages` | Array de mensajes informativos                   |
| `data`     | Objeto con la información del servidor eliminado |
| `data.id`  | ID del servidor eliminado                        |

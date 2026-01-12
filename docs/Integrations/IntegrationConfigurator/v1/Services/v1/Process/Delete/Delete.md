## Eliminar Proceso

### Método HTTP

`DELETE`

### URL

```
{{server_orchestrator}}/api/v1/processes/delete
```

### Parámetros de Query

| Key  | Value                                  | Description                     |
| ---- | -------------------------------------- | ------------------------------- |
| `id` | `a627d86f-1092-4341-a9ad-21e6efc5f8c1` | ID único del proceso a eliminar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Eliminación Exitosa

```json
{
  "code": 10,
  "messages": ["deleted succefully"],
  "data": {
    "id": "a627d86f-1092-4341-a9ad-21e6efc5f8c1"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo      | Descripción                                     |
| ---------- | ----------------------------------------------- |
| `code`     | Código de respuesta interno (10 = éxito)        |
| `messages` | Array de mensajes informativos                  |
| `data`     | Objeto con la información del proceso eliminado |
| `data.id`  | ID del proceso eliminado                        |

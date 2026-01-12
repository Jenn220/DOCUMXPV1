## Eliminar Sincronización

### Método HTTP

`DELETE`

### URL

```
{{server_orchestrator}}/api/v1/synchronizations/delete
```

### Parámetros de Query

| Key  | Value                                  | Description                        |
| ---- | -------------------------------------- | ---------------------------------- |
| `id` | `7654cb16-e955-4605-8579-b891a67f94c7` | ID de la sincronización a eliminar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Eliminación Exitosa

```json
{
  "code": 10,
  "messages": ["deleted succefully"],
  "data": {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa10aec"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo      | Descripción                              |
| ---------- | ---------------------------------------- |
| `code`     | Código de respuesta interno (10 = éxito) |
| `messages` | Array con mensajes del resultado         |
| `data`     | Objeto con los datos de la eliminación   |
| `data.id`  | ID de la sincronización eliminada        |

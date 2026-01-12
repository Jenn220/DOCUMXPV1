## Eliminar Integración

### Método HTTP

`DELETE`

### URL

```
{{server_orchestrator}}/api/v1/integrations/delete
```

### Parámetros de Query

| Key  | Value                                  | Description                           |
| ---- | -------------------------------------- | ------------------------------------- |
| `id` | `e47c3813-7daf-407f-bc02-544d57290f1b` | ID único de la integración a eliminar |

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

| Campo      | Descripción                                           |
| ---------- | ----------------------------------------------------- |
| `code`     | Código de respuesta interno (10 = éxito)              |
| `messages` | Array de mensajes informativos                        |
| `data`     | Objeto con la información de la integración eliminada |
| `data.id`  | ID de la integración eliminada                        |

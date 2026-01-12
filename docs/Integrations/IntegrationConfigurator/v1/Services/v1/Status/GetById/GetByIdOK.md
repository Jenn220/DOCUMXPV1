## Obtener Estado por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/status/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                     |
| ---- | -------------------------------------- | ------------------------------- |
| `id` | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID único del estado a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "key": "active",
    "text": "Activo",
    "color": "#1B3E19",
    "background": "#E2F7E2"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo             | Descripción                              |
| ----------------- | ---------------------------------------- |
| `code`            | Código de respuesta interno (20 = éxito) |
| `messages`        | Array de mensajes informativos           |
| `data`            | Objeto con la información del estado     |
| `data.id`         | ID del estado                            |
| `data.key`        | Clave del estado                         |
| `data.text`       | Texto del estado                         |
| `data.color`      | Color del texto                          |
| `data.background` | Color de fondo                           |

## Crear Estado

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/status/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "key": "active",
  "text": "Activo",
  "color": "79FF33"
}
```

### Descripción de Campos

| Campo   | Tipo   | Restricciones                           | Descripción                 |
| ------- | ------ | --------------------------------------- | --------------------------- |
| `id`    | string | Máximo: 100 caracteres, **Obligatorio** | ID del estado               |
| `key`   | string | Máximo: 100 caracteres, **Obligatorio** | Clave del estado            |
| `text`  | string | Máximo: 100 caracteres, **Obligatorio** | Texto del estado            |
| `color` | string | Máximo: 100 caracteres, **Obligatorio** | Color (formato hexadecimal) |

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
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

| Campo             | Descripción                                 |
| ----------------- | ------------------------------------------- |
| `code`            | Código de respuesta interno (10 = éxito)    |
| `messages`        | Array de mensajes informativos              |
| `data`            | Objeto con la información del estado creado |
| `data.id`         | ID del estado                               |
| `data.key`        | Clave del estado                            |
| `data.text`       | Texto del estado                            |
| `data.color`      | Color del texto                             |
| `data.background` | Color de fondo                              |

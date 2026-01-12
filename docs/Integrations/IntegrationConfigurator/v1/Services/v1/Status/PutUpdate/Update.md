## Actualizar Estado

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/status/update
```

### Parámetros de Query

| Key  | Value    | Description                      |
| ---- | -------- | -------------------------------- |
| `id` | `123456` | ID único del estado a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "C001",
  "type": "BD",
  "server": "localhost",
  "port": "9090",
  "user": "admin",
  "password": "admin123",
  "adapter": "ssql"
}
```

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

```json
{
  "code": 11,
  "messages": ["upated succesfully"],
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

| Campo             | Descripción                                      |
| ----------------- | ------------------------------------------------ |
| `code`            | Código de respuesta interno (11 = éxito)         |
| `messages`        | Array de mensajes informativos                   |
| `data`            | Objeto con la información actualizada del estado |
| `data.id`         | ID del estado                                    |
| `data.key`        | Clave del estado                                 |
| `data.text`       | Texto del estado                                 |
| `data.color`      | Color del texto                                  |
| `data.background` | Color de fondo                                   |

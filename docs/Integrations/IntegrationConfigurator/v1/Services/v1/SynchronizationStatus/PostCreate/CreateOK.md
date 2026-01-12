## Crear Estado de Sincronización

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/synchronizationStates/create
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "key": "success",
  "text": "Exitoso",
  "color": "#1B3E19",
  "background": "#E2F7E2"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo   | Requerido | Descripción                            |
| ------------ | ------ | --------- | -------------------------------------- |
| `key`        | string | Sí        | Clave identificadora del estado        |
| `text`       | string | Sí        | Texto descriptivo del estado           |
| `color`      | string | Sí        | Color del texto en formato hexadecimal |
| `background` | string | Sí        | Color de fondo en formato hexadecimal  |

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
  "data": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "key": "success",
    "text": "Exitoso",
    "color": "#1B3E19",
    "background": "#E2F7E2"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo             | Descripción                               |
| ----------------- | ----------------------------------------- |
| `code`            | Código de respuesta interno (10 = creado) |
| `messages`        | Array con mensajes del resultado          |
| `data`            | Objeto con los datos del estado creado    |
| `data.id`         | ID único del estado de sincronización     |
| `data.key`        | Clave identificadora del estado           |
| `data.text`       | Texto descriptivo del estado              |
| `data.color`      | Color del texto en formato hexadecimal    |
| `data.background` | Color de fondo en formato hexadecimal     |

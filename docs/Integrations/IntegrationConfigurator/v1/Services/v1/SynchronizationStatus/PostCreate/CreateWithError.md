## Crear Estado de Sincronización - Error de Validación

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

### 400 Bad Request - Error de Validación

```json
{
  "code": 50,
  "messages": [
    {
      "object": "not created succefully"
    },
    {
      "text": "is required"
    }
  ],
  "data": {
    "key": "success",
    "text": "",
    "color": "#1B3E19",
    "background": "#E2F7E2"
  }
}
```

### Descripción de la Respuesta de Error

| Campo      | Descripción                                   |
| ---------- | --------------------------------------------- |
| `code`     | Código de respuesta interno (50 = error)      |
| `messages` | Array con objetos describiendo los errores    |
| `data`     | Objeto con los datos enviados en la solicitud |

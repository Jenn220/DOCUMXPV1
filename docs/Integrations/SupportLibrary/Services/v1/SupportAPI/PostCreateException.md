## Registrar Excepción

### Método HTTP

`POST`

### URL

```
{{server_exceptions_library}}/api/exceptions
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "clientApp": "opl.printer",
  "process": "FACTURA_PINT",
  "referenceID": "212121-878787-455445-454",
  "priority": 1,
  "messages": [
    "es obligatorio la facturacion",
    "la impresora no responde",
    "falta papel"
  ],
  "date": "2025-12-10T15:30:45.123Z"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo         | Tipo   | Descripción                                   |
| ------------- | ------ | --------------------------------------------- |
| `clientApp`   | string | Identificador de la aplicación cliente        |
| `process`     | string | Nombre del proceso donde ocurrió la excepción |
| `referenceID` | string | Identificador de referencia del proceso       |
| `priority`    | number | Nivel de prioridad de la excepción            |
| `messages`    | array  | Lista de mensajes de error                    |
| `date`        | string | Fecha y hora de la excepción (formato ISO)    |

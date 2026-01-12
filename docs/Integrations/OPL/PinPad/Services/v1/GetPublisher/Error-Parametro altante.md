## Obtener Configuración de Pinpad sin Parámetros

### Método HTTP

`GET`

### URL

```
{{base_url}}/api/v1/publisher/P004
```

### Headers

| Key           | Value                      | Description                  |
| ------------- | -------------------------- | ---------------------------- |
| Authorization | Bearer yyyyyyiyiyiyiyiy... | Token JWT para autenticación |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 500 Internal Server Error - Parámetro Faltante

```json
{
  "code": 500,
  "process": "P004",
  "message": "Error al publicar: Missing required parameter in the query string"
}
```

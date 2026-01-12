## Obtener Configuración de Pinpad sin Autorización

### Método HTTP

`GET`

### URL

```
{{base_url}}/api/v1/publisher/P004
```

### Parámetros de Query

| Key           | Value                                | Description        |
| ------------- | ------------------------------------ | ------------------ |
| restaurant_id | 123e4567-e89b-12d3-a456-426614174000 | ID del restaurante |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 401 Unauthorized - Falta Header de Autorización

```json
{
  "msg": "Missing Authorization Header"
}
```

## Obtener Configuración de Pinpad con ID Inválido

### Método HTTP

`GET`

### URL

```
{{base_url}}/api/v1/publisher/P004
```

### Headers

| Key           | Value                               | Description                  |
| ------------- | ----------------------------------- | ---------------------------- |
| Authorization | Bearer iyiyiyiyiyyyyyiiiiiyiyiyy... | Token JWT para autenticación |

### Parámetros de Query

| Key           | Value                                | Description        |
| ------------- | ------------------------------------ | ------------------ |
| restaurant_id | 00000000-0000-0000-0000-000000000000 | ID del restaurante |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 500 Internal Server Error - Datos No Encontrados

```json
{
  "code": 500,
  "process": "P004",
  "message": "Error al publicar: No se encontraron datos"
}
```

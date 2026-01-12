## Obtener Configuración de Pinpad por Restaurante

### Método HTTP

`GET`

### URL

```
{{serverPinpad}}/api/v1/publisher/P004
```

### Headers

| Key           | Value                | Description                  |
| ------------- | -------------------- | ---------------------------- |
| Authorization | Bearer {{jwt_token}} | Token JWT para autenticación |
| Content-Type  | application/json     |                              |

### Parámetros de Query

| Key           | Value                                | Description        |
| ------------- | ------------------------------------ | ------------------ |
| restaurant_id | 096c55b8-68f5-62b8-c479-ced7c304c574 | ID del restaurante |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 200 OK - Datos Recuperados Correctamente

```json
{
  "code": 200,
  "process": "P004",
  "message": "Datos recuperados correctamente",
  "data": {
    "pinpad_config": {
      "enabled": true,
      "device_type": "terminal",
      "connection_settings": {
        "host": "192.168.1.100",
        "port": 8080
      }
    }
  }
}
```

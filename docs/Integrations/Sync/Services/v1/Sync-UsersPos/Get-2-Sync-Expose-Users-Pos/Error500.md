## Obtener Usuarios POS

### Método HTTP

`GET`

### URL

```
{{server_pub}}/api/users_pos
```

### Parámetros de Query

| Key           | Value                                | Descripción                    |
| ------------- | ------------------------------------ | ------------------------------ |
| cdn_id        | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant_id | e17d03da-b8b6-f424-febc-3a767b6401bb | Identificador del restaurante  |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 400 Bad Request - Error Interno del Servidor

```json
{
  "code": 400,
  "status": "error",
  "message": "Error interno del servidor.",
  "details": [
    {
      "field": "base_de_datos",
      "message": "No se pudo conectar a la base de datos principal."
    },
    {
      "field": "servicio_de_autenticacion",
      "message": "Tiempo de espera agotado al consultar el token del usuario."
    }
  ]
}
```

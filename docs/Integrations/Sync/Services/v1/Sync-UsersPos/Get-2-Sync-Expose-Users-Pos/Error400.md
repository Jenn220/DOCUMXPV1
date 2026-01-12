## Obtener Usuarios POS

### Método HTTP

`GET`

### URL

```
{{server_pub}}/api/users_pos
```

### Autenticación

| Tipo          | Token                            |
| ------------- | -------------------------------- |
| Authorization | `eyJhbGciOiJIUzI1NiIsInR5cCI...` |

### Parámetros de Query

| Key           | Value                                | Descripción                    |
| ------------- | ------------------------------------ | ------------------------------ |
| cdn_id        | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant_id | e17d03da-b8b6-f424-febc-3a767b6401bb | Identificador del restaurante  |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 400 Bad Request - Parámetros Inválidos

```json
{
  "code": 400,
  "status": "error",
  "message": "Parámetros inválidos",
  "details": [
    {
      "field": "limit",
      "message": "El parámetro 'limit' debe ser mayor que 0."
    },
    {
      "field": "restaurante_id",
      "message": "Este campo es obligatorio."
    }
  ]
}
```

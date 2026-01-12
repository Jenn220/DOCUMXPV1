## Obtener Usuario por ID

### Método HTTP

`GET`

### URL

```
{{server_BackOffice_InternalClients}}/api/v1/users/getuserbyid
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | Franchise ID (UUID) |
| `userId`    | `c17b6e8d-88a5-9eb5-1f44-aeec161494da` | User ID (UUID)      |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Success",
  "data": {
    "id": "c17b6e8d-88a5-9eb5-1f44-aeec161494da",
    "user_name": "Juan",
    "user_last_name": "Pérez"
  }
}
```

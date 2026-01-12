## Obtener Configuraciones por Franquicia

### Método HTTP

`GET`

### URL

```
{{server_BackOffice_InternalClients}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key         | Value                                  | Description                     |
| ----------- | -------------------------------------- | ------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia a consultar |
| `user`      | `c17b6e8d-88a5-9eb5-1f44-aeec161494da` | ID del usuario                  |
| `country`   | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                     |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Success",
  "data": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "menu_deep_level_nested": 3
    }
  ]
}
```

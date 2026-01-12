## Iniciar Sesión

### Método HTTP

`POST`

### URL

```
{{server_auth}}/login
```

### Headers

| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "email": "daniel.llerena@kfc.com.ec",
  "password": "Maker*4033"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo      | Tipo   | Descripción                    |
| ---------- | ------ | ------------------------------ |
| `email`    | string | Correo electrónico del usuario |
| `password` | string | Contraseña del usuario         |

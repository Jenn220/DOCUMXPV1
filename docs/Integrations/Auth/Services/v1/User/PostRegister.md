## Registrar Usuario

### Método HTTP

`POST`

### URL

```
{{server_auth}}/register
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "username": "Daniel Llerena",
  "email": "daniel.llerena@kfc.com.ec",
  "password": "Maker*1111",
  "confirm_password": "Maker*1111"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo              | Tipo   | Descripción                    |
| ------------------ | ------ | ------------------------------ |
| `username`         | string | Nombre completo del usuario    |
| `email`            | string | Correo electrónico del usuario |
| `password`         | string | Contraseña para la cuenta      |
| `confirm_password` | string | Confirmación de la contraseña  |

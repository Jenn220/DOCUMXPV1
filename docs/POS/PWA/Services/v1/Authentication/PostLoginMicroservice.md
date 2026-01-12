## Login Microservice

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "authorizationRequest": {
    "username": "user@example.com",
    "password": "password123",
    "grant_type": "password"
  }
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                             | Tipo   | Descripción                                  |
| --------------------------------- | ------ | -------------------------------------------- |
| `authorizationRequest`            | object | Objeto con las credenciales de autenticación |
| `authorizationRequest.username`   | string | Correo electrónico del usuario               |
| `authorizationRequest.password`   | string | Contraseña del usuario                       |
| `authorizationRequest.grant_type` | string | Tipo de concesión de autorización            |

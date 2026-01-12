## Buscar Usuario

### Método HTTP

`POST`

### URL

```
{{server_pwa}}/hera/Users/find-user
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "username": "user@example.com",
  "email": "user@example.com"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo      | Tipo   | Descripción                             |
| ---------- | ------ | --------------------------------------- |
| `username` | string | Nombre de usuario a buscar              |
| `email`    | string | Correo electrónico del usuario a buscar |

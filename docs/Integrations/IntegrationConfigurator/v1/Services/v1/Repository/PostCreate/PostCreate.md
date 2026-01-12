## Crear Repositorio

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/repositories/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "port": 9562,
  "username": "admin",
  "password": "admin123",
  "databaseName": "mxp-dev",
  "authTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "url": "https://apim-hera.azure-api.net/mxpi-init-prepro1",
  "repositoryDescription": "Reposirorio para mxp legacy"
}
```

### Descripción de Campos

| Campo                   | Tipo    | Descripción                                   |
| ----------------------- | ------- | --------------------------------------------- |
| `port`                  | integer | Puerto del repositorio                        |
| `username`              | string  | Nombre de usuario para autenticación          |
| `password`              | string  | Contraseña para autenticación                 |
| `databaseName`          | string  | Nombre de la base de datos                    |
| `authTypeId`            | string  | ID del tipo de autenticación (desde catálogo) |
| `statusId`              | string  | ID del estado del repositorio                 |
| `url`                   | string  | URL del repositorio                           |
| `repositoryDescription` | string  | Descripción del repositorio                   |

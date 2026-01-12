## Actualizar Servidor

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/servers/update
```

### Parámetros de Query

| Key  | Value    | Description                        |
| ---- | -------- | ---------------------------------- |
| `id` | `123456` | ID único del servidor a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "mysql",
  "type": "BD",
  "url": "https://server.com"
}
```

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

```json
{
  "code": 11,
  "messages": ["upated succesfully"],
  "data": {
    "name": "server_centos",
    "typeServerId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
    "url": "https://server.com",
    "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                        |
| ------------------- | -------------------------------------------------- |
| `code`              | Código de respuesta interno (11 = éxito)           |
| `messages`          | Array de mensajes informativos                     |
| `data`              | Objeto con la información actualizada del servidor |
| `data.name`         | Nombre del servidor                                |
| `data.typeServerId` | ID del tipo de servidor                            |
| `data.url`          | URL del servidor                                   |
| `data.statusId`     | ID del estado del servidor                         |

## Crear Servidor

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/servers/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "S001",
  "name": "server_centos",
  "type": "win",
  "url": "https://server.com"
}
```

### Descripción de Campos

| Campo  | Tipo   | Restricciones          | Descripción         |
| ------ | ------ | ---------------------- | ------------------- |
| `code` | string | Máximo: 10 caracteres  | Código del servidor |
| `name` | string | Máximo: 200 caracteres | Nombre del servidor |
| `type` | string | -                      | Tipo de servidor    |
| `url`  | string | Máximo: 300 caracteres | URL del servidor    |

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succesfully"],
  "data": {
    "id": "a4d9ba2b-7b84-47bf-b298-033ffd446729",
    "code": "S001",
    "name": "server_centos",
    "typeServerId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
    "url": "https://server.com",
    "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                   |
| ------------------- | --------------------------------------------- |
| `code`              | Código de respuesta interno (10 = éxito)      |
| `messages`          | Array de mensajes informativos                |
| `data`              | Objeto con la información del servidor creado |
| `data.id`           | ID único generado para el servidor            |
| `data.code`         | Código del servidor                           |
| `data.name`         | Nombre del servidor                           |
| `data.typeServerId` | ID del tipo de servidor                       |
| `data.url`          | URL del servidor                              |
| `data.statusId`     | ID del estado del servidor                    |

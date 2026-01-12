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
  "name": "server_centos",
  "typeServerId": "1b689793-a9d8-47a3-bb6d-92d652befbfd",
  "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3",
  "url": "https://server.com"
}
```

### Descripción de Campos

| Campo          | Tipo   | Restricciones          | Descripción                |
| -------------- | ------ | ---------------------- | -------------------------- |
| `name`         | string | Máximo: 200 caracteres | Nombre del servidor        |
| `typeServerId` | string | -                      | ID del tipo de servidor    |
| `statusId`     | string | **Obligatorio**        | ID del estado del servidor |
| `url`          | string | Máximo: 300 caracteres | URL del servidor           |

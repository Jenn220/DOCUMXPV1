## Crear Entidad

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/entities/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "sdfsfdfdsf",
  "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
  "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": "10",
  "messages": ["Creado Correctamente"],
  "data": {
    "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
    "name": "plu",
    "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
    "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                    |
| ------------------- | ---------------------------------------------- |
| `code`              | Código de respuesta interno ("10" = éxito)     |
| `messages`          | Array de mensajes informativos                 |
| `data`              | Objeto con la información de la entidad creada |
| `data.id`           | ID único generado para la entidad              |
| `data.name`         | Nombre de la entidad                           |
| `data.typeId`       | ID del tipo de entidad                         |
| `data.repositoryId` | ID del repositorio                             |
| `data.statusId`     | ID del estado de la entidad                    |

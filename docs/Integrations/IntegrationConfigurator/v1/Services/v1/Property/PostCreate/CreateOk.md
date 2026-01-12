## Crear Propiedad

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/properties/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "description",
  "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
  "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["Creado Correctamente"],
  "data": {
    "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
    "code": "P001",
    "name": "description",
    "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
    "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo           | Descripción                                      |
| --------------- | ------------------------------------------------ |
| `code`          | Código de respuesta interno (10 = éxito)         |
| `messages`      | Array de mensajes informativos                   |
| `data`          | Objeto con la información de la propiedad creada |
| `data.id`       | ID único generado para la propiedad              |
| `data.code`     | Código de la propiedad                           |
| `data.name`     | Nombre de la propiedad                           |
| `data.typeId`   | ID del tipo de propiedad                         |
| `data.entityId` | ID de la entidad asociada                        |
| `data.statusId` | ID del estado de la propiedad                    |

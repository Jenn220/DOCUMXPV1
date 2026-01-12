## Obtener Propiedad por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/properties/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                          |
| ---- | -------------------------------------- | ------------------------------------ |
| `id` | `06b8588c-4cef-4f9e-b3ae-2283508be599` | ID único de la propiedad a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
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

| Campo           | Descripción                               |
| --------------- | ----------------------------------------- |
| `code`          | Código de respuesta interno (20 = éxito)  |
| `messages`      | Array de mensajes informativos            |
| `data`          | Objeto con la información de la propiedad |
| `data.id`       | ID único de la propiedad                  |
| `data.code`     | Código de la propiedad                    |
| `data.name`     | Nombre de la propiedad                    |
| `data.typeId`   | ID del tipo de propiedad                  |
| `data.entityId` | ID de la entidad asociada                 |
| `data.statusId` | ID del estado de la propiedad             |

## Obtener Propiedad por Código

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/properties/getByCode
```

### Parámetros de Query

| Key    | Value  | Description                        |
| ------ | ------ | ---------------------------------- |
| `code` | `P001` | Código de la propiedad a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "entities": [
      {
        "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
        "code": "P001",
        "name": "description",
        "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
        "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                      | Descripción                              |
| -------------------------- | ---------------------------------------- |
| `code`                     | Código de respuesta interno (20 = éxito) |
| `messages`                 | Array de mensajes informativos           |
| `data`                     | Objeto con los datos de propiedades      |
| `data.entities`            | Array con las propiedades encontradas    |
| `data.entities[].id`       | ID único de cada propiedad               |
| `data.entities[].code`     | Código de la propiedad                   |
| `data.entities[].name`     | Nombre de la propiedad                   |
| `data.entities[].typeId`   | ID del tipo de propiedad                 |
| `data.entities[].entityId` | ID de la entidad asociada                |
| `data.entities[].statusId` | ID del estado de la propiedad            |

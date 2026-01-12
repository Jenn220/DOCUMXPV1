## Obtener Propiedades por ID de Entidad

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/properties/getByEntityId
```

### Parámetros de Query

| Key        | Value                                  | Description                                     |
| ---------- | -------------------------------------- | ----------------------------------------------- |
| `entityId` | `059bb531-5b34-4435-bdad-21c81b41cac1` | ID de la entidad para consultar sus propiedades |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "properties": [
      {
        "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
        "code": "P001",
        "name": "description",
        "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
        "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "8f4c76a0-0779-40df-9fd6-5acba2e57333",
        "code": "P002",
        "name": "name",
        "typeId": "4bbd7a39-31a9-4eb8-abd9-f8aea46df7ea",
        "entityId": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                        | Descripción                                        |
| ---------------------------- | -------------------------------------------------- |
| `code`                       | Código de respuesta interno (20 = éxito)           |
| `messages`                   | Array de mensajes informativos                     |
| `data`                       | Objeto con los datos de propiedades                |
| `data.properties`            | Array con las propiedades de la entidad consultada |
| `data.properties[].id`       | ID único de cada propiedad                         |
| `data.properties[].code`     | Código de la propiedad                             |
| `data.properties[].name`     | Nombre de la propiedad                             |
| `data.properties[].typeId`   | ID del tipo de propiedad                           |
| `data.properties[].entityId` | ID de la entidad asociada                          |
| `data.properties[].statusId` | ID del estado de la propiedad                      |

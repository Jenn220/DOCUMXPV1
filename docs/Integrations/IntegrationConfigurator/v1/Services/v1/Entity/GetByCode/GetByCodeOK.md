## Obtener Entidad por Código

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/entities/getByCode
```

### Parámetros de Query

| Key    | Value  | Description                      |
| ------ | ------ | -------------------------------- |
| `code` | `E001` | Código de la entidad a consultar |

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
        "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
        "code": "1",
        "name": "plu",
        "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
        "repositoryId": "6bd36e91-c0de-4b6d-87b8-5dea7f2c2274",
        "repositoryDescription": "Reposirorio para mxp legacy",
        "repositoryName": "mxp-dev",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                                   | Descripción                              |
| --------------------------------------- | ---------------------------------------- |
| `code`                                  | Código de respuesta interno (20 = éxito) |
| `messages`                              | Array de mensajes informativos           |
| `data`                                  | Objeto con los datos de entidades        |
| `data.entities`                         | Array con las entidades encontradas      |
| `data.entities[].id`                    | ID único de cada entidad                 |
| `data.entities[].code`                  | Código de la entidad                     |
| `data.entities[].name`                  | Nombre de la entidad                     |
| `data.entities[].typeId`                | ID del tipo de entidad                   |
| `data.entities[].repositoryId`          | ID del repositorio                       |
| `data.entities[].repositoryDescription` | Descripción del repositorio              |
| `data.entities[].repositoryName`        | Nombre del repositorio                   |
| `data.entities[].statusId`              | ID del estado de la entidad              |

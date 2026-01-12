## Obtener Proceso por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/processes/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                      |
| ---- | -------------------------------------- | -------------------------------- |
| `id` | `a627d86f-1092-4341-a9ad-21e6efc5f8c1` | ID único del proceso a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "a627d86f-1092-4341-a9ad-21e6efc5f8c1",
    "code": "E001",
    "name": "my name",
    "description": "",
    "typeId": "fc1e4f86-a544-4d8f-95c1-870b7f1a6dd1",
    "connectionId": "2d089505-110c-4fb5-a23e-cd7223dce61b",
    "statusId": "34c25c17-a5b5-48e1-9862-7f275f376698",
    "entities": [
      {
        "id": "5af18a9a-4e98-4f05-9abc-a15bcd1643b9",
        "properties": [
          {
            "id": "29ccdd74-21ec-4dcb-aa05-b57786cdc0e0",
            "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
          },
          {
            "id": "9d0f5e1c-cb39-48f1-9cae-06230b27571c",
            "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
          }
        ],
        "filters": [
          {
            "propertyId": "06b8588c-4cef-4f9e-b3ae-2283508be599",
            "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
            "isGlobalVariable": false,
            "value": "KFC"
          },
          {
            "propertyId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
            "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
            "isGlobalVariable": true,
            "value": [
              {
                "globalVariableId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e0",
                "globalVariableName": "country",
                "globalVariableValue": [
                  {
                    "globalVariableValueId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e2",
                    "globalVariableValueName": "countryName"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                                        | Descripción                                                       |
| -------------------------------------------- | ----------------------------------------------------------------- |
| `code`                                       | Código de respuesta interno (20 = éxito)                          |
| `messages`                                   | Array de mensajes informativos                                    |
| `data`                                       | Objeto con la información del proceso                             |
| `data.id`                                    | ID único del proceso                                              |
| `data.code`                                  | Código del proceso                                                |
| `data.name`                                  | Nombre del proceso                                                |
| `data.description`                           | Descripción del proceso                                           |
| `data.typeId`                                | ID del tipo de proceso                                            |
| `data.connectionId`                          | ID de la conexión                                                 |
| `data.statusId`                              | ID del estado del proceso                                         |
| `data.entities`                              | Array de entidades con sus propiedades y filtros                  |
| `data.entities[].filters[].isGlobalVariable` | Indica si el filtro usa variables globales                        |
| `data.entities[].filters[].value`            | Valor del filtro (puede ser string o array de variables globales) |

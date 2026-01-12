## Crear Proceso de Transformación

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/processes/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "my name",
  "description": "",
  "typeId": "fc1e4f86-a544-4d8f-95c1-870b7f1a6dd1",
  "connectionId": null,
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "typeTransformation": "98f556df-6edc-4e7c-8fad-b127ad2f3541",
  "withResponse": true,
  "withCache": false,
  "entities": null
}
```

### Descripción de Campos

| Campo                | Tipo        | Restricciones                                                         | Descripción                                   |
| -------------------- | ----------- | --------------------------------------------------------------------- | --------------------------------------------- |
| `name`               | string      | **Obligatorio**                                                       | Nombre del proceso                            |
| `description`        | string      | Opcional                                                              | Descripción del proceso                       |
| `typeId`             | string      | Máximo: 10 caracteres                                                 | ID del tipo de proceso                        |
| `connectionId`       | string/null | -                                                                     | ID de la conexión (null para transformación)  |
| `statusId`           | string      | -                                                                     | ID del estado del proceso                     |
| `typeTransformation` | string      | **Obligatorio** si el tipo es transformación, opcional en otros casos | ID del tipo de transformación                 |
| `withResponse`       | boolean     | -                                                                     | Indica si requiere respuesta                  |
| `withCache`          | boolean     | -                                                                     | Indica si usa caché                           |
| `entities`           | array/null  | -                                                                     | Lista de entidades (null para transformación) |

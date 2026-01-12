## Crear Proceso

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
  "connectionId": "712feaea-8228-4f03-9457-3ce36e618c56",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "typeTransformation": null,
  "withResponse": true,
  "withCache": false,
  "entities": [
    {
      "id": "059bb531-5b34-4435-bdad-21c81b41cac1",
      "properties": [
        {
          "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
          "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        },
        {
          "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
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
  ],
  "recommendedSettings": false,
  "method": [
    {
      "method_id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
      "method_name": "POST"
    }
  ],
  "script": null
}
```

### Descripción de Campos

| Campo                   | Tipo        | Restricciones                                                     | Descripción                                |
| ----------------------- | ----------- | ----------------------------------------------------------------- | ------------------------------------------ |
| `name`                  | string      | **Obligatorio**                                                   | Nombre del proceso                         |
| `description`           | string      | Opcional                                                          | Descripción del proceso                    |
| `typeId`                | string      | Máximo: 10 caracteres                                             | ID del tipo de proceso                     |
| `connectionId`          | string      | -                                                                 | ID de la conexión                          |
| `statusId`              | string      | -                                                                 | ID del estado del proceso                  |
| `typeTransformation`    | string/null | Obligatorio si el tipo es transformación, opcional en otros casos | Tipo de transformación                     |
| `withResponse`          | boolean     | -                                                                 | Indica si requiere respuesta               |
| `withCache`             | boolean     | -                                                                 | Indica si usa caché                        |
| `entities`              | array       | -                                                                 | Lista de entidades del proceso             |
| `entities[].id`         | string      | Máximo: 255 caracteres                                            | ID de la entidad                           |
| `entities[].properties` | array       | -                                                                 | Propiedades de la entidad                  |
| `entities[].filters`    | array       | -                                                                 | Filtros aplicados a la entidad             |
| `recommendedSettings`   | boolean     | -                                                                 | Indica si usa configuraciones recomendadas |
| `method`                | array       | -                                                                 | Métodos HTTP permitidos                    |
| `script`                | string/null | -                                                                 | Script personalizado                       |

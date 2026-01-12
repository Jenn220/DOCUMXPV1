## Actualizar Proceso

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/processes/update
```

### Parámetros de Query

| Key  | Value                                  | Description                       |
| ---- | -------------------------------------- | --------------------------------- |
| `id` | `a627d86f-1092-4341-a9ad-21e6efc5f8c1` | ID único del proceso a actualizar |

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
  ]
}
```

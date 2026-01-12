## Crear Proceso con Mapeo de Entidades

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
      "name": "plus",
      "toName": "Configurations_BO_Plus",
      "properties": [
        {
          "id": "06b8588c-4cef-4f9e-b3ae-2283508be599",
          "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "fromName": "plu_id",
          "fromType": "",
          "toName": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "toType": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
          "defaultValue": "",
          "isPrimaryKey": "true"
        },
        {
          "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
          "internalStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "fromName": "plu_description",
          "fromType": "",
          "toName": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "toType": "",
          "defaultValue": ""
        }
      ],
      "filters": [
        {
          "propertyId": "06b8588c-4cef-4f9e-b3ae-2283508be599",
          "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
          "value": "plu_id"
        },
        {
          "propertyId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
          "operatorId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
          "value": "12312"
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

### Descripción de Campos Adicionales

| Campo                                  | Tipo        | Descripción                                   |
| -------------------------------------- | ----------- | --------------------------------------------- |
| `entities[].name`                      | string      | Nombre de la entidad extraída                 |
| `entities[].toName`                    | string      | Nombre de la entidad a cargar                 |
| `entities[].properties[].fromName`     | string      | Nombre de la propiedad de la entidad extraída |
| `entities[].properties[].fromType`     | string      | Tipo de dato de origen (opcional)             |
| `entities[].properties[].toName`       | string      | Nombre de la propiedad de la entidad a cargar |
| `entities[].properties[].toType`       | string      | Tipo de dato de destino                       |
| `entities[].properties[].defaultValue` | string      | Valor por defecto                             |
| `entities[].properties[].isPrimaryKey` | string      | Indica si es llave primaria                   |
| `recommendedSettings`                  | boolean     | Indica si usa configuraciones recomendadas    |
| `method`                               | array       | Métodos HTTP permitidos                       |
| `script`                               | string/null | Script personalizado                          |

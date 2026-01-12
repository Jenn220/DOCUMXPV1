## 1. Actualizar Adaptador

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/adapters/update
```

### Parámetros de Query

| Key  | Value                                  | Description                         |
| ---- | -------------------------------------- | ----------------------------------- |
| `id` | `7654cb16-e955-4605-8579-b891a67f94c7` | ID único del adaptador a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "mongo",
  "typeAdapaterId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
}
```

### Descripción de Campos

| Campo            | Tipo   | Restricciones                                                                      | Descripción                            |
| ---------------- | ------ | ---------------------------------------------------------------------------------- | -------------------------------------- |
| `name`           | string | -                                                                                  | Nombre del adaptador                   |
| `typeAdapaterId` | string | Máximo: 100 caracteres<br/>Valores permitidos: `FILE`, `BD`, `API_REST`, `API_SOAP` | Identificador del tipo de adaptador    |
| `statusId`       | string | -                                                                                  | Identificador del estado del adaptador |

### Notas

- El campo `typeAdapaterId` solo acepta los siguientes valores:
  - `FILE`
  - `BD`
  - `API_REST`
  - `API_SOAP`
- El campo `version` no está presente en la actualización

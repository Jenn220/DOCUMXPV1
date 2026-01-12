## Crear Entidad

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/entities/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "sdfsfdfdsf",
  "typeId": "d528abf5-ec41-4c8f-9bc1-8211855c3749",
  "repositoryId": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1",
  "repositoryDescription": "Reposirorio para mxp legacy",
  "repositoryName": "mxp-dev",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Descripción de Campos

| Campo                   | Tipo   | Descripción                 |
| ----------------------- | ------ | --------------------------- |
| `name`                  | string | Nombre de la entidad        |
| `typeId`                | string | ID del tipo de entidad      |
| `repositoryId`          | string | ID del repositorio          |
| `repositoryDescription` | string | Descripción del repositorio |
| `repositoryName`        | string | Nombre del repositorio      |
| `statusId`              | string | ID del estado de la entidad |

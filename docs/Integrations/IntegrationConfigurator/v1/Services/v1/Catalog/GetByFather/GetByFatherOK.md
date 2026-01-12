## Obtener Catálogos por ID del Padre

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/getByFatherId
```

### Parámetros de Query

| Key    | Value | Description                                        |
| ------ | ----- | -------------------------------------------------- |
| `code` | `1`   | Código del catálogo padre para consultar sus hijos |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "catalogs": [
      {
        "id": "aba246fc-76a2-48ea-968d-17a51702861f",
        "code": 2,
        "name": "Extracción",
        "value": "extract",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "623acd2c-b882-41ac-8182-16b9293ebb08",
        "code": 3,
        "name": "Transformación",
        "value": "transform",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "764ca591-9a83-48e0-b1f7-b6d43e0e2267",
        "code": 4,
        "name": "Carga",
        "value": "load",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      },
      {
        "id": "764ca591-9a83-48e0-b1f7-b6d43e0e2267",
        "code": 5,
        "name": "Publicación",
        "value": "publish",
        "fatherId": 1,
        "isFather": false,
        "detail": "",
        "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                      | Descripción                                        |
| -------------------------- | -------------------------------------------------- |
| `code`                     | Código de respuesta interno (20 = éxito)           |
| `messages`                 | Array de mensajes informativos                     |
| `data`                     | Objeto con los datos de los catálogos              |
| `data.catalogs`            | Array con los catálogos hijos del padre consultado |
| `data.catalogs[].id`       | ID único de cada catálogo                          |
| `data.catalogs[].code`     | Código numérico del catálogo                       |
| `data.catalogs[].name`     | Nombre del catálogo                                |
| `data.catalogs[].value`    | Valor del catálogo                                 |
| `data.catalogs[].fatherId` | ID del padre                                       |
| `data.catalogs[].isFather` | Indica si es un catálogo padre (false para hijos)  |
| `data.catalogs[].detail`   | Detalle adicional del catálogo                     |
| `data.catalogs[].statusId` | ID del estado del catálogo                         |

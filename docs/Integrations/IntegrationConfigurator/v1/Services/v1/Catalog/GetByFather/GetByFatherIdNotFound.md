## Obtener Catálogos por ID del Padre (con Error)

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

### Error - No Encontrado

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

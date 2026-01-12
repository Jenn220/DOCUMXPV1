## Obtener Catálogo por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                       |
| ---- | -------------------------------------- | --------------------------------- |
| `id` | `51faf974-5c9e-4936-b234-91a173356dea` | ID único del catálogo a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "messages": ["Encontrado Correctamente"],
  "data": {
    "id": "51faf974-5c9e-4936-b234-91a173356dea",
    "code": 1,
    "name": "Tipo proceso",
    "value": "process_type",
    "fatherId": null,
    "isFather": true,
    "detail": "",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo           | Descripción                              |
| --------------- | ---------------------------------------- |
| `code`          | Código de respuesta interno (20 = éxito) |
| `messages`      | Array de mensajes informativos           |
| `data`          | Objeto con la información del catálogo   |
| `data.id`       | ID único del catálogo                    |
| `data.code`     | Código numérico del catálogo             |
| `data.name`     | Nombre del catálogo                      |
| `data.value`    | Valor del catálogo                       |
| `data.fatherId` | ID del padre (null si es padre)          |
| `data.isFather` | Indica si es un catálogo padre           |
| `data.detail`   | Detalle adicional del catálogo           |
| `data.statusId` | ID del estado del catálogo               |

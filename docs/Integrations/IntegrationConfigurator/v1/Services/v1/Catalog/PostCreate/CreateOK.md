## Crear Catálogo

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "prueba",
  "code": 1,
  "value": "prueba",
  "fatherId": "0",
  "detail": "",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": "10",
  "messages": ["Creado correctamente"],
  "data": {
    "id": "351faf974-5c9e-4936-b234-91a173356dea",
    "code": 1,
    "name": "prueba",
    "value": "prueba",
    "fatherId": null,
    "isFather": true,
    "detail": "",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo           | Descripción                                   |
| --------------- | --------------------------------------------- |
| `code`          | Código de respuesta interno ("10" = éxito)    |
| `messages`      | Array de mensajes informativos                |
| `data`          | Objeto con la información del catálogo creado |
| `data.id`       | ID único generado para el catálogo            |
| `data.code`     | Código numérico del catálogo                  |
| `data.name`     | Nombre del catálogo                           |
| `data.value`    | Valor del catálogo                            |
| `data.fatherId` | ID del padre (null si es padre)               |
| `data.isFather` | Indica si es un catálogo padre                |
| `data.detail`   | Detalle adicional del catálogo                |
| `data.statusId` | ID del estado del catálogo                    |

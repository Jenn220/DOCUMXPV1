## Crear Integración

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/integrations/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchiseId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "status": "A",
  "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
  "userId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "hourToExecute": ""
}
```

### Descripción de Campos

| Campo           | Tipo   | Restricciones                 | Descripción                                  |
| --------------- | ------ | ----------------------------- | -------------------------------------------- |
| `franchiseId`   | string | Máximo: 255 caracteres        | ID de la franquicia                          |
| `status`        | string | Mínimo: 1, Máximo: 1 carácter | Estado de la integración                     |
| `observations`  | string | Máximo: 300 caracteres        | Observaciones sobre la integración           |
| `userId`        | string | Máximo: 255 caracteres        | ID del usuario que crea la integración       |
| `hourToExecute` | string | Máximo: 50 caracteres         | Hora programada para ejecutar la integración |

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 200,
  "messages": "created succefully",
  "data": {
    "name": "Asignación de documentos",
    "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "country": {
      "country_id": "857accc3-c59a-4b6c-ae84-5942f5a14581",
      "country_name": "Ecuador",
      "country_code": "ECU"
    },
    "company": {
      "company_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "company_name": "INT FOOD SERVICE S.A",
      "company_code": 1
    },
    "franchise": {
      "franchise_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "franchise_name": "GUS",
      "franchise_code": 9
    },
    "restaurant": {
      "restaurant_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "restaurant_name": "G048",
      "restaurant_code": 456
    },
    "integrator": [
      {
        "integrator_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
        "integrator_name": "integración global 200",
        "integrator_code": "I001"
      },
      {
        "integrator_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
        "integrator_name": "Prueba integracion process",
        "integrator_code": "I002"
      }
    ],
    "status": "3fa85f64-5717-4562-b3fc-2c963f66afa4"
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo             | Descripción                                                 |
| ----------------- | ----------------------------------------------------------- |
| `code`            | Código de estado HTTP (200 = éxito)                         |
| `messages`        | Mensaje de confirmación                                     |
| `data`            | Objeto con la información completa de la integración creada |
| `data.name`       | Nombre de la asignación                                     |
| `data.userId`     | ID del usuario                                              |
| `data.country`    | Información del país (obligatorio)                          |
| `data.company`    | Información de la compañía (obligatorio)                    |
| `data.franchise`  | Información de la franquicia (obligatorio)                  |
| `data.restaurant` | Información del restaurante (obligatorio)                   |
| `data.integrator` | Lista de integradores (al menos uno requerido)              |
| `data.status`     | ID del estado                                               |

## Obtener Asignación de Integraciones por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key  | Value                                  | Description                           |
| ---- | -------------------------------------- | ------------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID único de la asignación a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "messages": "Data returned succesfully",
  "data": {
    "id": "69503d8f-fa70-2196-f0a0-e3a85fa17aec",
    "name": "Asignación de documentos",
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
    "status": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "key": "success",
      "text": "Exitoso",
      "color": "#1B3E19",
      "background": "#E2F7E2"
    }
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo             | Descripción                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `code`            | Código de estado HTTP (200 = éxito)                                  |
| `messages`        | Mensaje de confirmación                                              |
| `data`            | Objeto con la información completa de la asignación                  |
| `data.id`         | ID único de la asignación                                            |
| `data.name`       | Nombre de la asignación                                              |
| `data.country`    | Información del país                                                 |
| `data.company`    | Información de la compañía                                           |
| `data.franchise`  | Información de la franquicia                                         |
| `data.restaurant` | Información del restaurante                                          |
| `data.integrator` | Lista de integradores asociados                                      |
| `data.status`     | Objeto con información del estado (id, key, text, color, background) |

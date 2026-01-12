## Actualizar Asignación de Integraciones por Restaurante

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/assignmentIntegrationsByRestaurant
```

### Parámetros de Query

| Key  | Value                                  | Description                            |
| ---- | -------------------------------------- | -------------------------------------- |
| `id` | `e47c3813-7daf-407f-bc02-544d57290f1b` | ID único de la asignación a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
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
```

## Respuestas del Servidor

### 200 OK - Actualización Exitosa

```json
{
  "code": 200,
  "messages": "created succefully",
  "data": {
    "id": "1234569",
    "name": "Integracion de Forma de Pagos",
    "status": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "observations": "",
    "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "process": [
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
      },
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                             |
| ------------------- | --------------------------------------- |
| `code`              | Código de estado HTTP (200 = éxito)     |
| `messages`          | Mensaje de confirmación                 |
| `data`              | Objeto con la información actualizada   |
| `data.id`           | ID único de la integración              |
| `data.name`         | Nombre de la integración                |
| `data.status`       | ID del estado                           |
| `data.observations` | Observaciones                           |
| `data.userId`       | ID del usuario                          |
| `data.process`      | Lista de procesos asociados con sus IDs |

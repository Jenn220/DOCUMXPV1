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
  "code": "I01",
  "name": "Integracion de Forma de Pagos",
  "status": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "observations": "",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
  "process": [
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    },
    {
      "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
    }
  ],
  "withResponse": true,
  "country": [
    {
      "country_id": "857accc3-c59a-4b6c-ae84-5942f5a14581",
      "country_name": "Ecuador",
      "country_code": "ECU"
    }
  ],
  "franchise": [
    {
      "franchise_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "franchise_name": "GUS",
      "franchise_code": 9
    }
  ],
  "chunkLoad": 50,
  "integrator": [
    {
      "integrator_id": "957accc3-c59a-4b6c-ae84-5942f5a14582",
      "integrator_name": "mxpv2.integration.init",
      "integrator_url": "135.237.217.108:5000/api/v1/facade"
    }
  ]
}
```

### Descripción de Campos

| Campo                          | Tipo    | Restricciones                    | Descripción                            |
| ------------------------------ | ------- | -------------------------------- | -------------------------------------- |
| `code`                         | string  | -                                | Código de la integración               |
| `name`                         | string  | Máximo: 100 caracteres           | Nombre de la integración               |
| `status`                       | string  | Máximo: 100 caracteres           | Estado de la integración               |
| `observations`                 | string  | Máximo: 255 caracteres, nullable | Observaciones sobre la integración     |
| `userId`                       | string  | Máximo: 255 caracteres           | ID del usuario que crea la integración |
| `process`                      | array   | -                                | Lista de procesos asociados            |
| `process[].id`                 | string  | Máximo: 100 caracteres           | ID de cada proceso                     |
| `withResponse`                 | boolean | -                                | Indica si requiere respuesta           |
| `country`                      | array   | -                                | Lista de países asociados              |
| `country[].country_id`         | string  | -                                | ID del país                            |
| `country[].country_name`       | string  | -                                | Nombre del país                        |
| `country[].country_code`       | string  | -                                | Código del país                        |
| `franchise`                    | array   | -                                | Lista de franquicias asociadas         |
| `franchise[].franchise_id`     | string  | -                                | ID de la franquicia                    |
| `franchise[].franchise_name`   | string  | -                                | Nombre de la franquicia                |
| `franchise[].franchise_code`   | integer | -                                | Código de la franquicia                |
| `chunkLoad`                    | integer | -                                | Tamaño de carga por lotes              |
| `integrator`                   | array   | -                                | Lista de integradores                  |
| `integrator[].integrator_id`   | string  | -                                | ID del integrador                      |
| `integrator[].integrator_name` | string  | -                                | Nombre del integrador                  |
| `integrator[].integrator_url`  | string  | -                                | URL del integrador                     |

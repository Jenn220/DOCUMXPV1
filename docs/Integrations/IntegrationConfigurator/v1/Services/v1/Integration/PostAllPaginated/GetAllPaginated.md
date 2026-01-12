## Obtener Integraciones Paginadas

### Método HTTP
`POST`

### URL
```
{{server_orchestrator}}/api/v1/integrations/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)
```json
{
  "search": "string",
  "sort_order": 0,
  "sort_field": "string",
  "rows": 20,
  "first": 1,
  "activeOnly": true
}
```

## Respuestas del Servidor

### 200 OK - Consulta Exitosa
```json
{
    "code": 20,
    "description": "Data returned succesfully",
    "data": {
        "total_rows": 100,
        "rows": [
            {
                "id": "1234569",
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
            },
            {
                "id": "123456789",
                "name": "Integracion de Forma de Pagos 2",
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
        ]
    }
}
```

### Descripción de la Respuesta Exitosa

| Campo | Descripción |
|-------|-------------|
| `code` | Código de respuesta interno (20 = éxito) |
| `description` | Descripción del resultado |
| `data` | Objeto con los datos paginados |
| `data.total_rows` | Número total de registros disponibles |
| `data.rows` | Array con los registros de la página actual |
| `data.rows[].id` | ID único de cada integración |
| `data.rows[].name` | Nombre de la integración |
| `data.rows[].status` | Estado de la integración |
| `data.rows[].observations` | Observaciones |
| `data.rows[].userId` | ID del usuario |
| `data.rows[].process` | Array de procesos asociados |
| `data.rows[].country` | Array de países asociados |
| `data.rows[].franchise` | Array de franquicias asociadas |
| `data.rows[].chunkLoad` | Tamaño de carga por lotes |
| `data.rows[].integrator` | Array de integradores |
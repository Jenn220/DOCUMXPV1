## Actualizar Integración

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/integrations/update
```

### Parámetros de Query

| Key  | Value                                  | Description                             |
| ---- | -------------------------------------- | --------------------------------------- |
| `id` | `e47c3813-7daf-407f-bc02-544d57290f1b` | ID único de la integración a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "code": "I01",
  "name": "Integracion de Forma de Pagos(UPDATE)",
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

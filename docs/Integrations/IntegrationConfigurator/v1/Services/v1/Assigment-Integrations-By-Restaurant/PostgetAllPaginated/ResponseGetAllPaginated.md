## Obtener Asignaciones de Integraciones Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/YOUR_REDIS_OR_AZURE_KEY_HERE
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
  "code": 200,
  "messages": "Data returned succesfully",
  "data": {
    "total_rows": 100,
    "rows": [
      {
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
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e3a85fa17aec",
        "name": "Asignación de impresoras",
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
      },
      {
        "id": "69503d8f-fa70-2196-f0a0-e3a85fa17aec",
        "name": "Asignación de cofiguraciones",
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
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo                    | Descripción                                 |
| ------------------------ | ------------------------------------------- |
| `code`                   | Código de estado HTTP (200 = éxito)         |
| `messages`               | Mensaje de confirmación                     |
| `data`                   | Objeto con los datos paginados              |
| `data.total_rows`        | Número total de registros disponibles       |
| `data.rows`              | Array con los registros de la página actual |
| `data.rows[].id`         | ID único de cada asignación                 |
| `data.rows[].name`       | Nombre de la asignación                     |
| `data.rows[].country`    | Información del país                        |
| `data.rows[].company`    | Información de la compañía                  |
| `data.rows[].franchise`  | Información de la franquicia                |
| `data.rows[].restaurant` | Información del restaurante                 |
| `data.rows[].integrator` | Lista de integradores asociados             |
| `data.rows[].status`     | Objeto con información del estado           |

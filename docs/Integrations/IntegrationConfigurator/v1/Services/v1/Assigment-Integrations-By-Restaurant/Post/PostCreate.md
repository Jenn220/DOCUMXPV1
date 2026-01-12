## Crear Asignación de Integraciones por Restaurante

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/assignmentIntegrationsByRestaurant
```

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

### Descripción de Campos

| Campo                          | Tipo    | Requerido       | Descripción                                    |
| ------------------------------ | ------- | --------------- | ---------------------------------------------- |
| `name`                         | string  | Sí              | Nombre de la asignación                        |
| `userId`                       | string  | Sí              | ID del usuario que realiza la asignación       |
| `country`                      | object  | **Obligatorio** | Información del país                           |
| `country.country_id`           | string  | Sí              | ID único del país                              |
| `country.country_name`         | string  | Sí              | Nombre del país                                |
| `country.country_code`         | string  | Sí              | Código del país                                |
| `company`                      | object  | **Obligatorio** | Información de la compañía                     |
| `company.company_id`           | string  | Sí              | ID único de la compañía                        |
| `company.company_name`         | string  | Sí              | Nombre de la compañía                          |
| `company.company_code`         | integer | Sí              | Código de la compañía                          |
| `franchise`                    | object  | **Obligatorio** | Información de la franquicia                   |
| `franchise.franchise_id`       | string  | Sí              | ID único de la franquicia                      |
| `franchise.franchise_name`     | string  | Sí              | Nombre de la franquicia                        |
| `franchise.franchise_code`     | integer | Sí              | Código de la franquicia                        |
| `restaurant`                   | object  | **Obligatorio** | Información del restaurante                    |
| `restaurant.restaurant_id`     | string  | Sí              | ID único del restaurante                       |
| `restaurant.restaurant_name`   | string  | Sí              | Nombre del restaurante                         |
| `restaurant.restaurant_code`   | integer | Sí              | Código del restaurante                         |
| `integrator`                   | array   | **Obligatorio** | Lista de integradores (al menos uno requerido) |
| `integrator[].integrator_id`   | string  | Sí              | ID único del integrador                        |
| `integrator[].integrator_name` | string  | Sí              | Nombre del integrador                          |
| `integrator[].integrator_code` | string  | Sí              | Código del integrador                          |
| `status`                       | string  | Sí              | ID del estado de la asignación                 |

### Notas

- Los campos `country`, `company`, `franchise` y `restaurant` son **obligatorios**
- El array `integrator` debe contener al menos una integración
- Todos los objetos anidados deben incluir sus respectivos `id`, `name` y `code`

## Obtener Vendedores por Período

### Método HTTP

`GET`

### URL

```
{{server-bo}}/api/v1/sellers
```

### Parámetros de Query

| Key             | Value                                  | Description        |
| --------------- | -------------------------------------- | ------------------ |
| `cdn_id`        | `bc2d88ba-da1e-4db7-55fe-32d1205ac4af` | ID de la cadena    |
| `restaurant_id` | `24260579-fadf-7b3f-aac7-5e16faff96d1` | ID del restaurante |
| `period_id`     | `26617b88-3c44-4c0b-87d7-616ec6339ffd` | ID del período     |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Data returned succesfully",
  "data": {
    "_id": "5b3b130c-e925-45dc-a6a3-c4a6616ffc5f",
    "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
    "cdn_name": "Cadena Ejemplo",
    "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
    "restaurant": "G008",
    "period_id": "26617b88-3c44-4c0b-87d7-616ec6339ffd",
    "final_date": "2025-12-02T00:00:00.000Z",
    "start_date": "2025-12-02T00:00:00.000Z",
    "sales": [
      {
        "cashier": "CINTHYA BARRE VARGAS",
        "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
        "payment_method": "EFECTIVO",
        "value": 0,
        "pos_calculated": 11.74,
        "transactions": 2
      },
      {
        "cashier": "Daniel Llerena",
        "payment_method_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
        "payment_method": "EFECTIVO",
        "value": 14.98,
        "transactions": 2
      }
    ],
    "total": [
      {
        "cashier": "CINTHYA BARRE VARGAS",
        "value": 5.74,
        "pos_calculated": 11.74,
        "transactions": 2,
        "cash_register_subscription_id": "c8c300cc-1b82-1742-9e86-b29712579f10",
        "cash_register_subscription_name": "caja001",
        "surplus_or_shortage": -6
      },
      {
        "cashier": "Daniel Llerena",
        "value": 14.98,
        "pos_calculated": 11.74,
        "transactions": 2,
        "cash_register_subscription_id": "c4c300cc-1b82-1742-9e86-b29712579f10",
        "cash_register_subscription_name": "caja002",
        "surplus_or_shortage": 3.74
      }
    ]
  }
}
```

#### Descripción de la Respuesta Exitosa

| Campo                                          | Description                                                   |
| ---------------------------------------------- | ------------------------------------------------------------- |
| `code`                                         | Código de respuesta (200 = éxito)                             |
| `description`                                  | Descripción del resultado                                     |
| `data`                                         | Objeto con los datos del período                              |
| `data._id`                                     | ID único del registro                                         |
| `data.cdn_id`                                  | ID de la cadena                                               |
| `data.cdn_name`                                | Nombre de la cadena                                           |
| `data.restaurant_id`                           | ID del restaurante                                            |
| `data.restaurant`                              | Código del restaurante                                        |
| `data.period_id`                               | ID del período                                                |
| `data.final_date`                              | Fecha final del período                                       |
| `data.start_date`                              | Fecha de inicio del período                                   |
| `data.sales`                                   | Array de ventas por cajero y método de pago                   |
| `data.sales[].cashier`                         | Nombre del cajero                                             |
| `data.sales[].payment_method_id`               | ID del método de pago                                         |
| `data.sales[].payment_method`                  | Nombre del método de pago                                     |
| `data.sales[].value`                           | Valor reportado por el cajero                                 |
| `data.sales[].pos_calculated`                  | Valor calculado por el sistema POS                            |
| `data.sales[].transactions`                    | Número de transacciones                                       |
| `data.total`                                   | Array con totales consolidados por cajero                     |
| `data.total[].cashier`                         | Nombre del cajero                                             |
| `data.total[].value`                           | Valor total reportado                                         |
| `data.total[].pos_calculated`                  | Valor total calculado por POS                                 |
| `data.total[].transactions`                    | Total de transacciones                                        |
| `data.total[].cash_register_subscription_id`   | ID de la caja registradora                                    |
| `data.total[].cash_register_subscription_name` | Nombre de la caja registradora                                |
| `data.total[].surplus_or_shortage`             | Sobrante o faltante (diferencia entre value y pos_calculated) |

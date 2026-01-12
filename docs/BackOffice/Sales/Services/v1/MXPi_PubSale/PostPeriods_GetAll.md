## Obtener Períodos

### Método HTTP

`POST`

### URL

```
{{server-bo}}/api/v1/periods
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "first": 0,
  "rows": 10,
  "sort_field": "start_date",
  "sort_order": -1,
  "search": "",
  "filter": [
    {
      "field": "restaurant",
      "value": "G008"
    }
  ]
}
```

### Descripción de Campos del Cuerpo

| Campo            | Tipo   | Description                                             |
| ---------------- | ------ | ------------------------------------------------------- |
| `cdn_id`         | string | ID de la cadena                                         |
| `first`          | number | Índice inicial de los registros                         |
| `rows`           | number | Cantidad de resultados a devolver por página            |
| `sort_field`     | string | Campo por el cual ordenar (por defecto start_date)      |
| `sort_order`     | number | Orden de clasificación (1: ascendente, -1: descendente) |
| `search`         | string | Filtro general para buscar texto                        |
| `filter`         | array  | Array de filtros específicos                            |
| `filter[].field` | string | Campo a filtrar                                         |
| `filter[].value` | string | Valor del filtro                                        |

### Respuestas del Servidor

#### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "description": "Data returned succesfully",
  "data": {
    "total_rows": 100,
    "rows": [
      {
        "_id": "5b3b130c-e925-45dc-a6a3-c4a6616ffc5f",
        "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
        "cdn_name": "Cadena Ejemplo",
        "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
        "restaurant": "G001",
        "period_id": "26617b88-3c44-4c0b-87d7-616ec6339ffd",
        "final_date": "2025-12-02T00:00:00.000Z",
        "start_date": "2025-12-02T00:00:00.000Z",
        "sales": [
          {
            "gross_sales": 19.5,
            "net_sales": 16.95,
            "tax_sales": 2.55,
            "tax_percentages": [
              {
                "percentage": 8,
                "amount": 2.55
              }
            ],
            "zero_sale": 0,
            "discount": {
              "total_discount": 0,
              "tax_discount": 0,
              "zero_discount": 0
            },
            "service": 0,
            "transactions": 3,
            "means_of_sale": "local"
          }
        ],
        "total": {
          "gross_sales": 19.5,
          "net_sales": 16.95,
          "tax_sales": 2.55,
          "tax_percentages": [
            {
              "percentage": 8,
              "amount": 2.55
            }
          ],
          "zero_sale": 0,
          "discount": {
            "total_discount": 0,
            "tax_discount": 0,
            "zero_discount": 0
          },
          "service": 0,
          "transactions": 3
        },
        "status": {
          "status_id": "1a6bb069-798a-e442-ac49-7cdcfbb612fc",
          "status_name": "Pendiente",
          "description": "Estado periodo de venta pendiente",
          "color": "#ff8080",
          "background_color": "#ffffff"
        }
      }
    ]
  }
}
```

#### Descripción de la Respuesta Exitosa

| Campo                                              | Description                                 |
| -------------------------------------------------- | ------------------------------------------- |
| `code`                                             | Código de respuesta (200 = éxito)           |
| `description`                                      | Descripción del resultado                   |
| `data`                                             | Objeto con los datos paginados              |
| `data.total_rows`                                  | Número total de registros disponibles       |
| `data.rows`                                        | Array con los registros de la página actual |
| `data.rows[]._id`                                  | ID único del período                        |
| `data.rows[].cdn_id`                               | ID de la cadena                             |
| `data.rows[].cdn_name`                             | Nombre de la cadena                         |
| `data.rows[].restaurant_id`                        | ID del restaurante                          |
| `data.rows[].restaurant`                           | Código del restaurante                      |
| `data.rows[].period_id`                            | ID del período                              |
| `data.rows[].final_date`                           | Fecha final del período                     |
| `data.rows[].start_date`                           | Fecha de inicio del período                 |
| `data.rows[].sales`                                | Array de ventas por medio de venta          |
| `data.rows[].sales[].gross_sales`                  | Ventas brutas                               |
| `data.rows[].sales[].net_sales`                    | Ventas netas                                |
| `data.rows[].sales[].tax_sales`                    | Impuestos sobre ventas                      |
| `data.rows[].sales[].tax_percentages`              | Array de porcentajes de impuestos           |
| `data.rows[].sales[].tax_percentages[].percentage` | Porcentaje del impuesto                     |
| `data.rows[].sales[].tax_percentages[].amount`     | Monto del impuesto                          |
| `data.rows[].sales[].zero_sale`                    | Venta tarifa cero                           |
| `data.rows[].sales[].discount`                     | Objeto de descuentos                        |
| `data.rows[].sales[].discount.total_discount`      | Descuento total                             |
| `data.rows[].sales[].discount.tax_discount`        | Descuento de impuestos                      |
| `data.rows[].sales[].discount.zero_discount`       | Descuento tarifa cero                       |
| `data.rows[].sales[].service`                      | Cargo por servicio                          |
| `data.rows[].sales[].transactions`                 | Número de transacciones                     |
| `data.rows[].sales[].means_of_sale`                | Medio de venta (local/delivery)             |
| `data.rows[].total`                                | Totales consolidados del período            |
| `data.rows[].total.gross_sales`                    | Total de ventas brutas                      |
| `data.rows[].total.net_sales`                      | Total de ventas netas                       |
| `data.rows[].total.tax_sales`                      | Total de impuestos                          |
| `data.rows[].total.tax_percentages`                | Array de totales por porcentaje de impuesto |
| `data.rows[].total.zero_sale`                      | Total venta tarifa cero                     |
| `data.rows[].total.discount`                       | Objeto de descuentos totales                |
| `data.rows[].total.service`                        | Total cargo por servicio                    |
| `data.rows[].total.transactions`                   | Total de transacciones                      |
| `data.rows[].status`                               | Objeto con información del estado           |
| `data.rows[].status.status_id`                     | ID del estado                               |
| `data.rows[].status.status_name`                   | Nombre del estado                           |
| `data.rows[].status.description`                   | Descripción del estado                      |
| `data.rows[].status.color`                         | Color del estado                            |
| `data.rows[].status.background_color`              | Color de fondo del estado                   |

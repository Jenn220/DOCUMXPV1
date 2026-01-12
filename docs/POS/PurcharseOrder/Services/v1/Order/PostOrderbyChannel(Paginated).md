## Obtener Órdenes por Canal

### Método HTTP

`POST`

### URL

```
{{server_purchaseOrders}}/api/v1/order/get_order_by_channel
```

### Parámetros de Query

| Key        | Value                                | Descripción                    |
| ---------- | ------------------------------------ | ------------------------------ |
| franchise  | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "first": 0,
  "rows": 10,
  "sort_field": "created_at",
  "sort_order": -1,
  "search": "",
  "filters": [
    {
      "field": "channel._id",
      "value": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo             | Tipo   | Descripción                                           |
| ----------------- | ------ | ----------------------------------------------------- |
| `first`           | number | Índice del primer registro a recuperar                |
| `rows`            | number | Cantidad de registros a recuperar                     |
| `sort_field`      | string | Campo por el cual ordenar los resultados              |
| `sort_order`      | number | Orden de clasificación (-1 descendente, 1 ascendente) |
| `search`          | string | Término de búsqueda                                   |
| `filters`         | array  | Lista de filtros a aplicar                            |
| `filters[].field` | string | Campo sobre el cual aplicar el filtro                 |
| `filters[].value` | string | Valor del filtro                                      |

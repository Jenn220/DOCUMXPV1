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

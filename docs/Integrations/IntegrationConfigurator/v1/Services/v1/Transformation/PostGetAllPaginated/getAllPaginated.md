## Obtener Transformaciones Paginadas

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/transformation/getAllPaginated
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "string",
  "sort_order": 0,
  "sort_field": "string",
  "rows": 20,
  "first": 1
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo    | Requerido | Descripción                                           |
| ------------ | ------- | --------- | ----------------------------------------------------- |
| `search`     | string  | No        | Texto de búsqueda                                     |
| `sort_order` | integer | No        | Orden de clasificación (1 ascendente, -1 descendente) |
| `sort_field` | string  | No        | Campo por el cual ordenar                             |
| `rows`       | integer | No        | Cantidad de registros por página                      |
| `first`      | integer | No        | Índice del primer registro a obtener                  |

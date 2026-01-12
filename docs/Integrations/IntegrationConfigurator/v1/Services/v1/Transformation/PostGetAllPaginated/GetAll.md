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
  "first": 1,
  "activeOnly": true
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
| `activeOnly` | boolean | No        | Filtra solo registros en estado activo                |

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Encontrado Correctamente",
  "data": {
    "total_rows": 100,
    "rows": [
      {
        "id": "98f556df-6edc-4e7c-8fad-b127ad2f3541",
        "code": "T001",
        "name": "Propagation Menu Plu",
        "description": "Transformation for the propagation of the products"
      },
      {
        "id": "98f556df-6edc-4e7c-8fad-b127ad2f3541",
        "code": "T002",
        "name": "Propagation Menu Menu",
        "description": "Transformation for the propagation of the menus"
      },
      {
        "id": "e28a77e1-c550-4efa-94e6-24566be52824",
        "code": "T003",
        "name": "Propagation Menu Suggested Questions",
        "description": "Transformation for the propagation of the suggested questions"
      },
      {
        "id": "0c139b10-9519-4d62-a28a-c4840339f28b",
        "code": "T004",
        "name": "Propagation Menu Up Selling",
        "description": "Transformation for the propagation of the up sellings"
      }
    ]
  }
}
```

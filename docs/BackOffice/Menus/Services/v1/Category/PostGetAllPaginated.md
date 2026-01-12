## Obtener Categorías Paginadas

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/category/getallpaginated
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |
| `country`   | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país         |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "pageNumber": 1,
  "pageSize": 10,
  "sortField": "name",
  "sortOrder": "asc",
  "filter": ""
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo    | Requerido | Descripción                       |
| ------------ | ------- | --------- | --------------------------------- |
| `pageNumber` | integer | Sí        | Número de página                  |
| `pageSize`   | integer | Sí        | Cantidad de registros por página  |
| `sortField`  | string  | No        | Campo por el cual ordenar         |
| `sortOrder`  | string  | No        | Orden de clasificación (asc/desc) |
| `filter`     | string  | No        | Filtro de búsqueda                |

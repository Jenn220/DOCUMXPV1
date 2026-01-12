## Obtener Todos los Productos Paginados

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/product/getallpaginated
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

### Descripción de Campos del Cuerpo

| Campo        | Tipo   | Description                                |
| ------------ | ------ | ------------------------------------------ |
| `pageNumber` | number | Número de página a consultar               |
| `pageSize`   | number | Cantidad de registros por página           |
| `sortField`  | string | Campo por el cual ordenar los resultados   |
| `sortOrder`  | string | Orden de clasificación (asc/desc)          |
| `filter`     | string | Término de búsqueda para filtrar productos |

## Obtener Todos los Iconos Paginados

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/icon/getall_paginated
```

### Parámetros de Query

No requiere parámetros de query.

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

| Campo        | Tipo   | Description                              |
| ------------ | ------ | ---------------------------------------- |
| `pageNumber` | number | Número de página a consultar             |
| `pageSize`   | number | Cantidad de registros por página         |
| `sortField`  | string | Campo por el cual ordenar los resultados |
| `sortOrder`  | string | Orden de clasificación (asc/desc)        |
| `filter`     | string | Término de búsqueda para filtrar iconos  |

## Obtener Todas las Preguntas Sugeridas Paginadas

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/suggestedquestion/getall_paginated
```

### Parámetros de Query

| Key         | Value                                  | Description         |
| ----------- | -------------------------------------- | ------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia |

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
| `filter`     | string | Término de búsqueda para filtrar preguntas |

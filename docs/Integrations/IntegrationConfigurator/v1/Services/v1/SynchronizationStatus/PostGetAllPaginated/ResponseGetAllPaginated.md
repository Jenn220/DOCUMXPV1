## Obtener Estados de Sincronización Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/YOUR_REDIS_OR_AZURE_KEY_HERE
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

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": 20,
  "description": "Data returned succesfully",
  "data": {
    "total_rows": 100,
    "rows": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "key": "success",
        "text": "Exitoso",
        "color": "#1B3E19",
        "background": "#E2F7E2"
      },
      {
        "id": "fd61c187-3ecc-4114-b83f-d10af3bc3256",
        "key": "error",
        "text": "Error",
        "color": "#810C22",
        "background": "#FBD5DC"
      },
      {
        "id": "f316a140-f62e-493e-b00e-7fbc19d9bbb5",
        "key": "running",
        "text": "Ejecutando",
        "color": "#1D1819",
        "background": "#DFDEDE"
      },
      {
        "id": "f285b374-252c-49df-a67f-a7eb6bd02a76",
        "key": "canceled",
        "text": "Cancelado",
        "color": "#810C22",
        "background": "#FBECD5"
      },
      {
        "id": "e2a3cc14-211c-4539-8b1e-52bc3a8c000f",
        "key": "deleted",
        "text": "Eliminado",
        "color": "#FF333B",
        "background": "#000000"
      },
      {
        "id": "e2a3cc14-211c-4539-8b1e-72bc3a8c001f",
        "key": "programmed",
        "text": "Programado",
        "color": "#0040B0",
        "background": "#EBF8FF"
      }
    ]
  }
}
```

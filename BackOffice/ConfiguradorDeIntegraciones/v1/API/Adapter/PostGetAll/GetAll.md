## Obtener Adaptadores Paginados

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/adapters/getAllPaginated
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "search": "",
  "sort_order": 0,
  "sort_field": "",
  "rows": 20,
  "first": 1,
  "activeOnly": true
}
```

### Descripción de Campos

| Campo        | Tipo    | Valores Permitidos | Descripción                                                           |
| ------------ | ------- | ------------------ | --------------------------------------------------------------------- |
| `search`     | string  | -                  | Término de búsqueda para filtrar resultados                           |
| `sort_order` | integer | `1`, `-1`, `0`     | Orden de clasificación (1: ascendente, -1: descendente, 0: sin orden) |
| `sort_field` | string  | -                  | Campo por el cual ordenar los resultados                              |
| `rows`       | integer | -                  | Número de registros por página                                        |
| `first`      | integer | -                  | Número de la primera página                                           |
| `activeOnly` | boolean | `true`, `false`    | Filtra los registros en estado activo cuando es `true`                |

### Notas

- `activeOnly: true` filtra únicamente los registros que están en estado activo
- El parámetro `sort_order` acepta tres valores: 1 (ascendente), -1 (descendente), 0 (sin orden específico)

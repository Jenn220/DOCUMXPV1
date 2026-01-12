## Eliminar Adaptador

### Método HTTP

`DELETE`

### URL

```
{{server_orchestrator}}/api/v1/adapters/Delete
```

### Parámetros de Query

| Key  | Value                                  | Description                       |
| ---- | -------------------------------------- | --------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID único del adaptador a eliminar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Notas

- Este endpoint elimina el adaptador identificado por el parámetro `id`
- La operación es irreversible

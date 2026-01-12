## Obtener Datos de PLUs por IDs

### Método HTTP

`GET`

### URL

```
{{server_BO_Menus}}/api/v1/product/getpludatabyids
```

### Parámetros de Query

| Key         | Value                                  | Description                  |
| ----------- | -------------------------------------- | ---------------------------- |
| `plu_ids`   | `string1`                              | ID del PLU (puede repetirse) |
| `plu_ids`   | `string2`                              | ID del PLU (puede repetirse) |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia          |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

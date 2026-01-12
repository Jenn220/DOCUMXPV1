## Eliminar Categoría de Menú

### Método HTTP

`DELETE`

### URL

```
{{server_BO_Menus}}/api/v1/menucategory/delete_category
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "string",
  "franchise_id": "string"
}
```

### Descripción de Campos del Cuerpo

| Campo          | Tipo   | Description                   |
| -------------- | ------ | ----------------------------- |
| `id`           | string | ID de la categoría a eliminar |
| `franchise_id` | string | ID de la franquicia           |

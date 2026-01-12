## Obtener Datos Relacionados por ID de Producto

### Método HTTP

`GET`

### URL

```
{{server_menus}}/api/v1/posplu/get_related_data_by_product_id
```

### Parámetros de Query

| Key                    | Value                                | Descripción                           |
| ---------------------- | ------------------------------------ | ------------------------------------- |
| franchise              | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia        |
| category_plu           | 9bdeeb7f-136c-8f6a-489b-d9fc02db904a | Identificador de categoría del PLU    |
| classification         | 3fa85f64-5717-4562-b3fc-2c963f66afa6 | Identificador de la clasificación     |
| plu                    | 3fa85f64-5717-4562-b3fc-2c963f66afa6 | Identificador del PLU                 |
| device                 | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador del dispositivo         |
| menu_deep_level_nested | 3                                    | Nivel de profundidad del menú anidado |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

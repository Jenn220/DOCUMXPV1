## Obtener Todos los Menús con Preguntas Sugeridas

### Método HTTP

`GET`

### URL

```
{{server_menus}}/menus/api/v1/menu/get_all_menus_plus_suggested_questions
```

### Parámetros de Query

| Key                    | Value                                | Descripción                            |
| ---------------------- | ------------------------------------ | -------------------------------------- |
| franchise              | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia         |
| restaurant             | 18ab3836-3202-f6d4-1eef-a5b5de5a8e40 | Identificador del restaurante          |
| category_id_plu        | 9bdeeb7f-136c-8f6a-489b-d9fc02db904a | Identificador de categoría del PLU     |
| device                 | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador del dispositivo          |
| menu_deep_level_nested | 3                                    | Nivel de profundidad del menú anidado  |
| cdn_tax_default        | d00c4be9-a547-f72d-b87b-2abaebc07f4b | Identificador del impuesto por defecto |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Obtener Inicio de Menús con Preguntas Sugeridas

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/menus/api/v1/menu/get_start_all_menus_plus_suggested_questions
```

### Headers

| Key          | Value            | Descripción                       |
| ------------ | ---------------- | --------------------------------- |
| Content-Type | application/json | Tipo de contenido de la solicitud |
| is_download  | is_download      | Indicador de descarga             |

### Parámetros de Query

| Key                    | Value                                | Descripción                          |
| ---------------------- | ------------------------------------ | ------------------------------------ |
| franchise              | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia       |
| restaurant             | 24260579-faf8-763f-aac7-5e16faff96d1 | Identificador del restaurante        |
| category_id_plu        | 9bdeeb7f-136c-8f6a-489b-d9fc02db904a | Identificador de categoría PLU       |
| device                 | 8028a2ff-c639-6df4-68e8-8982c0256be3 | Identificador del dispositivo        |
| menu_deep_level_nested | 3                                    | Nivel de anidamiento del menú        |
| cdn_tax_default        | 568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d | Impuesto predeterminado de la cadena |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

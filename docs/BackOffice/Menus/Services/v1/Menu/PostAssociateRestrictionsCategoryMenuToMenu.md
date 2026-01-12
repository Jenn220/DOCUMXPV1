## Asociar Restricciones de Categoría al Menú

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/menu/asocciate_restrictions_category_menu_to_menu
```

### Parámetros de Query

| Key         | Value                                  | Description                       |
| ----------- | -------------------------------------- | --------------------------------- |
| `franchise` | `bc2d8ada-e25e-1bb7-55fe-32d1205ac4af` | ID de la franquicia               |
| `user`      | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "menu_id": "string",
  "category_id": "string",
  "restrictions": {
    "restaurants": ["string"],
    "schedules": [
      {
        "day": 0,
        "start_time": "string",
        "end_time": "string"
      }
    ]
  }
}
```

### Descripción de Campos del Cuerpo

| Campo                                 | Tipo     | Description                             |
| ------------------------------------- | -------- | --------------------------------------- |
| `menu_id`                             | string   | ID del menú                             |
| `category_id`                         | string   | ID de la categoría a restringir         |
| `restrictions`                        | object   | Objeto de restricciones                 |
| `restrictions.restaurants`            | string[] | Array de IDs de restaurantes permitidos |
| `restrictions.schedules`              | array    | Array de horarios de disponibilidad     |
| `restrictions.schedules[].day`        | number   | Día de la semana (0-6)                  |
| `restrictions.schedules[].start_time` | string   | Hora de inicio del horario              |
| `restrictions.schedules[].end_time`   | string   | Hora de fin del horario                 |

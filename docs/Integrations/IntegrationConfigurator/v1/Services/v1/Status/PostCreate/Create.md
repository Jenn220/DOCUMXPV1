## Crear Estado

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/status/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "key": "active",
  "text": "Activo",
  "color": "#1B3E19",
  "background": "#E2F7E2"
}
```

### Descripción de Campos

| Campo        | Tipo   | Restricciones                           | Descripción                           |
| ------------ | ------ | --------------------------------------- | ------------------------------------- |
| `id`         | string | Máximo: 100 caracteres, **Obligatorio** | ID del estado                         |
| `key`        | string | Máximo: 100 caracteres, **Obligatorio** | Clave del estado                      |
| `text`       | string | Máximo: 100 caracteres, **Obligatorio** | Texto del estado                      |
| `color`      | string | Máximo: 100 caracteres, **Obligatorio** | Color del texto (formato hexadecimal) |
| `background` | string | Máximo: 100 caracteres, **Obligatorio** | Color de fondo (formato hexadecimal)  |

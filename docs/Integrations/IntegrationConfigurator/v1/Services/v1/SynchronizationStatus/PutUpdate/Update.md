## Actualizar Estado de Sincronización

### Método HTTP

`PUT`

### URL

```
{{server_orchestrator}}/api/v1/synchronizationStates/update
```

### Parámetros de Query

| Key  | Value                                  | Description                                  |
| ---- | -------------------------------------- | -------------------------------------------- |
| `id` | `b5ad9754-0419-46e5-b556-7ab1ab8db3e1` | ID del estado de sincronización a actualizar |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "key": "success",
  "text": "Exitoso",
  "color": "#1B3E19",
  "background": "#E2F7E2"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo   | Requerido | Descripción                            |
| ------------ | ------ | --------- | -------------------------------------- |
| `key`        | string | No        | Clave identificadora del estado        |
| `text`       | string | No        | Texto descriptivo del estado           |
| `color`      | string | No        | Color del texto en formato hexadecimal |
| `background` | string | No        | Color de fondo en formato hexadecimal  |

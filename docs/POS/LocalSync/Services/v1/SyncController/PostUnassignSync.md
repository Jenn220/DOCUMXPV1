## Desasignar Sincronización

### Método HTTP

`POST`

### URL

```
{{server_localSync}}/api/unassign_Sync
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchise": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "restaurant": "24260579-faf8-763f-aac7-5e16faff96d1"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo   | Descripción                    |
| ------------ | ------ | ------------------------------ |
| `franchise`  | string | Identificador de la franquicia |
| `restaurant` | string | Identificador del restaurante  |

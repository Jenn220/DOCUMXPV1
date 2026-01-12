## Ejecutar Transacción - Impresión de Factura

### Método HTTP

`POST`

### URL

```
{{server}}/api/v1/transaction/TX012
```

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
  "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "period_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo           | Tipo   | Descripción             |
| --------------- | ------ | ----------------------- |
| `restaurant_id` | string | ID UUID del restaurante |
| `cdn_id`        | string | ID UUID de la cadena    |
| `period_id`     | string | ID UUID del período     |

### Respuestas del Servidor

#### 400 Bad Request - Campos Faltantes

```json
{
  "code": 400,
  "status": "success",
  "alert": "Impresión NO generada correctamente",
  "messages": ["faltan campos....."]
}
```

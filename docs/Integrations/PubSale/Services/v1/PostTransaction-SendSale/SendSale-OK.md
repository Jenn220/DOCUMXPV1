## Ejecutar Transacción - Impresión de Factura

### Método HTTP

`POST`

### URL

```
{{server_pub_sale}}/api/v1/transaction/TX012
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
  "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "restaurant_id": "24260579-faf8-763f-aac7-5e16faff96d1",
  "period_id": "51cf8bd2-6159-49fe-b303-579e7eba3a7e"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo           | Tipo   | Descripción             |
| --------------- | ------ | ----------------------- |
| `cdn_id`        | string | ID UUID de la cadena    |
| `restaurant_id` | string | ID UUID del restaurante |
| `period_id`     | string | ID UUID del período     |

### Respuestas del Servidor

#### 200 OK - Impresión Exitosa

```json
{
  "code": 200,
  "status": "success",
  "alert": "Impresión generada correctamente",
  "messages": ["Impresión de factura completada"]
}
```

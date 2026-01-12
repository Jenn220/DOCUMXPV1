## Obtener Variables de Entorno por Dominio

### Método HTTP

`POST`

### URL

```
{{server_configurations}}/api/v1/enviromentvariables/get_values_by_domain
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "domain": "backoffice.kfc.com.mx"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo    | Tipo   | Requerido | Descripción         |
| -------- | ------ | --------- | ------------------- |
| `domain` | string | Sí        | Dominio a consultar |

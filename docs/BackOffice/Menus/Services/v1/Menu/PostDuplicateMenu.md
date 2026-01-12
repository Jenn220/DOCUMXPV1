## Duplicar Menú

### Método HTTP

`POST`

### URL

```
{{server_BO_Menus}}/api/v1/menu/duplicate_menu
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
["902499bf-284f-4f2e-80b7-60ef60c6bd9c"]
```

### Descripción de Campos del Cuerpo

| Campo | Tipo     | Description                      |
| ----- | -------- | -------------------------------- |
| Array | string[] | Array de IDs de menús a duplicar |

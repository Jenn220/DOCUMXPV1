## Crear Catálogo

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/catalogs/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "prueba",
  "code": 1,
  "value": "prueba",
  "fatherId": null,
  "isFather": true,
  "detail": "",
  "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Descripción de Campos

| Campo      | Tipo        | Restricciones                  | Descripción                                                          |
| ---------- | ----------- | ------------------------------ | -------------------------------------------------------------------- |
| `name`     | string      | varchar(250) - **Obligatorio** | Nombre del catálogo                                                  |
| `code`     | number      | **Obligatorio**                | Código numérico del catálogo                                         |
| `value`    | string      | varchar(250) - **Obligatorio** | Valor del catálogo                                                   |
| `fatherId` | string/null | Por defecto: `null`            | ID del padre cuando es hijo, se crea con el código interno del padre |
| `isFather` | boolean     | -                              | Indica si es un catálogo padre                                       |
| `detail`   | string      | varchar(300), nullable         | Detalle adicional del catálogo                                       |
| `statusId` | string      | Por defecto: activo            | ID del estado del catálogo                                           |

## Validar Subsidio

### Método HTTP

`POST`

### URL

```
{{server_POS_Subsidy}}/api/v1/subsidy/validate
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "id_restaurant": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "cash_register_subscription_id": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_seller": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "name_seller": "Juan.Maya",
  "id_administrator": "",
  "id_campaign": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_product": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_client": ""
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                           | Tipo   | Descripción                                                 |
| ------------------------------- | ------ | ----------------------------------------------------------- |
| `id_restaurant`                 | string | ID del restaurante                                          |
| `cash_register_subscription_id` | string | ID de la caja física                                        |
| `id_seller`                     | string | ID del vendedor                                             |
| `name_seller`                   | string | Nombre del vendedor                                         |
| `id_administrator`              | string | ID del administrador (opcional cuando se aprobó el gerente) |
| `id_campaign`                   | string | ID de la campaña                                            |
| `id_product`                    | string | ID del producto                                             |
| `id_client`                     | string | ID del cliente (opcional si la campaña es mayor a cero)     |

### Respuestas del Servidor

**200 OK - Consulta Exitosa**

```json
{
  "enable": "true",
  "subsidy_plus": 2,
  "id_subsidy_plus_aplicated": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "payment_methods": []
}
```

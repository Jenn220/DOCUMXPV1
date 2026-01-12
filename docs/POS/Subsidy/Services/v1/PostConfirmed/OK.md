## Confirmar Subsidio

### Método HTTP

`POST`

### URL

```
{{server_subsidio}}/api/v1/subsidy/confirmed
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
  "id_campaign": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_product": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_subsidy_plus": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "id_client": "",
  "id_order": ""
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                           | Tipo   | Descripción                                             |
| ------------------------------- | ------ | ------------------------------------------------------- |
| `id_restaurant`                 | string | ID del restaurante                                      |
| `cash_register_subscription_id` | string | ID de la caja física                                    |
| `id_seller`                     | string | ID del vendedor                                         |
| `name_seller`                   | string | Nombre del vendedor                                     |
| `id_campaign`                   | string | ID de la campaña                                        |
| `id_product`                    | string | ID del producto                                         |
| `id_subsidy_plus`               | string | ID del subsidio plus (Menus_POS_Enabled_Subsidy_Plus)   |
| `id_client`                     | string | ID del cliente (opcional si la campaña es mayor a cero) |
| `id_order`                      | string | ID de la orden                                          |

### Respuestas del Servidor

**200 OK - Consulta Exitosa**

```json
{
  "response": true
}
```

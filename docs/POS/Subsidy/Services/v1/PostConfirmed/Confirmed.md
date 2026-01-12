## Confirmar Subsidio

### Método HTTP

`POST`

### URL

```
{{server_POS_Subsidy}}/api/v1/subsidy/confirmed
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
  "id_client": "",
  "subsidy_plus": 2,
  "id_subsidy_plus_aplicated": "07feacd6-998b-4218-aa99-693ce1b350bd",
  "confirmed": "true"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                           | Tipo   | Descripción                                                                                                       |
| ------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------- |
| `id_restaurant`                 | string | ID del restaurante                                                                                                |
| `cash_register_subscription_id` | string | ID de la caja física                                                                                              |
| `id_seller`                     | string | ID del vendedor                                                                                                   |
| `name_seller`                   | string | Nombre del vendedor                                                                                               |
| `id_client`                     | string | ID del cliente para confirmar que el mismo que apartó sea el que pagó                                             |
| `subsidy_plus`                  | number | Cantidad de subsidio plus                                                                                         |
| `id_subsidy_plus_aplicated`     | string | ID del intento de subsidio plus aplicado                                                                          |
| `confirmed`                     | string | Indica si se confirma (true) o libera el intento de consumo de subsidio y devuelve el dinero a la campaña (false) |

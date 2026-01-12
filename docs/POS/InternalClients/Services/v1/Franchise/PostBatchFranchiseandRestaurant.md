## Procesar Lote de Franquicia y Restaurante

### Método HTTP

`POST`

### URL

```
{{server_internalClients}}/api/v1/franchise/batch_franchise_and_restaurant
```

### Parámetros de Query

| Key        | Value           | Descripción                    |
| ---------- | --------------- | ------------------------------ |
| franchise  | franchise-uuid  | Identificador de la franquicia |
| restaurant | restaurant-uuid | Identificador del restaurante  |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "period": [
    {
      "_id": "00000000-0000-0000-0000-000000000000",
      "restaurant_id": "00000000-0000-0000-0000-000000000000",
      "user_id": "00000000-0000-0000-0000-000000000000",
      "cdn_id": "00000000-0000-0000-0000-000000000000",
      "restaurant_name": "Restaurant Name",
      "cdn_restaurant_name": "CDN Restaurant Name",
      "start_date": "2023-01-01T00:00:00Z",
      "final_date": "2023-12-31T23:59:59Z",
      "periodtype": "monthly",
      "status_Period": {
        "_id": "00000000-0000-0000-0000-000000000000",
        "status_name": "Active",
        "description": "Active period",
        "color": "#00FF00",
        "background_color": "#FFFFFF",
        "codeType": "ACTIVE",
        "statusIcon": "check",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z"
      }
    }
  ],
  "cash_registers_suscription": [
    {
      "cash_registers_subscriptions_id": "00000000-0000-0000-0000-000000000000",
      "cash_register_subscriptions_name": "Cash Register 1",
      "type_fund_id": "00000000-0000-0000-0000-000000000000",
      "value_fund": 1000,
      "status_cash_register_subscription": "00000000-0000-0000-0000-000000000000",
      "status_fund_id": "00000000-0000-0000-0000-000000000000",
      "user": {
        "_id": "00000000-0000-0000-0000-000000000000",
        "name": "User Name"
      },
      "device_active": {
        "os_name": "Windows",
        "unique_id_device": "device-12345"
      },
      "profile_id": "00000000-0000-0000-0000-000000000000",
      "reason_rejection_id": "00000000-0000-0000-0000-000000000000",
      "txt_reason_rejection": "Rejection reason text",
      "is_active": true,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                                            | Tipo    | Descripción                                          |
| ---------------------------------------------------------------- | ------- | ---------------------------------------------------- |
| `period`                                                         | array   | Lista de períodos                                    |
| `period[]._id`                                                   | string  | Identificador del período                            |
| `period[].restaurant_id`                                         | string  | Identificador del restaurante                        |
| `period[].user_id`                                               | string  | Identificador del usuario                            |
| `period[].cdn_id`                                                | string  | Identificador de la cadena                           |
| `period[].restaurant_name`                                       | string  | Nombre del restaurante                               |
| `period[].cdn_restaurant_name`                                   | string  | Nombre de la cadena del restaurante                  |
| `period[].start_date`                                            | string  | Fecha de inicio del período (formato ISO)            |
| `period[].final_date`                                            | string  | Fecha de finalización del período (formato ISO)      |
| `period[].periodtype`                                            | string  | Tipo de período                                      |
| `period[].status_Period`                                         | object  | Estado del período                                   |
| `period[].status_Period._id`                                     | string  | Identificador del estado                             |
| `period[].status_Period.status_name`                             | string  | Nombre del estado                                    |
| `period[].status_Period.description`                             | string  | Descripción del estado                               |
| `period[].status_Period.color`                                   | string  | Color del estado                                     |
| `period[].status_Period.background_color`                        | string  | Color de fondo del estado                            |
| `period[].status_Period.codeType`                                | string  | Código del tipo de estado                            |
| `period[].status_Period.statusIcon`                              | string  | Ícono del estado                                     |
| `period[].status_Period.created_at`                              | string  | Fecha de creación del estado (formato ISO)           |
| `period[].status_Period.updated_at`                              | string  | Fecha de actualización del estado (formato ISO)      |
| `cash_registers_suscription`                                     | array   | Lista de suscripciones de cajas registradoras        |
| `cash_registers_suscription[].cash_registers_subscriptions_id`   | string  | Identificador de la suscripción de caja registradora |
| `cash_registers_suscription[].cash_register_subscriptions_name`  | string  | Nombre de la suscripción de caja registradora        |
| `cash_registers_suscription[].type_fund_id`                      | string  | Identificador del tipo de fondo                      |
| `cash_registers_suscription[].value_fund`                        | number  | Valor del fondo                                      |
| `cash_registers_suscription[].status_cash_register_subscription` | string  | Estado de la suscripción de caja registradora        |
| `cash_registers_suscription[].status_fund_id`                    | string  | Identificador del estado del fondo                   |
| `cash_registers_suscription[].user`                              | object  | Usuario asociado                                     |
| `cash_registers_suscription[].user._id`                          | string  | Identificador del usuario                            |
| `cash_registers_suscription[].user.name`                         | string  | Nombre del usuario                                   |
| `cash_registers_suscription[].device_active`                     | object  | Dispositivo activo                                   |
| `cash_registers_suscription[].device_active.os_name`             | string  | Nombre del sistema operativo                         |
| `cash_registers_suscription[].device_active.unique_id_device`    | string  | Identificador único del dispositivo                  |
| `cash_registers_suscription[].profile_id`                        | string  | Identificador del perfil                             |
| `cash_registers_suscription[].reason_rejection_id`               | string  | Identificador de razón de rechazo                    |
| `cash_registers_suscription[].txt_reason_rejection`              | string  | Texto de razón de rechazo                            |
| `cash_registers_suscription[].is_active`                         | boolean | Indica si está activo                                |
| `cash_registers_suscription[].created_at`                        | string  | Fecha de creación (formato ISO)                      |
| `cash_registers_suscription[].updated_at`                        | string  | Fecha de actualización (formato ISO)                 |

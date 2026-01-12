## Notificar Período

### Método HTTP

`POST`

### URL

```
{{server_cod}}/api/cod/period/notify
```

### Headers

| Key           | Value            | Descripción                       |
| ------------- | ---------------- | --------------------------------- |
| Content-Type  | application/json | Tipo de contenido de la solicitud |
| Authorization | Bearer {{token}} | Token de autenticación            |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "restaurant_id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
  "restaurant_name": "KFC Reforma",
  "street": "Av. Paseo de la Reforma 222",
  "state": "Ciudad de México",
  "phone": "+525555551234",
  "franchise_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "franchise_name": "KFC México",
  "period_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
  "status": true,
  "configuration": {
    "couch_db": {
      "url": "http://couchdb.example.com:5984",
      "database": "kfc_orders",
      "username": "admin",
      "password": "password123"
    },
    "server_opl": {
      "url": "http://opl-server.example.com",
      "port": 8080,
      "apiKey": "OPL_API_KEY_123"
    },
    "events_opl": [
      {
        "eventId": "EVT001",
        "eventName": "ORDER_CREATED",
        "enabled": true
      },
      {
        "eventId": "EVT002",
        "eventName": "ORDER_COMPLETED",
        "enabled": true
      }
    ],
    "digital_order_mode": [
      {
        "modeId": "MODE001",
        "modeName": "KIOSK",
        "enabled": true
      },
      {
        "modeId": "MODE002",
        "modeName": "MOBILE",
        "enabled": true
      }
    ]
  },
  "cash_register_digital": [
    {
      "cash_register_id": "aa4ece7c-ec6e-ab01-26a7-95d2c2c809c0",
      "cash_register_name": "Caja 1",
      "user_seller_id": "c17b6e8d-88a5-9eb5-1f44-aeec161494da",
      "status": true
    },
    {
      "cash_register_id": "bb5fdf8d-fd7f-bc12-37b8-a6c3d3d910d1",
      "cash_register_name": "Caja 2",
      "user_seller_id": "d28c7f9e-99b6-ae96-2f55-bffd272605eb",
      "status": true
    }
  ]
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                                         | Tipo    | Descripción                           |
| --------------------------------------------- | ------- | ------------------------------------- |
| `restaurant_id`                               | string  | Identificador del restaurante         |
| `restaurant_name`                             | string  | Nombre del restaurante                |
| `street`                                      | string  | Dirección del restaurante             |
| `state`                                       | string  | Estado o ciudad                       |
| `phone`                                       | string  | Teléfono del restaurante              |
| `franchise_id`                                | string  | Identificador de la franquicia        |
| `franchise_name`                              | string  | Nombre de la franquicia               |
| `period_id`                                   | string  | Identificador del período             |
| `status`                                      | boolean | Estado del período                    |
| `configuration`                               | object  | Configuración del sistema             |
| `configuration.couch_db`                      | object  | Configuración de CouchDB              |
| `configuration.couch_db.url`                  | string  | URL de CouchDB                        |
| `configuration.couch_db.database`             | string  | Nombre de la base de datos            |
| `configuration.couch_db.username`             | string  | Usuario de CouchDB                    |
| `configuration.couch_db.password`             | string  | Contraseña de CouchDB                 |
| `configuration.server_opl`                    | object  | Configuración del servidor OPL        |
| `configuration.server_opl.url`                | string  | URL del servidor OPL                  |
| `configuration.server_opl.port`               | number  | Puerto del servidor                   |
| `configuration.server_opl.apiKey`             | string  | Clave API                             |
| `configuration.events_opl`                    | array   | Lista de eventos OPL                  |
| `configuration.events_opl[].eventId`          | string  | Identificador del evento              |
| `configuration.events_opl[].eventName`        | string  | Nombre del evento                     |
| `configuration.events_opl[].enabled`          | boolean | Estado del evento                     |
| `configuration.digital_order_mode`            | array   | Modos de orden digital                |
| `configuration.digital_order_mode[].modeId`   | string  | Identificador del modo                |
| `configuration.digital_order_mode[].modeName` | string  | Nombre del modo                       |
| `configuration.digital_order_mode[].enabled`  | boolean | Estado del modo                       |
| `cash_register_digital`                       | array   | Cajas registradoras digitales         |
| `cash_register_digital[].cash_register_id`    | string  | Identificador de la caja registradora |
| `cash_register_digital[].cash_register_name`  | string  | Nombre de la caja registradora        |
| `cash_register_digital[].user_seller_id`      | string  | Identificador del usuario vendedor    |
| `cash_register_digital[].status`              | boolean | Estado de la caja registradora        |

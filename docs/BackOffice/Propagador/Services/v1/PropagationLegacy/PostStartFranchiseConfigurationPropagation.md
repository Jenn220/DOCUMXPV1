## Iniciar Propagación de Configuración de Franquicia

### Método HTTP

`POST`

### URL

```
{{server_propagation}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key          | Value                                  | Description                       |
| ------------ | -------------------------------------- | --------------------------------- |
| `user`       | `3fa85f64-5717-4562-b3fc-2c963f66afa6` | ID del usuario que hace la acción |
| `country_id` | `d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f` | ID del país                       |

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "_id": "UUID('6fca9d50-87f3-189d-e2e6-91b5e3c601bc')",
  "franchise_name": "Franquicia 1",
  "country_id": "UUID('f2c13a02-3cb5-4781-9e10-d3f1519c51e2')",
  "menu_deep_level_nested": 3,
  "decimal_quantity": 6,
  "decimal_quantity_presentation": 2,
  "limit_time_remove_plu_from_order": 10,
  "limit_time_redirect_payments": 30,
  "limit_characters_comments": 100,
  "limit_max_size_batch_syncronize_orders": 100,
  "retries_period": 3,
  "theme_by_franchise": {
    "theme_id": "UUID('f5a6f1d1-0c76-41cb-9a5a-88d2ca7d4f8f')",
    "is_active": true
  },
  "status_franchise": "UUID('f5a6f1d1-0c76-41cb-9a5a-88d2ca7d4f8f')",
  "restaurants": [
    {
      "_id": "UUID('f5a6f1d1-0c76-41cb-9a5a-88d2ca7d4f8f')",
      "restaurant_name": "Restaurante Español",
      "company_id": "UUID('f5a6f1d1-0c76-41cb-9a5a-88d2ca7d4f8f')",
      "description": "mi descripcion",
      "address": "mi address",
      "cdn_restaurant_id": "UUID('f5a6f1d1-0c76-41cb-9a5a-88d2ca7d4f8f')",
      "restaurant_code": "KFC 001",
      "restaurant_image": "https://repositoryUatBO.azureedge.YOUR_REDIS_OR_AZURE_KEY_HERE.png",
      "city_id": "UUID('0fb70b94-ff83-4587-bcac-fcea5e719b5d')",
      "category_plu_default": "UUID('49c2e3df-ad5c-3bfb-7696-4d11175d7700')",
      "active_sincronization_chouch_db": true,
      "type_period_default": "Manual",
      "active_cash_reconciliation": true,
      "couch_db": {
        "username": "admin",
        "password": "admin",
        "endpoint": "https://172.177.155.78:6984/",
        "alias": "CDB_001_ECU_KFC_001"
      },
      "limit_retry_get_all_menus_products_max": 7,
      "retry_time_get_all_menus_products": 5,
      "status_restaurant": "UUID('49c2e3df-ad5c-3bfb-7696-4d11175d7700')",
      "schedules": {
        "is_active": true,
        "is_every_days": false,
        "every_days": [
          {
            "start": "10:00:00",
            "end": "12:00:00"
          }
        ],
        "monday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "tuesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "wednesday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "thursday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "friday": [
          {
            "start": "10:00",
            "end": "15:00"
          }
        ],
        "saturday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ],
        "sunday": [
          {
            "start": "12:00",
            "end": "18:00"
          }
        ]
      },
      "cash_registers_subscriptions": [
        {
          "_id": "UUID('6c2b968e-4d45-498a-9055-40fb25d66e73')",
          "cash_registers_subscriptions_name": "Caja 1",
          "description": "Caja Principal",
          "payment_type_default": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
          "method_payment_default": "UUID('6c5a9727-9303-99b8-e363-552d320738ff')",
          "default_value_fund": 50,
          "type_fund_id": "UUID('5f46c3b5-2a64-40db-81f9-d8a6bfb47c85')",
          "status_cash_register": "UUID('5f46c3b5-2a64-40db-81f9-d8a6bfb47c85')",
          "created_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
          "created_at": "2024-02-06T03:18:52.852Z",
          "updated_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
          "updated_at": "2024-05-31T06:42:27.014Z"
        }
      ],
      "created_at": "2024-02-06T03:18:52.852Z",
      "updated_at": "2024-05-31T06:42:27.014Z"
    }
  ],
  "tax_default": "UUID('397f770e-83dd-1942-83d3-676805bea4ca')",
  "administrators": [
    {
      "user_id": "UUID('397f770e-83dd-1942-83d3-676805bea4ca')"
    }
  ],
  "information_block_images": [
    {
      "imagen_id": "UUID('vok1vuvi8O004uKfP+Ccxw==')"
    }
  ],
  "created_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
  "updated_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
  "created_at": "2024-02-06T03:18:52.852Z",
  "updated_at": "2024-05-31T06:42:27.014Z",
  "limit_max_downloaded_restaurants": 3
}
```

### Descripción de Campos del Cuerpo

| Campo                                                                            | Tipo    | Description                                         |
| -------------------------------------------------------------------------------- | ------- | --------------------------------------------------- |
| `_id`                                                                            | string  | Identificador único de la franquicia                |
| `franchise_name`                                                                 | string  | Nombre de la franquicia                             |
| `country_id`                                                                     | string  | ID del país                                         |
| `menu_deep_level_nested`                                                         | number  | Nivel de anidación del menú                         |
| `decimal_quantity`                                                               | number  | Cantidad de decimales                               |
| `decimal_quantity_presentation`                                                  | number  | Cantidad de decimales para presentación             |
| `limit_time_remove_plu_from_order`                                               | number  | Tiempo límite para remover PLU de orden (minutos)   |
| `limit_time_redirect_payments`                                                   | number  | Tiempo límite para redirección de pagos (segundos)  |
| `limit_characters_comments`                                                      | number  | Límite de caracteres para comentarios               |
| `limit_max_size_batch_syncronize_orders`                                         | number  | Tamaño máximo del lote de sincronización de órdenes |
| `retries_period`                                                                 | number  | Período de reintentos                               |
| `theme_by_franchise`                                                             | object  | Configuración de tema de la franquicia              |
| `theme_by_franchise.theme_id`                                                    | string  | ID del tema                                         |
| `theme_by_franchise.is_active`                                                   | boolean | Indica si el tema está activo                       |
| `status_franchise`                                                               | string  | ID del estado de la franquicia                      |
| `restaurants`                                                                    | array   | Array de restaurantes de la franquicia              |
| `restaurants[]._id`                                                              | string  | ID del restaurante                                  |
| `restaurants[].restaurant_name`                                                  | string  | Nombre del restaurante                              |
| `restaurants[].company_id`                                                       | string  | ID de la compañía                                   |
| `restaurants[].description`                                                      | string  | Descripción del restaurante                         |
| `restaurants[].address`                                                          | string  | Dirección del restaurante                           |
| `restaurants[].cdn_restaurant_id`                                                | string  | ID del restaurante en CDN                           |
| `restaurants[].restaurant_code`                                                  | string  | Código del restaurante                              |
| `restaurants[].restaurant_image`                                                 | string  | URL de imagen del restaurante                       |
| `restaurants[].city_id`                                                          | string  | ID de la ciudad                                     |
| `restaurants[].category_plu_default`                                             | string  | Categoría PLU por defecto                           |
| `restaurants[].active_sincronization_chouch_db`                                  | boolean | Sincronización CouchDB activa                       |
| `restaurants[].type_period_default`                                              | string  | Tipo de período por defecto                         |
| `restaurants[].active_cash_reconciliation`                                       | boolean | Conciliación de caja activa                         |
| `restaurants[].couch_db`                                                         | object  | Configuración de CouchDB                            |
| `restaurants[].couch_db.username`                                                | string  | Usuario de CouchDB                                  |
| `restaurants[].couch_db.password`                                                | string  | Contraseña de CouchDB                               |
| `restaurants[].couch_db.endpoint`                                                | string  | Endpoint de CouchDB                                 |
| `restaurants[].couch_db.alias`                                                   | string  | Alias único del restaurante                         |
| `restaurants[].limit_retry_get_all_menus_products_max`                           | number  | Reintentos máximos para obtener menús               |
| `restaurants[].retry_time_get_all_menus_products`                                | number  | Tiempo entre reintentos (segundos)                  |
| `restaurants[].status_restaurant`                                                | string  | ID del estado del restaurante                       |
| `restaurants[].schedules`                                                        | object  | Configuración de horarios                           |
| `restaurants[].schedules.is_active`                                              | boolean | Horarios activos                                    |
| `restaurants[].schedules.is_every_days`                                          | boolean | Horario todos los días                              |
| `restaurants[].schedules.every_days`                                             | array   | Horarios para todos los días                        |
| `restaurants[].schedules.monday`                                                 | array   | Horarios de lunes                                   |
| `restaurants[].schedules.tuesday`                                                | array   | Horarios de martes                                  |
| `restaurants[].schedules.wednesday`                                              | array   | Horarios de miércoles                               |
| `restaurants[].schedules.thursday`                                               | array   | Horarios de jueves                                  |
| `restaurants[].schedules.friday`                                                 | array   | Horarios de viernes                                 |
| `restaurants[].schedules.saturday`                                               | array   | Horarios de sábado                                  |
| `restaurants[].schedules.sunday`                                                 | array   | Horarios de domingo                                 |
| `restaurants[].cash_registers_subscriptions`                                     | array   | Array de cajas registradoras                        |
| `restaurants[].cash_registers_subscriptions[]._id`                               | string  | ID de la caja registradora                          |
| `restaurants[].cash_registers_subscriptions[].cash_registers_subscriptions_name` | string  | Nombre de la caja                                   |
| `restaurants[].cash_registers_subscriptions[].description`                       | string  | Descripción de la caja                              |
| `restaurants[].cash_registers_subscriptions[].payment_type_default`              | string  | Tipo de pago por defecto                            |
| `restaurants[].cash_registers_subscriptions[].method_payment_default`            | string  | Método de pago por defecto                          |
| `restaurants[].cash_registers_subscriptions[].default_value_fund`                | number  | Valor de fondo por defecto                          |
| `restaurants[].cash_registers_subscriptions[].type_fund_id`                      | string  | ID del tipo de fondo                                |
| `restaurants[].cash_registers_subscriptions[].status_cash_register`              | string  | Estado de la caja registradora                      |
| `restaurants[].cash_registers_subscriptions[].created_user`                      | string  | Usuario creador                                     |
| `restaurants[].cash_registers_subscriptions[].created_at`                        | string  | Fecha de creación (ISO 8601)                        |
| `restaurants[].cash_registers_subscriptions[].updated_user`                      | string  | Usuario actualizador                                |
| `restaurants[].cash_registers_subscriptions[].updated_at`                        | string  | Fecha de actualización (ISO 8601)                   |
| `restaurants[].created_at`                                                       | string  | Fecha de creación del restaurante (ISO 8601)        |
| `restaurants[].updated_at`                                                       | string  | Fecha de actualización del restaurante (ISO 8601)   |
| `tax_default`                                                                    | string  | ID del impuesto por defecto                         |
| `administrators`                                                                 | array   | Array de administradores                            |
| `administrators[].user_id`                                                       | string  | ID del usuario administrador                        |
| `information_block_images`                                                       | array   | Array de imágenes de bloqueo                        |
| `information_block_images[].imagen_id`                                           | string  | ID de la imagen                                     |
| `created_user`                                                                   | string  | Usuario creador                                     |
| `updated_user`                                                                   | string  | Usuario actualizador                                |
| `created_at`                                                                     | string  | Fecha de creación (ISO 8601)                        |
| `updated_at`                                                                     | string  | Fecha de actualización (ISO 8601)                   |
| `limit_max_downloaded_restaurants`                                               | number  | Límite máximo de restaurantes descargados           |

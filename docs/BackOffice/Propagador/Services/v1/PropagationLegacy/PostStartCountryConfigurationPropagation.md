## Iniciar Propagación de Configuración de País

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
  "_id": "UUID('eab98ae7-0550-0fec-ef40-4eac9a7cbf28')",
  "currencies": [
    {
      "currency_id": "UUID('b1c23d45-6789-0123-4567-abcdef987654')"
    }
  ],
  "max_amount_end_customer": 50,
  "session_expiration_time": 10,
  "api_base_url_customer": "https://apim-dev-ec.azure-api.net/external-apis/customer",
  "client_id_api_customer": "f2ffebd1-77eb-49d2-a623-99824b1f485d",
  "client_secret_api_customer": "c0f2afed-edc3-4cec-8af0-ef58fcb50062",
  "denominations": [
    {
      "denomination_id": "UUID('vok1vuvi8O004uKfP+Ccxw==')"
    }
  ],
  "documents_identity": [
    {
      "document_id": "UUID('Cz6k44QtBOnQg+KHP8q6Eg==')"
    }
  ],
  "notification_push": {
    "limit_time_minutes": 1,
    "retries": 3,
    "limit_time_minutes_block": 5
  },
  "notification_otp": {
    "limit_time_minutes": 2,
    "retries": 3,
    "limit_time_minutes_block": 5
  },
  "transaction_lock_time": 1,
  "allows_client_change": true,
  "deleted_limit": 3,
  "legal_notes": "<p>REGLAMENTOS DE COMPROBANTES DE VENTA, RETENCIÓN Y COMPLEMENTARIOS</p>",
  "images_login": [
    {
      "imagen_id": "UUID('vok1vuvi8O004uKfP+Ccxw==')"
    }
  ],
  "limit_failed_attempts": 5,
  "max_limit_fund": 10,
  "limit_time_block_user": 5,
  "created_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
  "updated_user": "UUID('1829da9e-fbbe-4a3b-d24a-3360b5bf6c08')",
  "created_at": "2024-02-06T03:18:52.852Z",
  "updated_at": "2024-05-31T06:42:27.014Z"
}
```

### Descripción de Campos del Cuerpo

| Campo                                        | Tipo    | Description                                                   |
| -------------------------------------------- | ------- | ------------------------------------------------------------- |
| `_id`                                        | string  | Identificador único de la configuración de país               |
| `currencies`                                 | array   | Lista de configuraciones de monedas aceptadas                 |
| `currencies[].currency_id`                   | string  | Identificador único de la moneda                              |
| `max_amount_end_customer`                    | number  | Monto máximo permitido para el cliente final                  |
| `session_expiration_time`                    | number  | Tiempo en minutos antes de que expire una sesión              |
| `api_base_url_customer`                      | string  | URL base de la API de clientes                                |
| `client_id_api_customer`                     | string  | Identificador del cliente para autenticación                  |
| `client_secret_api_customer`                 | string  | Secreto del cliente para autenticación                        |
| `denominations`                              | array   | Lista de denominaciones aceptadas                             |
| `denominations[].denomination_id`            | string  | Identificador único de la denominación                        |
| `documents_identity`                         | array   | Lista de tipos de documentos de identidad aceptados           |
| `documents_identity[].document_id`           | string  | Identificador único del tipo de documento                     |
| `notification_push`                          | object  | Configuración para notificaciones push                        |
| `notification_push.limit_time_minutes`       | number  | Tiempo límite en minutos antes de reintentar                  |
| `notification_push.retries`                  | number  | Número máximo de reintentos permitidos                        |
| `notification_push.limit_time_minutes_block` | number  | Tiempo en minutos antes de bloquear intentos adicionales      |
| `notification_otp`                           | object  | Configuración para notificaciones OTP                         |
| `notification_otp.limit_time_minutes`        | number  | Tiempo límite en minutos antes de reintentar OTP              |
| `notification_otp.retries`                   | number  | Número máximo de reintentos permitidos para OTP               |
| `notification_otp.limit_time_minutes_block`  | number  | Tiempo en minutos antes de bloquear intentos adicionales      |
| `transaction_lock_time`                      | number  | Tiempo en minutos para bloquear la transacción                |
| `allows_client_change`                       | boolean | Indica si se permite el cambio de cliente                     |
| `deleted_limit`                              | number  | Límite de eliminaciones permitidas                            |
| `legal_notes`                                | string  | Notas legales en formato HTML                                 |
| `images_login`                               | array   | Lista de imágenes para la pantalla de inicio de sesión        |
| `images_login[].imagen_id`                   | string  | Identificador único de la imagen                              |
| `limit_failed_attempts`                      | number  | Número máximo de intentos fallidos                            |
| `max_limit_fund`                             | number  | Límite máximo de fondos permitidos                            |
| `limit_time_block_user`                      | number  | Tiempo en minutos antes de desbloquear usuario                |
| `created_user`                               | string  | Identificador del usuario que creó la configuración           |
| `updated_user`                               | string  | Identificador del usuario que realizó la última actualización |
| `created_at`                                 | string  | Fecha de creación (formato ISO 8601)                          |
| `updated_at`                                 | string  | Fecha de última actualización (formato ISO 8601)              |

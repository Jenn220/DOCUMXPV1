## Obtener Órdenes Sincronizadas

### Método HTTP

`GET`

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
import { Versioning } from './version';

export const environment = {
  production: true,
  baseUrl: "https://apim-dev-ec.azure-api.net",
  signalrUrl: "https://func-mxpv2-dev-ec-notification-push.azurewebsites.net",
  heraUrl: "https://3654fe7d-ca3a-4bc9-a09f-3e7a97148461.mock.pstmn.io/hera",
  hera_service: 'hera',
  menus_service: 'menus',
  external_clients_service: 'external_clients',
  internal_clients_service: 'internalClients',
  payments_service: 'payments',
  orders_service: 'orders',
  purchaseOrders: 'purchaseorders',
  billing_service: 'billing',
  configurations_service: 'configuration',
  recaptcha: {
    siteKey: '6LcfCIoqAAAAAFYcTdNFlmo8XX2mosVb5iqCqjTQ',
    siteKeyV2: '6Lcph5EqAAAAAIwcjD3hJVUUVaLLIGGdSha2Pg0-',
  },
  authenticationHeraUrl: "https://3654fe7d-ca3a-4bc9-a09f-3e7a97148461.mock.pstmn.io",
  hera_authentication_service: 'Authentication',
  hera_users_service: 'Users',
  support_service: 'https://func-mxpv2-dev-ec-notification-push.azurewebsites.net/supportService',
  inactivityTimeout: 10,
  authenticationAresUrl: 'https://130.213.225.52:8080/api/auth',
  collections: {
    version: Versioning.version,
    environment: 'dev'
  },
  max_wait_time_ms: 3000,
  dynatrace: {
    enabled: false,
    scriptUrl: ''
  },
  cuponUrl:'https://web-mxpv2-dev-integrations-cupons.azurewebsites.net'
};

```

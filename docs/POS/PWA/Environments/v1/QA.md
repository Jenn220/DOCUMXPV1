## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Configuración General

```typescript
export const environment = {
  production: true,
  baseUrl: "https://apim-uat-swo2-ec.azure-api.net",
  signalrUrl:
    "https://func-mxpv2-uat-swo2-ec-notification-push.azurewebsites.net",
  heraUrl: "https://3654fe7d-ca3a-4bc9-a09f-3e7a97148461.mock.pstmn.io",
  hera_service: "hera",
  menus_service: "menus",
  external_clients_service: "external_clients",
  internal_clients_service: "internalClients",
  payments_service: "payments",
  orders_service: "orders",
  purchaseOrders: "purchaseorders",
  billing_service: "billing",
  configurations_service: "configuration",
  authenticationHeraUrl:
    "https://3654fe7d-ca3a-4bc9-a09f-3e7a97148461.mock.pstmn.io",
  hera_authentication_service: "Authentication",
  hera_users_service: "Users",
  support_service:
    "https://func-mxpv2-dev-ec-notification-push.azurewebsites.net/supportService",
  inactivityTimeout: 10,
  authenticationAresUrl: "https://130.213.225.52:8080/api/auth",
  max_wait_time_ms: 3000,
  cuponUrl: "https://web-mxpv2-dev-integrations-cupons.azurewebsites.net",
};
```

### Configuración de reCAPTCHA

```typescript
recaptcha: {
  siteKey: '6LcfCIoqAAAAAFYcTdNFlmo8XX2mosVb5iqCqjTQ',
  siteKeyV2: '6Lcph5EqAAAAAIwcjD3hJVUUVaLLIGGdSha2Pg0-'
}
```

### Configuración de Colecciones

```typescript
collections: {
  version: Versioning.version,
  environment: 'qa'
}
```

### Configuración de Dynatrace

```typescript
dynatrace: {
  enabled: true,
  scriptUrl: 'https://js-cdn.dynatrace.com/jstag/185a0521924/bf92517jbz/da298b19f860dee2_complete.js'
}
```

---

## Checklist de Configuración

- [ ] Validar URL base de API
- [ ] Configurar URL de SignalR
- [ ] Validar URLs de servicios Hera
- [ ] Verificar servicios configurados
- [ ] Configurar claves de reCAPTCHA
- [ ] Validar URL de autenticación ARES
- [ ] Configurar timeout de inactividad
- [ ] Validar tiempo máximo de espera
- [ ] Verificar versión de colecciones
- [ ] Confirmar configuración de Dynatrace
- [ ] Validar URL de cupones

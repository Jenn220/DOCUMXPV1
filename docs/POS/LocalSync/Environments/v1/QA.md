## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Configuración General

```typescript
export const environment = {
  production: true,
  baseUrl: "https://apim-uat-swo2-ec.azure-api.net",
  internal_clients_service: "internalClients",
  fund_service: "fund",
  purchase_orders: "purchaseorders",
  syncInterval: "5",
  support_base_url: "http://130.213.195.90:8080/",
};
```

### Configuración de CouchDB

```typescript
couchDB: {
  url: "https://20.161.25.26:6984/",
  username: "admin",
  password: "PasswordKFC2025",
  version: "v002",
  environment: "qa"
}
```

---

## Checklist de Configuración

- [ ] Validar URL base de API
- [ ] Verificar servicios configurados
- [ ] Configurar intervalo de sincronización
- [ ] Validar URL base de soporte
- [ ] Configurar credenciales de CouchDB
- [ ] Verificar versión de CouchDB
- [ ] Confirmar entorno de CouchDB

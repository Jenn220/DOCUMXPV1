## Configuración del Entorno de Desarrollo

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Configuración General

```typescript
export const environment = {
  production: false,
  baseUrl: "https://apim-dev-ec.azure-api.net",
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
  url: "https://135.119.181.27:6984/",
  username: "admin",
  password: "PasswordKFC2025",
  version: "v001",
  environment: "dev"
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

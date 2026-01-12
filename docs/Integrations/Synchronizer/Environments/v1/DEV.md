## Configuración del Entorno de Desarrollo

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Logging

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_integration:rIJEUAk8WyynPhC4@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_MXPi_Configurator",
    "Collections": {
      "LogApplication": "Integration_LogApplication",
      "Catalog": "Integration_Catalog"
    }
  }
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB
- [ ] Verificar colecciones en MongoDB

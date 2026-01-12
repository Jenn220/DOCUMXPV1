## Configuración del Entorno de QA

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

### Base de Datos Legacy

```json
{
  "LegacyDB": {
    "ConnectionString": "Server=localhost;Database=dbprueba;User Id=opheliaapp;Password=ADMIN;"
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
      "Synchronization": "Integration_Synchronization",
      "SynchronizationStates": "Integration_SynchronizationStates",
      "Connection": "Integration_Connection",
      "Integration": "Integration_Integration",
      "Process": "Integration_Process",
      "Status": "Integration_Status",
      "Entity": "Integration_Entity",
      "Property": "Integration_Property",
      "Server": "Integration_Server",
      "Repository": "Integration_Repository",
      "Adapter": "Integration_Adapter",
      "Catalog": "Integration_Catalog",
      "CodeConfigurator": "Integration_CodeConfigurator",
      "Transformation": "Integration_Transformation",
      "For_Restaurants": "Integration_For_Restaurants"
    }
  }
}
```

### CORS

```json
{
  "Cors": {
    "AllowedOrigins": ["http://localhost:4202"]
  }
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de LegacyDB
- [ ] Configurar credenciales de MongoDB
- [ ] Validar orígenes permitidos en CORS
- [ ] Verificar colecciones en MongoDB

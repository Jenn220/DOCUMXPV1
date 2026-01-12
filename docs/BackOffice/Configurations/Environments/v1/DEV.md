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

### EventBus

```json
{
  "EventBus": {
    "ConnectionString": "Endpoint=sb://YOUR_SERVICEBUS.servicebus.windows.net/;SharedAccessKeyName=YOUR_POLICY;SharedAccessKey=YOUR_KEY_HERE
    "Topic": {
      "Name": "topic_kfc_propagation_dev",
      "Subscriptions": {
        "SubsBoStartUpdateTemporaryEntities": {
          "Name": "subs_bo_start_update_temporary_configurations",
          "Filter": "filter_start_update_temporary_configurations"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional_configurations",
          "Filter": "filter_start_update_transactional_configurations"
        },
        "SubsBoEndUpdateTransactionalEntities": {
          "Name": "subs_bo_end_update_transactional_entities",
          "Filter": "filter_end_update_transactional_entities"
        }
      }
    }
  }
}
```

### EventStore

```json
{
  "EventStore": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net",
    "DatabaseName": "DEV_KFC_BO_Configurations",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_Configurations_BO_Country_Configurations": "Configurations_BO_Country_Configurations_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net",
    "DatabaseName": "DEV_KFC_BO_Configurations",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "Departament_internal": "Configurations_BO_Departament_Internal",
      "Classification": "Configurations_BO_Classification",
      "Currency": "Configurations_BO_Currency",
      "Country": "Configurations_BO_Country",
      "Taxes": "Configurations_BO_Taxes",
      "Color": "Configurations_BO_Color",
      "IconCategory": "Configurations_BO_Icon_Category",
      "EnviromentVariables": "Configurations_BO_Enviroment_Variables",
      "Province": "Configurations_BO_Province",
      "City": "Configurations_BO_City",
      "CountryConfigurations": "Configurations_BO_Country_Configurations",
      "CurrencyDenomination": "Configurations_BO_Currency_Denomination",
      "DocumentIdentity": "Configurations_BO_Document_Identity",
      "DeviceImages": "Configurations_BO_Country_Device_Images_Login",
      "Country_Propag_Temp": "Configurations_BO_Temp_Country_Configurations",
      "Propagator_Country_Configurations_Data": "Propagations_BO_Country_Configurations_Data"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-bo.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False",
    "AddMinutesForExpirationTime": "1.0"
  }
}
```

### Hosts Permitidos

```json
{
  "AllowedHosts": "*"
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de EventBus
- [ ] Configurar ConnectionString de EventStore
- [ ] Configurar credenciales de MongoDB
- [ ] Configurar password de Redis
- [ ] Validar suscripciones de EventBus
- [ ] Verificar colecciones en MongoDB

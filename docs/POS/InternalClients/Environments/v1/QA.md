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

### AppHash

```json
{
  "apphash": "valorapphash"
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
          "Name": "subs_bo_start_update_temporary_internalclients",
          "Filter": "filter_start_update_temporary_internalclients"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional_internalclients",
          "Filter": "filter_start_update_transactional_internalclients"
        },
        "SubsBoEndUpdateTransactionalEntities": {
          "Name": "subs_bo_end_update_transactional_entities",
          "Filter": "filter_end_update_transactional_entities"
        },
        "SubsPosStartPropagation": {
          "Name": "subs_pos_start_propagation_internalclients",
          "Filter": "filter_pos_start_propagation_internalclients"
        },
        "SubsPosEndPropagation": {
          "Name": "subs_pos_end_propagation",
          "Filter": "filter_pos_end_propagation"
        },
        "SubsStegingStartPropagation": {
          "Name": "subs_pos_start_steging_propagation_internalclients",
          "Filter": "filter_pos_start_steging_propagation_internalclients"
        },
        "SubsStegingEndPropagation": {
          "Name": "subs_pos_end_steging_propagation",
          "Filter": "filter_pos_end_steging_propagation"
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
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_InternalClients",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_InternalClients_POS_FranchiseConfigurations": "InternalClients_POS_Franchise_Configuration_EventStore",
      "EventStore_InternalClients_POS_CountryConfigurations": "InternalClients_POS_Country_Configuration_EventStore",
      "EventStore_InternalClients_POS_Restaurant_Enabling_Taxes": "InternalClients_POS_Restaurant_Enabling_Taxes_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_InternalClients",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "Franchise_Configurations": "InternalClients_POS_Franchise_Configurations",
      "Restaurant_Period": "InternalClients_POS_RestaurantPeriod",
      "Country_Configurations": "InternalClients_POS_Country_Configurations",
      "Franchise": "InternalClients_POS_Franchise",
      "Drivethru": "InternalClients_POS_Drivethru",
      "Document_Type": "InternalClients_POS_DocumentType",
      "Channel": "InternalClients_POS_Channels",
      "HalfIntegration": "InternalClients_POS_Half_Integration",
      "StatusCashRegisterSubscription": "InternalClients_POS_Status_Cash_Register_Subscription",
      "TypeFund": "InternalClients_POS_Type_Fund",
      "StatusFund": "InternalClients_POS_Status_Fund",
      "Fund": "InternalClients_POS_Fund",
      "RestaurantEnablingTaxes": "InternalClients_POS_Restaurant_Enabling_Taxes",
      "StatusPeriod": "InternalClients_POS_Status_Period",
      "Propagator_FranchiseConfigurationsNestedData": "Propagations_BO_Franchise_Configurations_Nested",
      "Propagator_CountryConfigrationsNestedData": "Propagations_BO_Country_Configurations_Nested",
      "Propagator_RestaurantEnablingTaxesNestedData": "Propagations_BO_Restaurant_Enabling_Taxes_Nested"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-ec.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False",
    "AddMinutesForExpirationTime": "5"
  }
}
```

### Transferencia de Staging

```json
{
  "StaggingTransfer": {
    "MaxDegreeOfParallelism": 10
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

- [ ] Configurar AppHash
- [ ] Configurar credenciales de EventBus
- [ ] Configurar ConnectionString de EventStore
- [ ] Configurar credenciales de MongoDB
- [ ] Configurar password de Redis
- [ ] Validar suscripciones de EventBus
- [ ] Verificar entidades en EventStore
- [ ] Verificar colecciones en MongoDB
- [ ] Configurar grado máximo de paralelismo

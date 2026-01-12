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
        "SubsPosStartPropagation": {
          "Name": "subs_pos_start_propagation_menus",
          "Filter": "filter_pos_start_propagation_menus"
        },
        "SubsPosEndPropagation": {
          "Name": "subs_pos_end_propagation",
          "Filter": "filter_pos_end_propagation"
        },
        "SubsStegingStartPropagation": {
          "Name": "subs_pos_start_steging_propagation_menus",
          "Filter": "filter_pos_start_steging_propagation_menus"
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
    "DatabaseName": "DEV_PROPAG_POS_Menus",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_PosPlu": "Menus_POS_Plu_EventStore",
      "EventStore_PosMenu": "Menus_POS_Menu_EventStore",
      "EventStore_PosSuggestedQuestion": "Menus_POS_Suggested_Question_EventStore",
      "EventStore_PosSchedulesRestaurantsRestriction": "Menus_POS_Schedules_Restaurants_Restriction_EventStore",
      "EventStore_PosCampaign": "Menus_POS_Campaign_EventStore",
      "EventStore_PosRestaurantEnablingTaxes": "Menus_POS_Restaurant_Enabling_Taxes_EventStore",
      "EventStore_PosEnabledSubsidyPlus": "Menus_POS_Enabled_Subsidy_Plus_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_Menus",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "PLU": "Menus_POS_PLU",
      "Schedules_Restaurants_Restrictions": "Menus_POS_Schedules_Restaurants_Restriction",
      "Menu": "Menus_POS_Menu",
      "Suggested_Questions": "Menus_POS_Suggested_Question",
      "RestaurantEnablingTaxes": "Menus_POS_Restaurant_Enabling_Taxes",
      "Propagator_PluData": "Propagations_BO_PluNested",
      "Propagator_MenuData": "Propagations_BO_MenuNested",
      "Propagator_RestrictionData": "Propagations_BO_Schedules_Restaurants_RestrictionNested",
      "Propagator_SugQuestionData": "Propagations_BO_SuggestedQuestionNested",
      "Propagator_UpsellingData": "Propagations_BO_UpsellingNested",
      "Propagator_CampaignData": "Propagations_BO_Campaign_Nested",
      "Propagator_EnabledSubsidyPlusData": "Propagations_BO_Enabled_Subsidy_Plus_Nested",
      "Menus_POS_Enabled_Subsidy_Plus": "Menus_POS_Enabled_Subsidy_Plus",
      "Menus_POS_Campaign": "Menus_POS_Campaign",
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

### Configuraciones de Preguntas Sugeridas

```json
{
  "SuggestedQuestionConfigurations": {
    "maximumLevelNestedNested": 5
  }
}
```

### Transferencia de Staging

```json
{
  "StegingTransfer": {
    "MaxDegreeOfParallelism": 10
  }
}
```

### URLs de APIs

```json
{
  "ApiUrls": {
    "IntegradorMicroservice": "http://132.196.144.251:8080/",
    "Enpoints": {
      "PublishOperationResult": "api/support/receiver"
    }
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
- [ ] Verificar entidades en EventStore
- [ ] Verificar colecciones en MongoDB
- [ ] Validar URLs de APIs
- [ ] Configurar grado máximo de paralelismo

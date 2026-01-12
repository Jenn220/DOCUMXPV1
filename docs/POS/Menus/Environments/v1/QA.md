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

### EventBus

```json
{
  "EventBus": {
    "ConnectionString": "Endpoint=sb://YOUR_SERVICEBUS.servicebus.windows.net/;SharedAccessKeyName=YOUR_POLICY;SharedAccessKey=YOUR_KEY_HERE
    "Topic": {
      "Name": "topic_kfc_propagation_dev",
      "Subscriptions": {
        "SubsPosStartPropagation": {
          "Name": "subs_pos_start_propagation",
          "Filter": "filter_pos_start_propagation"
        },
        "SubsPosEndPropagation": {
          "Name": "subs_pos_end_propagation",
          "Filter": "filter_pos_end_propagation"
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
      "EventStore_PosSchedulesRestaurantsRestriction": "Menus_POS_Schedules_Restaurants_Restriction_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_PROPAG_POS_Menus",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "PLU": "Menus_POS_PLU",
      "Schedules_Restaurants_Restrictions": "Menus_POS_Schedules_Restaurants_Restriction",
      "Menu": "Menus_POS_Menu",
      "Suggested_Questions": "Menus_POS_Suggested_Question",
      "Propagator_PluData": "Propagations_BO_PluNested",
      "Propagator_MenuData": "Propagations_BO_MenuNested",
      "Propagator_RestrictionData": "Propagations_BO_Schedules_Restaurants_RestrictionNested",
      "Propagator_SugQuestionData": "Propagations_BO_SuggestedQuestionNested",
      "Propagator_UpsellingData": "Propagations_BO_UpsellingNested"
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

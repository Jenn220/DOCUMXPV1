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
          "Name": "subs_pos_start_propagation_subsidy",
          "Filter": "filter_pos_start_propagation_subsidy"
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
    "DatabaseName": "DEV_KFC_POS_Subsidy",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_PosCampaign": "Subsidy_POS_Campaign_EventStore",
      "EventStore_PosEnabledSubsidyPlus": "Subsidy_POS_Enabled_Subsidy_Plus_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_Subsidy",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "Propagator_CampaignData": "Propagations_BO_Campaign_Nested",
      "Propagator_EnabledSubsidyPlusData": "Propagations_BO_Enabled_Subsidy_Plus_Nested",
      "Subsidy_POS_Campaign": "Subsidy_POS_Campaign",
      "Subsidy_POS_Enabled_Subsidy_Plus": "Subsidy_POS_Enabled_Subsidy_Plus",
      "Subsidy_POS_Transactions": "Subsidy_POS_Transactions",
      "Subsidy_Pos_Transactions_Temp": "Subsidy_POS_Transactions_Temp"
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
- [ ] Validar suscripciones de EventBus
- [ ] Verificar entidades en EventStore
- [ ] Verificar colecciones en MongoDB

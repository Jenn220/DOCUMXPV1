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
          "Name": "subs_bo_start_update_temporary_payments",
          "Filter": "filter_start_update_temporary_payments"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional_payments",
          "Filter": "filter_start_update_transactional_payments"
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
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_BO_Payments",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_Payments_BO_PaymentsTypes": "Payments_BO_Payments_Types_EventStore",
      "EventStore_Payments_BO_PaymentsRestrictions": "Payments_BO_Payments_Restrictions_EventStore",
      "EventStore_Payments_BO_FranchiseEnablingPaymentsMethod": "Payments_BO_Franchise_Enabling_Payments_Method_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_BO_Payments",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "Payments_Method": "Payments_BO_Payments_Method",
      "Payments_Types_Status": "Payments_BO_Payments_Types_Status",
      "Payments_Payments_Types": "Payments_BO_Payments_Types",
      "Propagator_Temp_Payments_Types": "Payments_BO_Temp_Payments_Types",
      "Propagator_Payments_Types_Data": "Propagations_BO_Payments_Types_Data",
      "Propagator_Temp_Payments_Restrictions": "Payments_BO_Temp_Payments_Restrictions",
      "Propagator_Temp_Franchise_Enabling_Payments_Method": "Payments_BO_Temp_Franchise_Enabling_Payments_Method",
      "Propagator_Payments_Restrictions_Data": "Propagations_BO_Payments_Restrictions_Data",
      "Propagador_Franchise_Enabling_Payments_Method_Data": "Propagations_BO_Franchise_Enabling_Payments_Method_Data",
      "Payments_Payments_Restrictions": "Payments_BO_Payments_Restrictions",
      "Payments_Franchise_Enabling_Payments_Method": "Payments_BO_Franchise_Enabling_Payments_Methods"
    }
  }
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de EventBus
- [ ] Configurar ConnectionString de EventStore
- [ ] Configurar credenciales de MongoDB
- [ ] Validar suscripciones de EventBus
- [ ] Verificar colecciones en MongoDB

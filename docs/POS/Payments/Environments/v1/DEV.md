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
          "Name": "subs_bo_start_update_temporary_entities",
          "Filter": "filter_start_update_temporary_entities"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional_entities",
          "Filter": "filter_start_update_transactional_entities"
        },
        "SubsBoEndUpdateTransactionalEntities": {
          "Name": "subs_bo_end_update_transactional_entities",
          "Filter": "filter_end_update_transactional_entities"
        },
        "SubsPosStartPropagation": {
          "Name": "subs_pos_start_propagation_payments",
          "Filter": "filter_pos_start_propagationn_payments"
        },
        "SubsPosEndPropagation": {
          "Name": "subs_pos_end_propagation",
          "Filter": "filter_pos_end_propagation"
        },
        "SubsStegingStartPropagation": {
          "Name": "subs_pos_start_steging_propagation_payments",
          "Filter": "filter_pos_start_steging_propagation_payments"
        },
        "SubsStegingEndPropagation": {
          "Name": "subs_steging_end_propagation",
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
    "DatabaseName": "DEV_KFC_POS_Payments",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_Payments_POS_PaymentsTypes": "Payments_POS_Payments_Types_EventStore",
      "EventStore_Payments_POS_PaymentsRestrictions": "Payments_POS_Payments_Restrictions_EventStore",
      "EventStore_Payments_POS_FranchiseEnablingPaymentsMethod": "Payments_POS_Franchise_Enabling_Payments_Method_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_Payments",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "Collections": {
      "Payments_Method": "Payments_POS_Payments_Method",
      "Payments_Types": "Payments_POS_Payments_Types",
      "Franchise_Payments_Restrictions": "Payments_POS_Franchise_Payments_Restrictions",
      "Payments_Status": "Payments_POS_Payments_Status",
      "Conciliation_Types": "Payments_POS_Conciliation_Types",
      "Payments_Types_Status": "Payments_POS_Payments_Status",
      "Franchise_Enabling_Payments_Method": "Payments_POS_Franchise_Enabling_Payments_Method",
      "Propagator_PaymentsTypesNestedData": "Propagations_BO_Payments_Types_Nested",
      "Payments_Card_Homologations": "Payments_POS_Card_Homologations",
      "Propagator_PaymentsRestrictionsNestedData": "Propagations_BO_Payments_Restrictions_Nested",
      "Propagator_FranchiseEnablingPaymentsMethodNestedData": "Propagations_BO_Franchise_Enabling_Payments_Method_Nested",
      "Franchise_Enabling_Payments_Methods": "Payments_POS_Franchise_Enabling_Payments_Methods"
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
  "StegingTransfer": {
    "MaxDegreeOfParallelism": 10
  }
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
- [ ] Configurar grado máximo de paralelismo

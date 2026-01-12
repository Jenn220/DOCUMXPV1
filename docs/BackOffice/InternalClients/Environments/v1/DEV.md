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
    "DatabaseName": "DEV_KFC_BO_InternalClients",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_InternalClients_BO_Franchise_Configuration": "InternalClients_BO_Franchise_Configuration_EventStore",
      "EventStore_InternalClients_BO_Restaurant_Enabling_Taxes": "InternalClients_BO_Restaurant_Enabling_Taxes_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_BO_InternalClients",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "DatabaseConfigurations": "DEV_KFC_BO_Configurations",
    "DatabaseMenus": "DEV_KFC_BO_Menus",
    "Collections": {
      "Franchise": "InternalClients_BO_Franchise",
      "Restaurant": "InternalClients_BO_Restaurant",
      "Users": "InternalClients_BO_Users",
      "Province": "InternalClients_BO_Province",
      "City": "InternalClients_BO_City",
      "Restrictions": "InternalClients_BO_Schedules_Restaurants_Restrictions",
      "StatusSubscription": "InternalClients_BO_Status_Restaurant_Cash_Registers_Subscriptions",
      "StatusFranchise": "InternalClients_BO_Status_Franchise",
      "StatusRestaurant": "InternalClients_BO_Status_Restaurant",
      "StatusUser": "InternalClients_BO_Status_User",
      "Subscriptions": "InternalClients_BO_Restaurant_Cash_Registers_Subscriptions",
      "InternalClients_Franchise_Configuration": "InternalClients_BO_Franchise_Configuration",
      "Propagator_Temp_Franchise_Configuration": "InternalClients_BO_Temp_Franchise_Configuration",
      "Propagator_Franchise_Configuration_Data": "Propagations_BO_Franchise_Configurations_Data",
      "Conf_Taxes": "Configurations_BO_Taxes",
      "Conf_theme": "Configurations_BO_Themes_Pos",
      "Internalclients_Franchise_InformationblockImages": "InternalClients_BO_Franchise_Information_block_Images",
      "Conf_OPLEventsCatalog": "Configurations_BO_OPL_Events_Catalog",
      "InternalClients_RestaurantEnablingTaxes": "InternalClients_BO_Restaurant_Enabling_Taxes",
      "Propagator_Temp_RestaurantEnablingTaxes": "InternalClients_BO_Temp_Restaurant_Enabling_Taxes",
      "Propagator_RestaurantEnablingTaxes_Data": "Propagations_BO_Restaurant_Enabling_Taxes_Data",
      "Menu_Plu": "Menus_BO_PLU"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-bo.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False",
    "AddMinutesForExpirationTime": "5.0"
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

## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

### Logging

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
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
  },
  "EventStore": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/", //"mongodb://localhost:27017/", //"mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_BO_InternalClients",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_InternalClients_BO_Franchise_Configuration": "InternalClients_BO_Franchise_Configuration_EventStore"
    }
  },
  "MongoDB": {
    "ConnectionString": "mongodb+srv://uatuser:FpLaADYetnNtDagc@mxpv2uatcluster.asrvjjn.mongodb.net/",
    "DatabaseName": "InternalClients_integrations",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "DatabaseConfigurations": "DEV_KFC_BO_Configurations",
    "Collections": {
      "Franchise": "Franchise",
      "Restaurant": "InternalClients_Restaurant",
      "Users": "InternalClients_Users",
      "Province": "InternalClients_Province",
      "City": "InternalClients_City",
      "Franchise_Configurations": "InternalClients_Franchise_Configurations",
      "Restrictions": "InternalClients_Schedules_Restaurants_Restrictions",

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
      "Internalclients_Franchise_InformationblockImages": "InternalClients_BO_Franchise_Information_block_Images"
    }
  },
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-eastus2-bo.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False",
    "AddMinutesForExpirationTime": "5.0"
  },
  "AllowedHosts": "*"
}
```

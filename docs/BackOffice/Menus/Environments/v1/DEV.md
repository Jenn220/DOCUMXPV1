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
          "Name": "subs_bo_start_update_temporary_menus",
          "Filter": "filter_start_update_temporary_menus"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional_menus",
          "Filter": "filter_start_update_transactional_menus"
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
    "DatabaseName": "DEV_PROPAG_BO_Menus",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_Propagator_Plu": "Menus_BO_PLU_EventStore",
      "EventStore_Propagator_Campaign": "Menus_BO_Campaign_EventStore",
      "EventStore_Propagator_Menu": "Menus_BO_Menu_EventStore",
      "EventStore_Propagator_SugQuestion": "Menus_BO_Suggested_Question_EventStore",
      "EventStore_Propagator_Restriction": "Menus_BO_Schedules_Restaurants_Restrictions_EventStore",
      "EventStore_Propagator_Upselling": "Menus_BO_Upselling_PLU_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_PROPAG_BO_Menus",
    "DatabasePropagator": "DEV_PROPAG_BO_Propagations",
    "DatabaseInternalClients": "DEV_KFC_BO_InternalClients",
    "Collections": {
      "Type_PLU": "Menus_BO_Type_PLU",
      "Category_PLU": "Menus_BO_Category_PLU",
      "Status_PLU": "Menus_BO_Status_PLU",
      "Upselling_PLU": "Menus_BO_Upselling_PLU",
      "Suggested_Question": "Menus_BO_Suggested_Question",
      "Suggested_Question_Answers": "Menus_BO_Suggested_Question_Answers",
      "Suggested_Question_Status": "Menus_BO_Status_Suggested_Question",
      "Suggested_Question_Types": "Menus_BO_Type_Suggested_Question",
      "PLU": "Menus_BO_PLU",
      "Tag_PLU": "Menus_BO_Tag_PLU",
      "Images_PLU": "Menus_BO_Images_PLU",
      "Devices_Images_PLU": "Menus_BO_Devices_Images_PLU",
      "Half_Integration": "Menus_BO_Half_Integration",
      "Menu_Category_Menu": "Menus_BO_Category_Menu",
      "Menu_Category_Image": "Menus_BO_Category_Image",
      "Schedules_Restaurants_Restrictions": "Menus_BO_Schedules_Restaurants_Restrictions",
      "Status_Menu": "Menus_BO_Status_Menu",
      "Menu": "Menus_BO_Menu",
      "Device_Images_Menu": "Menus_BO_Device_Images_Menu",
      "Images_Menu": "Menus_BO_Images_Menu",
      "Icon_Menu": "Menus_BO_Icon_Menu",
      "ProgrammationPrice": "Menus_BO_Programmation_Price_PLU",
      "ProgrammationPriceStatus": "Menus_BO_Programmation_Price_PLU_Status",
      "MenuStatusCategoryProduct": "Menus_BO_Status_Category_PLU",
      "ClassificationReplica": "Menus_BO_Configuration_Classification",
      "Suggested_Question_Type": "Menus_BO_Type_Suggested_Question",
      "InternalClients_Users": "Menus_BO_InternalClients_Users",
      "PLU_Propag_temp": "Menus_BO_Temp_PLU",
      "Menu_Propag_temp": "Menus_BO_Temp_Menu",
      "SugQuestion_Propag_Temp": "Menus_BO_Temp_Suggested_Question",
      "Restriction_Propag_Temp": "Menus_BO_Temp_Schedules_Restaurants_Restrictions",
      "Upselling_Propag_Temp": "Menus_BO_Temp_Upselling_PLU",
      "Campaign_Propag_temp": "Menus_BO_Temp_Campaign",
      "Propagator_PluData": "Propagations_BO_PluData",
      "Propagator_MenuData": "Propagations_BO_MenuData",
      "Propagator_RestrictionData": "Propagations_BO_Schedules_Restaurants_RestrictionsData",
      "Propagator_SugQuestionData": "Propagations_BO_SuggestedQuestionData",
      "Propagator_UpsellingData": "Propagations_BO_UpsellingData",
      "Propagator_CampaignData": "Propagations_BO_Campaign_Data",
      "InternalClients_Franchise_Configuration": "InternalClients_BO_Franchise_Configuration",
      "Campaign": "Menus_BO_Campaign"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-bo.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False"
  }
}
```

### Azure Storage

```json
{
  "AccessStorage": {
    "ConnectionString": "DefaultEndpointsProtocol=https;AccountName=YOUR_ACCOUNT;AccountKey=YOUR_KEY_HERE;EndpointSuffix=core.windows.net
    "SasToken": "?sv=2022-11-02&ss=bfqt&srt=c&sp=rwdlacupyx&se=2027-10-12T06:11:35Z&st=2024-10-11T22:11:35Z&spr=https,http&sig=GetYXNz2pp8t7nok%2FOBPSg%2F1T4%2BkZrFK%2Fax%2BeZ7TqMY%3D",
    "CdnAzure": "https://repositoryDevBO.azureedge.net",
    "MaxSizeUploadMb": 10,
    "SubDirectoryRootImgesPlu": "/imagesplu/",
    "SubDirectoryRootCategoryMenu": "/categorymenu/",
    "SubDirectoryRootImgesMenu": "/imagesmenu/"
  }
}
```

### URLs de APIs

```json
{
  "ApiUrls": {
    "ConfigurationMicroservice": "https://apim-dev-bo.azure-api.net/configurations/",
    "InternalClientsMicroservice": "https://apim-dev-bo.azure-api.net/internalclients/",
    "Enpoints": {
      "GetTaxesByCountry": "api/v1/tax/getbycountry",
      "GetDeparmentByFranchise": "api/v1/departamentinternal/getbyfranchise",
      "GetClassificationByFranchise": "api/v1/classification/getbyfranchise",
      "GetAllColor": "api/v1/color/getall_colors",
      "GetUserById": "api/v1/users/getuserbyid",
      "GetValuesByDomain": "api/v1/EnviromentVariables/get_values_by_domain",
      "GetRestaurantByFranchise": "api/v1/restaurants/getallbyfranchise",
      "GetConfigurationsByFranchise": "YOUR_REDIS_OR_AZURE_KEY_HERE"
    }
  }
}
```

### Otras Configuraciones

```json
{
  "RetriesOptions": {
    "retriesNumber": 3,
    "retrySecondsAtemp": 1
  },
  "SuggestedQuestionConfigurations": {
    "maximumLevelNestedNested": 5,
    "defaultMaximumDuplicatedQuestions": 3
  },
  "AllowedHosts": "*"
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de EventBus
- [ ] Configurar ConnectionString de EventStore
- [ ] Configurar credenciales de MongoDB
- [ ] Configurar password de Redis
- [ ] Actualizar AccountKey de Azure Storage
- [ ] Verificar expiración del SAS Token
- [ ] Validar suscripciones de EventBus
- [ ] Validar endpoints de microservicios
- [ ] Verificar colecciones en MongoDB

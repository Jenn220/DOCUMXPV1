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
          "Name": "subs_bo_start_update_temporary",
          "Filter": "filter_start_update_temporary"
        },
        "SubsBoEndUpdateTemporaryEntities": {
          "Name": "subs_bo_end_update_temporary_entities",
          "Filter": "filter_end_update_temporary_entities"
        },
        "SubsPosStartPropagation": {
          "Name": "subs_pos_start_propagation",
          "Filter": "filter_pos_start_propagation"
        },
        "SubsPosEndPropagation": {
          "Name": "subs_pos_end_propagation",
          "Filter": "filter_pos_end_propagation"
        },
        "SubsBoStartUpdateTransactionalEntities": {
          "Name": "subs_bo_start_update_transactional",
          "Filter": "filter_start_update_transactional"
        },
        "SubsBoEndUpdateTransactionalEntities": {
          "Name": "subs_bo_end_update_transactional_entities",
          "Filter": "filter_end_update_transactional_entities"
        },
        "SubsPosStartStagingEntities": {
          "Name": "subs_pos_start_steging_propagation",
          "Filter": "filter_pos_start_steging_propagation"
        },
        "SubsPosEndStagingEntities": {
          "Name": "subs_pos_end_steging_propagation",
          "Filter": "filter_pos_end_steging_propagation"
        }
      }
    },
    "PosNotification": {
      "Topic": "pos_topic_function_ec_notification",
      "Subscription": "subs_pos_stagging_notification",
      "Filter": ""
    }
  }
}
```

### EventStore

```json
{
  "EventStore": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_PROPAG_BO_Propagations",
    "RepositoryType": "MongoDB",
    "Entities": {
      "EventStore_Propagator": "Propagations_BO_EventStore"
    }
  }
}
```

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseMain": "DEV_PROPAG_BO_Propagations",
    "DatabaseMenus": "DEV_PROPAG_BO_Menus",
    "DatabasePayments": "DEV_KFC_BO_Payments",
    "DatabaseConfigurations": "DEV_KFC_BO_Configurations",
    "DatabaseInternalClients": "DEV_KFC_BO_InternalClients",
    "Collections": {
      "Main_GeneralSummary": "Propagations_BO_GeneralSummary",
      "Main_PluData": "Propagations_BO_PluData",
      "Main_MenuData": "Propagations_BO_MenuData",
      "Main_SuggestedQuestionData": "Propagations_BO_SuggestedQuestionData",
      "Main_RestrictionData": "Propagations_BO_Schedules_Restaurants_RestrictionsData",
      "Main_UpsellingData": "Propagations_BO_UpsellingData",
      "Main_PluNestedData": "Propagations_BO_PluNested",
      "Main_MenuNestedData": "Propagations_BO_MenuNested",
      "Main_SugQuestionNestedData": "Propagations_BO_SuggestedQuestionNested",
      "Main_RestrictionNestedData": "Propagations_BO_Schedules_Restaurants_RestrictionNested",
      "Main_UpsellingNestedData": "Propagations_BO_UpsellingNested",
      "Conf_Taxes": "Configurations_BO_Taxes",
      "Conf_Color": "Configurations_BO_Color",
      "Conf_Classification": "Configurations_BO_Classification",
      "Conf_Currency": "Configurations_BO_Currency",
      "Conf_CurrencyDenomination": "Configurations_BO_Currency_Denomination",
      "Conf_DocumentIdentity": "Configurations_BO_Document_Identity",
      "Conf_DeviceImages": "Configurations_BO_Country_Device_Images_Login",
      "Conf_Status_DocumentIdentity": "Configurations_BO_Status_Document_Identity",
      "Menus_Category_PLU": "Menus_BO_Category_PLU",
      "Menus_Images_PLU": "Menus_BO_Images_PLU",
      "Menus_Status_PLU": "Menus_BO_Status_PLU",
      "Menus_Tag_PLU": "Menus_BO_Tag_PLU",
      "Menus_Type_PLU": "Menus_BO_Type_PLU",
      "Menus_Devices_Images_PLU": "Menus_BO_Devices_Images_PLU",
      "Menus_Status_Category_PLU": "Menus_BO_Status_Category_PLU",
      "Menus_Status_MENU": "Menus_BO_Status_Menu",
      "Menus_HalfIntegration_MENU": "Menus_BO_Half_Integration",
      "Menus_DeviceImage_MENU": "Menus_BO_Device_Images_Menu",
      "Menus_Icon_MENU": "Menus_BO_Icon_Menu",
      "Menus_Category_MENU": "Menus_BO_Category_Menu",
      "Menus_SuggestedQuestionStatusEntity": "Menus_BO_Status_Suggested_Question",
      "Menus_SuggestedQuestionTypeEntity": "Menus_BO_Type_Suggested_Question",
      "Menus_RestrictionTempEntity": "Menus_BO_Temp_Schedules_Restaurants_Restrictions",
      "Menus_PLU": "Menus_BO_PLU",
      "Main_PaymentsTypesData": "Propagations_BO_Payments_Types_Data",
      "Main_PaymentsTypesNestedData": "Propagations_BO_Payments_Types_Nested",
      "PaymentsTypes_Status_PAYMENTS": "Payments_BO_Payments_Types_Status",
      "Main_FranchiseConfigurationsData": "Propagations_BO_Franchise_Configurations_Data",
      "Main_FranchiseConfigurationsNestedData": "Propagations_BO_Franchise_Configurations_Nested",
      "Internalclients_Franchise_InformationblockImages": "InternalClients_BO_Franchise_Information_block_Images",
      "Internalclients_Status_Restaurant": "InternalClients_BO_Status_Restaurant",
      "Internalclients_Status_Franchise": "InternalClients_BO_Status_Franchise",
      "Configurations_Taxes": "Configurations_BO_Taxes",
      "Internalclients_StatusCashRegister": "InternalClients_BO_Status_Restaurant_Cash_Registers_Subscriptions",
      "Internalclients_CashRegister": "InternalClients_BO_Status_Restaurant_Cash_Registers_Subscriptions",
      "Conf_theme": "Configurations_BO_Themes_Pos",
      "Conf_Icon": "Configurations_BO_Icon",
      "Conf_Theme_ImageLogo": "Configurations_BO_Theme_images_Logo",
      "Conf_Theme_ImageBackground": "Configurations_BO_Theme_images_Logo",
      "Main_CountryConfigurationsData": "Propagations_BO_Country_Configurations_Data",
      "Main_CountryConfigurationsNestedData": "Propagations_BO_Country_Configurations_Nested",
      "Main_PaymentRestrictionsData": "Propagations_BO_Payments_Restrictions_Data",
      "Main_PaymentsRestrictionsNestedData": "Propagations_BO_Payments_Restrictions_Nested",
      "Conf_OPLEventsCatalog": "Configurations_BO_OPL_Events_Catalog",
      "Internalclients_Franchise_Configuration": "InternalClients_BO_Franchise_Configuration",
      "Conf_Departament": "Configurations_BO_Departament_Internal",
      "Main_RestaurantEnablingTaxesData": "Propagations_BO_Restaurant_Enabling_Taxes_Data",
      "Main_RestaurantEnablingTaxesNestedData": "Propagations_BO_Restaurant_Enabling_Taxes_Nested",
      "Main_FranchiseEnablingPaymentsMethodData": "Propagations_BO_Franchise_Enabling_Payments_Method_Data",
      "Main_FranchiseEnablingPaymentsMethodNestedData": "Propagations_BO_Franchise_Enabling_Payments_Method_Nested",
      "Main_CampaignData": "Propagations_BO_Campaign_Data",
      "Main_CampaignNestedData": "Propagations_BO_Campaign_Nested"
    }
  }
}
```

### URLs de APIs

```json
{
  "ApiUrls": {
    "IntegradorMicroservice": "",
    "Enpoints": {
      "PublishOperationResult": ""
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
- [ ] Configurar URLs de APIs
- [ ] Verificar colecciones en MongoDB

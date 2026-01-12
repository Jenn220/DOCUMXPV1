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

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://integrationUser:JfCDwCTeLWNG5I1d@integrationstest.evhlykk.mongodb.net/",
    "DatabaseName": "Menus",
    "Collections": {
      "Type_PLU": "Menu_Type_PLU",
      "Category_PLU": "Menu_Category_PLU",
      "Status_PLU": "Menu_Status_PLU",
      "Upselling_PLU": "Menu_Upselling_PLU",
      "Suggested_Question": "Menu_Suggested_Question",
      "Suggested_Question_Answers": "Menu_Suggested_Question_Answers",
      "Suggested_Question_Status": "Menu_Status_Suggested_Question",
      "Suggested_Question_Types": "Menu_Type_Suggested_Question",
      "PLU": "Menu_PLU",
      "Tag_PLU": "Menu_Tag_PLU",
      "Images_PLU": "Menu_Images_PLU",
      "Devices_Images_PLU": "Menu_Devices_Images_PLU",
      "Half_Integration": "Menu_Half_Integration",
      "Menu_Category_Menu": "Menu_Category_Menu",
      "Menu_Category_Image": "Menu_Category_Image",
      "Schedules_Restaurants_Restrictions": "Menu_Schedules_Restaurants_Restrictions",
      "Status_Menu": "Menu_Status_Menu",
      "Menu": "Menu_Menu",
      "Device_Images_Menu": "Menu_Device_Images_Menu",
      "Images_Menu": "Menu_Images_Menu",
      "Icon_Menu": "Menu_Icon_Menu",
      "ProgrammationPrice": "Menu_Programmation_Price_PLU",
      "ProgrammationPriceStatus": "Menu_Programmation_Price_PLU_Status",
      "MenuStatusCategoryProduct": "Menu_Status_Category_PLU",
      "ClassificationReplica": "Menu_Configuration_Classification",
      "Suggested_Question_Type": "Menu_Type_Suggested_Question",
      "InternalClients_Users": "Menu_InternalClients_Users"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-eastus2-bo.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False"
  }
}
```

### Azure Storage

```json
{
  "AccessStorage": {
    "ConnectionString": "DefaultEndpointsProtocol=https;AccountName=YOUR_ACCOUNT;AccountKey=YOUR_KEY_HERE;EndpointSuffix=core.windows.net
    "SasToken": "?sv=2022-11-02&ss=b&srt=co&sp=r&se=2027-06-03T00:45:13Z&st=2024-02-06T16:45:13Z&spr=https&sig=mEIXMZ1csb%2B%2FLe10ZLnv9fEVfHHmKPLz08%2B4dCVOZl8%3D",
    "CdnAzure": "https://repositoryBO.azureedge.net",
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
    "ConfigurationMicroservice": "https://apim-dev-eastus2-bo.azure-api.net/configurations/",
    "InternalClientsMicroservice": "https://apim-dev-eastus2-bo.azure-api.net/internalclients/",
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
    "maximumLevelNestedNested": 5
  },
  "AllowedHosts": "*"
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB
- [ ] Configurar password de Redis
- [ ] Actualizar AccountKey de Azure Storage
- [ ] Verificar expiración del SAS Token
- [ ] Validar endpoints de microservicios
- [ ] Verificar colecciones en MongoDB

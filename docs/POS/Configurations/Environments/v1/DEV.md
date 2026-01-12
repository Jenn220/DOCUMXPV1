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

### MongoDB

```json
{
  "MongoDB": {
    "ConnectionString": "mongodb+srv://dev_swo:YXDZMeq3MKIqOK13@ec-mxpv2-dev.3hro7.mongodb.net/",
    "DatabaseName": "DEV_KFC_POS_Configurations",
    "Collections": {
      "City": "Configurations_POS_City",
      "Province": "Configurations_POS_Province"
    }
  }
}
```

### Redis Cache

```json
{
  "ReddisCache": {
    "ConnectionString": "redis-mxpv2-dev-ec.redis.cache.windows.net:6380,password=YOUR_REDIS_OR_AZURE_KEY_HERE=,ssl=True,abortConnect=False",
    "AddMinutesForExpirationTime": "1.0"
  }
}
```

### Servicio de Login

```json
{
  "LoginService": {
    "Url": "https://3654fe7d-ca3a-4bc9-a09f-3e7a97148461.mock.pstmn.io",
    "LoginMicroserviceToken": "YOUR_REDIS_OR_AZURE_KEY_HERE",
    "ClientId": "jsakhdalskdjasoidjasoidsa",
    "ClientSecret": "asdjlasldjasldkjasld"
  }
}
```

### Google reCAPTCHA

```json
{
  "GoogleRecaptcha": {
    "Url": "https://www.google.com/recaptcha/api/siteverify",
    "ApiKeySecretV2": "6Lcph5EqAAAAACnrq70VDFQyFshZ3FydzFaW9ivz",
    "ApiKeySecretV3": "6LcfCIoqAAAAAMk_4b_NrKXmvBWW1mWNKZcJDnei"
  }
}
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB
- [ ] Verificar colecciones en MongoDB
- [ ] Configurar password de Redis
- [ ] Validar URL de servicio de login
- [ ] Configurar ClientId y ClientSecret
- [ ] Validar claves secretas de reCAPTCHA V2 y V3
- [ ] Verificar URL de Google reCAPTCHA

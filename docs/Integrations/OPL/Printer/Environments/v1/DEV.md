## Configuración del Entorno de Desarrollo

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Conexión a Base de Datos de Entidades

```bash
CONNECTION_ENTITY_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CONNECTION_ENTITY_DB_PORT=
CONNECTION_ENTITY_DB_USER=dev_integration
CONNECTION_ENTITY_DB_PSWD=rIJEUAk8WyynPhC4
CONNECTION_ENTITY_DB_NAME=MXP_integrations
CONNECTION_ENTITY_DB_ADAPTER=Mongo
```

### Colecciones Extraídas

```bash
COLLECTION_DOCUMENT_TEMPLATES=Settings_BO_Printing_Documents
COLLECTION_STORE_DOCUMENTS=Centralized_Data
COLLECTION_PRINT_SETTINGS=Settings_BO_Printing_Settings
COLLECTION_BILLING_INFORMATION=billing_information
```

### Configuración de Extracción

```bash
EXTRACT_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_PORT=
EXTRACT_USER=dev_integration
EXTRACT_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_REPOSITORY=MXP_integrations
EXTRACT_ADAPTER=Mongo
```

### Configuración de Extracción - Settings

```bash
EXTRACT_SETTINGS_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_SETTINGS_PORT=
EXTRACT_SETTINGS_USER=dev_integration
EXTRACT_SETTINGS_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_SETTINGS_REPOSITORY=DEV_KFC_MXPi_Settings
EXTRACT_SETTINGS_ADAPTER=Mongo
```

### Configuración de Carga

```bash
LOAD_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
LOAD_PORT=
LOAD_USER=dev_integration
LOAD_PASSWORD=rIJEUAk8WyynPhC4
LOAD_REPOSITORY=MXP_integrations
LOAD_ADAPTER=Mongo
```

### Configuración de Seguridad

```bash
APP_SECRET_KEY=abc123xyz666
JWT_SECRET_KEY=abc123xyz666
JWT_TOKEN_LOCATION=header
```

### APIs Externas

```bash
OPENAI_API_KEY=abc123xyz666
REPLICATE_API_KEY=abc123xyz666
GOOGLE_GENAI_API_KEY=abc123xyz666-abc123xyz666
```

### Conexión a Base de Datos OPL

```bash
CONNECTION_OPL_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CONNECTION_OPL_DB_PORT=
CONNECTION_OPL_DB_USER=dev_integration
CONNECTION_OPL_DB_PSWD=rIJEUAk8WyynPhC4
CONNECTION_OPL_DB_NAME=DEV_KFC_MXPi_Opl
CONNECTION_OPL_DB_ADAPTER=Mongo
```

### Configuración de Idioma

```bash
LANGUAGE_MESSAGES=es
```

### Conexión a Caché

```bash
CACHE_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CACHE_DB_PORT=
CACHE_DB_USER=dev_integration
CACHE_DB_PSWD=rIJEUAk8WyynPhC4
CACHE_DB_NAME=MXP_integrations
CACHE_ENTITY_NAME=Integration_Caches
CACHE_ADAPTER=Mongo
```

### Configuración de Excepciones

```bash
EXCEPTIONS_COLLECTION=Exceptions_Logs
EXCEPTIONS_CONNECTION_STRING=mongodb+srv://dev_integration:rIJEUAk8WyynPhC4@ec-mxpv2-dev.3hro7.mongodb.net/
EXCEPTIONS_DB_NAME=MXP_integrations
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Validar colecciones extraídas
- [ ] Configurar credenciales de extracción
- [ ] Configurar credenciales de extracción para settings
- [ ] Configurar credenciales de carga
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Configurar credenciales de MongoDB OPL
- [ ] Configurar credenciales de caché
- [ ] Validar configuración de excepciones
- [ ] Validar URL de API de soporte

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

### Configuración de Extracción

```bash
EXTRACT_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_PORT=
EXTRACT_USER=dev_integration
EXTRACT_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_REPOSITORY=MXP_integrations
EXTRACT_ADAPTER=Mongo
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

### Configuración de Impresión

```bash
LOAD_REST_PRINT=http://192.168.101.121:5000
REPOSITORY_PRINT=api/ImpresionTickets/AbrirCajon/
NAME_DRAWER=caja2
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

### Gestión de Excepciones

```bash
EXCEPTION_STRATEGY=Rest
EXCEPTION_APP_CODE=MXPi-Pub-Device
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Configurar credenciales de extracción
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Validar configuración de impresión
- [ ] Configurar credenciales de MongoDB OPL
- [ ] Configurar credenciales de caché
- [ ] Validar URL de API de soporte

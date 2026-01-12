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
CONNECTION_ENTITY_DB_NAME=DEV_KFC_MXPi_Sync
```

### Conexión a Base de Datos de Caché

```bash
CACHE_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CACHE_DB_PORT=
CACHE_DB_USER=dev_integration
CACHE_DB_PSWD=rIJEUAk8WyynPhC4
CACHE_DB_NAME=DEV_KFC_MXPi_Sync
CACHE_ADAPTER=Mongo
CACHE_ENTITY_NAME=Sync_Integration_Caches
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

### Configuración de Idioma

```bash
LANGUAGE_MESSAGES=es
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

### Conexión a Base de Datos de Usuarios ARES

```bash
CONNECTION_USERS_ARES_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CONNECTION_USERS_ARES_DB_PORT=
CONNECTION_USERS_ARES_DB_USER=dev_integration
CONNECTION_USERS_ARES_DB_PSWD=rIJEUAk8WyynPhC4
CONNECTION_USERS_ARES_DB_NAME=DEV_KFC_MXPi_Settings
CONNECTION_USERS_ARES_DB_ENTITY=Settings_BO_Users_Pos
CONNECTION_USERS_ARES_DB_ADAPTER=Mongo
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Configurar credenciales de MongoDB para caché
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Validar URL de API de soporte
- [ ] Configurar credenciales de MongoDB para usuarios ARES
- [ ] Verificar entidad de usuarios ARES

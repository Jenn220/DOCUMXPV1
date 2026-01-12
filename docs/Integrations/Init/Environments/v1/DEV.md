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
```

### Conexión a Base de Datos de Caché

```bash
CACHE_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CACHE_DB_PORT=
CACHE_DB_USER=dev_integration
CACHE_DB_PSWD=rIJEUAk8WyynPhC4
CACHE_DB_NAME=MXP_integrations
CACHE_ENTITY_NAME=Integration_Caches
DEFAULT_MONGO_CONN_STR=mongodb+srv://dev_integration:rIJEUAk8WyynPhC4@ec-mxpv2-dev.3hro7.mongodb.net
```

### Configuración de Seguridad

```bash
JWT_SECRET_KEY=abc123xyz666
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

### Configuración de Métodos de Pago

```bash
PAYMENT_METHODS_ENTITY=ecu/23/formaspago/cargarporcadena
```

### Gestión de Excepciones

```bash
EXCEPTION_STRATEGY=Rest
EXCEPTION_APP_CODE=MXPi-Init
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

### Configuración CORS

```bash
CORS_ENV=dev
```

### API de Hashing

```bash
HASHING_API_URL=https://130.213.225.52:8080/hash/hash
```

### Configuración de Propagación

```bash
PROPAGATION_MENU_PLUS_KEY=mxp_v2.USP_Propagate_Menu_Plus
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Configurar credenciales de MongoDB para caché
- [ ] Actualizar JWT_SECRET_KEY
- [ ] Configurar API keys externas (OpenAI, Replicate, Google GenAI)
- [ ] Verificar URL de API de soporte
- [ ] Validar URL de API de hashing
- [ ] Verificar configuración de propagación

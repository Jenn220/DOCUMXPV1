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

### Conexión a Base de Datos de Procesos

```bash
PROCESS_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
PROCESS_DB_PORT=
PROCESS_DB_USER=dev_integration
PROCESS_DB_PSWD=rIJEUAk8WyynPhC4
PROCESS_DB_NAME=MXP_integrations
PROCESS_PK_NAME="code"
```

### Conexión a Base de Datos de Caché

```bash
CACHE_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
CACHE_DB_PORT=
CACHE_DB_USER=dev_integration
CACHE_DB_PSWD=rIJEUAk8WyynPhC4
CACHE_DB_NAME=MXP_integrations
CACHE_ADAPTER=Mongo
CACHE_ENTITY_NAME=Integration_Caches
DEFAULT_MONGO_CONN_STR=mongodb+srv://dev_integration:rIJEUAk8WyynPhC4@ec-mxpv2-dev.3hro7.mongodb.net
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

### Gestión de Excepciones

```bash
EXCEPTION_STRATEGY=Rest
EXCEPTION_APP_CODE=MXPi-Pub-Fe-Authorization
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

### Credenciales Estrategit

```bash
TOKEN_ESTRATEGIT=YOUR_REDIS_ACCESS_KEY_HERE
SUSCRIPTOR_ESTRATEGIT=12
```

### Configuración CORS

```bash
CORS_ENV=dev
```

### Configuración de Entidades y Repositorios

```bash
TRAZABILITY_ENTITY_NAME=Pub_Fe_Authorization
DATA_ENTITY_NAME=PurchaseOrders_POS_Order
REPOSITORY_ESTRATEGIT=api/kfc/consultarComprobante
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Configurar credenciales de MongoDB para procesos
- [ ] Configurar credenciales de MongoDB para caché
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Verificar credenciales de Estrategit
- [ ] Validar URL de API de soporte
- [ ] Verificar nombres de entidades
- [ ] Validar repositorio de Estrategit

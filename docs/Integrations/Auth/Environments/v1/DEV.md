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

### Conexión para Pruebas

```bash
TESTING_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
TESTING_DB_USER=dev_integration
TESTING_DB_PASSWORD=rIJEUAk8WyynPhC4
TESTING_DB_TABLE_NAME=MXP_integrations
```

### Configuración de Idioma

```bash
LANGUAGE_MESSAGES=es
```

### Gestión de Excepciones

```bash
EXCEPTION_STRATEGY=Rest
EXCEPTION_APP_CODE=MXPi-Auth
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

### Configuración CORS

```bash
CORS_ENV=dev
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para entidades
- [ ] Actualizar JWT_SECRET_KEY
- [ ] Configurar API keys externas
- [ ] Configurar credenciales de base de datos de pruebas
- [ ] Validar URL de API de soporte
- [ ] Verificar configuración de excepciones
- [ ] Confirmar entorno CORS

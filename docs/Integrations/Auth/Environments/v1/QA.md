## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Conexión a Base de Datos de Entidades

```bash
CONNECTION_ENTITY_DB_HOST=ec-mxpv2-qa.irplcko.mongodb.net
CONNECTION_ENTITY_DB_PORT=
CONNECTION_ENTITY_DB_USER=app_uat_integration
CONNECTION_ENTITY_DB_PSWD=2tg0tTzCxPMueq7I
CONNECTION_ENTITY_DB_NAME=UAT_KFC_MXPi_Auth
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
TESTING_DB_HOST=ec-mxpv2-qa.irplcko.mongodb.net
TESTING_DB_USER=app_uat_integration
TESTING_DB_PASSWORD=2tg0tTzCxPMueq7I
TESTING_DB_TABLE_NAME=UAT_KFC_MXPi_Auth
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
SUPPORT_API=http://130.213.195.90:8080/api/support/receiver
```

### Configuración CORS

```bash
CORS_ENV=qa
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

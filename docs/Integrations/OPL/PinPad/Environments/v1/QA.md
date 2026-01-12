## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Conexión a Base de Datos de Procesos

```bash
PROCESS_DB_HOST=ec-mxpv2-qa.irplcko.mongodb.net
PROCESS_DB_PORT=
PROCESS_DB_USER=app_uat_integration
PROCESS_DB_PSWD=2tg0tTzCxPMueq7I
PROCESS_DB_NAME=UAT_KFC_MXPi_Sync
PROCESS_PK_NAME="code"
```

### Conexión a Base de Datos de Pinpad

```bash
PINPAD_DB_HOST=ec-mxpv2-dev.3hro7.mongodb.net
PINPAD_DB_PORT=
PINPAD_DB_USER=dev_integration
PINPAD_DB_PSWD=rIJEUAk8WyynPhC4
PINPAD_DB_NAME=MXP_integrations
PINPAD_ADAPTER=Mongo
PINPAD_ENTITY_NAME=Settings_BO_Payment_Card_Settings
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
EXCEPTION_APP_CODE=MXPV2-PUB-FE
```

### API de Soporte

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de MongoDB para procesos
- [ ] Configurar credenciales de MongoDB para Pinpad
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Validar URL de API de soporte
- [ ] Verificar configuración de excepciones

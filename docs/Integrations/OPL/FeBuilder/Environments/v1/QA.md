## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Configuración de Extracción

```bash
EXTRACT_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_PORT=
EXTRACT_USER=dev_integration
EXTRACT_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_REPOSITORY=MXP_integrations
EXTRACT_ADAPTER=Mongo
```

### Configuración de Catálogo - Métodos de Pago

```bash
CATALOG_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
CATALOG_PORT=
CATALOG_USER=dev_integration
CATALOG_PASSWORD=rIJEUAk8WyynPhC4
CATALOG_REPOSITORY=DEV_KFC_MXPi_Configurator
CATALOG_ADAPTER=Mongo
```

### Configuración de Catálogo SIR

```bash
CATALOG_SIR_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
CATALOG_SIR_PORT=
CATALOG_SIR_USER=dev_integration
CATALOG_SIR_PASSWORD=rIJEUAk8WyynPhC4
CATALOG_SIR_REPOSITORY=QA_KFC_MXPi_Settings
CATALOG_SIR_ADAPTER=Mongo
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

### Entidades

```bash
BILLING_INFORMATION_ENTITY=billing_information
NUMBER_SEQUENCE_ENTITY=number_sequence
INTEGRATION_CATALOG_ENTITY=Integration_Catalog
CATALOG_SIR_ENTITY=Settings_BO_Method_Payment_SIR
FILTERS_SIR_ARRAY='["ALIA","AMERICAN EXPRES","CAJA CHICA OTROS","CAMPAÑA SOLIDARIA","CHEQUES","CORTESIAS","CREDITO SC","CUENTAS COBRAR","CUMPLEANIOS","CUPON EFECTIVO","CUPON PREPAGADO","DATAFONO","DESCUENTOS","DINERS CLUB","DISCOVER","D-UNAPICHI","EFECTIVO","FALTANTE","GLOVO","KFC CLUB","MASTER CARD","NOTAS CREDITO","NOTAS DEBITO","PedidosYa","POSMANUAL","RAPPI","RETENCION","RETENCION_IVA","TARJETAS","TARJETAS DE DEBITO","TOTAL","UBER","UNIONPAY","VISA"]'
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
CODE_NUMBER_COMPANY=41261533
```

### API de Soporte

```bash
SUPPORT_API=http://130.213.195.90:8080/api/support/receiver
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de extracción
- [ ] Configurar credenciales de catálogo
- [ ] Configurar credenciales de catálogo SIR
- [ ] Configurar credenciales de carga
- [ ] Validar entidades configuradas
- [ ] Verificar filtros SIR
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Validar URL de API de soporte

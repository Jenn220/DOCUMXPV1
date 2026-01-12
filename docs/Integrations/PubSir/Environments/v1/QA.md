## Configuración del Entorno de QA

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### API de Soporte

```bash
SUPPORT_API=http://130.213.195.90:8080/api/support/receiver
```

### Configuración de Seguridad

```bash
JWT_SECRET_KEY=abc123xyz666
```

### Versión de Interface

```bash
INTERFACE_VERSION=2
```

### Conexión a Caché

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

### Claves de Entidades

```bash
CASH_CLOSURE_KEY=Pub_Sale_Cash_Closure
PRODUCT_MEANS_KEY=Pub_Sale_Sale_Product_Means
PAYMENT_METHOD_KEY=Pub_Sale_Sale_Payment_Method
SALE_PRODUCT_KEY=Pub_Sale_Sale_Product
PRODUCT_NUM_KEY=Pub_Sale_Sale_Product_Num
HOURLY_SALE_KEY=Pub_Sale_Hourly_Sale
PAYMENT_METHOD_FOR_CHANNELS_KEY=Pub_Sale_Sale_Payment_Method_For_Channels
PAYMENT_METHODS_CATALOG_KEY=Settings_BO_Method_Payment_SIR
UUIDS_KEY=uuids
```

---

## Checklist de Configuración

- [ ] Verificar URL de API de soporte
- [ ] Actualizar JWT_SECRET_KEY
- [ ] Configurar credenciales de caché MongoDB
- [ ] Validar claves de entidades
- [ ] Verificar versión de interface

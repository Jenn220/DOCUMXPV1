## Configuración del Entorno de Desarrollo

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Configuración de Extracción - General

```bash
EXTRACT_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_USER=dev_integration
EXTRACT_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_ADAPTER=Mongo
```

### Configuración de Extracción - Órdenes de Compra

```bash
EXTRACT_PURCHASE_ORDERS_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_PURCHASE_ORDERS_USER=dev_integration
EXTRACT_PURCHASE_ORDERS_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_PURCHASE_ORDERS_ADAPTER=Mongo
EXTRACT_PURCHASE_ORDERS_REPOSITORY=DEV_KFC_POS_PurchaseOrders
```

### Configuración de Extracción - Catálogo

```bash
EXTRACT_CATALOG_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_CATALOG_USER=dev_integration
EXTRACT_CATALOG_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_CATALOG_REPOSITORY=DEV_KFC_MXPi_Settings
EXTRACT_CATALOG_ADAPTER=Mongo
```

### Configuración de Extracción - Clientes Internos

```bash
EXTRACT_INTERNAL_CLIENTS_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_INTERNAL_CLIENTS_USER=dev_integration
EXTRACT_INTERNAL_CLIENTS_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_INTERNAL_CLIENTS_REPOSITORY=DEV_KFC_POS_InternalClients
EXTRACT_INTERNAL_CLIENTS_ADAPTER=Mongo
```

### Configuración de Extracción - Homologación

```bash
EXTRACT_HOMOLOGATION_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
EXTRACT_HOMOLOGATION_USER=dev_integration
EXTRACT_HOMOLOGATION_PASSWORD=rIJEUAk8WyynPhC4
EXTRACT_HOMOLOGATION_REPOSITORY=homologation_v1_v2
EXTRACT_HOMOLOGATION_ADAPTER=Mongo
```

### Configuración de Carga - Ventas

```bash
LOAD_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
LOAD_USER=dev_integration
LOAD_PASSWORD=rIJEUAk8WyynPhC4
LOAD_REPOSITORY=DEV_KFC_MXPi_PubSale
LOAD_ADAPTER=Mongo
```

### Configuración de Carga - Logs

```bash
LOAD_LOGS_SERVER=ec-mxpv2-dev.3hro7.mongodb.net
LOAD_LOGS_USER=dev_integration
LOAD_LOGS_PASSWORD=rIJEUAk8WyynPhC4
LOAD_LOGS_REPOSITORY=DEV_KFC_MXPi_PubSIR
LOAD_LOGS_ADAPTER=Mongo
SIR_LOGS_CATALOG_KEY=Pub_SIR_Logs_Sales_Interface
```

### Configuración de Carga - SIR

```bash
LOAD_SIR_ADAPTER=Rest
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

### Configuración de Órdenes de Compra

```bash
PURCHASE_ORDERS_CATALOG_KEY=PurchaseOrders_POS_Order
EXTRACT_FILTER_DOCUMENT_TYPE=Factura
EXTRACT_FILTER_STATUS=Entregada
```

### Configuración de Conciliación

```bash
CONCILIATION_SUBSCRIPTION_CATALOG_KEY=PurchaseOrders_POS_Conciliation_Cash_Register_Subscription
CONCILIATION_TYPE_DES_FILTER=DES
CONCILIATION_CARD_PAYMENT_METHOD_FILTER=Favoritos
CONCILIATION_TYPES_CATALOG_KEY=PurchaseOrders_POS_Conciliation_Types
```

### Claves de Catálogo

```bash
TO_NAME_HOURLY_SALE=Pub_Sale_Hourly_Sale
TO_NAME_CASH_CLOSURE=Pub_Sale_Cash_Closure
TO_NAME_PAYMENTS_METHODS=Pub_Sale_Sale_Payment_Method
TO_NAME_SALE_METHOD_FOR_CHANNELS=Pub_Sale_Sale_Payment_Method_For_Channels
TO_NAME_SALE_PRODUCTS=Pub_Sale_Sale_Product
TO_NAME_RESTAURANT_PERIOD=InternalClients_POS_RestaurantPeriod
CATALOG_SALE_PRODUCT_MEANS=Pub_Sale_Sale_Product_Means
CATALOG_SALE_PRODUCT_NUM=Pub_Sale_Sale_Product_Num
CATALOG_UUID=uuids
CATALOG_SIR_SERVICE_CONFIGURATION=Settings_BO_SIR_Service_Configuration
SIR_CATALOG_KEY=Settings_BO_Method_Payment_SIR
```

### Configuración de Idioma

```bash
LANGUAGE_MESSAGES=es
```

### APIs de Servicios

```bash
SUPPORT_API=http://132.196.144.251:8080/api/support/receiver
URL_SIR=http://52.254.119.33:5000/api/v1/facade
SERVICE_TIMEOUT=10
```

---

## Checklist de Configuración

- [ ] Configurar credenciales de extracción MongoDB
- [ ] Configurar credenciales de carga MongoDB
- [ ] Configurar credenciales de caché
- [ ] Actualizar claves de seguridad (APP_SECRET_KEY, JWT_SECRET_KEY)
- [ ] Configurar API keys externas
- [ ] Verificar URLs de servicios (SUPPORT_API, URL_SIR)
- [ ] Validar claves de catálogo
- [ ] Verificar filtros de órdenes de compra
- [ ] Configurar timeout de servicios

# Manual de Instalación y Configuración

## 📋 Requisitos Previos

- **Node.js** (versión 16 o superior)
- **npm** o **yarn**
- **Git**

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd MXP-DOC-V2
```

### 2. Instalar Dependencias

```bash
npm install
```

### 3. Iniciar Servidor de Desarrollo

```bash
npm start
```

Abre automáticamente `http://localhost:3000`

## 💻 Comandos Básicos

```bash
npm start        # Modo desarrollo
npm run build    # Compilar para producción
npm run serve    # Previsualizar build
npm run clear    # Limpiar caché
```

## 📁 Estructura del Proyecto

```
MXP-DOC-V2/
├── .docusaurus/          # Generado automáticamente (no editar)
├── docs/
│   ├── BackOffice/
│   │   ├── Configurations/
│   │   ├── InternalClients/
│   │   ├── Menus/
│   │   ├── Payments/
│   │   ├── Propagador/
│   │   └── Sales/
│   ├── Integrations/
│   │   ├── Auth/
│   │   ├── FeAuth/
│   │   ├── Init/
│   │   ├── IntegrationConfigurator/
│   │   ├── OPL/
│   │   ├── PubSale/
│   │   ├── PubSir/
│   │   ├── SupportLibrary/
│   │   ├── Sync/
│   │   └── Synchronizer/
│   └── POS/
│       ├── COD/
│       ├── Configurations/
│       ├── InternalClients/
│       ├── InvoiceCalculator/
│       ├── LocalSync/
│       ├── Menus/
│       ├── Payments/
│       ├── PurchaseOrder/
│       ├── PWA/
│       └── Subsidy/
├── node_modules/         # Dependencias (no versionar)
├── src/                  # Archivos fuente personalizados
├── .gitignore           # Archivos ignorados por Git
├── docusaurus.config.js # Configuración principal
├── Manual.md            # Este manual
├── package.json         # Dependencias y scripts
└── sidebars.js          # Configuración del sidebar
```

## 📝 Agregar Nueva Documentación

1. Crear archivo `.md` en la carpeta correspondiente dentro de `docs/`
2. Agregar referencia en `sidebars.js`
3. Guardar y revisar en el navegador (hot-reload automático)

---

**Versión**: 1.0

## Obtener Integración

### Método HTTP

`GET`

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
{
  "_id": {
    "$binary": {
      "base64": "o62/LZW5TPyE5LeDLyg7Tg==",
      "subType": "04"
    }
  },
  "integration_name": "Integración homologación de usuario administrador por país",
  "integration_observations": "Integración de usuario administrador, extracción de id desde legacy, transformación-homologación y carga",
  "user_id": {
    "$binary": {
      "base64": "GCnanvu+SjvSSjNgtb9sCA==",
      "subType": "04"
    }
  },
  "status_id": {
    "$binary": {
      "base64": "NMJcF6W1SOGYYn8nXzdmmA==",
      "subType": "04"
    }
  },
  "with_Reponse": true,
  "integration_code": "I0001",
  "chunkLoad": 0,
  "process": [
    {
      "$binary": {
        "base64": "5jpoCf7FQYOYUbF3ZczzSQ==",
        "subType": "04"
      }
    },
    {
      "$binary": {
        "base64": "QJ0et9RhTqGcJeuw/NYUfA==",
        "subType": "04"
      }
    },
    {
      "$binary": {
        "base64": "8WVcMTjZTheXvFy/vH5e9w==",
        "subType": "04"
      }
    }
  ],
  "country": [
    {
      "Country_id": {
        "$binary": {
          "base64": "hXrMw8WaS2yuhFlC9aFFgQ==",
          "subType": "04"
        }
      },
      "Country_name": "Ecuador",
      "Country_code": "ECU"
    }
  ],
  "integrator": [
    {
      "Integrator_id": {
        "$binary": {
          "base64": "7ZBMwYbeSImFE+G0QCmn2w==",
          "subType": "04"
        }
      },
      "Integrator_name": "mxpv2.integration.init",
      "Integrator_url": "http://135.224.227.204:5000/api/v1/facade"
    }
  ],
  "franchise": [],
  "created_at": "2025-07-21T11:18:02.191Z",
  "updated_at": "2025-07-21T11:18:02.191Z"
}
```

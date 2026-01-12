## Obtener Integración por ID

### Método HTTP

`GET`

### URL

```
{{server_orchestrator}}/api/v1/integrations/getById
```

### Parámetros de Query

| Key  | Value                                  | Description                            |
| ---- | -------------------------------------- | -------------------------------------- |
| `id` | `ac248fe2-2d7e-461f-b245-50557a4eeec1` | ID único de la integración a consultar |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

## Respuestas del Servidor

### 200 OK - Consulta Exitosa

```json
{
  "code": "I0137",
  "withResponse": true,
  "chunkLoad": 0,
  "syncId": "",
  "country": "ECU",
  "franchise_id": 0,
  "processes": {
    "EXTRACTS": [
      {
        "code": "E0082",
        "withResponse": true,
        "withCache": true,
        "syncId": "",
        "configuration": {
          "connection": {
            "server": "192.168.1.70",
            "port": "",
            "user": "NAME",
            "password": "123456789",
            "repository": "USERNAME",
            "adapter": "CND ADAPTADOR"
          },
          "entities": [
            {
              "name": "CND_ENTITY",
              "properties": [
                {
                  "name": "cnd_properties",
                  "type": "string"
                }
              ],
              "filters": [
                {
                  "name": "cnd_properties",
                  "operator": "equal",
                  "value": "countryName"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

La respuesta contiene información básica de la integración incluyendo código, país, ID de franquicia y los procesos de extracción (EXTRACTS) configurados.

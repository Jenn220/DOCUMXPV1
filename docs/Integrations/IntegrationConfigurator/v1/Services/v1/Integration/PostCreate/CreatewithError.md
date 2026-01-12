## Crear Integración (con Error)

### Método HTTP

`POST`

### URL

```
{{server_orchestrator}}/api/v1/integrations/create
```

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "franchiseId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "status": "A",
  "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
  "userId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "hourToExecute": ""
}
```

### Error - No Creado

```json
{
  "code": 50,
  "messages": [
    {
      "object": "not created succefully"
    },
    {
      "status": "is required"
    },
    {
      "userId": "is required"
    }
  ],
  "data": {
    "franchiseId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "status": "A",
    "observations": "sdfgsdgdfjsgsdfhj fdgjhdfsgkhdfsjkghfds",
    "userId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "hourToExecute": ""
  }
}
```

### Descripción de la Respuesta de Error

| Campo      | Descripción                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| `code`     | Código de respuesta interno (50 = error)                                      |
| `messages` | Array con objetos de mensajes de error indicando campos faltantes o inválidos |
| `data`     | Objeto con los datos enviados en la solicitud                                 |

**Nota:** Este endpoint tiene un body diferente al anterior porque probablemente son dos versiones diferentes del mismo endpoint o diferentes casos de uso. El error indica que faltan campos requeridos en la estructura completa de la integración.

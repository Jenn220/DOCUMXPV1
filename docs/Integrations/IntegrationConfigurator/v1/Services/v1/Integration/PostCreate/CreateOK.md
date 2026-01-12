## Crear Integración

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

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
  "data": {
    "name": "Integracion de Forma de Pagos",
    "status": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "observations": "",
    "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
    "process": [
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
      },
      {
        "id": "b5ad9754-0419-46e5-b556-7ab1ab8db3e1"
      }
    ]
  }
}
```

### Descripción de la Respuesta Exitosa

| Campo               | Descripción                                        |
| ------------------- | -------------------------------------------------- |
| `code`              | Código de respuesta interno (10 = éxito)           |
| `messages`          | Array de mensajes informativos                     |
| `data`              | Objeto con la información de la integración creada |
| `data.name`         | Nombre de la integración                           |
| `data.status`       | Estado de la integración                           |
| `data.observations` | Observaciones                                      |
| `data.userId`       | ID del usuario                                     |
| `data.process`      | Array de procesos asociados con sus IDs            |

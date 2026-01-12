## Crear Log de Aplicación

### Método HTTP

`POST`

### URL

```
{{server_synchronizer}}/api/v1/logApplication/Create
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

```json
{
  "synchronizationId": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "processId": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
  "synchronizationName": "Data Sync Process",
  "integrationId": [
    "9bdeeb7f-136c-8f6a-489b-d9fc02db904a",
    "8028a2ff-c639-6df4-68e8-8982c0256be3"
  ],
  "message": "Synchronization completed successfully",
  "additionalInformation": "Total records processed: 1500",
  "entryDate": "2025-12-10T10:30:00Z",
  "status_Id": "568fa93e-8d4c-fa6e-e9cc-ce1fbdeb525d"
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                   | Tipo   | Descripción                                      |
| ----------------------- | ------ | ------------------------------------------------ |
| `synchronizationId`     | string | Identificador único de la sincronización         |
| `processId`             | string | Identificador del proceso                        |
| `synchronizationName`   | string | Nombre del proceso de sincronización             |
| `integrationId`         | array  | Lista de identificadores de integraciones        |
| `message`               | string | Mensaje descriptivo del log                      |
| `additionalInformation` | string | Información adicional del proceso                |
| `entryDate`             | string | Fecha y hora de entrada (formato ISO 8601)       |
| `status_Id`             | string | Identificador del estado del proceso de registro |

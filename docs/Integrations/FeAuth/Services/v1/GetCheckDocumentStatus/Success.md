## Consultar Comprobante Electrónico por Access Key

### Método HTTP

`POST`

### URL

```
{{server_pub}}/P002
```

### Autenticación

| Tipo         | Token       |
| ------------ | ----------- |
| Bearer Token | `{{token}}` |

### Parámetros de Query

| Key          | Value                                             |
| ------------ | ------------------------------------------------- |
| `access_key` | YOUR_REDIS_OR_AZURE_KEY_HERE |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "status": "success",
  "message": "Data retrieved successfully",
  "data": {
    "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "document": {
      "document_id": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
      "sequential": "050-070-000470031",
      "acces_key": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "type_document": "01",
      "country": "EC",
      "created_date": "04/06/2025 11:03:14",
      "base64": "YOUR_REDIS_ACCESS_KEY_HERE"
    },
    "fe_authorization_status": [
      {
        "codigo": "-1",
        "mensaje": "EL COMPROBANTE YA EXISTE EN SEEDBILLING POR FAVOR CONSULTAR EL ESTADO",
        "idDocumento": null,
        "xml": null,
        "estado": "ERROR ENVIO",
        "creation_date": "2025-06-04T16:12:07.302089+00:00"
      },
      {
        "codigo": "-1",
        "mensaje": "EL COMPROBANTE YA EXISTE EN SEEDBILLING POR FAVOR CONSULTAR EL ESTADO",
        "idDocumento": null,
        "xml": null,
        "estado": "ERROR ENVIO",
        "creation_date": "2025-06-04T16:12:07.302089+00:00"
      },
      {
        "codigo": "-1",
        "mensaje": "EL COMPROBANTE YA EXISTE EN SEEDBILLING POR FAVOR CONSULTAR EL ESTADO",
        "idDocumento": null,
        "xml": null,
        "estado": "ERROR ENVIO",
        "creation_date": "2025-06-04T16:12:07.302089+00:00"
      },
      {
        "codigo": "-1",
        "mensaje": "EL COMPROBANTE YA EXISTE EN SEEDBILLING POR FAVOR CONSULTAR EL ESTADO",
        "idDocumento": null,
        "xml": null,
        "estado": "ERROR ENVIO",
        "creation_date": "2025-06-04T16:12:07.302089+00:00"
      }
    ]
  }
}
```

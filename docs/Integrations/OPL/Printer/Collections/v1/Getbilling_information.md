## Obtener Información de Facturación

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
      "base64": "8sE6Ajy1R4GeENPxUTxR8g==",
      "subType": "04"
    }
  },
  "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
  "restaurant_id": "18ab3836-3202-f6d4-1eef-a5b5de5a8e40",
  "company_id": "6c5a9727-9303-99b8-e363-552d320738ff",
  "description": "Compañia kfc ecuador",
  "business_name": "INT FOOD SERVICES CORP SA",
  "document_identity_type_id": "6c5a9727-9303-99b8-e363-552d320738ff",
  "tax_identification_number": "1791415132001",
  "resolution_number": "RES-2024-00123",
  "headquarters_address": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
  "restaurant_address": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
  "required_to_keep_accounting": "Sí",
  "full_name": "María José  Hernández Zurita",
  "phone": "0986610329",
  "email": "mari_jhz@hotmail.com",
  "address": "Guayaquil",
  "tax_payer": "GRAN CONTRIBUYENTE",
  "tax_payer_type": "Especial",
  "tax_payer_resolution": "NAC-GCFOIOC21-00000900-E",
  "issue_type_name": "Emisión Normal",
  "issue_type_code": 1,
  "issue_date": "27/03/2025 12:30:25.213",
  "billing_label": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
  "billing_link_label": "Para obtener su factura electrónica ingrese a:",
  "billing_link": "https://facturacion.kfc.ec",
  "billing_access_key_label": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
  "document_type": [
    {
      "document_key": "FACTURA-ECU",
      "document_name": "Factura",
      "document_code": "01"
    },
    {
      "document_key": "NOTA_CREDITO-ECU",
      "document_name": "Nota de crédito",
      "document_code": "04"
    }
  ],
  "branche_office": {
    "branche_office_name": "GUS COTOCOLLAO",
    "branche_office_series": "005",
    "branche_office_address": "PICHINCHA / QUITO / AV. DE LA PRENSA N61-104 Y AV. DEL MAESTRO",
    "point_of_issue": [
      {
        "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019251",
        "point_of_emission": "050",
        "sequential_vuocher": [
          {
            "document_code": "01",
            "sequential": 470132
          },
          {
            "document_code": "04",
            "sequential": 115
          }
        ],
        "environment_name": "Pruebas",
        "environment_code": 1
      },
      {
        "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019252",
        "point_of_emission": "051",
        "sequential_vuocher": [
          {
            "document_code": "01",
            "sequential": 322423
          },
          {
            "document_code": "04",
            "sequential": 33
          }
        ],
        "environment_name": "Pruebas",
        "environment_code": 1
      },
      {
        "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
        "point_of_emission": "052",
        "sequential_vuocher": [
          {
            "document_code": "01",
            "sequential": 386
          },
          {
            "document_code": "04",
            "sequential": 90
          }
        ],
        "environment_name": "Pruebas",
        "environment_code": 1
      }
    ],
    "cdn_restaurant_id": "G001"
  },
  "fe_build_code_number": "41261533",
  "time_zone": "America/Guayaquil"
}
```

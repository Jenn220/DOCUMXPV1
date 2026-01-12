## Obtener Autorización de Facturación Electrónica

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
      "base64": "l8s8k9IgSYK0o3ZS0jhnfg==",
      "subType": "04"
    }
  },
  "document": {
    "document_id": {
      "$binary": {
        "base64": "zgmBytDwQtyzxC3jc+U3ww==",
        "subType": "04"
      }
    },
    "sequential": "902-001-000000061",
    "access_key": "YOUR_REDIS_OR_AZURE_KEY_HERE",
    "type_document": "01",
    "country": "EC",
    "datetime": "2025-08-15T09:01:58.960Z",
    "invoice": {
      "companyTaxData": {
        "name": "QA: INT FOOD SERVICES CORP SA",
        "identificationNumber": "1791415132001",
        "specialTaxpayer": "GRAN CONTRIBUYENTE",
        "isSpecialTaxpayer": "Sí",
        "specialTaxpayerCode": "NAC-GCFOIOC21-00000900-E",
        "typeTax": "Especial",
        "obligatoryToKeepAccounts": "Sí",
        "resolutionCode": "RES-2024-00123",
        "companyAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
        "restaurantAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
        "issueType": "Emisión Normal"
      },
      "dataInvoice": {
        "sequential": "902-001-000000061",
        "accessKey": "YOUR_REDIS_OR_AZURE_KEY_HERE",
        "transaction": "G008F000000630",
        "legend": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
        "linkLabel": "Para obtener su factura electrónica ingrese a:",
        "urlDocument": "https://facturacion.kfc.ec",
        "accessKeyLabel": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
        "environment": "Pruebas",
        "createdAt": "2025-08-15T09:01:58.960Z",
        "document": {
          "client": {
            "client_id": "ECU1122345678",
            "name": "ALTAFULLA  GONZALES",
            "last_name": "",
            "phone": "2232658",
            "email": "alti@kfc.com.ec",
            "gov_id_type": "Cedula",
            "gov_id_number": "1122345678"
          },
          "orderInvoice": {
            "order_id": "0cb57bf6-0948-4ebe-ab77-bfbab9fab92c",
            "invoice_id": null,
            "invoice_key_aut": null,
            "products": [
              {
                "plu_id": 57621,
                "plu_name": "MEDIO ESPECIAL",
                "plu_quantity": 1,
                "plu_description": null,
                "price": {
                  "total_per_plu": {
                    "currency_code": "USD",
                    "subtotal_without_taxes": {
                      "$numberDecimal": "10.86087"
                    },
                    "discount_percentage": 0,
                    "discounts_value": 0,
                    "subtotal_include_discounts": {
                      "$numberDecimal": "10.86087"
                    },
                    "tax_value": {
                      "$numberDecimal": "1.629131"
                    },
                    "total": {
                      "$numberDecimal": "12.49"
                    },
                    "taxes": [
                      {
                        "tax_name": "IVA 15%",
                        "tax_code": "d00c4be9-a547-f72d-b87b-2abaebc07f4b",
                        "tax_percentage": 15,
                        "total_tax_value": {
                          "$numberDecimal": "1.629131"
                        },
                        "base_amount": {
                          "$numberDecimal": "10.86087"
                        }
                      }
                    ]
                  },
                  "total_price": {
                    "currency_code": "USD",
                    "subtotal_without_taxes": {
                      "$numberDecimal": "10.86087"
                    },
                    "discount_percentage": 0,
                    "discounts_value": 0,
                    "subtotal_include_discounts": {
                      "$numberDecimal": "10.86087"
                    },
                    "tax_value": {
                      "$numberDecimal": "1.629131"
                    },
                    "total": {
                      "$numberDecimal": "12.49"
                    },
                    "taxes": [
                      {
                        "tax_name": "IVA 15%",
                        "tax_code": "d00c4be9-a547-f72d-b87b-2abaebc07f4b",
                        "tax_percentage": 15,
                        "total_tax_value": {
                          "$numberDecimal": "1.6291305"
                        },
                        "base_amount": {
                          "$numberDecimal": "10.86087"
                        }
                      }
                    ]
                  }
                }
              }
            ]
          },
          "payment_methods": [
            {
              "payment_methods_id": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
              "processor": "",
              "currency_code": "USD",
              "payment_method_code": "3be0126a-e739-3b40-6feb-f4aa92d73a7c",
              "transaction_type": "credit",
              "transaction_id": "",
              "transaction_status": "APPROVED",
              "reference_number": "",
              "exact_payment": true,
              "customer_cash_amount": "0.00",
              "total_bill": 12.49,
              "additional_info_payment_methods": null,
              "acquirer": {
                "code": "",
                "name": ""
              },
              "transaction_date": {
                "date": "2025-08-15T14:00:49.458Z",
                "time_zone_type": 3,
                "time_zone_name": "America/Guayaquil"
              }
            }
          ],
          "additional_data": []
        }
      },
      "dataCredit": {
        "sequential": "",
        "accessKey": "",
        "transaction": "",
        "legend": "",
        "linkLabel": "",
        "urlDocument": "",
        "accessKeyLabel": "",
        "environment": null,
        "createdAt": "Fri Aug 15 2025",
        "document": {
          "client": {
            "client_id": "",
            "name": "",
            "last_name": "",
            "phone": "",
            "email": "",
            "gov_id_type": "",
            "gov_id_number": ""
          },
          "orderInvoice": {
            "order_id": "",
            "invoice_id": "",
            "invoice_key_aut": "",
            "products": []
          },
          "payment_methods": [],
          "additional_data": []
        },
        "motivo": ""
      },
      "document_code": "01",
      "fe_authorization_status": {
        "codigo": "0",
        "mensaje": "COMPROBANTE CREADO Y REGISTRO CORRECTAMENTE",
        "idDocumento": "YOUR_REDIS_OR_AZURE_KEY_HERE",
        "xml": null,
        "estado": "ENVIADO",
        "creation_date": "2025-08-19T11:43:33"
      }
    },
    "base64": "YOUR_REDIS_ACCESS_KEY_HERE"
  },
  "fe_authorization_status": [
    {
      "codigo": "0",
      "mensaje": "COMPROBANTE CREADO Y REGISTRO CORRECTAMENTE",
      "idDocumento": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "xml": null,
      "estado": "ENVIADO",
      "creation_date": "2025-08-19T11:43:33"
    },
    {
      "codigo": "0",
      "mensaje": "COMPROBANTE RECHAZADO POR AUTORIZACION El establecimiento 902 está cerrado",
      "estado": "XA",
      "creation_date": "2025-08-19T11:43:55"
    }
  ],
  "runtime": "2025-08-19T11:43:44"
}
```

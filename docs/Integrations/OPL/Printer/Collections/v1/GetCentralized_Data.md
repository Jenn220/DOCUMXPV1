## Obtener Datos Centralizados

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
      "base64": "FuhUjCJdRJ+z/oW8GTWGrg==",
      "subType": "04"
    }
  },
  "type_document": "FACTURA",
  "transaction": {
    "point_of_sale": {
      "cdn_id": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
      "restaurant_id": "e17d03da-b8b6-f424-febc-3a767b6401bb",
      "cash_register_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "cash_register_name": "EC-CAJA001",
      "user_seller_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
      "user_seller_name": "Daniel Llerena",
      "device_os_name": "ios",
      "source_app_name": "Maxpoint 2.0",
      "half_integration_id": 3,
      "half_integration_name": "App"
    },
    "client": {
      "client_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "name": "María José ",
      "last_name": "Hernández Zurita ",
      "phone": "+593986610329",
      "email": "mari_jhz@hotmail.com",
      "gov_id_type": "CI",
      "gov_id_number": "0929691038",
      "external_id": "030B9503-85CF-E511-80C6-000D3A3261F3",
      "additional_info": {
        "birthdate": ""
      }
    },
    "order": {
      "order_id": "0001292432-010103",
      "createdAt": "Wed Sep 11 2024 12:14:40 GMT-0500 (Colombia Standard Time)",
      "selected_shipping_method": "pickup",
      "accumulate_points": false,
      "redeem_points": false,
      "stock": false,
      "discount": false,
      "order_comment": "",
      "annulation_comment": "",
      "products": [
        {
          "plu_id": "401",
          "plu_name": "COMBO IDEAL",
          "plu_quantity": 1,
          "plu_comment": "",
          "price": {
            "total_per_plu": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": 0,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "taxes_percentage": 15,
              "tax_value": 0.85,
              "total": 6.5,
              "total_before_sale": 6.5,
              "suggested_price": 0
            },
            "total_price": {
              "currency_code": "USD",
              "subtotal_without_taxes": 5.65,
              "discount_percentage": null,
              "discounts_value": 0,
              "subtotal_include_discounts": 5.65,
              "taxes_percentage": 15,
              "tax_value": 0.85,
              "total": 6.5,
              "total_before_sale": 6.5,
              "suggested_price": 0
            }
          },
          "modifier_groups": [
            {
              "suggested_question_id": "7421A2EE-B13B-EA11-80EA-000D3A019254",
              "description": "Es necesario elegir uno",
              "selected_modifiers": [
                {
                  "plu_id": "402",
                  "plu_name": "COMBO IDEAL",
                  "plu_quantity": 1,
                  "plu_comment": "",
                  "price": {
                    "total_per_plu": {
                      "currency_code": "USD",
                      "subtotal_without_taxes": 5.65,
                      "discount_percentage": 0,
                      "discounts_value": 0,
                      "subtotal_include_discounts": 5.65,
                      "taxes_percentage": 15,
                      "tax_value": 0.85,
                      "total": 6.5,
                      "total_before_sale": 6.5,
                      "suggested_price": 0
                    },
                    "total_price": {
                      "currency_code": "USD",
                      "subtotal_without_taxes": 5.65,
                      "discount_percentage": null,
                      "discounts_value": 0,
                      "subtotal_include_discounts": 5.65,
                      "taxes_percentage": 15,
                      "tax_value": 0.85,
                      "total": 6.5,
                      "total_before_sale": 6.5,
                      "suggested_price": 0
                    }
                  },
                  "modifier_groups": [],
                  "additional_info_modifier_groups": null
                }
              ]
            }
          ],
          "additional_info_order": null
        }
      ],
      "stock_details": null
    },
    "shipping_method": null,
    "payments": {
      "totals": [
        {
          "currency_code": "USD",
          "subtotal_without_taxes": 5.65,
          "discount_percentage": 0,
          "discounts_value": 0,
          "subtotal_include_discounts": 5.65,
          "taxes_percentage": 15,
          "tax_value": 0.85,
          "total_before_sale": 6.5,
          "total": 6.5
        },
        {
          "currency_code": "Points",
          "subtotal_without_taxes": 0,
          "discount_percentage": 0,
          "discounts_value": 0,
          "subtotal_include_discounts": 0,
          "taxes_percentage": 15,
          "tax_value": 0,
          "total_before_sale": 0,
          "total": 0
        }
      ],
      "shipping_cost": null,
      "extra_charges": null,
      "taxes": [
        {
          "name": "IVA 15%",
          "currency_code": "USD",
          "subtotal_without_taxes": 5.65,
          "percentage": 15,
          "total": 0.85
        }
      ],
      "discounts": [
        {
          "name": "OFF5APP",
          "percentage_discount": false,
          "amount_discount": true,
          "currency_code": "USD",
          "total_before_sale": 0,
          "subtotal_without_discounts": 4.65,
          "percentage": 0,
          "total": 4.3478,
          "total_with_taxes": 5
        }
      ],
      "payment_methods": [
        {
          "payment_methods_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
          "processor": "DEUNA",
          "currency_code": "USD",
          "payment_method_code": "93",
          "transaction_type": "credit",
          "transaction_id": "",
          "transaction_status": "APPROVED",
          "tid": null,
          "mid": null,
          "authorization_code": null,
          "voucher": null,
          "reference_number": null,
          "exact_payment": true,
          "customer_cash_amount": "0.0000",
          "total_bill": 6.5,
          "acquirer": {
            "code": " ",
            "name": " "
          },
          "card": {
            "mask": "360857XXXXXXX2001",
            "bin": "360857",
            "last_four_digits": "2001",
            "brand": "diners_club",
            "external_card_brand_id": "D20A9503-85CF-E511-80C6-000D3A3261F3",
            "holder": " ",
            "card_country": " "
          },
          "transaction_date": {
            "date": "2024-09-11 05:14:41",
            "time_zone_type": 3,
            "time_zone_name": "America/Guayaquil"
          },
          "additional_info_payment_methods": null
        }
      ]
    },
    "marketing": null,
    "additional_info_transaction": null
  },
  "feBuilder": {
    "companyTaxData": {
      "name": "INT FOOD SERVICES CORP SA",
      "identificationNumber": "1791415132001",
      "specialTaxpayer": "GRAN CONTRIBUYENTE",
      "isSpecialTaxpayer": "Sí",
      "specialTaxpayerCode": "NAC-GCFOIOC21-00000900-E",
      "typeTax": "Especial",
      "obligatoryToKeepAccounts": "Sí",
      "resolutionCode": "RES-2024-00123",
      "companyAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador",
      "restaurantAddress": "Av. Amazonas y Naciones Unidas, Quito, Ecuador"
    },
    "dataInvoice": {
      "sequential": "098-088-000000172",
      "accessKey": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "transaction": "G001F000000089",
      "legend": "Estimado cliente: Por favor verifique los datos de su factura, únicamente se aceptarán cambios el mismo día de emisión.",
      "linkLabel": "Para obtener su factura electrónica ingrese a:",
      "urlDocument": "https://facturacion.kfc.ec",
      "accessKeyLabel": "(Usuario: CI/RUC, Clave: CI/RUC) o a la página web del SRI con la Clave de Acceso:",
      "createdAt": "06/06/2025 10:37:28"
    },
    "dataCredit": {}
  },
  "pubDevice": {
    "turnero": {
      "codeQr": "dsfsdfsd",
      "typeQr": "type1"
    },
    "kds": {}
  },
  "promotions": {
    "cupones": {
      "codeQr": "dsfsdfsd",
      "typeQr": "type1",
      "text": ""
    }
  },
  "fe_authorization_status": {
    "codigo": "0",
    "mensaje": "COMPROBANTE AUTORIZADO",
    "estado": "A",
    "creation_date": "2025-06-25T14:24:06.148769-05:00"
  }
}
```

## Obtener Configuración de Impresión

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
      "base64": "cYgvFvdBRk6475+PjRfVdA==",
      "subType": "04"
    }
  },
  "country_id": {
    "$binary": {
      "base64": "1srIPWzl9i4mKB4umue1Hw==",
      "subType": "04"
    }
  },
  "cdn_id": {
    "$binary": {
      "base64": "vC2K2uJeG7dV/jLRIFrErw==",
      "subType": "04"
    }
  },
  "restaurant_id": {
    "$binary": {
      "base64": "JCYFefr4dj+qx14W+v+W0Q==",
      "subType": "04"
    }
  },
  "cash_registers": [
    {
      "cash_register_id": {
        "$binary": {
          "base64": "qk7OfOxuqwEmp5XSwsgJwA==",
          "subType": "04"
        }
      },
      "cash_register_name": "CAJA01",
      "printing_channel": [
        {
          "channel_id": {
            "$binary": {
              "base64": "+R7gOnToCEKvSAW3c29VGg==",
              "subType": "04"
            }
          },
          "channel_name": "FACTURA",
          "documents_to_print": ["FACTURA", "NOTA_CREDITO"],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "3hzDaaR86796PWCs3AbNjA==",
              "subType": "04"
            }
          },
          "channel_name": "LINEA",
          "documents_to_print": ["ORDEN_PEDIDO"],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "NTjAdg289rHUC/6qh+KZLQ==",
              "subType": "04"
            }
          },
          "channel_name": "VOUCHER",
          "documents_to_print": [
            "ARQUEO",
            "CORTE_XX",
            "DESASIGNADO_CAJERO_DEN",
            "FIN_DE_DIA",
            "RETIRO_FONDO_ASIGNADO",
            "RETIROS_FORMASPAGO",
            "VOUCHER_CANCELADO_NO_APROBADO",
            "VOUCHER_APROBADO",
            "RETIRO_EFECTIVO",
            "VOUCHER_NO_APROBADO",
            "VOUCHER_ANULACION",
            "DESASIGNADO_CAJERO",
            "FALTANTE_CXC",
            "CAJA_CHICA",
            "CUPON"
          ],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "lM4oeMARkFz1hqdQHtQyrg==",
              "subType": "04"
            }
          },
          "channel_name": "COCINA",
          "documents_to_print": [],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        }
      ]
    },
    {
      "cash_register_id": {
        "$binary": {
          "base64": "QSohKC2op0KC1eXANrGNFw==",
          "subType": "04"
        }
      },
      "cash_register_name": "CAJA02",
      "printing_channel": [
        {
          "channel_id": {
            "$binary": {
              "base64": "r5isD/gZzv32TGD46PewIg==",
              "subType": "04"
            }
          },
          "channel_name": "FACTURA",
          "documents_to_print": ["FACTURA", "NOTA_CREDITO"],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "3hzDaaR86796PWCs3AbNjA==",
              "subType": "04"
            }
          },
          "channel_name": "LINEA",
          "documents_to_print": ["ORDEN_PEDIDO"],
          "printers": [
            {
              "printer_name": "linea",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "NTjAdg289rHUC/6qh+KZLQ==",
              "subType": "04"
            }
          },
          "channel_name": "VOUCHER",
          "documents_to_print": [
            "ARQUEO",
            "CORTE_XX",
            "DESASIGNADO_CAJERO",
            "FIN_DE_DIA",
            "RETIRO_FONDO_ASIGNADO",
            "RETIROS_FORMASPAGO",
            "VOUCHER_CANCELADO_NO_APROBADO",
            "VOUCHER_APROBADO",
            "RETIRO_EFECTIVO",
            "VOUCHER_NO_APROBADO",
            "VOUCHER_ANULACION"
          ],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "lM4oeMARkFz1hqdQHtQyrg==",
              "subType": "04"
            }
          },
          "channel_name": "COCINA",
          "documents_to_print": [],
          "printers": [
            {
              "printer_name": "cocina",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        }
      ]
    },
    {
      "cash_register_id": {
        "$binary": {
          "base64": "7/Rg5wGpZEWM0pz4/K8WfA==",
          "subType": "04"
        }
      },
      "cash_register_name": "CAJA03",
      "printing_channel": [
        {
          "channel_id": {
            "$binary": {
              "base64": "r5isD/gZzv32TGD46PewIg==",
              "subType": "04"
            }
          },
          "channel_name": "FACTURA",
          "documents_to_print": ["FACTURA", "NOTA_CREDITO"],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "3hzDaaR86796PWCs3AbNjA==",
              "subType": "04"
            }
          },
          "channel_name": "LINEA",
          "documents_to_print": ["ORDEN_PEDIDO"],
          "printers": [
            {
              "printer_name": "cocina",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "NTjAdg289rHUC/6qh+KZLQ==",
              "subType": "04"
            }
          },
          "channel_name": "VOUCHER",
          "documents_to_print": [
            "ARQUEO",
            "CORTE_XX",
            "DESASIGNADO_CAJERO",
            "FIN_DE_DIA",
            "RETIRO_FONDO_ASIGNADO",
            "RETIROS_FORMASPAGO",
            "VOUCHER_CANCELADO_NO_APROBADO",
            "VOUCHER_APROBADO",
            "RETIRO_EFECTIVO",
            "VOUCHER_NO_APROBADO",
            "VOUCHER_ANULACION"
          ],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        }
      ]
    },
    {
      "cash_register_id": {
        "$binary": {
          "base64": "uc1aF8EHC0GAwLw9mMDYEw==",
          "subType": "04"
        }
      },
      "cash_register_name": "CAJA04",
      "printing_channel": [
        {
          "channel_id": {
            "$binary": {
              "base64": "r5isD/gZzv32TGD46PewIg==",
              "subType": "04"
            }
          },
          "channel_name": "FACTURA",
          "documents_to_print": ["FACTURA", "NOTA_CREDITO"],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "3hzDaaR86796PWCs3AbNjA==",
              "subType": "04"
            }
          },
          "channel_name": "LINEA",
          "documents_to_print": ["ORDEN_PEDIDO"],
          "printers": [
            {
              "printer_name": "cocina",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        },
        {
          "channel_id": {
            "$binary": {
              "base64": "NTjAdg289rHUC/6qh+KZLQ==",
              "subType": "04"
            }
          },
          "channel_name": "VOUCHER",
          "documents_to_print": [
            "ARQUEO",
            "CORTE_XX",
            "DESASIGNADO_CAJERO",
            "FIN_DE_DIA",
            "RETIRO_FONDO_ASIGNADO",
            "RETIROS_FORMASPAGO",
            "VOUCHER_CANCELADO_NO_APROBADO",
            "VOUCHER_APROBADO",
            "RETIRO_EFECTIVO",
            "VOUCHER_NO_APROBADO",
            "VOUCHER_ANULACION"
          ],
          "printers": [
            {
              "printer_name": "caja2",
              "printer_brand": "POSIFLEX",
              "is_balancing": 0,
              "printer_name_balancing": "",
              "printer_url": "http://192.168.101.121",
              "printer_port": "5000"
            }
          ]
        }
      ]
    }
  ]
}
```

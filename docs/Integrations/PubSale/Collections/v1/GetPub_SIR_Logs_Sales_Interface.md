## Obtener Logs de Interfaz de Ventas SIR

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
      "base64": "l3BD840ZQnCrRj0gCh8HEw==",
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
      "base64": "GKs4NjIC9tQe76W13lqOQA==",
      "subType": "04"
    }
  },
  "period_id": {
    "$binary": {
      "base64": "bjtij1vuTSKSpW81qpONxA==",
      "subType": "04"
    }
  },
  "period_date": "22/10/2025",
  "sales": [
    {
      "cierre_cajas": [
        {
          "venta_bruta": 46.55,
          "venta_neta": 40.48,
          "venta_cero": 0,
          "iva": 6.07,
          "descuento": 0,
          "descuento_iva": 0,
          "descuento_cero": 0,
          "servicio": 0,
          "transacciones": 9,
          "id_canal_menu_medio": -1,
          "id_medio": -1,
          "medio": "Total",
          "es_mercadito": "NO",
          "total_clientes": 0
        },
        {
          "venta_bruta": 46.55,
          "venta_neta": 40.48,
          "venta_cero": 0,
          "iva": 6.07,
          "descuento": 0,
          "descuento_iva": 0,
          "descuento_cero": 0,
          "servicio": 0,
          "transacciones": 9,
          "id_canal_menu_medio": 1,
          "id_medio": 1,
          "medio": "Local",
          "es_mercadito": "NO",
          "total_clientes": 0
        }
      ]
    },
    {
      "din_trans": [
        {
          "Cod_Cajero": "GUARACA MALAN VICTOR GERARDO",
          "Cod_FormaPago": -1,
          "Valor": "32.32",
          "Num_Trans": 6,
          "Recap": 0,
          "IDDocumento": "-1",
          "numero_factura": ""
        },
        {
          "Cod_Cajero": "GUARACA MALAN VICTOR GERARDO",
          "Cod_FormaPago": 9,
          "Valor": "50.0",
          "Num_Trans": 6,
          "Recap": 0,
          "IDDocumento": "-1",
          "numero_factura": ""
        }
      ]
    },
    {
      "plus_trans": [
        {
          "plu_id": 12259,
          "num_plu": 708,
          "cnt": 6,
          "vb": 11.94,
          "vn": 10.38,
          "bi": 10.38,
          "bc": 0,
          "iva": 1.56,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 1.99,
          "vnu": 1.73,
          "biu": 1.73,
          "bcu": 0,
          "iu": 0.26,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 15079,
          "num_plu": 849,
          "cnt": 1,
          "vb": 1.99,
          "vn": 1.73,
          "bi": 1.73,
          "bc": 0,
          "iva": 0.26,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 1.99,
          "vnu": 1.73,
          "biu": 1.73,
          "bcu": 0,
          "iu": 0.26,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 60171,
          "num_plu": 60171,
          "cnt": 3,
          "vb": 18.72,
          "vn": 16.28,
          "bi": 16.28,
          "bc": 0,
          "iva": 2.44,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 6.24,
          "vnu": 5.43,
          "biu": 5.43,
          "bcu": 0,
          "iu": 0.81,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 39667,
          "num_plu": 1719,
          "cnt": 2,
          "vb": 0,
          "vn": 0,
          "bi": 0,
          "bc": 0,
          "iva": 0,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 0,
          "vnu": 0,
          "biu": 0,
          "bcu": 0,
          "iu": 0,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 64066,
          "num_plu": 64066,
          "cnt": 3,
          "vb": 0,
          "vn": 0,
          "bi": 0,
          "bc": 0,
          "iva": 0,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 0,
          "vnu": 0,
          "biu": 0,
          "bcu": 0,
          "iu": 0,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 12248,
          "num_plu": 700,
          "cnt": 1,
          "vb": 5.75,
          "vn": 5,
          "bi": 5,
          "bc": 0,
          "iva": 0.75,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 5.75,
          "vnu": 5,
          "biu": 5,
          "bcu": 0,
          "iu": 0.75,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 39669,
          "num_plu": 1721,
          "cnt": 2,
          "vb": 0,
          "vn": 0,
          "bi": 0,
          "bc": 0,
          "iva": 0,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 0,
          "vnu": 0,
          "biu": 0,
          "bcu": 0,
          "iu": 0,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 65477,
          "num_plu": 65477,
          "cnt": 1,
          "vb": 0,
          "vn": 0,
          "bi": 0,
          "bc": 0,
          "iva": 0,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 0,
          "vnu": 0,
          "biu": 0,
          "bcu": 0,
          "iu": 0,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 64775,
          "num_plu": 64775,
          "cnt": 1,
          "vb": 4.5,
          "vn": 3.91,
          "bi": 3.91,
          "bc": 0,
          "iva": 0.59,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 4.5,
          "vnu": 3.91,
          "biu": 3.91,
          "bcu": 0,
          "iu": 0.59,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 4639,
          "num_plu": 317,
          "cnt": 2,
          "vb": 1.4,
          "vn": 1.22,
          "bi": 1.22,
          "bc": 0,
          "iva": 0.18,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 0.7,
          "vnu": 0.61,
          "biu": 0.61,
          "bcu": 0,
          "iu": 0.09,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        },
        {
          "plu_id": 17931,
          "num_plu": 944,
          "cnt": 1,
          "vb": 2.25,
          "vn": 1.96,
          "bi": 1.96,
          "bc": 0,
          "iva": 0.29,
          "di": 0,
          "dc": 0,
          "srv": 0,
          "vbu": 2.25,
          "vnu": 1.96,
          "biu": 1.96,
          "bcu": 0,
          "iu": 0.29,
          "id_cmm": 1,
          "id_medio": 1,
          "es_mcd": "NO"
        }
      ]
    },
    {
      "venta_por_hora": [
        {
          "Tiempo": "12:00 - 12:59",
          "Transacciones": 5,
          "Valor": 22.95
        },
        {
          "Tiempo": "10:00 - 10:59",
          "Transacciones": 1,
          "Valor": 7.74
        },
        {
          "Tiempo": "09:00 - 09:59",
          "Transacciones": 1,
          "Valor": 1.4
        },
        {
          "Tiempo": "11:00 - 11:59",
          "Transacciones": 2,
          "Valor": 14.46
        }
      ]
    },
    {
      "medio_formaspago": [
        {
          "codigo_forma_pago": 9,
          "valor": 46.55,
          "transacciones": 9,
          "id_canal_menu_medio": 1,
          "medio": "Local"
        }
      ]
    }
  ],
  "creation_date": {
    "$date": "2025-10-24T17:26:54.015Z"
  }
}
```

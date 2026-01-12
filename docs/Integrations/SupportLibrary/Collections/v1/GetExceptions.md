## Exception

### Método HTTP

`GET`

### URL

````

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Estructura de la Colección

```json
{
  "_id": {
    "$oid": "68503eeff07a29d941912e57"
  },
  "clientApp": "MXPi-Opl-Printer",
  "process": "TX007",
  "referenceID": "TX007_PRINT",
  "priority": 2,
  "messages": [
    "Transacción Fallida: Error en la carga del documento: HTTPConnectionPool(host='192.168.101.121', port=5000): Max retries exceeded with url: /api/ImpresionTickets/Impresion (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x000001B64CF946E0>, 'Connection to 192.168.101.121 timed out. (connect timeout=10)'))"
  ],
  "date": "2025-06-16T10:57:41-0500"
}
````

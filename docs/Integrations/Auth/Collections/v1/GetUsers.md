## Users

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
    "$oid": "67881a6872b71b7e220c9e17"
  },
  "username": "Daniel Llerena",
  "email": "daniel.llerena@kfc.com.ec",
  "password": {
    "$binary": {
      "base64": "YOUR_REDIS_OR_AZURE_KEY_HERE",
      "subType": "00"
    }
  }
}
```

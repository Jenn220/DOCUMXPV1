## Validar Respuesta de Captcha

### Método HTTP

`GET`

### URL

```
{{server_pwa}}/YOUR_REDIS_OR_AZURE_KEY_HERE
```

### Parámetros de Query

| Key        | Value              | Descripción                        |
| ---------- | ------------------ | ---------------------------------- |
| token      | captcha_token_here | Token del captcha a validar        |
| isVersion3 | true               | Indica si es versión 3 del captcha |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

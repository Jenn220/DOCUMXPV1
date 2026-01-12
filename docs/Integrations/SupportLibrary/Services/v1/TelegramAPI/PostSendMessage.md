## Enviar Mensaje a Telegram

### Método HTTP

`POST`

### URL

```
https://api.telegram.org/bot{{TELEGRAM_BOT_TOKEN}}/sendMessage
```

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)

````json
{
  "chat_id": "6590911745",
  "text": "🚨 *Exception Report* 🚨\n\n**📱 Application**: `opl.printer`\n\n**🔄 Process**: `FACTURA_PINT`\n\n**🔢 Reference ID**: `212121-878787-455445-454`\n\n**⚠️ Priority**: `1`\n\n**💬 Messages**:\n```\n- es obligatorio la facturacion\n- la impresora no responde\n- falta papel\n```\n**📅 Date**: `2025-12-10T15:30:45.123Z`\n\n---\n",
  "parse_mode": "Markdown"
}
````

### Descripción del Cuerpo de la Solicitud

| Campo        | Tipo   | Descripción                                        |
| ------------ | ------ | -------------------------------------------------- |
| `chat_id`    | string | Identificador único del chat o usuario de Telegram |
| `text`       | string | Contenido del mensaje a enviar                     |
| `parse_mode` | string | Modo de análisis del texto (Markdown, HTML, etc.)  |

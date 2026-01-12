## Calcular Factura

### Método HTTP

`POST`

### URL
```
{{server_invoice_calculator}}/Calculator/api/v1/calculator/calculate_invoice/:country
```

### Parámetros de Ruta (Path Variables)

| Key     | Value | Descripción             |
| ------- | ----- | ----------------------- |
| country | 1     | Country ID (número)     |

### Parámetros de Query

No requiere parámetros de query.

### Cuerpo de la Solicitud (raw - JSON)
```json
{
    "currency_code": "USD",
    "default_franchise_tax": {
        "tax_name": "IVA 15 %",
        "value": 15
    },
    "discounts": [
        {
            "discount": 10,
            "is_percentage": true
        }
    ],
    "items": [
        {
            "id": "uirewyuriyewiruyewruiew",
            "pvp": 300,
            "quantity": 1,
            "taxes": [
                {
                    "tax_name": "IVA 15 %",
                    "value": 15
                },
                {
                    "tax_name": "IVA 10 %",
                    "value": 10
                }
            ],
            "discounts": [
                {
                    "discount": 10,
                    "is_percentage": true
                }
            ]
        },
        {
            "pvp": 200,
            "quantity": 3,
            "taxes": [
                {
                    "tax_name": "IVA 17 %",
                    "value": 17
                }
            ],
            "discounts": []
        }
    ],
    "decimal_quantity_presentation": 2,
    "decimal_quantity": 6
}
```

### Descripción del Cuerpo de la Solicitud

| Campo                             | Tipo    | Descripción                                      |
| --------------------------------- | ------- | ------------------------------------------------ |
| `currency_code`                   | string  | Código de la moneda                              |
| `default_franchise_tax`           | object  | Impuesto de franquicia por defecto               |
| `default_franchise_tax.tax_name`  | string  | Nombre del impuesto                              |
| `default_franchise_tax.value`     | number  | Valor del impuesto                               |
| `discounts`                       | array   | Lista de descuentos aplicables                   |
| `discounts[].discount`            | number  | Valor del descuento                              |
| `discounts[].is_percentage`       | boolean | Indica si el descuento es porcentual             |
| `items`                           | array   | Lista de items de la factura                     |
| `items[].id`                      | string  | ID de referencia para respuesta                  |
| `items[].pvp`                     | number  | Precio de venta al público                       |
| `items[].quantity`                | number  | Cantidad del item                                |
| `items[].taxes`                   | array   | Lista de impuestos aplicables al item            |
| `items[].taxes[].tax_name`        | string  | Nombre del impuesto                              |
| `items[].taxes[].value`           | number  | Valor del impuesto                               |
| `items[].discounts`               | array   | Lista de descuentos aplicables al item           |
| `items[].discounts[].discount`    | number  | Valor del descuento                              |
| `items[].discounts[].is_percentage` | boolean | Indica si el descuento es porcentual           |
| `decimal_quantity_presentation`   | number  | Cantidad de decimales para presentación          |
| `decimal_quantity`                | number  | Cantidad de decimales para cálculos              |
s
### Respuestas del Servidor

**200 OK - Consulta Exitosa**
```json
{
    "items": [
        {
            "id": "uirewyuriyewiruyewruiew",
            "currency_code": "USD",
            "subtotal_without_taxes": 5.65,
            "discount_percentage": null,
            "discounts_value": 0,
            "subtotal_include_discounts": 5.65,
            "tax_value": 0.85,
            "total": 6.5,
            "taxes": [
                {
                    "tax_name": "IVA 10 %",
                    "tax_code": "iva23313",
                    "tax_percentage": 10,
                    "total_tax_vulue": 4.99,
                    "base_amount": 130
                }
            ]
        }
    ],
    "total": {
        "currency_code": "USD",
        "subtotal_without_taxes": 5.65,
        "discount_percentage": null,
        "discounts_value": 0,
        "subtotal_include_discounts": 5.65,
        "tax_value": 0.85,
        "total": 6.5,
        "total_before_sale": 6.5,
        "suggested_price": 0,
        "taxes": [
            {
                "tax_name": "IVA 10 %",
                "tax_code": "iva23313",
                "tax_percentage": 10,
                "total_tax_vulue": 4.99,
                "base_amount": 130
            }
        ]
    }
}
```
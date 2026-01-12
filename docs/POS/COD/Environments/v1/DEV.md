## Configuración del Entorno de Desarrollo

### Tipo de Configuración

Variables de entorno y configuración de aplicación

---

### Logging

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "System": "Warning",
      "Microsoft.AspNetCore": "Warning",
      "System.Net.Http.HttpClient": "Warning"
    }
  }
}
```

### Hosts Permitidos

```json
{
  "AllowedHosts": "*"
}
```

### Serilog

```json
{
  "Serilog": {
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft": "Warning",
        "Microsoft.Hosting.Lifetime": "Information"
      }
    },
    "Enrich": ["FromLogContext", "WithThreadId"],
    "WriteTo": [
      {
        "Name": "Console"
      },
      {
        "Name": "Seq",
        "Args": {
          "serverUrl": "http://localhost:5341"
        }
      }
    ]
  }
}
```

---

## Checklist de Configuración

- [ ] Verificar niveles de logging configurados
- [ ] Validar configuración de Serilog
- [ ] Configurar URL del servidor Seq
- [ ] Verificar enriquecedores de logs
- [ ] Validar destinos de escritura de logs

# Endpoint: Crear Adaptador

## Método HTTP

`POST`

## URL

```
{{server_orchestrator}}/api/v1/adapters/create
```

## Cuerpo de la Solicitud (raw - JSON)

```json
{
  "name": "mongo",
  "typeAdapaterId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
  "version": "8.0",
  "statusId": "676f8b52-09d0-4bb5-94ef-d854b4a26fd3"
}
```

## Descripción de Campos

| Campo            | Tipo   | Restricciones                                                                      | Descripción                            |
| ---------------- | ------ | ---------------------------------------------------------------------------------- | -------------------------------------- |
| `name`           | string | -                                                                                  | Nombre del adaptador                   |
| `typeAdapaterId` | string | Máximo: 100 caracteres<br/>Valores permitidos: `FILE`, `BD`, `API_REST`, `API_SOAP` | Identificador del tipo de adaptador    |
| `version`        | string | varchar(12)                                                                        | Versión del adaptador                  |
| `statusId`       | string | -                                                                                  | Identificador del estado del adaptador |

## Notas

- El campo `typeAdapaterId` solo acepta los siguientes valores:
  - `FILE`
  - `BD`
  - `API_REST`
  - `API_SOAP`
- La versión tiene un límite de 12 caracteres

## Respuestas del Servidor

### 200 OK - Creación Exitosa

```json
{
  "code": 10,
  "messages": ["created succefully"],
  "data": {
    "id": "1829da9e-fbbe-4a3b-d24a-3360b5bf6c08",
    "code": "A001",
    "name": "mongo",
    "typeAdapaterId": "69503d8f-fa70-2196-f0a0-e3a85fa10aec",
    "statusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

#### Descripción de la Respuesta Exitosa

| Campo                 | Descripción                              |
| --------------------- | ---------------------------------------- |
| `code`                | Código de respuesta interno (10 = éxito) |
| `messages`            | Lista de mensajes informativos           |
| `data.id`             | ID único generado para el adaptador      |
| `data.code`           | Código del adaptador                     |
| `data.name`           | Nombre del adaptador                     |
| `data.typeAdapaterId` | ID del tipo de adaptador                 |
| `data.statusId`       | ID del estado del adaptador              |

### 404 Not Found - Error

```json
{
  "error": {
    "name": "mockNotFoundError",
    "header": "Unable to find mock",
    "message": "Please refresh and try again."
  }
}
```

#### Descripción del Error

| Campo           | Descripción                      |
| --------------- | -------------------------------- |
| `error.name`    | Nombre del error                 |
| `error.header`  | Encabezado descriptivo del error |
| `error.message` | Mensaje de ayuda para el usuario |

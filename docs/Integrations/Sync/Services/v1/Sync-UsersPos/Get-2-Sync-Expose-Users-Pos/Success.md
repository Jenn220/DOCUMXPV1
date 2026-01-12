## Obtener Usuarios POS

### Método HTTP

`GET`

### URL

```
{{server_pub}}/api/users_pos
```

### Autenticación

| Tipo          | Token                            |
| ------------- | -------------------------------- |
| Authorization | `yyyyyyiyiyiyiiiiyiyiyiyiyiy...` |

### Parámetros de Query

| Key           | Value                                | Descripción                    |
| ------------- | ------------------------------------ | ------------------------------ |
| cdn_id        | bc2d8ada-e25e-1bb7-55fe-32d1205ac4af | Identificador de la franquicia |
| restaurant_id | e17d03da-b8b6-f424-febc-3a767b6401bb | Identificador del restaurante  |

### Cuerpo de la Solicitud

No requiere cuerpo en la solicitud.

### Respuestas del Servidor

#### 200 OK - Consulta Exitosa

```json
{
  "code": 200,
  "status": "success",
  "message": "Data retrieved successfully",
  "details": [
    {
      "user": {
        "uuid": "f9675801-d657-49f2-a4d4-c22ae456c9f3",
        "first_name": "Carlos",
        "last_name": "Zambrano",
        "email": "carlos.zambrano@kfc.com.ec",
        "phone": "123456789",
        "address": "Fake Street 123",
        "birth_date": "1990-01-01",
        "user": "carlos.zambrano",
        "password": "sdasdasDE3RFeqfergwerbwwerwee"
      },
      "roles_profiles_franchise": [
        {
          "uuid": "550e8400-e29b-41d4-a716-446655440001",
          "role_name": "Administrador",
          "profiles": [
            {
              "profile_uuid": "550e8400-e29b-41d4-a716-446655440001",
              "profile_name": "Administrator",
              "franchises": [
                {
                  "uuid": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
                  "franchise_name": "GUS Franchise",
                  "country_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
                  "country": "Ecuador",
                  "restaurants": [
                    {
                      "uuid": "e17d03da-b8b6-f424-febc-3a767b6401bb",
                      "restaurant_name": "G001",
                      "address": "Direccion Restaurante Gus",
                      "phone": "987654321",
                      "city": "0fb70b94-ff83-4587-bcac-fcea5e719b5d"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "user": {
        "uuid": "f9675801-d657-49f2-a4d4-c22ae456c9f3",
        "first_name": "Daniel",
        "last_name": "Llerena",
        "email": "daniel.llerena@kfc.com.ec",
        "phone": "123456789",
        "address": "Fake Street 123",
        "birth_date": "1990-01-01",
        "user": "daniel.llerena",
        "password": "sdasdasDE3RFeqfergwerbwwerwee"
      },
      "roles_profiles_franchise": [
        {
          "uuid": "550e8400-e29b-41d4-a716-446655440001",
          "role_name": "mesero",
          "profiles": [
            {
              "profile_uuid": "550e8400-e29b-41d4-a716-446655440001",
              "profile_name": "mesero",
              "franchises": [
                {
                  "uuid": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
                  "franchise_name": "GUS Franchise",
                  "country_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
                  "country": "Ecuador",
                  "restaurants": [
                    {
                      "uuid": "e17d03da-b8b6-f424-febc-3a767b6401bb",
                      "restaurant_name": "G001",
                      "address": "Direccion Restaurante Gus",
                      "phone": "987654321",
                      "city": "0fb70b94-ff83-4587-bcac-fcea5e719b5d"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "user": {
        "uuid": "f9675801-d657-49f2-a4d4-c22ae456c9f3",
        "first_name": "Pepito",
        "last_name": "Pepito",
        "email": "pepito.pepito@kfc.com.ec",
        "phone": "123456789",
        "address": "Fake Street 123",
        "birth_date": "1990-01-01",
        "user": "pepito.pepito",
        "password": "sdasdasDE3RFeqfergwerbwwerwee"
      },
      "roles_profiles_franchise": [
        {
          "uuid": "550e8400-e29b-41d4-a716-446655440001",
          "role_name": "Cajero",
          "profiles": [
            {
              "profile_uuid": "550e8400-e29b-41d4-a716-446655440001",
              "profile_name": "Cajero",
              "franchises": [
                {
                  "uuid": "bc2d8ada-e25e-1bb7-55fe-32d1205ac4af",
                  "franchise_name": "GUS Franchise",
                  "country_id": "d6cac83d-6ce5-f62e-2628-1e2e9ae7b51f",
                  "country": "Ecuador",
                  "restaurants": [
                    {
                      "uuid": "e17d03da-b8b6-f424-febc-3a767b6401bb",
                      "restaurant_name": "G001",
                      "address": "Direccion Restaurante Gus",
                      "phone": "987654321",
                      "city": "0fb70b94-ff83-4587-bcac-fcea5e719b5d"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

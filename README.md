# PictogramCollector (mediafranca)

## Visión General

**PictogramCollector** es una solución de recolección de datos ligera y gratuita alojada en la organización **mediafranca**. Utiliza la infraestructura nativa de GitHub para almacenar y servir un archivo JSON centralizado.

---

## 1. Acceso Público a los Datos

El archivo JSON centralizado se sirve públicamente a través de GitHub Pages o mediante el enlace Raw de GitHub.

**URL de GitHub Pages:**
`https://mediafranca.github.io/pictogram-collector/data.json`

**URL de GitHub Raw:**
`https://raw.githubusercontent.com/mediafranca/pictogram-collector/main/data.json`

---

## 2. API de Ingesta de Datos

### Requisitos Previos
Necesitas un **Token de Acceso Personal (PAT)** de GitHub con el permiso `public_repo`.

### Endpoint
`POST https://api.github.com/repos/mediafranca/pictogram-collector/dispatches`

### Ejemplo de Petición `curl`

```bash
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token TU_TOKEN_DE_ACCESO_PERSONAL" \
  -d '{
    "event_type": "append-row",
    "client_payload": {
      "nombre": "Pictograma Ejemplo",
      "descripcion": "Enviado a mediafranca",
      "timestamp": "2026-01-31"
    }
  }' \
  https://api.github.com/repos/mediafranca/pictogram-collector/dispatches
```

---

## 3. Ingesta Manual

1. Ve a la pestaña **Actions**.
2. Selecciona **Collect Data**.
3. Haz clic en **Run workflow** e ingresa el JSON en el campo `data`.

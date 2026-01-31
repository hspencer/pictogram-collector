# Pictogramas Seleccionados por la Comunidad (mediafranca)

## Contexto del Proyecto

**pictogram-colector** es el repositorio central de contribuciones para **Pictos.net**. 

Pictos.net es una aplicación web que permite a los usuarios crear y gestionar pictogramas de alta calidad con metadatos enriquecidos, almacenándolos localmente en el navegador. Para fomentar la colaboración y construir una biblioteca global curada, este repositorio actúa como el "Servidor de Recolección", donde los usuarios pueden enviar pictogramas seleccionados para formar parte de la **"Selección de la Comunidad"**.

---

## 1. Acceso a la Biblioteca Colaborativa

La colección completa se consolida automáticamente en un único archivo JSON con el formato oficial de Pictos.net (Graph Dump).

- **URL Pública (GitHub Pages):** [https://mediafranca.github.io/pictogram-collector/data.json](https://mediafranca.github.io/pictogram-collector/data.json)
- **URL Directa (GitHub Raw):** [https://raw.githubusercontent.com/mediafranca/pictogram-collector/main/data.json](https://raw.githubusercontent.com/mediafranca/pictogram-collector/main/data.json)

---

## 2. API de Contribución

Los desarrolladores o sistemas integrados pueden enviar nuevos pictogramas (filas individuales o bibliotecas completas) utilizando la API de GitHub.

### Requisitos
- Un **Personal Access Token (PAT)** de GitHub con permisos de escritura en este repositorio.

### Endpoint
`POST https://api.github.com/repos/mediafranca/pictogram-collector/dispatches`

### Estructura de la Petición
El sistema acepta tanto una única fila de pictograma como un objeto completo con múltiples filas. El proceso de automatización se encarga de:
1. Validar la estructura.
2. Evitar duplicados basados en el ID del pictograma.
3. Actualizar el timestamp global de la colección.

**Ejemplo de contribución vía `curl`:**

```bash
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token TU_TOKEN_DE_ACCESO" \
  -d '{
    "event_type": "append-row",
    "client_payload": {
      "id": "P_12345",
      "UTTERANCE": "una persona caminando bajo la lluvia",
      "status": "completed",
      "elements": [...],
      "prompt": "..."
    }
  }' \
  https://api.github.com/repos/mediafranca/pictogram-collector/dispatches
```

---

## 3. Funcionamiento Interno

Este repositorio utiliza **GitHub Actions** para procesar cada envío:
- **Evento**: `repository_dispatch` (vía API) o `workflow_dispatch` (manual).
- **Lógica**: Un script de Python (`scripts/append_data.py`) concatena las nuevas entradas al archivo `data.json`.
- **Persistencia**: El sistema realiza un commit automático con los cambios, manteniendo la biblioteca siempre actualizada.
- **Despliegue**: GitHub Pages sirve el archivo actualizado de forma estática y gratuita.

import json
import sys
import os
from datetime import datetime

def append_to_pictos_collection(new_data_str):
    file_path = 'data.json'
    
    try:
        # 1. Parsear el nuevo dato
        new_payload = json.loads(new_data_str)
        
        # 2. Cargar o inicializar el contenedor principal
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    main_data = json.load(f)
                except json.JSONDecodeError:
                    main_data = {}
        else:
            main_data = {}

        # 3. Asegurar estructura base de Pictos.net (Selección de la Comunidad)
        if not isinstance(main_data, dict) or "rows" not in main_data:
            main_data = {
                "version": "3.0.0",
                "type": "pictonet_graph_dump",
                "title": "Selección de la Comunidad - Pictos.net",
                "description": "Biblioteca colaborativa de pictogramas curados por la comunidad.",
                "rows": []
            }
        
        # Actualizar timestamp de la colección
        main_data["timestamp"] = datetime.utcnow().isoformat() + "Z"

        # 4. Extraer filas del payload
        if isinstance(new_payload, dict) and "rows" in new_payload:
            new_rows = new_payload["rows"]
        elif isinstance(new_payload, dict) and ("UTTERANCE" in new_payload or "id" in new_payload):
            new_rows = [new_payload]
        elif isinstance(new_payload, list):
            new_rows = new_payload
        else:
            print("Error: Formato de datos no reconocido.")
            sys.exit(1)

        # 5. Concatenar filas evitando duplicados por ID
        existing_ids = {row.get("id") for row in main_data["rows"] if isinstance(row, dict) and "id" in row}
        
        added_count = 0
        for row in new_rows:
            if not isinstance(row, dict): continue
            row_id = row.get("id")
            if row_id not in existing_ids:
                main_data["rows"].append(row)
                existing_ids.add(row_id)
                added_count += 1
        
        # 6. Guardar el JSON actualizado
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(main_data, f, indent=2, ensure_ascii=False)
            
        print(f"Proceso completado. Filas nuevas agregadas: {added_count}. Total en colección: {len(main_data['rows'])}")
        
    except Exception as e:
        print(f"Error crítico: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python append_data.py '<json_string>'")
        sys.exit(1)
    
    append_to_pictos_collection(sys.argv[1])

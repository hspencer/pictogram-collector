import json
import sys
import os

def append_to_json(new_data_str):
    file_path = 'data.json'
    
    try:
        # Cargar datos existentes
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        
        # Parsear nueva fila
        new_row = json.loads(new_data_str)
        
        # Agregar a la lista
        data.append(new_row)
        
        # Guardar de nuevo
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print("Fila agregada exitosamente.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python append_data.py '<json_string>'")
        sys.exit(1)
    
    append_to_json(sys.argv[1])

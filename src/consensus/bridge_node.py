import json
import os
import time

class BridgeNode:
    def __init__(self, storage_path=None):
        # Si no nos dan una ruta (como un pendrive), usamos la carpeta por defecto
        if storage_path is None:
            self.storage_path = "storage/dtn_buffer.json"
        else:
            self.storage_path = os.path.join(storage_path, "aether_dtn_buffer.json")
            
        self._ensure_storage()

    def _ensure_storage(self):
        """Crea la estructura de carpetas necesaria."""
        directory = os.path.dirname(self.storage_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump([], f)

    def save_packet(self, origin, payload, signature):
        """Guarda el mensaje firmado en el 'silo' de datos."""
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
        
        packet = {
            "id": len(data) + 1,
            "origin": origin,
            "payload": payload,
            "signature": signature,
            "arrival_time": time.time(),
            "status": "stored" # Listo para ser movido por radio o por pendrive
        }
        
        data.append(packet)
        
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return packet["id"]

# Instancia por defecto
node = BridgeNode()
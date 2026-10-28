import logging
import os

def inicializar_registros():
    # Obtenemos la ruta exacta de la carpeta del proyecto para guardar el log de forma segura
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo_log = os.path.join(ruta_carpeta, "logs.txt")
    
    # Esta función configura el sistema para guardar el historial de eventos en la carpeta local
    logging.basicConfig(
        filename=ruta_archivo_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    # Devolvemos el objeto listo para usarlo en los demás archivos
    return logging.getLogger("SoftwareFJ")
import os
import sys
import yt_dlp
import time

def get_download_folder():
    """Ottiene la cartella Download dell'utente in modo cross-platform."""
    return os.path.join(os.path.expanduser("~"), "Downloads")

def download_video(video_url):
    download_path = get_download_folder()
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Usa il titolo del video come nome file
        'format': 'best'  # Qualità massima disponibile
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info)  # Ottieni il nome del file scaricato

        # Imposta manualmente la data di modifica a quella attuale
        current_time = time.time()
        os.utime(filename, (current_time, current_time))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]  # URL passato da Unity
        download_video(video_url)
        print("Download completato!")
    else:
        print("Errore: nessun URL fornito.")

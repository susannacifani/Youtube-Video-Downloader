import os
import sys
import yt_dlp

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
        ydl.download([video_url])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]  # URL passato da Unity
        download_video(video_url)
        print("Download completato!")
    else:
        print("Errore: nessun URL fornito.")

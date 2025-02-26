using System.Collections;
using System.Diagnostics;
using System.IO;
using UnityEngine;
using TMPro;

public class PythonRunner : MonoBehaviour
{
    public TMP_InputField urlInput;
    public TMP_Text statusText;

    public void DownloadVideo()
    {
        string videoUrl = urlInput.text;
        if (string.IsNullOrEmpty(videoUrl))
        {
            statusText.text = "Enter a valid URL!";
            return;
        }

        // Mostra subito "Download in corso..."
        statusText.text = "Downloading...";

        StartCoroutine(RunPythonScript(videoUrl));
    }

    private IEnumerator RunPythonScript(string videoUrl)
    {
        yield return null; // Assicura che Unity aggiorni l'UI prima di iniziare il processo

        string pythonExe = Path.Combine(Application.streamingAssetsPath, "ytdownloader", "Scripts", "python.exe");
        string scriptPath = Path.Combine(Application.streamingAssetsPath, "main.py");

        ProcessStartInfo psi = new ProcessStartInfo
        {
            FileName = pythonExe,
            Arguments = $"\"{scriptPath}\" \"{videoUrl}\"",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using (Process process = new Process { StartInfo = psi })
        {
            process.Start();
            process.WaitForExit(); // Aspetta la fine del processo
        }

        // Una volta terminato, mostra "Download completato!"
        statusText.text = "Download completed!";
    }
}

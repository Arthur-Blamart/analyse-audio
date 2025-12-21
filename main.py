import os
import librosa
import numpy as np

from parser import save_to_json

fichier_audio = "assets/Darude.mp3"

y, sr = librosa.load(fichier_audio)

# Tempo (pulsation) et rythme
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
tempo = tempo.item() if hasattr(tempo, 'item') else float(tempo)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# 2. Tonalité
# Extraire le chroma (Graphe des harmoniques par note)
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
# Moyenner sur le temps pour obtenir le profil de tonalité
chroma_mean = np.mean(chroma, axis=1)
# Trouver la note dominante
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
key_index = np.argmax(chroma_mean)
key = notes[key_index]

# Afficher les résultats
print(f"Tonalité détectée: {key}")
print(f"Tempo (BPM): {tempo:.2f}")
print(f"Nombre de battements: {len(beat_frames)}")
print(f"Durée totale: {librosa.get_duration(y=y, sr=sr):.2f} secondes")
print(f"\nPremiers temps de battement (secondes): {beat_times[:10]}")


os.makedirs('resultat', exist_ok=True)

save_to_json('resultat/analyse_rythme.json',key, tempo, beat_times.tolist(), librosa.get_duration(y=y, sr=sr))
print(f"\Données sauvegardées dans: resultat/analyse_rythme.json")
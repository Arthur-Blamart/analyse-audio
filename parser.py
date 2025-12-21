import json

def save_to_json(filename, key, tempo, beat_times, duration):
    data = {
        "key": key,
        "tempo": tempo,
        "beat_times": beat_times,
        "duration": duration
    }
    with open(filename, 'w') as fic:
        json.dump(data, fic, indent=4)
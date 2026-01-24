import random
import subprocess
import time

def get_duration(path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "csv=p=0",
            path
        ],
        capture_output=True,
        text=True
    )
    return float(result.stdout.strip())


def play_random_clip(path, clip_length=5):
    duration = get_duration(path)

    if duration <= clip_length:
        raise ValueError("Clip longer than file")

    start = random.uniform(0, duration - clip_length)

    subprocess.run([
        "ffplay",
        "-ss", str(start),
        "-t", str(clip_length),
        "-nodisp",
        "-autoexit",
        "-hide_banner",
        "-loglevel", "error",
        "-stats",
        "-window_title", "DCI Quiz",
        path
    ])
    
def create_random_clip(path, clip_length=5):
    duration = get_duration(path)

    if duration <= clip_length:
        raise ValueError("Clip longer than file")

    start = random.uniform(0, duration - clip_length)
    return start

def play_clip(path, start, clip_length):
    subprocess.run([
        "ffplay",
        "-ss", str(start),
        "-t", str(clip_length),
        "-nodisp",
        "-autoexit",
        "-hide_banner",
        "-loglevel", "error",
        "-stats",
        "-window_title", "DCI Quiz",
        path
    ])

import random
import subprocess
import time

ffplay_process = None

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
    stop_audio()
    duration = get_duration(path)

    if duration <= clip_length:
        raise ValueError("Clip longer than file")

    start = random.uniform(0, duration - clip_length)

    global ffplay_process
    ffplay_process = subprocess.Popen([
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
    stop_audio()
    global ffplay_process
    ffplay_process = subprocess.Popen([
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

def stop_audio():
    global ffplay_process
    if ffplay_process is None:
        return
    if ffplay_process.poll() is None:
        ffplay_process.terminate()
        try:
            ffplay_process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            ffplay_process.kill()
    ffplay_process = None

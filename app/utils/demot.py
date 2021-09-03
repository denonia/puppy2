import io
import subprocess


def count_frames(file: str) -> int:
    cmd = (
        "ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 "
        + file
    )

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    return int(p.stdout.readline())


def create_demot(file_in: str, file_out: str, caption1: str, caption2: str) -> int:

    cmd = (
        "ffmpeg -y -i "
        + file_in
        + " -vf scale=424:328,pad=width=574:height=522:x=75:y=45,"
        + 'drawtext=fontfile=assets/times.ttf:text="'
        + caption1
        + '":fontcolor=white:fontsize=48:x=\(w-text_w\)/2:y=400,'
        + 'drawtext=fontfile=assets/times.ttf:text="'
        + caption2
        + '":fontcolor=white:fontsize=30:x=\(w-text_w\)/2:y=460,'
        + "drawbox=68:38:436:340:white@0.7:2 "
        + "-progress - "
        + file_out
    )

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
        if line.startswith("frame="):
            yield int(line[6:])

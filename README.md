# Drumless

Upload a song, get it back without the drums, then practise along with it.

[audio-separator](https://github.com/nomadkaraoke/python-audio-separator) (BS-RoFormer SW, 6 stems, CPU only) splits the song, and ffmpeg sums every
non-drum stem into a drumless track. The page plays the drumless track, the drums only, or the original, at 50–100 % speed
(pitch kept), with a whole-track repeat and a draggable loop section on a zoomable waveform. The loop is remembered per song. A manual click (start, end, BPM and number of beats: you set three, the fourth follows) can cover a drums-only intro.

## Run it

```bash
uv sync
DRUMLESS_DATA=./data uv run uvicorn drumless_web.app:app --port 8000
```

Needs `ffmpeg` on the PATH. The first track downloads the model into `$DRUMLESS_DATA/models`.

| Environment | Default | |
|---|---|---|
| `DRUMLESS_DATA` | `/data` | Where tracks (`tracks/<id>/`) and models live |
| `DRUMLESS_MODEL` | `BS-Roformer-SW.ckpt` | Any model audio-separator supports; the output stems are mixed by name |

## How it works

- `drumless_web/app.py`: the FastAPI app (upload, list, download, rename, cancel, delete, loop, click, peaks).
- `drumless_web/worker.py`: storage and the single separation worker. There is no database: each `tracks/<id>/` directory is the
  whole state (`meta.json`, the original, `no_drums.flac`, `drums.flac`, cached `peaks_*.bin`), so a restart just queues unfinished tracks again.
- `drumless_web/page.py`: the whole UI, one inline HTML page.
- Waveform peaks are one byte per 5 ms (`/api/tracks/<id>/peaks/<stem>`), computed by ffmpeg + numpy on first use and cached.

## Deployment

It ships as a container: build it with the `Dockerfile` (port 8000) and mount a volume at `/data` for tracks and models. CPU only:
separating a 4-minute song takes about half an hour and ~5 GiB of RAM with the default model, which scores about 14 dB drums SDR
(vs ~11 for htdemucs_ft) for ~1.7x the CPU time. Quality over speed: bleed in the drumless track is what you hear when playing along.

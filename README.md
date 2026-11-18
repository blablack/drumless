# Drumless

Upload a song, get it back without the drums, then practise along with it.

[audio-separator](https://github.com/nomadkaraoke/python-audio-separator) (BS-RoFormer SW, 6 stems, CPU only) splits the song, and ffmpeg sums every
non-drum stem into a drumless track. The page plays the drumless track, the drums only, or the original, at 50–100 % speed
(pitch kept), with a whole-track repeat and a draggable loop section on a zoomable waveform. Several named loops can be saved per song (the selected one is looped, drawn on the waveform with the others). A manual click (start, end, BPM and number of beats: you set three, the fourth follows) can cover a drums-only intro, with an optional count-in (beats of click before the music when you press play).

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

- `drumless_web/vendor/`: the bundled Signalsmith Stretch build (MIT, see its README). The page plays through WebAudio: the stem is decoded
  in the browser, played natively at 100% and through the stretcher below that, so the loop is gapless and the click shares the music's clock.
- `drumless_web/app.py`: the FastAPI app (upload, list, download, rename, cancel, delete, loops, click, peaks), plus a web app manifest and icon (`drumless_web/static/`) so a phone can install the page as an app.
- `drumless_web/worker.py`: storage and the single separation worker. There is no database: each `tracks/<id>/` directory is the
  whole state (`meta.json`, the original, `no_drums.flac`, `drums.flac`, cached `peaks_*.bin`), so a restart just queues unfinished tracks again.
- `drumless_web/page.py`: the whole UI, one inline HTML page.
- Waveform peaks are one byte per 5 ms (`/api/tracks/<id>/peaks/<stem>`), computed by ffmpeg + numpy on first use and cached.

## Deployment

It ships as a container: build it with the `Dockerfile` (port 8000) and mount a volume at `/data` for tracks and models. CPU only:
separating a 4-minute song takes about half an hour and ~5 GiB of RAM with the default model, which scores about 14 dB drums SDR
(vs ~11 for htdemucs_ft) for ~1.7x the CPU time. Quality over speed: bleed in the drumless track is what you hear when playing along.

## License

Drumless is free software under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0-or-later): if you run a modified
version for other people, including as a hosted service, you must offer them the source of your changes.

The separation models that audio-separator downloads are not part of this repository and carry their own licenses (some are
non-commercial): check the ones you use.

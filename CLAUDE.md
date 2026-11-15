# CLAUDE.md

Drumless: FastAPI app that splits an uploaded song into stems (audio-separator + ffmpeg) and plays them back for practising
(stem switch, slow-down, repeat, per-song draggable loop on a zoomable waveform). See README.md.

- The UI is a single inline page in `drumless_web/page.py` (raw string, no build step); there is no JS engine locally, so
  syntax-check it with `pip install esprima` or look at it in headless Firefox against a stub server.
- No database: `tracks/<id>/meta.json` plus the audio is the state. Edits from request handlers go through `worker.update_meta`
  (locked); the separation worker rewrites its own copy of meta while a track is processing, so endpoints refuse edits then (409).
- Quality over speed: the user drums along to the output, so hours per song is fine — do not trade separation quality for time.
- This repo is public and environment-agnostic: keep hostnames, registry addresses, node names, CI details and the like out of it.
  Build and deployment specifics live outside the repo.

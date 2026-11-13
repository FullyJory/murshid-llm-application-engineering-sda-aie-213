# Setup, saving, and recovery

## Required

- A browser, internet connection and a Google account able to use Colab.
- Python 3 runtime, CPU (no accelerator). Use the free option; no billing or API credentials are needed.
- Basic Python: strings, dictionaries, functions and indentation.
- One notebook saved in your own Drive. Name it `murshid_your_name.ipynb`.

There is **nothing to install**. Imports are standard-library modules: json, re, sys, time, uuid, pathlib, copy, zipfile. Data is included as Python literals; no remote dataset download or Drive mount is needed. The application itself uses no network calls.

## One notebook, four days

Start blank on Day 1. Add cells 1–3. On Day 2 append cells 4–6; on Day 3 append 7–10; on Day 4 append 11–14. The labeled boundaries in `labs/day*.py` tell you where to create a new code cell. Keep the code's indentation. Never create four independent notebooks for submission.

Before adding a new day, run all previous cells from the top. Save a daily backup of the same notebook (`day-1`, `day-2`, etc. in your Git history), not a different project. The reference notebook has the complete sequence for comparison/recovery.

## Troubleshooting

| Symptom | Action |
|---|---|
| `NameError` | Run prior cells in order; later cells depend on earlier definitions. |
| Indentation/Syntax error | Compare your cell to its source block; use spaces and preserve quotes. |
| Assertion fails | Read the expected result; undo your last change or inspect input, schema, tool or cache. Do not remove assertions. |
| Runtime disconnected | Reconnect, then rerun from cell 1 through your current day. |
| Output file disappeared | Runtime storage is temporary. Rerun to recreate; download outputs before disconnecting. |
| Colab cannot allocate a session | Wait and reconnect, or use local Python. Free-service availability is not guaranteed. |
| Different trace ID or time | Expected. Compare answers, codes and counts instead. |

The supplied complete sequence can be run repeatedly from the top: setup resets the client, records and cache. Running only a single later cell may preserve old state; use a full rerun for trustworthy results.

## Local fallback (one shared process)

From the repository directory:

```bash
python -c "from pathlib import Path; ns={}; [exec(Path(f'labs/day{d}.py').read_text(), ns) for d in range(1,5)]"
```

## Download before leaving

Use Colab's Files panel to download JSON files from `murshid_outputs/`. Day 4 also produces `murshid_submission.zip`. The ZIP contains JSON outputs, **not the notebook**; download the notebook separately using File → Download → Download .ipynb. Inspect all files before uploading to your own repository. Only synthetic data belongs in this project.

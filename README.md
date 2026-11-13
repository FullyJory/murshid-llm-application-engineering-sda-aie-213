# Murshid Mini · LLM Application Engineering

**Four days. One notebook. One cumulative project.**

Training program: **LLM Application Engineering · SDA-AIE-213**  
Instructor: **Meaad Al-Marri**  
Level: beginner to intermediate, with basic Python familiarity  
Daily schedule: 150 minutes training and activities, 30 minutes prayer breaks, 60 minutes lab. Prayer breaks follow local times.

Build a tiny fictional service assistant from scratch using Python's standard library. Learn how an application validates inputs, structures a ticket, calls a read-only tool, checks ownership, tests behavior, and safely caches public answers. Day 4 completes the same project started on Day 1; there is no separate capstone.

> **Honest scope:** `mode=mock`. FakeClient is a deterministic rule-based simulator, **not a language model**. There are no paid APIs, keys, packages, GPU requirements, model downloads, or real personal data. The prompt is a teaching artifact, not instructions executed by a model. This lab teaches application engineering, not model training, live LLM quality, or production security.

## Start here

1. Read [Setup and recovery](docs/setup.md).
2. Open [Google Colab](https://colab.research.google.com/) and create **one blank notebook** named `murshid_your_name.ipynb`.
3. Choose Python 3 with **CPU / no hardware accelerator**. No installation cell is needed.
4. Follow [Day 1](docs/day-1.md). Copy or type its labeled code cells in order from [day1.py](labs/day1.py), understand them, and run each one.
5. **Keep the same saved notebook for all four days.** Append Day 2, Day 3, and Day 4 cells below your previous cells. Do not start a new notebook each day.
6. Save your notebook to your own Google Drive. At the end of each day download a `.ipynb` backup and the JSON outputs from the Colab Files panel. On the next day reopen your saved copy, not a fresh reference copy.

The Colab notebook contains **code cells only**. All explanations, instructions, slide mappings and expected outcomes live here on GitHub. Code comments label days and cells; printed results appear beneath the code when run.

[Open reference in Colab](https://colab.research.google.com/github/almiyead-rgb/murshid-llm-application-engineering-sda-aie-213/blob/main/notebooks/murshid.ipynb) · [Complete reference notebook](notebooks/murshid.ipynb) · [Expected results](expected/README.md) · [Technical documentation](docs/technical.md) · [Dataset card](data/README.md) · [Submission and Git guidance](docs/git.md)

The complete reference notebook is for checking or recovery; do not run later days before building and explaining their components. To open it in Colab, use **File → Open notebook → GitHub** and paste this repository URL, then select `notebooks/murshid.ipynb` and save your own copy. This optional shortcut does not change the one-notebook rule.

## The four stages

| Day | Build in the same notebook | Cells | Expected milestone | Guide |
|---|---|---:|---|---|
| 1 | Dataset, FakeClient, `ask`, baseline validation | 1–3 | Three known answers; empty input does not call the mock | [Day 1](docs/day-1.md) |
| 2 | Structured ticket, validation, read-only status tool | 4–6 | Five scenarios; no unauthorized status disclosure or mutation | [Day 2](docs/day-2.md) |
| 3 | Versioned prompt, guards, pipeline, golden tests | 7–10 | 10/10 specified behavioral tests | [Day 3](docs/day-3.md) |
| 4 | Public exact cache, measurements, regression and export | 11–14 | 3→1 mock calls; hits `[false,true,true]`; complete report | [Day 4](docs/day-4.md) |

These are acceptance results for these fixed fixtures, not guarantees about arbitrary inputs. Trace IDs and execution times vary. No real API speed or money savings are claimed.

## Learning by building, not just running

For each labeled cell: read the day's GitHub explanation, type/copy the code into the next cell in your notebook, predict its output, run it, compare the result, and explain one decision to a partner. Try the small change in the daily guide and rerun tests. A working copied notebook alone is not evidence of understanding.

Basic variables, dictionaries, functions, and indentation are assumed. Helpers for timing, JSON saving, reference extraction and export are supplied to keep each lab within one hour. No framework or infrastructure setup is required.

## Local alternative and verification

Python 3.9+ is sufficient:

```bash
python -m unittest discover -s tests -v
```

To rebuild the reference notebook after editing lab scripts:

```bash
python tools/build_notebook.py
```

Run code sequentially in a fresh kernel/session. Four scripts share state; do not run Day 2 as a separate Python process without Day 1. See [setup](docs/setup.md) for a one-process local runner.

## Student repository requirements

Your final repository must include a clear project description, professional README with setup/use instructions, technical documentation, meaningful Git history, training-program attribution, your completed cumulative notebook and results. Use [the checklist](docs/git.md). Include the [SDAIA Academy GitHub account](https://github.com/SDAIAAcademy) where relevant. This course repository does not claim Academy endorsement or certification of the implementation.

Support high-quality Saudi technical projects voluntarily: star work you genuinely value, follow relevant accounts, contribute improvements, use issues/forks/pull requests constructively, and share outstanding projects. Social actions are **not graded or required to pass**.

# Video learning path

[Learning hub](../README.md) · [Setup](setup.md) · [Daily labs](../README.md#your-four-day-roadmap) · [Submission](git.md)

Use these resources **optionally, outside the daily one-hour lab**. Watch only what helps you, then follow the repository's current instructions. You do not need to finish a playlist to start the project. The lab guides, code and expected outputs are the source of truth for this course.

**Resource check:** links were checked through indexed YouTube information, not watched in full. Labels below describe their learning purpose, not necessarily the exact video title. Some recordings are older, and menus, sign-in screens and available features may differ. Videos are external resources, not course-owned material or an endorsement. If a video suggests paid APIs, keys, extra software, GPU runtimes or model downloads, skip those steps: **none are needed for Murshid Mini**.

## 1. Before Day 1: start from zero

Follow this order if the tools are new to you. Skip steps you already know.

| Step | Resource | What to do afterwards |
|---|---|---|
| 1 | [Create a GitHub account](https://www.youtube.com/watch?v=YxTrIlY4TR4) · older recording | Create or use your own account. Use the current official guide below if screens differ. Never share your password or recovery codes. |
| 2 | [Create a repository: official GitHub video](https://www.youtube.com/watch?v=-RZ03WHqkaY) | Create your own project repository with a clear name and a README. Review visibility before publishing. |
| 2, Arabic alternative | [Repository creation walkthrough in Arabic](https://www.youtube.com/watch?v=NZ4U9OZdtxk) | The same outcome as Step 2; watching both is unnecessary. |
| 3 | [Introduction to Google Colab](https://www.youtube.com/watch?v=ZdIyMWWGB4U) | Open a blank Python 3 notebook, connect a CPU runtime, add a code cell and run `print("Hello, Murshid!")`. Expected output: `Hello, Murshid!`. |
| 4 | [Save Colab work to Drive and GitHub: Arabic walkthrough](https://www.youtube.com/watch?v=h5oy_7IJ8Sg) | Save your working notebook in your own Drive. Reopen that **same notebook** on all four days. Follow [submission guidance](git.md) before uploading. |

**Current official references:** [Colab FAQ](https://research.google.com/colaboratory/faq.html) and [Getting started with your GitHub account](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account).

**Ready check:** you can find your saved notebook, run a cell and locate your own GitHub repository. Now open the [Day 1 lab](day-1.md), not a new tutorial project.

## 2. Day 1: understand the interface, then build

**Lab:** [Day 1 guide](day-1.md) · [Code: cells 1–3](../labs/day1.py) · [Expected baseline](../expected/baseline_results.json)

- [API concepts](https://www.youtube.com/watch?v=kG-fLp9BTRo): understand a request, response and interface. Relate this to `ask` and its response fields. **Do not register for a paid API.** `FakeClient` returns fixed synthetic answers locally.
- [Prompting concepts](https://www.youtube.com/watch?v=1c9iyoVIwDs): optional conceptual enrichment for Days 1 and 3. No prompting service or live model is required. The Day 3 prompt is a teaching artifact and is not executed by an LLM in this lab.

**Explain before leaving:** what goes into `ask`, what comes back, and why a deterministic mock is not a language model.

## 3. Day 2: structured data and tools

**Lab:** [Day 2 guide](day-2.md) · [Code: cells 4–6](../labs/day2.py) · [Expected scenarios](../expected/day2_results.json)

- [JSON concepts](https://www.youtube.com/watch?v=iiADhChRriM): understand objects, keys, values and data types. Compare JSON with the Python dictionaries in the lab. Python uses `True`/`False`; JSON uses `true`/`false`. Let `json.dump`/`json.dumps` perform conversion instead of pasting JSON literals into Python.

**Apply to your existing notebook:** validate the ticket fields, call the read-only lookup, and compare the five scenarios. A reference number alone must not grant access to another fictional user's record.

## 4. Day 3: guard inputs and evaluate behavior

**Lab:** [Day 3 guide](day-3.md) · [Code: cells 7–10](../labs/day3.py) · [Expected evaluation](../expected/day3_results.json)

- [Prompt injection concepts](https://www.youtube.com/watch?v=jrHRe9lSqqA): understand why untrusted input must not become trusted instructions. The lab's small keyword filter demonstrates a boundary, **not complete prompt-injection protection**.
- [LLM-as-a-judge concepts](https://www.youtube.com/watch?v=trfUBIDeI1Y): optional advanced context only. Murshid Mini uses deterministic assertions and ten golden cases. It does **not** call an LLM judge or measure real model quality.

**Apply to your existing notebook:** run the guard scenarios and explain the ten fixed test results. Passing these cases is useful evidence within the fixtures, not proof that all inputs are safe.

## 5. Day 4: caching, export and publish

**Lab:** [Day 4 guide](day-4.md) · [Code: cells 11–14](../labs/day4.py) · [Expected final report](../expected/final_report.json)

| Resource | Use it for | Important boundary |
|---|---|---|
| [Prompt caching concepts](https://www.youtube.com/watch?v=u57EnkQaUTY) | Optional comparison of caching ideas | Provider-side prompt caching reuses model computation. This lab instead implements a **local exact-response cache** for public FAQ answers. It does not implement provider prompt caching or prove real API cost savings. |
| [Download a Colab notebook](https://www.youtube.com/watch?v=KXr8w6IFtkg) | Export your own `.ipynb` | The project's generated ZIP contains JSON outputs, **not** the notebook. Download the notebook separately. |
| [How to upload files and folders to GitHub: official GitHub video](https://www.youtube.com/watch?v=tlu5e0TxSzo) | Upload the notebook, documentation and generated results | Review files for secrets and personal data first. Use meaningful commit messages. See [versioning and submission](git.md). |
| [Profile README](https://www.youtube.com/watch?v=T_PKBNImooA) | Optional personal portfolio extension after submission | A profile README is different from this project's required repository README. You do not need a profile README to finish the course. |

**Final check:** your one notebook contains all four days, the golden tests pass, repeated public questions show the expected cache behavior, and your repository explains the synthetic data, operation, limitations and training-program attribution. Verify the [submission checklist](git.md), including the [SDAIA Academy link](https://github.com/SDAIAAcademy), before sharing.

## If a video does not match your screen

1. Return to [Setup and recovery](setup.md) for the lab's required outcome.
2. Use the official references above for current account and Colab guidance.
3. Continue with the daily written guide; no video is a prerequisite for assessment.
4. Do not weaken tests, expose private data or add a paid dependency to follow a recording.

# Day 1 — Build a small, testable application

## Code to build today
Open [Day 1 code](../labs/day1.py). Copy/type each labeled block into its own new code cell in your original notebook (cells 1–3). Run in order. Explanations stay here; Colab contains code only. Compare [recorded outputs](../expected/README.md).

## What you are building
Today you create the first part of **Murshid**, a fictional service assistant. A `FakeClient` returns deliberately fixed answers. This is a free simulation of an LLM application's engineering boundaries, **not a live language model**, general language understanding, or a deployed government service.

By the end of Day 4, the same notebook will contain the complete project. There is no separate extra final project.

## Before you start
1. Sign in to Google Colab with an account permitted for your training.
2. Create **one new notebook** and name it `murshid.ipynb`. Save it in your Google Drive. This is your working notebook for **all four days**.
3. Select a Python 3 runtime with no hardware accelerator (CPU). Connect to the runtime.
4. Keep the GitHub day guide open beside Colab. Put the supplied Python code cells in Colab in their numbered order. Explanations and expected results stay in GitHub; Colab contains code cells and their outputs.
5. No paid plan, API key, package installation, GPU, model download, or Drive mounting is required. The project uses Python's standard library. Colab itself needs internet, and its free runtimes may disconnect.

The repository notebook at [`notebooks/murshid.ipynb`](../notebooks/murshid.ipynb) is a reference. Do not create a second working copy each day. Build each day's cells in the notebook you created above, then use the reference to check your work.

## Link to the slides
| Slides | What to apply |
|---|---|
| 1–6 | Distinguish a model from an application; define Murshid's boundaries. |
| 7–13 | Follow a fixed workflow, read a response, and build a mock client. |
| 15–16 | Record only useful technical information and check your understanding. |
| 17–20 | Build, compare outputs, test, and save the day's checkpoint. |

## 60-minute lab
| Time | Build from scratch in your notebook |
|---|---|
| 0–10 min | Create the notebook, connect to CPU, and run the standard-library environment cell. Read the small fixed-response dataset. |
| 10–20 min | Add the response dictionary and `FakeClient` from the Day 1 code in small cells. Explain the mapping in your own words. |
| 20–35 min | Add `ask`: validate input before calling the client; return the response contract with a trace ID and measured duration. |
| 35–45 min | Run the three questions below and the empty-input check. Compare the fields and answers. |
| 45–55 min | Run the checks, inspect `baseline_results.json`, and correct any mismatch. |
| 55–60 min | Save the notebook and download the results. Record a meaningful Day 1 Git commit. |

## The dataset
The first dataset is a tiny hand-written mapping between selected questions and responses. It teaches an interface contract without network calls. Matching a known question does not demonstrate reasoning. Unknown phrasings may produce clarification rather than an intelligent answer. The examples are fictional and contain no real application records or personal information.

## Expected results
The normal response has `trace_id`, `answer`, `model`, and `latency_ms`.

| Input | Expected answer |
|---|---|
| `كيف أتابع طلبي؟` | `يمكنك متابعة حالة طلبك باستخدام رقم المرجع.` |
| `How can I check my application status?` | `You can check your application status using its reference number.` |
| `ساعدني` | `ما الخدمة التي تحتاج مساعدة بشأنها؟` |

`model` must be `training-mock`. `trace_id` must be nonempty. `latency_ms` must be nonnegative. **Do not compare exact trace IDs or times**: they vary by run and are not model inference benchmarks. Empty text must be rejected before a client call. Other questions follow the documented fallback behavior, not general language understanding.

## Completion checklist
- [ ] I can explain each of the four response fields.
- [ ] The three supported examples match the reference answers.
- [ ] Empty input does not call the client.
- [ ] I saved `baseline_results.json` and my notebook.
- [ ] I can identify which part is simulated.

## Tomorrow
Reopen **this same notebook**, rerun Day 1 from the top if the runtime reset, and append Day 2 cells below it. Do not delete Day 1 or create a new daily notebook. The notebook is saved; runtime variables and generated files may not survive a disconnect.

## Explain one decision
Before committing, explain to a partner one input, its route, its expected result, and one limitation. Make one small documented change without removing or weakening tests.

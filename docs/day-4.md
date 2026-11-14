# Day 4 — Measure, cache, and finish the project

## Code to build today
Open [Day 4 code](../labs/day4.py). Copy/type each labeled block into its own new code cell in your original notebook (cells 11–14). Run in order. Explanations stay here; Colab contains code only. Compare [recorded outputs](../expected/README.md).

## Starting point and outcome
Reopen **the same `murshid.ipynb`** and run the earlier cells from the top. Today you add an exact-match cache for general service questions, measure behavior, rerun the regression suite, and export the finished project. The four daily stages together are the final project.

## Link to the slides
| Slides | What to apply |
|---|---|
| 1–6 | Distinguish measured Python time, mock call counts, and hypothetical cost. |
| 7–12 | Cache eligibility, versioned keys, invalidation, and a controlled comparison. |
| 13–16 | Integration, reporting, and peer review. |
| 17–20 | Add caching, compare reference results, rerun tests, and submit. |

## 60-minute lab
| Time | Action |
|---|---|
| 0–15 min | Restore prior state; add the general-question cache and counters without changing the ticket contract or authorization. |
| 15–30 min | Run the three-repeat experiment, version-change test, and status-query exclusion test. |
| 30–45 min | Rerun all ten Day 3 cases and Day 2 cases. Export results and complete your evaluation report. |
| 45–60 min | Demonstrate with a partner, save your notebook, and check your GitHub submission against the checklist. |

## Controlled cache experiment
Start with fresh counters and an empty cache for each comparison. Use **the same supported general service question three times**.

| Measurement | Without cache | With initially empty cache |
|---|---:|---:|
| Requests | 3 | 3 |
| Mock-client calls | 3 | 1 |
| Cache hits | 0 | 2 |
| Hit rate | 0% | 66.7% |

The cache-hit sequence is `false, true, true`. These are deterministic counts for this experiment, not a promised latency improvement or real financial saving.

## Required regression checks
1. **Version change:** change the prompt or guide version used by the cache key. The first request with the new key must have `cache_hit=false`.
2. **Status exclusion:** application-status requests must not enter the shared cache. `REF-1001` still returns `under_review` to its owner, `REF-9999` still returns `not_found`, and `REF-1002` still returns `access_denied` to `demo-user-1` without its actual status.
3. **Pipeline behavior:** the Day 3 suite still passes all ten cases. Cache tests are reported separately, not silently counted as part of those ten.
4. **Reproducibility:** after saving, restart the runtime and run all project cells from the top. Verify the outputs again. This catches hidden state or out-of-order execution.

## Your final report
Record:
- Mode: `mock`, with **zero external model API calls**.
- Test results and any failures, without hiding them.
- Measured Python execution time, with units; exact times vary.
- Cache experiment counts and hit rate.
- Hypothetical cost calculations clearly labeled as examples, not billed amounts.
- One limitation and one feasible future improvement.

No production deployment, paid API experiment, or extra model training is required.

## Final submission
Follow [the repository and Git checklist](git.md). Submit your own repository link with:
- the cumulative notebook you built from Day 1;
- a clear README and run instructions;
- synthetic-data documentation and technical documentation;
- generated results/evaluation evidence;
- daily meaningful version history and program attribution.

Save and download files before ending the Colab session. A saved notebook is persistent in Drive, but runtime files may disappear. Do not submit private data, credentials, or unrelated Drive files.

## Explain one decision
Before committing, explain to a partner one input, its route, its expected result, and one limitation. Make one small documented change without removing or weakening tests.


## Extra homework

Complete this optional practice **after today’s core lab**, in a **separate notebook**. Keep building the required four-day project in your original cumulative notebook; do not paste these extension cells into it.

### Day 4 homework: evaluate three real-model answers

**Your task:** complete Assignment B using the three synthetic FAQ paraphrases. Generate each answer, record actual token counts and inference time, calculate the keyword indicator, and review the meaning of every answer.

[Assignment instructions](../extensions/README.md#assignment-b--evaluate-three-real-model-faq-paraphrases) · [Solution notebook](../extensions/homework_evaluation.ipynb) · [Python code](../extensions/homework_evaluation.py) · [Full example output](../extensions/expected/evaluation_result.json) · [Video and practice](../extensions/VIDEOS.md#3-prepare-for-assignment-b-tokens-and-evaluation)

**How to run:** open the evaluation notebook as a separate Colab copy, select Python 3/CPU, and run its three cells in order. Use the [real-model setup](../extensions/README.md#colab-setup-real-model-notebooks). The notebook is self-contained: it loads its own model and does not require Day 1 extension variables. Packages and weights need internet; no paid inference API or key is required.

### What your run should show

Your report includes `mode: "real_local_model"`, `total: 3`, `external_inference_api_calls: 0`, and cases `E01`, `E02`, `E03`. The recorded example has:

| Case | Reference answer observation | Reference keyword indicator |
|---|---|---|
| E01 | `Use its reference number` | `true` |
| E02 | `Reference number` | `true` |
| E03 | `Use its reference number` | `true` |

The example report's `keyword_hits` is `3`. This counts answers containing both “reference” and “number”; it is **not semantic accuracy**. Keep your actual count even if it differs. Each case also includes input tokens, output tokens including special tokens, and `inference_seconds`. Generated text and timing may vary; inspect meaning instead of forcing identical text or timing.

Save `murshid_live_outputs/evaluation_result.json`. **A successful submission:** all three actual cases, their generation settings and measurements, plus your manual assessment of whether each answer is supported by the synthetic context. Include failures and explain one improvement. An incorrect generated answer is evaluation evidence, while a download/import exception is a setup failure; handle the latter with [troubleshooting](../extensions/README.md#if-something-fails).

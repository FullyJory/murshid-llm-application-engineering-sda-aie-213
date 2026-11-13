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

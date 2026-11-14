# Day 2 — Structured tickets and one read-only tool

## Code to build today
Open [Day 2 code](../labs/day2.py). Copy/type each labeled block into its own new code cell in your original notebook (cells 4–6). Run in order. Explanations stay here; Colab contains code only. Compare [recorded outputs](../expected/README.md).

## Starting point and outcome
Open the **same `murshid.ipynb`** you created on Day 1. Rerun the earlier cells in order. Append today's cells below them. Today you add a structured ticket, validation, and a local status lookup. You are extending your project, not starting another one.

The tool uses a synthetic dictionary, not a website, external database, or real Ministry system. No new packages or accounts are needed.

## Link to the slides
| Slides | What to apply |
|---|---|
| 1–8 | JSON, the ticket contract, type checks, and business rules. |
| 9–12 | A bounded read-only tool and its controlled call sequence. |
| 13–15 | Synthetic records, ownership checks, and an end-to-end trace. |
| 17–20 | Build the ticket/tool workflow and check the five reference cases. |

## Dataset explanation
Each fictional record has a reference such as `REF-1001`, an owner identifier such as `demo-user-1`, and a status. These are deliberately simple identifiers, not national IDs. The demo session supplies the user identity separately from the question. Never accept an owner claimed in a question as authentication.

- `REF-1001` belongs to the demo user used in the normal path and has status `under_review`.
- `REF-1002` belongs to a different demo user and exercises authorization refusal.
- `REF-9999` is deliberately absent and exercises missing-record handling.

Do not replace this dataset with real records, names, phone numbers, government identifiers, or secrets. The small dataset is for branch testing, not representative statistics.

## 60-minute lab
| Time | Action in the existing notebook |
|---|---|
| 0–10 min | Restore Day 1 state; read the synthetic records and the ticket fields. |
| 10–20 min | Add the ticket builder and provided reference-extraction helper. Trace one example manually. |
| 20–35 min | Add `validate_ticket` and the read-only `check_status` function. Check authorization before exposing a record status. |
| 35–45 min | Connect the workflow. Handle missing references and cancellation without calling the status tool. |
| 45–55 min | Run the five cases below and a Day 1 regression check; save `day2_results.json`. |
| 55–60 min | Save the same notebook and commit your Day 2 checkpoint. |

## Reference cases
| Question / session | Expected behavior |
|---|---|
| `ما حالة طلبي REF-1001 في الرياض؟`, `demo-user-1` | Ticket uses `application_status`, `Riyadh`, `REF-1001`, `needs_clarification=false`; lookup returns `under_review`. |
| `أريد حالة طلبي` | `request_id=null`, `needs_clarification=true`; answer `ما رقم مرجع الطلب؟`; zero status-tool calls. |
| `ما حالة REF-9999؟` | Lookup returns `not_found`. |
| `ألغ طلبي REF-1001` | Unsupported mutation is refused; zero status-tool calls; dataset is unchanged. |
| Status of `REF-1002`, `demo-user-1` | `access_denied`; no actual record status or other user's details are returned. |

A successful ticket for the first example is:

```json
{"service":"application_status","city":"Riyadh","request_id":"REF-1001","needs_clarification":false}
```

A successful tool result for that ticket is:

```json
{"request_id":"REF-1001","status":"under_review"}
```

These technical labels are for transparent classroom testing. A real service may need a generic response that does not reveal whether someone else's record exists. The demo's identity and authorization mechanisms are teaching fixtures, not production authentication.

## Completion checklist
- [ ] Every ticket is validated before the tool.
- [ ] Missing input and cancellation make zero tool calls.
- [ ] The ownership check does not reveal another user's status.
- [ ] The synthetic records remain unchanged.
- [ ] Day 1 questions still work.
- [ ] I saved the notebook and `day2_results.json` and described one issue I corrected.

Tomorrow, continue in this notebook by adding input/output checks and a small regression suite.

## Explain one decision
Before committing, explain to a partner one input, its route, its expected result, and one limitation. Make one small documented change without removing or weakening tests.


## Extra homework

Complete this optional practice **after today’s core lab**, in a **separate notebook**. Keep building the required four-day project in your original cumulative notebook; do not paste these extension cells into it.

### Day 2 homework: validate and dispatch tool calls

**Your task:** build the dispatcher described in Assignment A. Validate the call shape, allow only `check_status`, check ownership using the separate demo identity, and leave records unchanged. Predict each outcome before opening the solution.

[Assignment instructions](../extensions/README.md#assignment-a--validate-and-route-structured-tool-calls) · [Solution notebook](../extensions/homework_tools.ipynb) · [Python code](../extensions/homework_tools.py) · [Full expected output](../extensions/expected/tools_result.json) · [Video and practice](../extensions/VIDEOS.md#2-prepare-for-assignment-a-structured-calls)

**How to run:** open the separate solution notebook in Colab and run both code cells in order. Use Python 3/CPU; no packages, model download or API key are needed. Alternatively, from the repository directory run `python extensions/homework_tools.py`.

### What your run should show

The printed JSON reports `mode: "simulated_tool_protocol"`, `passed: 7`, `total: 7`, and `records_unchanged: true`. All seven case entries should have `passed: true`:

| Case | Input being checked | Exact result |
|---|---|---|
| 1 | Owned reference | `{"code": "ok", "status": "under_review"}` |
| 2 | Another user's reference | `{"code": "unavailable"}` |
| 3 | Absent reference | `{"code": "unavailable"}` |
| 4 | Disallowed tool | `{"code": "tool_not_allowed"}` |
| 5 | Unexpected owner argument | `{"code": "invalid_arguments"}` |
| 6 | Numeric reference instead of a string | `{"code": "invalid_arguments"}` |
| 7 | String instead of a call object | `{"code": "invalid_call"}` |

These outcomes are deterministic for the supplied inputs. Cases 2–7 are **correct refusals**, not runtime crashes. The call objects are supplied by hand; this exercise teaches Python dispatch and validation, not model-selected tools.

**A successful submission:** your separate notebook, the seven-case output, and an explanation of why validation and authorization are different. If an assertion fails, compare the case's actual dictionary with the table and fix your code without weakening the expected result.

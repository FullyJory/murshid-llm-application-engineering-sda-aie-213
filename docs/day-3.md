# Day 3 — Guardrails and a golden test set

## Code to build today
Open [Day 3 code](../labs/day3.py). Copy/type each labeled block into its own new code cell in your original notebook (cells 7–10). Run in order. Explanations stay here; Colab contains code only. Compare [recorded outputs](../expected/README.md).

## Starting point and outcome
Continue in your **original `murshid.ipynb`**. Run Days 1 and 2 in order first. Today you connect a controlled pipeline and test its behavior with ten deliberately chosen cases. There is still no live LLM, external API, package installation, or paid resource.

## Link to the slides
| Slides | What to apply |
|---|---|
| 1–6 | Pipeline stages, separation of decisions from wording, and a versioned response template. |
| 7–10 | Input checks, injection examples, data boundaries, and output validation. |
| 11–15 | Golden cases, property-based comparison, pass rate, and diagnosis. |
| 17–20 | Add checks, run ten cases, document results, and save the checkpoint. |

## Why these tests?
The synthetic cases intentionally exercise normal behavior and refusal paths. A correct refusal is a passing test. `100%` means the implementation passed these **ten selected mock cases**, not that it is generally safe or accurate. Keyword-based filters can miss attacks and can reject harmless input. Do not label them production security.

## 60-minute lab
| Time | Action |
|---|---|
| 0–15 min | Reopen and rerun your earlier notebook cells; append the Day 3 pipeline helpers and inspect the test cases. |
| 15–30 min | Add input/output checks and connect the pipeline. Run the complete suite. |
| 30–45 min | Compare each result with its expected behavior. Inspect a malformed-output example and explain why the validation rejects it. |
| 45–60 min | Record your results and one explained change, review with a partner, save the notebook, and commit the Day 3 checkpoint. |

## Expected results and comparison rules
The suite labels its cases `C01` through `C10`. Run the supplied suite rather than manually inventing a new numbering scheme.

The slide-defined anchors are:
- `C03`: authorized status lookup → `under_review`.
- `C04`: absent reference → `not_found`.
- `C05`: missing reference → clarification before any status-tool call.
- `C07`: another user's record → `access_denied`, with no private status returned.
- `C10`: deliberately malformed output → rejected by the output contract.

C01/C02 are the Arabic/English FAQs (`ok`); C06 is an unavailable visa-fee question (`out_of_scope`); C08 is an instruction override (`blocked_instruction`); C09 is blank (`invalid_input`). C10 returns `invalid_schema`. Results are saved in `day3_results.json`. Read each input and expectation before running it.

The completed reference implementation should report:

```text
passed=10
total=10
pass_rate=100%
mode=mock
```

Compare behavior and required fields, not transient IDs or exact elapsed time. A failure message should identify which case and expected behavior differed. Read it, fix the responsible function, and rerun the suite. Do not remove a failing case just to obtain a higher score.

## Completion checklist
- [ ] All ten cases are recorded with a pass/fail result.
- [ ] I can explain one successful answer, one clarification, and one correct refusal.
- [ ] Invalid output does not pass the schema check.
- [ ] I documented one change and what remains untested.
- [ ] My results clearly say `mode=mock`.
- [ ] I saved the notebook and generated test-results file before leaving Colab.

Tomorrow's work adds measurement and caching to **this same project**. Do not start a separate final-project notebook.

## Explain one decision
Before committing, explain to a partner one input, its route, its expected result, and one limitation. Make one small documented change without removing or weakening tests.


## Extra homework

Complete this optional practice **after today’s core lab**, in a **separate notebook**. Keep building the required four-day project in your original cumulative notebook; do not paste these extension cells into it.

### Day 3 homework: recognize a deliberate error and fix the input

**Your task:** predict the validation result for `None`, blank text, and text longer than 500 characters. Then supply a valid question and explain why a caught rejection can be a successful test.

[Error exercise instructions](../extensions/README.md#separate-input-error-practice) · [Solution notebook](../extensions/error_examples.ipynb) · [Python code](../extensions/error_examples.py) · [Full expected output](../extensions/expected/errors_result.json) · [Video and practice](../extensions/VIDEOS.md#4-recognize-and-correct-an-expected-error)

**How to run:** open the separate error notebook in Colab and run its code cell. Python 3/CPU and the standard library are enough. Alternatively, run `python extensions/error_examples.py` from the repository directory.

### What your run should show

| Input | Exact caught error type and message | Your correction |
|---|---|---|
| `None` | `ValueError: Enter a non-empty question string.` | Use a question string |
| Blank spaces | `ValueError: Enter a non-empty question string.` | Enter a nonblank question |
| 501 characters | `ValueError: Use at most 500 characters.` | Shorten to at most 500 characters |

The JSON contains three `intentional_caught_errors`, each with `expected_rejection: true`, followed by:

```json
{
  "corrected_input": "accepted",
  "checks": "passed"
}
```

This final snippet is an excerpt from the full report. The example catches the errors, so the successful run prints JSON rather than an unhandled traceback. These messages and outcomes are deterministic. `ModuleNotFoundError`, an interrupted runtime or a failed assertion is a different situation; use the [troubleshooting guide](../extensions/README.md#if-something-fails).

**A successful submission:** the three observed rejections, your corrected valid input, and a short explanation of `raise`, `try` and `except`. This is a separate validation exercise; it does not silently change the functions in your other notebooks.


### Save, upload, and submit your work

- **Core lab:** save today's changes in your original cumulative project notebook. Update `notebooks/murshid.ipynb` in your own GitHub repository; do not create a new core project each day.
- **This homework:** use its own Colab notebook and choose **File → Save a copy in Drive**. A suggested name is `day3_errors_your_name.ipynb`. Keep it separate from the core notebook and other homework.
- Run and save your work, then choose **File → Download → Download .ipynb**. Upload the downloaded homework to `homework/day3_errors.ipynb` in your own repository. Include generated reports where available; keep printed results in your saved notebook.
- Follow the [step-by-step upload and submission guide](git.md#upload-everything-to-your-own-github-repository). Check filenames, outputs and privacy before committing.
- Submit your **own repository's root link** to the instructor through her specified channel, after checking that she can open it. Keep the same repository link for later updates. See [the final access checklist](git.md#submit-your-repository-link-to-the-instructor).

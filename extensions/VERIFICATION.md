# Check your extension work

Use this checklist after running your **own separate extension notebooks**. A reference output helps you compare; it does not replace executing your copy.

[Extension guide](README.md) · [Learning roadmap](OBJECTIVES.md) · [Video path](VIDEOS.md)

## Before you run

- [ ] I saved my original cumulative Murshid notebook and its results.
- [ ] I opened the extension in a separate notebook and optional runtime.
- [ ] I selected Python 3 on CPU and followed the supplied setup cell.
- [ ] I allowed time and disk space for packages and model weights in the real-model activities.
- [ ] If a restart was requested, I restarted the optional runtime and ran all cells from the beginning.
- [ ] I used only the supplied synthetic questions and records, not personal information or secrets.

Assignment A and the error exercise use the standard library only. The real-model demo and evaluation download FLAN-T5 small and install their dependencies. No paid inference API or API key is needed. Save results before a Colab runtime disconnects.

## Real-model demo

Open [the notebook](live_model_demo.ipynb), then compare with [the demo result](expected/live_demo_result.json).

- [ ] Model loading completed before I ran generation.
- [ ] I can identify the input, generated answer, and model information in my report.
- [ ] I read the answer and explained whether it answers the question.
- [ ] I saved the actual answer rather than rewriting it to match the reference.

An incorrect answer is a model-quality observation. A download exception is an environment failure. Treat them differently when explaining what happened.

## Tool assignment

Run [Assignment A](homework_tools.ipynb) and compare with [the tool results](expected/tools_result.json).

- [ ] The seven supplied cases report their intended outcomes.
- [ ] Valid calls reach only the allowed read-only tool.
- [ ] Invalid calls and arguments are rejected.
- [ ] Unauthorized callers cannot see another user's record status.
- [ ] The synthetic records are unchanged after the tests.

These labels are **expected application results**, not crashes:

| Result | What it means | Correct response |
|---|---|---|
| `invalid_call` | The call structure is invalid. | Correct the structure or retain the rejection in a negative test. |
| `invalid_arguments` | An argument fails validation. | Fix the field, type, or value; keep the validation rule. |
| `tool_not_allowed` | The tool is not on the allowlist. | Use the supported tool; do not bypass the allowlist. |
| `unavailable` | No usable record can be disclosed to this caller. | Check the fictional reference and identity without exposing someone else's record. |

## Input-error practice

Run [the error notebook](error_examples.ipynb) and compare with [the error results](expected/errors_result.json).

| Input | Expected result |
|---|---|
| `None` | Caught `ValueError`: `Enter a non-empty question string.` |
| Blank text | Caught `ValueError`: `Enter a non-empty question string.` |
| More than 500 characters | Caught `ValueError`: `Use at most 500 characters.` |
| Corrected nonblank question of at most 500 characters | Accepted without a validation error. |

- [ ] I saw all three intentional error cases and the corrected accepted input.
- [ ] I can explain why catching an expected exception keeps the exercise running.
- [ ] I understand that this is a separate validation example, not an automatic change to every model function.

## Real-model evaluation

Run [Assignment B](homework_evaluation.ipynb) and compare with [the evaluation report](expected/evaluation_result.json).

- [ ] My report includes `E01`, `E02`, and `E03`.
- [ ] Every case retains its question, answer, actual token counts, and measured time.
- [ ] I recorded the model and generation settings.
- [ ] I inspected the answers as well as the keyword-check score.
- [ ] I explained one answer difference or one limitation of the three-case sample.

The reference records **3/3 keyword hits**. That is not “100% semantic accuracy.” Do not change your answers to reproduce that score. Compare required fields and the measurement method; exact wording, timing, and counts may differ.

## Troubleshoot before asking for help

| Symptom | Next step |
|---|---|
| A name is undefined | Run preceding cells in order; a restarted runtime has lost its variables. |
| `ModuleNotFoundError` | Check that setup finished in this optional runtime; follow any restart prompt and run all cells again. |
| A dependency mismatch | Use a fresh optional runtime and its supplied setup. Do not modify the core notebook to fix extension dependencies. |
| `OSError` or model download/loading failure | Check the connection and model-host availability. Preserve the error text and retry when the underlying issue is resolved. |
| Runtime disconnects or memory is exhausted | Save what you can, reconnect to an available CPU runtime, and rerun setup. |
| An answer is wrong | Keep it in the report and explain the model's mistake. |

Exception wording may differ by software version. If you need help, share the failing cell, error message, and last successful step, with private details removed.

## Save your checkpoint

- [ ] I saved each extension notebook under its own filename.
- [ ] I downloaded generated JSON reports before ending the session.
- [ ] My repository contains my actual results, a short interpretation, and no secrets or private records.
- [ ] My original four-day project remains intact.

Explain your work to a partner using [the learning roadmap](OBJECTIVES.md). Keep these small demonstrations in their teaching context: synthetic identities are not production authentication, and a few test cases do not establish general security or model quality.

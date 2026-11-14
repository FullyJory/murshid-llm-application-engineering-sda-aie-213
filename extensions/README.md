# Optional extensions: a real model and two independent assignments

These extensions complement **LLM Application Engineering (SDA-AIE-213)**. They are separate from the four-day Murshid core project. The core remains a free, deterministic Python simulation with no model download. Nothing in this folder replaces or changes it.

**Do not add these cells to your cumulative `murshid.ipynb`.** Keep your original project and daily results. For an extension, open its own notebook and save a separate copy in Google Drive. Use a separate runtime, or disconnect the core runtime before beginning an extension so that package installation cannot affect your core session.

The extensions are optional practice **outside the one-hour daily lab**. They are not extra requirements for completing the original project. There is no additional grading weight defined here.

## Choose your activity

| Activity | What actually runs | Prerequisites | Files |
|---|---|---|---|
| Real-model demonstration | FLAN-T5 small generates text on CPU | Python basics; internet; model and package downloads | [Demo notebook](live_model_demo.ipynb) |
| Assignment A: controlled tools | Hand-written structured calls handled by Python validation and a read-only tool | Core Day 2; standard library only | [Solution notebook](homework_tools.ipynb), [Python solution](homework_tools.py) |
| Input-error practice | Caught Python validation errors and a corrected input | Standard library only | [Practice notebook](error_examples.ipynb), [Python solution](error_examples.py) |
| Assignment B: small evaluation | FLAN-T5 small generates answers to three synthetic FAQ paraphrases; code records tokens and time | Demo; core Days 3–4 | [Solution notebook](homework_evaluation.ipynb), [Python solution](homework_evaluation.py) |

The real-model examples do not require a paid API or API key. They **do require downloading model weights and Python packages**. A free Colab CPU runtime is the intended environment, but availability, download speed, memory, and execution time depend on the service and your session. This is not a promise of unlimited free resources or error-free execution.

## Colab setup: real-model notebooks

1. Finish saving your core notebook and export its results first.
2. Open Google Colab, select **File → Open notebook → GitHub**, and paste this repository's GitHub URL. Select `extensions/live_model_demo.ipynb` or `extensions/homework_evaluation.ipynb`. Alternatively, download the chosen notebook from GitHub and upload it through Colab's notebook picker.
3. Save a **new copy** in Drive with a distinctive name, such as `murshid_optional_live_demo.ipynb`. Do not overwrite `murshid.ipynb`.
4. Select a Python 3 runtime and CPU/no hardware accelerator. GPU is not required.
5. Run the notebook's first installation/setup cell exactly as supplied. It preserves an existing PyTorch installation, installs `torch==2.6.0` from the official CPU package source only if PyTorch is absent, and installs `transformers==4.49.0` and `sentencepiece==0.2.0`. Preserving Colab's existing PyTorch avoids independently downgrading it away from matching companion packages. Do not install a guessed list or upgrade packages independently.
6. If Colab explicitly requests a runtime restart after installation, restart the optional runtime, then choose **Run all from the first cell** to restore imports, variables, and setup. If a runtime was disconnected or replaced, rerun setup before loading the model.
7. Run the remaining code cells in order. The model-loading cell downloads **`google/flan-t5-small`** from Hugging Face on first use. It is not a hosted inference request. Do not provide personal data, service records, or secrets.
8. Wait for model loading to finish before generating. Save the notebook and download any generated results from Colab's Files panel before ending the session.

The code was tested locally with PyTorch 2.6.0; that is not a claim that this exact notebook was executed in a hosted Colab session. If you encounter a dependency mismatch, reset or replace the **optional** runtime and rerun its setup rather than altering your core notebook.

The notebooks contain code and outputs; this guide contains the instructions and interpretation. Read the comments in each code cell before running it. Do not paste shell commands into a Python cell unless the provided notebook uses the appropriate notebook syntax.

## Colab setup: Assignment A

Open `extensions/homework_tools.ipynb` using the same GitHub notebook picker and save a separate Drive copy. Use Python 3 on CPU. This assignment uses only Python's standard library: **no pip installation, model weights, API, or authentication setup is needed**. Run cells in order. The source file is also provided for inspection and ordinary Python execution.

## Demonstration: watch a real model generate

Use [the demonstration notebook](live_model_demo.ipynb) and inspect [the recorded demo result](expected/live_demo_result.json). Compare what you observe with the core's `FakeClient`:

- In the core, answers come from a hand-written mapping. In this demo, downloaded model weights produce output tokens.
- A model response can be incomplete, incorrect, or inconsistent with an instruction. Read it rather than assuming it is correct because it was generated successfully.
- The application still needs clear inputs, bounded behavior, output checks, and evaluation. A real model does not replace those engineering controls.
- A small English-language example is not evidence of strong Arabic service performance or suitability for government deployment.

Explain to a partner which code loads the model, which part builds its input, and which part decodes the generated output. Describe one difference between the generated answer and a fixed mock answer. A run that produces an imperfect answer can still be a useful demonstration.

## Assignment A — Validate and route structured tool calls

### Your task, before reading the solution

Build a small dispatcher around one read-only application-status tool. Use fictional records and synthetic demo users. Treat the structured call as **untrusted input**, even when it is written in JSON.

1. Define the accepted call structure and validate its required fields and types.
2. Use an explicit allowlist of permitted tool names. Reject unknown or mutation-oriented tools.
3. Validate the reference argument before invoking the tool.
4. Supply the demo identity separately from the call. Do not let a user-provided owner field grant permission.
5. Check record ownership and return no private record status for an unauthorized user.
6. Test a valid call, malformed arguments, an unknown tool, a missing record, and a record owned by someone else.
7. Confirm that the records are unchanged after the complete test run.

### What to submit

Your separate notebook or Python file, the test output, and a short explanation of why validation and authorization are different. Identify the demo's limitations: synthetic identity is not real authentication, and this is not native function calling by a hosted model provider.

### Solution and expected results

After attempting the task, inspect [the Python solution](homework_tools.py) or [solution notebook](homework_tools.ipynb), then compare with [the recorded tool results](expected/tools_result.json). Match documented status/validation behavior and test outcomes. Do not substitute the solution's recorded run for your own execution.

**This assignment is simulated structured tool calling.** The model does not select the tool, and no external system is changed. It teaches a boundary that a future real-model integration would still need.

## Assignment B — Evaluate three real-model FAQ paraphrases

### Your task, before reading the solution

Evaluate the real model on the supplied three synthetic FAQ paraphrases. This small exercise demonstrates measurement, not a benchmark.

1. Inspect each synthetic question and reference expectation. State what a correct answer would need to convey.
2. Load the same small model used by the solution; use the documented greedy generation settings rather than sampled generation.
3. Generate an answer for each input, preserving each input, output, and case identifier (`E01`, `E02`, `E03`) together in the report so that each case can be inspected.
4. Record actual tokenizer-based input/output token counts and measured execution time with units. Do not estimate tokens by word count.
5. Compare answers with the reference criteria and inspect disagreements manually. A simple automated score is not a substitute for semantic review.
6. Report all three cases, including failures, and state what the evaluation does **not** establish.

### What to submit

A separate notebook or Python file, its observed report, and a short interpretation. Include model identity, generation settings, environment information where available, and at least one limitation. State that external model API calls and billed API cost are zero; compute hypothetical API prices only if separately labeled as hypothetical.

### Solution and reference observations

Use [the Python solution](homework_evaluation.py) or [solution notebook](homework_evaluation.ipynb), then inspect [the recorded evaluation results](expected/evaluation_result.json). Recorded answers and metrics are observations from a specific run, **not guaranteed output targets**. Greedy decoding reduces sampling variation but does not guarantee identical text or timing across versions, devices, or environments.

Compare the report schema, case coverage, generation settings, and calculation method. Explain answer differences. Do not require a particular latency, pass rate, or token count merely because it appeared in one reference run. A three-case score does not measure general reasoning, Arabic competence, security, or production readiness.

## Correct rejection versus a runtime failure

A refusal can be the **correct expected result**. Assignment A returns structured dictionaries for deliberate invalid requests; it must not crash simply because a test request is invalid. Compare the full records in [tools_result.json](expected/tools_result.json).

| Label in the supplied tool results | Interpretation | What the learner should do |
|---|---|---|
| `invalid_call` | The call object does not satisfy the accepted call structure. | Inspect the object's structure and the validator; use the valid reference call. |
| `invalid_arguments` | Arguments fail the tool's required-field, type, or value checks. | Correct the arguments before dispatching; do not weaken validation to make the test pass. |
| `tool_not_allowed` | The requested tool is not on the allowlist. | Use the supported read-only tool; a deliberately forbidden call should stay rejected. |
| `unavailable` | The safe response does not expose a usable record to this caller. | Check the synthetic reference and demo identity. Do not bypass ownership checks or expose another user's status. |

These labels are intended application results, **not Python exceptions or evidence of a broken notebook**. The corresponding rejection tests pass when the protected action is not performed and no private record is exposed.

### Separate input-error practice

Run [error_examples.ipynb](error_examples.ipynb), or inspect [error_examples.py](error_examples.py), and compare with [errors_result.json](expected/errors_result.json). The exercise deliberately catches these `ValueError` cases so that learners can see both an error and the correction:

| Deliberate input | Expected exception type | Expected message |
|---|---|---|
| `None` or a blank question | `ValueError` | `Enter a non-empty question string.` |
| A question longer than 500 characters | `ValueError` | `Use at most 500 characters.` |
| A corrected, nonblank question of at most 500 characters | No validation error | The question is accepted. |

This is a **standalone validation exercise**, not a claim that these checks are automatically integrated into every model function. Its exact messages are part of this exercise's contract. A learner should be able to explain why each invalid case was rejected and show the corrected case being accepted.

### Acceptance checklist

- [ ] The demo produces and records a real model response; I do not treat that as proof of correctness.
- [ ] Assignment A records intended validation and authorization rejections without unexpected crashes.
- [ ] The input-error exercise shows the two documented messages and a corrected accepted question.
- [ ] Assignment B records all three real-model outputs, token counts, timing, and keyword-check results.
- [ ] I distinguish a selected-case keyword hit from semantic correctness or general model accuracy.

The recorded evaluation run has **3/3 keyword hits**, with answers `Use its reference number`, `Reference number`, and `Use its reference number`. This is an observed lexical check on three synthetic cases, **not 100% semantic accuracy**. Your run may differ; preserve and discuss its actual results.

## If something fails

- **A name is undefined:** run the preceding cells in order; a fresh runtime has no variables from yesterday.
- **`ModuleNotFoundError` (a possible setup failure):** verify that the setup cell completed in this runtime. Follow any restart message instead of repeatedly installing unrelated versions.
- **`OSError` or another download/loading error (a possible environment failure):** check your network and whether the model-hosting service is reachable. Retry the failed download only when the connection is restored. The core project remains usable without model downloads.
- **The runtime is disconnected or runs out of memory:** save work, reconnect to an available CPU runtime, and follow setup again. Do not subscribe to a paid plan just to finish the core course.
- **The generated answer looks wrong:** record it and discuss the failure. Successful execution does not imply a correct answer.
- **Your values differ from reference output:** first compare settings and software versions; timing differences are normal. Preserve the actual observation rather than editing it to match.

These exception names describe possible failure categories, not fabricated tracebacks or a promise of an exact version-specific message. There is no guarantee of zero errors. Keep the error message and the last completed step when asking the instructor for help, and remove any private information from screenshots.

## Coverage and attribution

Read [the objective and slide mapping](OBJECTIVES.md) for the distinction between real execution, simulation, and conceptual coverage. Course context: **LLM Application Engineering — SDA-AIE-213**; instructor: **Meaad Al-Marri**. [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy). This attribution does not imply endorsement of the implementation.

# Extension objectives and honest coverage map

These optional activities extend the **20-slides-per-day** version of the four-day course. Slide numbers restart at 1 each day. They do not alter the original cumulative notebook or expand its one-hour daily lab. Keep extensions in independent notebooks and schedule them outside the core lab.

## Coverage labels

- **Actual:** the code really performs the named operation in the specified environment.
- **Simulated:** deterministic data or hand-written calls stand in for a model/provider/system. The application logic executes, but the substituted service does not.
- **Conceptual:** discussed in slides or documentation without a working integration here.
- **Not covered:** beyond this package's implemented scope.

“Actual” does not mean production-ready. “Simulated” does not mean the validation code is imaginary: the checks execute, but the calls and identities are teaching fixtures.

## Learning outcomes

After the real-model demonstration, a learner should be able to:
1. Distinguish loading model weights locally from invoking a hosted inference API.
2. Identify input tokenization, model generation, and decoded output.
3. Explain why a generated answer requires verification even when the program ran successfully.

After Assignment A, a learner should be able to:
1. Validate the structure and values of an untrusted tool-call object.
2. Route only explicitly allowed tool names to a bounded read-only function.
3. Keep identity/ownership checks separate from a model's or user's claimed intent.
4. Test refusals and confirm that underlying records remain unchanged.

After Assignment B, a learner should be able to:
1. Run a small real-model evaluation on three synthetic FAQ paraphrases.
2. Record actual tokenizer counts and elapsed time rather than invented metrics.
3. Inspect answers and distinguish test-case success from broad model quality.
4. Document configuration, observed results, and limitations without promising reproducibility of exact wording or speed.

## Slide-by-slide alignment

| Activity | Course slides | Practice and coverage |
|---|---|---|
| Real-model demo | Day 1, slides 1–6: model/application distinction and architecture | **Actual** CPU model generation; **conceptual** production architecture. The application wrapper and model are still separate responsibilities. |
| Real-model demo | Day 1, slides 7–8 and 11–12: call/workflow, request, response | **Actual** local tokenizer/generation/decoding; **conceptual** hosted provider request/response behavior. |
| Real-model demo | Day 1, slide 10: API | Explains the difference between a local Python model interface and a hosted HTTP API. **No hosted model API integration.** |
| Real-model demo | Day 1, slides 13–14: mock client and model options | Contrast **simulated** `FakeClient` with **actual** FLAN-T5 small generation. Commercial-provider comparison remains **conceptual**. |
| Real-model demo | Day 1, slide 5: hallucination | Learners inspect output and identify possible failure; this is not a comprehensive hallucination benchmark. |
| Assignment A | Day 2, slides 1–8: structured outputs, JSON, contracts, validation | **Actual** schema/value checks on **simulated** structured calls; no guarantee that a real model will emit valid JSON. |
| Assignment A | Day 2, slides 9–12: function calling and tool cycle | **Actual** allowlist routing and Python function invocation; call selection is **simulated**. Native provider function calling is **not implemented**. |
| Assignment A | Day 2, slides 13–15: records, read-only access, end-to-end flow | **Actual** checks over synthetic data, with **simulated** identity; production authentication is **not covered**. |
| Assignment A | Day 3, slides 7–10: guardrails and output checking | **Actual** bounded validation and refusal tests. Complete prompt-injection defense and personal-data protection are **not established**. |
| Assignment B | Day 3, slides 11–15: golden cases, comparison, pass rate, diagnosis | **Actual** generation and reporting for three cases, distinct from the core's ten mock regression cases. The small sample is not a benchmark. |
| Assignment B | Day 4, slides 1–6: quality, cost, time, per-request measures | **Actual** token counts and measured time; API billing/cost calculations remain **conceptual or explicitly hypothetical**. No billed API call occurs. |
| Assignment B | Day 4, slides 14–15: evaluation report and peer review | **Actual** report creation and learner review, including failures and limitations. |
| All extensions | Each day's slides 17–20: core lab | Separate optional activities. They neither replace the core checkpoint nor become mandatory additions to its hour. |

## Deliberate error outputs

The independent [input-error exercise](error_examples.ipynb) demonstrates caught `ValueError` outputs and a corrected accepted question. It complements Day 1 input handling and Day 3 validation. It does not automatically add that validation to all real-model functions. Compare its [recorded results](expected/errors_result.json).

Assignment A's `invalid_call`, `invalid_arguments`, `tool_not_allowed`, and `unavailable` results are expected application-level refusals. They differ from an unexpected Python traceback caused by missing packages or a failed model download. Learners must explain this distinction rather than treating every refusal as an error to remove.

Assignment B's recorded 3/3 keyword hits are lexical matches for those three cases only, not a claim of semantic accuracy, broad objective coverage, or readiness for deployment.

## What stays in the core

The original four-day project continues to teach a deterministic response contract, validated tickets, a read-only synthetic status tool, guarded workflow, ten selected regression cases, and a versioned exact cache for public/general questions. Its deterministic outputs make beginner debugging easier. The extension model must not silently replace `FakeClient` in that core notebook: such a replacement changes the tests and the meaning of the expected results.

The core's ten-case report and Assignment B's three-case report are **different evaluations**. Keep their filenames, inputs, and summaries separate. Do not combine their scores into one “accuracy” figure.

## What this extension does not implement

- Hosted commercial model API authentication, billing, retries, rate-limit management, or production provider integration.
- Native provider tool/function calling or an autonomous model choosing and executing tools.
- Real user authentication, Ministry system access, real application records, or mutation operations.
- Fine-tuning, model training from scratch, retrieval-augmented generation, or a production vector database.
- A general prompt-injection prevention system or regulatory/security certification.
- Production deployment, vLLM serving, scaling, service monitoring, or availability guarantees.
- A validated comparison between multiple models, an Arabic benchmark, or general model-quality claims from three examples.

Day 4's caching objectives remain implemented in the core mock project. These independent extensions do not claim to benchmark real-model cache speedups or financial savings.

## How to judge completion

For the demo, require a successful documented generation attempt and a correct explanation of its boundaries, not a particular answer. If execution is blocked by downloads or runtime limits, record that blocker rather than claiming a completed model run.

For Assignment A, use the supplied deterministic validation/authorization cases and unchanged-record checks. For Assignment B, require a complete, honest observed report for all three inputs, configuration details, and a short error analysis. A lower answer-quality score is an observation to explain, not a reason to fabricate a passing result.

The supplied solutions and files in [`expected/`](expected/) are comparison references. A reference generated elsewhere is not evidence that the learner's runtime passed. Learners must run, save, and explain their own results.

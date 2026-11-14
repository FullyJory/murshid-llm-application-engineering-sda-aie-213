# Your extension learning roadmap

Use these optional activities after the relevant core lessons. They run in **separate notebooks**, outside the daily one-hour lab. Keep your cumulative Murshid notebook unchanged.

[Start the extensions](README.md) · [Watch the video path](VIDEOS.md) · [Check your work](VERIFICATION.md)

## 1. See a real model generate text

**Start after Day 1.** Open [the real-model demo](live_model_demo.ipynb).

| Connect to your slides | What to do | Explain it in your own words |
|---|---|---|
| Day 1, slides 1–6 | Follow the input through the application to the model. | How is an application different from its model? |
| Day 1, slides 7–8 and 11–12 | Find tokenization, generation, and decoding in the code. | What goes in, and what comes out? |
| Day 1, slides 10 and 13–14 | Compare the local model call with `FakeClient`. | Why does this demo need model weights, while the core does not? |
| Day 1, slide 5 | Read the answer critically. | Is the answer correct and supported, or merely fluent? |

Here, downloaded **FLAN-T5 small** weights generate tokens on CPU. The core's `FakeClient` instead returns fixed answers. This demo uses a local Python model interface, not a paid hosted inference API. You do not need an API key.

**Your checkpoint:** show one generated answer, identify the three processing steps, and describe one limitation. Compare the report structure with [the demo reference](expected/live_demo_result.json); do not require identical wording or timing.

## 2. Control a read-only tool

**Start after Day 2.** Attempt [Assignment A](README.md#assignment-a--validate-and-route-structured-tool-calls), then use [the solution notebook](homework_tools.ipynb) or [Python solution](homework_tools.py).

| Connect to your slides | What to do | Explain it in your own words |
|---|---|---|
| Day 2, slides 1–8 | Validate the structured call and its arguments. | Why can valid JSON still contain an invalid request? |
| Day 2, slides 9–12 | Route only an allowed tool name to the read-only function. | Why should arbitrary tool names be rejected? |
| Day 2, slides 13–15 | Check the synthetic record's ownership. | Why is a reference number not proof of ownership? |
| Day 3, slides 7–10 | Run invalid-input and refusal cases. | When is a rejected request the correct result? |

You supply structured calls by hand; a model does not choose the tool in this exercise. The dispatcher, validation, and ownership checks execute as ordinary Python. The demo users and records are fictional, so keep real service data out.

**Your checkpoint:** run the tool scenarios, confirm that records are unchanged, and explain the difference between validation and authorization. Compare with [the tool reference results](expected/tools_result.json).

## 3. Read an error and correct its cause

**Use alongside Days 1–3.** Open [the input-error practice](error_examples.ipynb) or read [its Python solution](error_examples.py).

1. Predict what will happen for `None`, a blank question, and a question longer than 500 characters.
2. Run the exercise and read the caught `ValueError` messages.
3. Replace the input with a nonblank question of at most 500 characters.
4. Show that the corrected question is accepted.

This is an independent validation exercise. Its function does not automatically become part of your other model functions.

**Your checkpoint:** distinguish an intended validation rejection from a setup problem such as a missing package. Use [the error reference results](expected/errors_result.json) and the [self-check](VERIFICATION.md).

## 4. Evaluate three real-model answers

**Start after Days 3–4 and the real-model demo.** Attempt [Assignment B](README.md#assignment-b--evaluate-three-real-model-faq-paraphrases), then use [the solution notebook](homework_evaluation.ipynb) or [Python solution](homework_evaluation.py).

| Connect to your slides | What to do | Explain it in your own words |
|---|---|---|
| Day 3, slides 11–15 | Run cases `E01`, `E02`, and `E03` and inspect every answer. | What does each case test? |
| Day 4, slides 1–6 | Record tokenizer counts and elapsed time. | Why are word counts different from token counts? |
| Day 4, slides 14–15 | Save a report and review it with a partner. | Which answer needs improvement, and why? |

The three inputs are synthetic FAQ paraphrases. Preserve the observed answers, even when they are poor. The keyword check is a small lexical test, not a measurement of general intelligence or semantic accuracy. Time and output can vary across environments and software versions.

**Your checkpoint:** save all three cases with their settings, answers, token counts, timing, and keyword results. Compare the fields and calculation method with [the evaluation reference](expected/evaluation_result.json). Explain one limitation and one improvement.

## Keep your results separate

- Your core notebook has ten fixed mock regression cases and a public-question cache experiment.
- Assignment B has three real-model FAQ cases.
- Assignment A tests hand-written tool calls.
- The error exercise tests input validation.

Do not combine these into one “model accuracy” percentage. Each result answers a different question. Do not replace the core's `FakeClient` with a real model during these activities: that would change the core's expected outputs and test behavior.

## Finish by teaching it back

Show a partner:
1. One real generated answer and your assessment of it.
2. One valid tool result and one correctly rejected request.
3. One deliberate error and the corrected input.
4. A three-case evaluation report with an honest explanation of its results.

Use [the self-check](VERIFICATION.md) before saving your extension work. These are small learning applications, not production services; use synthetic data and keep credentials and private records out of your repository.

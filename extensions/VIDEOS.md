# Watch, practise, and explain

[Extension activities](README.md) · [Your learning roadmap](OBJECTIVES.md) · [Check your work](VERIFICATION.md)

Choose the video for the activity you are working on. Watch outside the scheduled core lab hour, pause to take notes, then use the supplied notebook. Each video below is in English. Enable captions if helpful. Keep the notebook's model, pinned setup and CPU settings even when a video uses another example or library version. No paid course, API subscription or GPU upgrade is needed for these activities.

## 1. Prepare for the real-model demonstration

**Watch:** [The pipeline function](https://www.youtube.com/watch?v=tiZFewofSLM) by Hugging Face.

**Focus:** follow the journey from text input to a model prediction. Our demonstration exposes tokenizer, model loading and generation directly instead of hiding them behind a pipeline helper.

**Practise:** open [live_model_demo.ipynb](live_model_demo.ipynb) in its own Colab runtime. Run setup and the remaining cells in order. Find the model identifier, the synthetic context, the question and the generated answer.

**Explain:** which line generates an answer instead of looking it up in a dictionary? Compare your output with [the example result](expected/live_demo_result.json), reviewing the meaning rather than requiring identical wording.

## 2. Prepare for Assignment A: structured calls

**Watch:** [Python Tutorial: Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I) by Corey Schafer.

**Focus:** distinguish JSON text from a Python dictionary and inspect nested keys and types. Python Booleans use `True`/`False`; JSON uses `true`/`false`.

**Practise:** attempt Assignment A in the [activity guide](README.md), then open [homework_tools.ipynb](homework_tools.ipynb). Trace `name` and `arguments` through the dispatcher. Change one field at a time and predict its rejection code before running.

**Explain:** why does a syntactically valid object still need an allowlist and an ownership check? This exercise uses supplied calls so you can concentrate on the application's validation and execution decisions.

## 3. Prepare for Assignment B: tokens and evaluation

**Watch first:** [The tokenization pipeline](https://www.youtube.com/watch?v=Yffk5aydLzg) by Hugging Face.

**Focus:** connect text, token IDs and model input. Find the actual tokenizer-based input and output counts in [homework_evaluation.ipynb](homework_evaluation.ipynb), rather than estimating tokens from word counts.

**Then watch:** [LLM & AI Agent Benchmarks vs Reality: Why AI Applications Break](https://www.youtube.com/watch?v=nVImVgKpoOY) by IBM Technology.

**Focus:** ask what a score measures and whether it reflects the task you care about. Apply that question to the notebook's small keyword metric.

**Practise:** run the three cases and inspect every answer. Record whether the answer correctly tells the user to use the reference number. Compare your report with [the example evaluation](expected/evaluation_result.json).

**Explain:** how could an answer contain both keywords yet still be wrong? Why should you keep a failed case in your report? Treat the keyword count as a simple indicator and add your own meaning-based review.

## 4. Recognize and correct an expected error

**Watch:** [Python Tutorial: Using Try/Except Blocks for Error Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8) by Corey Schafer.

**Focus:** follow `raise`, `try` and `except`, and distinguish a handled invalid input from an interrupted program.

**Practise:** run [error_examples.ipynb](error_examples.ipynb). Predict the message for a blank question and a question longer than 500 characters. Compare with [the recorded error examples](expected/errors_result.json), then submit a short valid question and observe acceptance.

**Explain:** why is `expected_rejection: true` a successful test here? Use the troubleshooting table in the [activity guide](README.md) for genuine setup or runtime failures.

## 5. Strengthen your tests

**Watch:** [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI) by Corey Schafer.

**Focus:** express a small expected behavior as an assertion and separate test cases so failures are easy to locate.

**Practise:** add one new synthetic invalid-call case to your own copy of Assignment A. Write the expected rejection before running it. Preserve the original cases and confirm that records remain unchanged.

**Explain:** what behavior does your new test protect? A passing test is evidence for that case, not permission to ignore other inputs.

## Keep your learning route simple

Return to [your activity instructions](README.md) after watching. Run your own notebook, read its output, compare the appropriate fields and save your own evidence. If a video uses a different environment, follow the setup provided here rather than installing unrelated packages.

For a written companion to the Hugging Face videos, read [Behind the pipeline](https://huggingface.co/learn/llm-course/en/chapter2/2). Keep the model-specific [FLAN-T5-small card](https://huggingface.co/google/flan-t5-small) alongside the real-model activity.

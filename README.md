
---

<div align="center">

# Jory Alshaalan

### Murshid Mini · LLM Application Engineering

**King Saud University · Computer Science**

**SDA-AIE-213 · [SDAIA Academy](https://github.com/SDAIAAcademy)**

</div>

---

## Project Overview

I developed **Murshid Mini**, a simulated LLM-based service assistant using **Python** and **Google Colab** as part of the **LLM Application Engineering (SDA-AIE-213)** training program.

The project demonstrates essential application engineering concepts, including structured data extraction, read-only tool integration, access control, input validation, automated testing, caching, and performance monitoring.

## Implementation & Results

I implemented and evaluated the application using synthetic service data and a deterministic mock client.

| Evaluation Metric | Result |
|---|---|
| Golden Test Cases | **10/10 Passed** |
| Test Pass Rate | **100%** |
| Cache Hit Rate | **66.7%** |
| Mock Client Calls | **Reduced from 3 to 1** |
| External API Calls | **0** |

## Technologies & Setup

**Python 3 · Google Colab · CPU · JSON · GitHub**

To run my implementation:

1. Open the completed notebook in the `notebooks` folder using Google Colab.
2. Select a **Python 3** runtime with CPU.
3. Run all cells sequentially.
4. Review the generated evaluation reports in the `results` folder.

No API keys, GPU, model downloads, or additional packages are required.

## Project Limitations

This implementation uses a deterministic **FakeClient**, not a live language model. All data is synthetic, and the application is intended for educational purposes rather than production use.


## Submitted Homework (Days 1–4)

The four extra-homework exercises are separate from the cumulative Murshid Mini project. Each notebook has been executed and includes saved cell outputs; generated JSON reports are committed under [`homework/results/`](homework/results/).

| Day | Exercise | Notebook | JSON report |
|---|---|---|---|
| 1 | Real-model generation (FLAN-T5) | [Day 1 notebook](homework/day1_real_model.ipynb) | [live_demo_result.json](homework/results/live_demo_result.json) |
| 2 | Validated tool dispatch (7/7 cases) | [Day 2 notebook](homework/day2_tools.ipynb) | [tools_result.json](homework/results/tools_result.json) |
| 3 | Expected input errors (3 caught cases) | [Day 3 notebook](homework/day3_errors.ipynb) | [errors_result.json](homework/results/errors_result.json) |
| 4 | Real-model evaluation (3 FAQ paraphrases) | [Day 4 notebook](homework/day4_evaluation.ipynb) | [evaluation_result.json](homework/results/evaluation_result.json) |

Days 1 and 4 run the open-source `google/flan-t5-small` locally on CPU. They require installing Python packages and downloading model weights, but no paid API keys. The other two homework notebooks use Python's standard library only. The Day 4 keyword indicator is **not** a semantic accuracy metric; case-by-case context support notes are included in its notebook output.

The homework is reproducible through [`homework/run_model_results.py`](homework/run_model_results.py) and [GitHub Actions](.github/workflows/generate-homework-results.yml).

## Acknowledgment

This project was completed as part of the **LLM Application Engineering (SDA-AIE-213)** training program under the guidance of **Meaad Al-Marri**.

Special thanks to **[SDAIA Academy](https://github.com/SDAIAAcademy)** and **Meaad Al-Marri** for providing this valuable learning opportunity and guidance throughout the program.

This educational implementation does not imply official SDAIA Academy certification or endorsement.

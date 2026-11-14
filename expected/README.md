# Expected results: compare your own run

Run your notebook from the first cell, then compare your results with these **mock-code reference outputs**. Match the stable answers, codes and counts. Your trace IDs and execution times will naturally differ.

| Day | Reference file | Stable checks |
|---|---|---|
| 1 | [baseline_results.json](baseline_results.json) | Three prescribed answers, training-mock, nonempty trace ID, latency ≥ 0; empty input adds no call |
| 2 | [day2_results.json](day2_results.json) | codes: under_review, needs_clarification, not_found, unsupported_action, access_denied; tool counts 1,0,1,0,1 |
| 3 | [day3_results.json](day3_results.json) | passed 10, total 10, pass_rate 100.0, mode mock |
| 4 | [day4_results.json](day4_results.json) | no-cache calls 3, cached calls 1, hits false/true/true, hit rate 66.7%, external calls 0 |
| Final | [final_report.json](final_report.json) | all ten tests still pass; cache comparison and limits recorded |

10/10 proves only that the listed fixtures passed. The hypothetical USD cost calculation is not billed usage. Internal `not_found`/`access_denied` codes are for teaching and should not be exposed as an existence oracle in a real service. This demo's user-facing answer is identical for both.

## Quality checks

Run `python -m unittest discover -s tests -v` from the repository directory to check eight test methods: fresh execution, repeat execution, daily replay, code parity, schema, guards, authorization and cache behavior. Look for `OK`. These tests use no network or third-party packages.

If you edit the lab scripts, regenerate and execute the reference notebook:

```bash
python tools/build_notebook.py
python tools/record_reference.py
python -m unittest discover -s tests -v
```

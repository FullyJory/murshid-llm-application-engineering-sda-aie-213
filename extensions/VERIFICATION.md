# Verification scope

Checked on 2026-11-14 in an isolated local Python 3.12 environment, using torch 2.6.0 CPU, transformers 4.49.0 and sentencepiece 0.2.0.

- Actual FLAN-T5-small weights downloaded from the pinned revision and executed on CPU.
- Real demo and real evaluation executed locally, including notebook cells. See `expected/` for observed reports, not promises of identical future answers or times.
- Tool homework: seven cases passed, including rejection cases and unchanged records.
- Error exercise: three intentionally caught ValueErrors matched their messages; corrected input was accepted.
- Original core test suite: eight test methods passed. No core lab, notebook, dataset, tests or expected-result file changed.
- Notebook setup preserves an existing torch installation; installs CPU torch only if absent. The installed torch version on a future Colab runtime may differ from this tested version.
- Colab itself was NOT execution-tested: the earlier browser attempt stopped at “Google sign-in required”. Reading stored outputs is not a fresh runtime test.

The local model cache was about 297 MB, excluding packages; the isolated environment was about 1.1 GB. These are observations, not exact download-size guarantees. CPU inference time varies; package and model download time is additional.

No hosted API, native provider function-calling protocol, live-model judge, production deployment, real identity system, comprehensive security testing, or Arabic-quality benchmark was tested. No paid endpoint or credential is required by these extensions.

# Project repository, version history, and submission checklist

## Your repository is the final deliverable
Create your own project repository on GitHub using a descriptive name, such as `murshid-llm-application-engineering`. Keep one cumulative notebook at `notebooks/murshid.ipynb`; the daily labs are stages of this single project.

Before publishing, follow your training provider's visibility instructions and confirm that the contents are safe to share. This project uses synthetic data. Never upload national IDs, real service records, passwords, access tokens, or other people's private information.

## Required elements
- [ ] A clear, comprehensive project description.
- [ ] A professional `README.md` explaining the idea, intended user, scope, and limitations.
- [ ] Simple setup, run, and use instructions, including the CPU-only, standard-library, no-key workflow.
- [ ] Appropriate technical documentation: pipeline, dataset/fields, validation, read-only tool, authorization fixture, cache rules, tests, and limitations.
- [ ] The complete cumulative notebook, with useful outputs and no private information.
- [ ] Results and an honest evaluation report identifying `mode=mock`.
- [ ] Meaningful version history demonstrating the four daily stages.
- [ ] Attribution to **LLM Application Engineering — SDA-AIE-213**, delivered within the SDAIA Academy training context, with instructor **Meaad Al-Marri**.
- [ ] A link to [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy) where appropriate.

Do not claim SDAIA endorsed your implementation, certified it, or authored your project unless you have explicit evidence. The link is attribution, not proof of approval.

## Recommended README sections
1. Project title and short description.
2. Problem and intended users.
3. What the project does and does not do.
4. Four-day development journey.
5. Environment and how to run the notebook from a fresh runtime.
6. Dataset source: hand-written synthetic teaching fixtures; field definitions.
7. Example inputs and expected outputs.
8. Tests and results.
9. Limitations and future improvement.
10. Program, instructor, and SDAIA Academy link.

Explain prominently that `FakeClient` is deterministic mock code, not a trained language model. The project demonstrates application engineering around a model-shaped interface.

## Beginner-friendly daily version workflow
You can use GitHub's website without installing Git or placing a GitHub token in Colab.

1. At the end of each day, save the **same notebook** in Drive.
2. Download that notebook as an `.ipynb` file, along with the day's JSON results.
3. Upload/update the same notebook path in your own repository. Do not create four unrelated final notebooks.
4. Inspect the changed files before committing. Keep unrelated and private files out.
5. Use a meaningful commit message, for example:
   - `Day 1: add mock client and response contract`
   - `Day 2: add validated tickets and authorized status lookup`
   - `Day 3: add guardrails and ten regression cases`
   - `Day 4: add cache experiment and final report`
6. Describe your change and the test you ran. Preserve earlier commits rather than replacing the repository history.

For later improvements, create a feature branch, make a small focused change, and open a pull request. Read and test a change before merging. Use an issue to describe a reproducible bug with expected versus actual behavior, but never include private data.

## Evidence and reproducibility
Before final submission, restart the Colab runtime and run the notebook from top to bottom. Record the result. If you change code after a successful test, rerun the affected checks. Do not describe an unexecuted check as passed. The reference repository's outputs are a comparison aid, not a substitute for your own run.

## Support the Saudi open-source community
As encouraged in the supplied academy project guidance, learners may:
- Star high-quality Saudi projects they have actually explored.
- Follow relevant Saudi accounts and watch repositories thoughtfully.
- Contribute useful documentation, tests, or code to open-source projects.
- Use forks, pull requests, and issues when they serve a genuine need.
- Share excellent projects with the technical community.

These are voluntary community activities, **not grading requirements**. Do not mass-star repositories or submit empty issues/pull requests. Read each project's contribution guide and license, and interact respectfully. No automated social actions are required by this lab.

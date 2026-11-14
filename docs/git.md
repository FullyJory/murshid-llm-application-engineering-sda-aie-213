# Project repository, version history, and submission checklist

## Your repository is the final deliverable
Create your own project repository on GitHub using a descriptive name, such as `murshid-llm-application-engineering`. Keep one cumulative notebook at `notebooks/murshid.ipynb`; the daily labs are stages of this single project.

Before publishing, follow your training provider's visibility instructions and confirm that the contents are safe to share. This project uses synthetic data. Never upload national IDs, real service records, passwords, access tokens, or other people's private information.

## Keep five notebooks, not five versions of the project

Use **one cumulative project notebook** for all four core labs, plus **one separate notebook for each extra homework** you complete. Save each in your own Google Drive. Do not append homework cells to the core project or overwrite one homework with another.

| Work | Suggested Drive filename | Repository destination |
|---|---|---|
| Core project, Days 1–4 | `murshid_project_your_name.ipynb` | `notebooks/murshid.ipynb` |
| Day 1 homework: real model | `day1_real_model_your_name.ipynb` | `homework/day1_real_model.ipynb` |
| Day 2 homework: tools | `day2_tools_your_name.ipynb` | `homework/day2_tools.ipynb` |
| Day 3 homework: errors | `day3_errors_your_name.ipynb` | `homework/day3_errors.ipynb` |
| Day 4 homework: evaluation | `day4_evaluation_your_name.ipynb` | `homework/day4_evaluation.ipynb` |

These are suggested names. Replace `your_name` with your name or an appropriate learner identifier. Homework remains separate optional practice; include the homework you complete without presenting untouched reference solutions as your own work.

## Save your own Colab copies

1. For the core project, create your notebook once on Day 1. Reopen that saved notebook on Days 2–4 and add the new core cells below earlier cells.
2. For homework, use its day's notebook link. In Colab choose **File → Save a copy in Drive**, then rename the copy using the table. If working from scratch, create a new notebook for that homework and save it under the matching name.
3. Confirm the name at the top before typing. Use the homework's own runtime/setup instructions; do not install its model packages into your core project's runtime.
4. Run your code and inspect the output. Save the notebook to Drive. Download it using **File → Download → Download .ipynb**.
5. Download generated JSON files from the Colab **Files** panel before disconnecting. For homework that only prints a report, retain the visible output in the saved notebook; a separate JSON export is optional. The project's ZIP contains JSON results, not the notebook, so download the `.ipynb` separately.

## Upload everything to your own GitHub repository

Use your own repository, not the instructor's reference repository. One repository can hold the core project and all your completed homework. A suggested structure is:

```text
murshid-llm-application-engineering/
  README.md
  notebooks/
    murshid.ipynb
  homework/
    day1_real_model.ipynb
    day2_tools.ipynb
    day3_errors.ipynb
    day4_evaluation.ipynb
  results/
    core/                 # Your daily JSON outputs and final_report.json
    day1/                 # live_demo_result.json, if completed
    day4/                 # evaluation_result.json, if completed
  docs/
    project-notes.md       # Explain the data, design and how to run
```

1. Sign into GitHub and create your own repository if you have not already done so. Add a README. Choose visibility according to your training provider's instructions and the privacy of your contents.
2. Download your saved Colab notebooks to your computer. Organize them into `notebooks`, `homework`, `results` and `docs` folders as above. Rename the downloaded copies to the repository names in the table. Keep the single core notebook at the same path on every update.
3. Open your repository's **Code** tab and choose **Add file → Upload files**. Drag the prepared folders/files into the upload area. Alternatively, enter the relevant existing repository folder first and upload its files there; check the destination paths before committing.
4. Inspect every file and saved cell output. Remove secrets, passwords, API keys, tokens, personal identifiers and real service data. Never upload credential files, model weights, package folders or your local virtual environment.
5. Enter a descriptive commit message, such as `Add Day 2 homework: tool validation`, then choose **Commit changes**. On later days, update the core notebook at its existing path and add the new homework separately. Do not delete and recreate the repository to update it.
6. Return to the Code tab. Open each uploaded notebook and result file to confirm it is present. If GitHub's notebook preview is unavailable, use the raw/download view or open that file in Colab to inspect it.
7. Update your README with relative links to your project notebook, completed homework, results and run instructions. Label the core as a mock and the model exercises as actual local model inference. Describe your own observations.

## Submit your repository link to the instructor

Submit the **root link to your own GitHub repository**, not a Colab editing link, a link to your Drive folder, or the instructor's reference repository. A root link has the form `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.

Before sending:
- [ ] The repository contains the cumulative project and every homework item I am submitting.
- [ ] My README points to each notebook and explains how to run it.
- [ ] Notebook outputs and reports are from my own execution and contain no secrets or private information.
- [ ] I copied the URL from my repository's Code page and opened it again to verify the owner and repository name.
- [ ] The instructor can access the repository. For a public repository, check the link in a signed-out/private browser window. For a private repository, use the instructor's confirmed GitHub account and the training provider's access instructions to grant the required read access, then verify access. Do not make private work public merely to avoid an access problem.

Send the link to **Meaad Al-Marri** through the submission channel she specifies. Follow the deadline she provides; this guide does not set a channel or date. You may use this message:

```text
Name: [your name]
Program: LLM Application Engineering — SDA-AIE-213
Repository: [your own repository URL]
Submitted work: cumulative project + [list the homework days included]
```

After sending, keep the same repository link. Make any requested corrections through new commits so the instructor can follow your updates.

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

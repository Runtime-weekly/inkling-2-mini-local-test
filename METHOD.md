# Tasks and evaluation method

These task descriptions summarize the historical briefs. They are not byte-identical prompts or a deterministic benchmark suite.

## Task 1: CSV Field Explorer

Start with an empty workspace. Ask the model to build a browser tool that accepts CSV, searches and sorts rows, edits values, charts numeric fields and remains usable across screen sizes. Include synthetic inputs with quoted commas, multiline quoted fields, escaped quotes, malformed rows and HTML-like text that must stay inert.

Evaluate parsing, sorting, filtering, editing, escaping and layout independently of the model. The recorded review used Chromium and Linux WebKit, including eight same-session viewport sizes and short embedded layouts. Two repair rounds addressed malformed quotes and clipped rows. The final suite recorded 118 assertions. These assertions are correlated checks of one artifact, not 118 independent successful tasks.

The initial run hit a 20,000-token output ceiling. Recovery preserved the failed record and full prior history, added feedback and raised the allowance to 65,536. A subsequent response completed at 18,167 output tokens with native tool calls. The history later reached 159,172 actual input tokens. The controller ended the session at a completed tool boundary after qualification; the model did not independently declare completion.

## Task 2: browser FPS

Ask the model to build a playable browser first-person shooter. Independently exercise keyboard/mouse focus, aiming, pause/resume, application state and touch-sized layouts. Include interruption and resume tests instead of checking only the first frame.

The recorded result passed 224 assertions and 36 checks across Chromium and Linux WebKit after three repair rounds. These are suite-specific counts, not comparable percentages or a general game-development benchmark.

## Harness and recording

Qwen was not used for these builds. Inkling generated the app code and native tool calls. The harness executed tools, retained history and supplied independently produced test feedback. RUNTIME/Codex authored the harness and review tests; the success is a model-plus-tools-plus-review result, not an unaided single response.

Keep prompts, tool definitions, sampling settings, failed attempts, interventions and final artifacts. Use disposable workspaces and explicit execution permissions for generated commands. A valid tool-call JSON object is not proof the action succeeded.

Record generation time, tool time, testing time, maintenance pauses and wall-clock time separately. Some builders shared one GPU runtime with overlapping requests. Do not add project wall-clock totals to infer overall elapsed time or treat them as isolated speed benchmarks.

## Additional runtime smoke tests

The historical qualification included text, a native tool roundtrip returning 462, a simple image-colour check, and a 131,939-token recall prompt with three audit facts. These are narrow smoke tests. They do not establish full vision quality or the model-card one-million-token capability.

## Repeating the experiment

Use the model identity and settings in SETUP.md with your chosen tool-capable harness. Write your checks before repairing failures, keep the inputs fixed and report every retry. Publish the resulting artifact and verification method, even if it fails. For a model comparison, use matched tools, tasks, budgets, checking and repeated trials. The historical case studies do not establish superiority over Qwen or any other model.

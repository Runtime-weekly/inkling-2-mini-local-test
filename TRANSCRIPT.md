# Episode transcript

Spoken narration for the November 26, 2026 revision. See RESULTS.md for precise timing values and METHOD.md for the scope of the checks.

We ran Inkling 2 Mini on one DGX Spark. It built a working data explorer and a browser game, with repairs along the way. Here is how the model works, what our checks found, and how much time those results took.

This is Inkling 2 Mini from Thinking Machines Lab, released on November twentieth, twenty twenty-six, with Apache two point oh weights. The exact checkpoint here is twenty-six point four billion total parameters, three point four billion active in the base mixture of experts, and five point four billion effective active parameters once the loop is counted. It is the NVFP four plus MXFP eight checkpoint, about twenty gigabytes on disk, served on the Spark through the pinned vLLM runtime.

The local endpoint was configured for two hundred sixty-two thousand tokens, even though the model card lists a one-million-token native context. Startup loaded the model in about ninety seconds in the qualification run. A patched restart, including the normal GPU warm-up, took about five minutes. Those are setup measurements, not a promise about every machine.

The unusual part is not just the size. Inkling uses a twenty-four-layer decoder-only transformer with sparse expert layers. The middle twelve layers run three times for every token, sharing their weights. So the model gets more computation per token without storing three separate copies of those layers.

That gives the model a kind of internal extra pass. It can spend more computation on a difficult step without writing every intermediate thought into the visible answer. But looping does not add facts to the weights. The authors' own documentation says that knowledge is still mostly a function of total parameter count. More passes can improve reasoning and long-context behavior; they do not magically turn a small model into a database.

Thinking Machines reports forty-eight point two percent on DeepSWE, forty-six point five percent on its Vals Index, and strong scores on BrowseComp, DeepSearchQA and MCP Atlas. Those are useful signals, but they are the authors' evaluations, with their own harnesses and conditions.

We are not going to redraw those numbers as if we reproduced them. Our test is different: one local checkpoint, one real machine, real tool calls, saved outputs, and independent browser checks. The question is narrower, but it is one that matters if you want to use the model rather than quote it.

First, we gave Inkling a blank workspace and a concrete product task: build a CSV field explorer that can load data, search it, sort it, edit a value, and remain usable when the screen size changes.

The model did not get a clean win on the first try. One run hit the output ceiling. The harness retained the complete history, raised the allowance, and continued from the saved state. The finished app then went through one hundred eighteen independent assertions across Chromium and WebKit, including short phone-shaped layouts. Two repair rounds addressed malformed quote handling and clipped rows.

This is the part I trust more than a screenshot of generated code. The model proposed the changes, but the browser checks decided whether the changes worked. The final status was verified in both engines. Physical iPhone behavior was not tested, so we are not calling this mobile-certified.

The second task was a browser FPS game. That sounds less useful than a business tool, but it exposes a different failure mode: the model has to keep track of input, focus, aiming, pause and resume, and the state of the running page.

The independent review recorded two hundred twenty-four assertions and thirty-six checks across Chromium and WebKit. It tested the active layout, focus, aiming, pause and resume, and touch-sized viewports. Three repair rounds were needed. That is not a bad result; it is the result. A system that can recover under a checked loop is more interesting than one that produces a pretty first screenshot.

Here is the less glamorous part. The CSV run used about fifty-nine minutes of model generation across its attempts and about seventy-two minutes wall-clock. The FPS run used about thirty-eight minutes of generation and about forty-five minutes wall-clock. Those numbers include retries, tool calls and the saved runtime recovery; they are not clean tokens-per-second benchmarks.

The startup log recorded about twenty-one point two gigabytes for the model allocation. It reported roughly sixty-seven point three gigabytes available for the key-value cache. The chart shows the original binary units from the log. This is unified memory. The operating system, browsers and other services also need room. The model fits, but that does not make every workload fast.

The honest result includes the projects we did not mark complete. A gallery hub changed after its first review and went back into repair. A Camaro builder was still in testing. We are not using those as proof of success.

That distinction matters because long-horizon agents can look impressive while they are working and still leave an almost-finished project behind. Our harness preserves the requests, tool results, failures and repairs, so the next run can start from evidence instead of a clean slate. It also gives us a way to say exactly where the current system stopped.

The active parameter count matters mainly for computation. All twenty-six point four billion parameters still need to be stored. The mixed precision weights help keep that memory footprint manageable. Reusing the middle layers adds computation without storing extra copies. Those are different benefits, and neither guarantees that an application will work.

For our use, Inkling 2 Mini looks most interesting as a local agent that can keep a long task alive, call tools, inspect the result, and repair a specific failure. It is not a drop-in replacement for every larger model, and our browser tests are not a general intelligence score. But the verified CSV and FPS runs show something concrete: this model can create useful artifacts, and a separate checker can push the result past the first draft.

That is the test I would repeat. Give the model a real task, keep the whole trace, check the result outside the model, and count the repairs. If the artifact survives, the claim is worth keeping. If it fails, save that too. Subscribe to RUNTIME if you want more local tests where the machine, not the marketing page, gets the final word.

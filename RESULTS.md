# Recorded results

Evidence cutoff: November 21, 2026. These are retained observations, not a live service-status report.

| Project | Result | Repairs | Model-call time | Wall-clock time |
|---|---|---:|---:|---:|
| CSV Field Explorer | 118 assertions passed in Chromium/WebKit | 2 | 3,593.35 s (59.89 min) | 4,298.22 s (71.64 min) |
| Browser FPS | 224 assertions and 36 checks passed in Chromium/WebKit | 3 | Approximately 38 min | Approximately 45 min |
| Gallery hub | Independent final qualification pending at cutoff | — | Not reported here | Not reported here |
| Camaro builder | Still in testing at cutoff | — | Not reported here | Not reported here |

The episode rounds the CSV generation figure down to about 59 minutes; the retained measurement is 59.89 minutes, approximately 60 minutes when rounded to the nearest minute. Use the measured value for comparisons.

The CSV run includes a 362.17-second maintenance pause. Model-call timings include failed attempts and can include serving overhead. They are not clean GPU compute timings or tokens-per-second benchmarks. The two projects' wall times are not directly comparable controlled measurements.

## Memory and startup

- Recorded model allocation: 19.74 GiB, approximately 21.20 decimal GB.
- Runtime-reported memory available for KV cache: 62.66 GiB, approximately 67.28 decimal GB. This is capacity reported at startup, not a measured per-task cache requirement.
- Weight loading: 90.04 seconds.
- A patched restart through HTTP readiness: approximately 306 seconds, including warmup.

Unified memory is shared by the GPU, operating system and other applications. Model allocation is not whole-system RAM usage. Native context configuration was 262,144; one-million-token operation was not measured.

## Interpretation

The evidence supports successful checked artifacts after repair in these two cases. It does not establish autonomous completion without oversight, general reliability, physical iPhone compatibility, a universal memory requirement, or superiority over another model. The active count affects computation; all weights still require storage. Looped layers reuse weights while adding computation.

Vendor benchmark values in the episode are attributed to Thinking Machines Lab. We did not reproduce those benchmark suites. See the official launch and model-card links in README.md for their conditions.

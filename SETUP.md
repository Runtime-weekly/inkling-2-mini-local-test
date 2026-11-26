# Setup and recorded configuration

## Identity

| Field | Recorded value |
|---|---|
| Publisher/checkpoint | `thinkingmachines/Inkling-2-Mini` |
| Revision | `ed40e7da625f594fc9c4990f5f66be24873c22d7` |
| Precision | Original mixed NVFP4/MXFP8, no requantization |
| Parameters | 26.4B total; 3.4B base active; 5.4B effective active compute with looping |
| Loop passes | Three |
| Hardware | One DGX Spark, GB10, unified memory |
| Runtime | vLLM dedicated ARM64 image, reported `0.1.dev25855+g7cb5dae22` |
| Image digest | `sha256:ecdf0ccc663d86332459f5a50a38c30861a5079bc3924aa08fdc657ef10dd648` |
| Configured context | 262,144 tokens |
| Model-card context | 1,000,000 tokens; full capacity not tested here |
| Tensor parallelism | 1 |
| GPU memory utilization | 0.70 |
| Speculative decoding | DSpark, seven draft tokens, probabilistic draft sampling |
| Agent requests | temperature 1.0; high reasoning (0.9) |

All weights still need storage. Active parameters describe computation, not the total memory requirement. The recorded runtime used GPU inference with no CPU weight offload. The separate XQ Uncensored variant is **not** the model tested in this episode.

## Bring up the official runtime

Use the [official DGX Spark instructions](https://recipes.vllm.ai/thinkingmachines/Inkling-2-Mini?hardware=dgx_spark_gb10&features=reasoning,tool_calling,spec_decoding) for Docker, NVIDIA container integration and current compatibility requirements. The following is a portable reconstruction of our settings, not a newly validated installation guide. It requires ARM64 Spark-compatible GPU infrastructure and adequate free memory.

Download the exact checkpoint with the Hugging Face CLI:

```sh
hf download thinkingmachines/Inkling-2-Mini \
  --revision ed40e7da625f594fc9c4990f5f66be24873c22d7 \
  --local-dir ./inkling-weights
```

From the directory containing `inkling-weights`:

```sh
docker run --rm --gpus all --ipc=host \
  -p 127.0.0.1:8112:8000 \
  -v "$PWD/inkling-weights:/model:ro" \
  vllm/vllm-openai@sha256:ecdf0ccc663d86332459f5a50a38c30861a5079bc3924aa08fdc657ef10dd648 \
  /model --served-model-name inkling-2-mini-26.4b-a3.4b-nvfp4-mxfp8 \
  --tensor-parallel-size 1 --max-model-len 262144 \
  --gpu-memory-utilization 0.70 --reasoning-parser inkling \
  --enable-auto-tool-choice --tool-call-parser inkling \
  --speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"probabilistic"}'
```

The historical run also mounted a local parser correction. This documentation release does not include that overlay. Complete non-streaming tool arguments in the original build could repeatedly rescan growing JSON prefixes after GPU generation finished. Our correction suppressed redundant intermediate deltas while preserving final arguments and streaming behavior. It passed 17 parity cases and a 54,301-character completion. Thus the stock command above is **not identical to the corrected historical runtime**. Check upstream fixes before large tool-output trials; keep streaming and non-streaming behavior separate in your results.

## Checks and troubleshooting

Run `python3 check_endpoint.py` after the server is ready. Expected result: the exact model appears in `/models` and a small chat request completes. This alone does not qualify vision, tools or long-context behavior.

- Allow time for kernel and vision warmup. Weight-load time and HTTP readiness are different measurements.
- If memory is insufficient, review other workloads and context/cache settings; do not assume active parameter count is the memory footprint.
- If a tool request appears stalled, inspect both GPU generation and CPU parsing. Do not replay a request with unknown execution status.
- Preserve full requests, finish reasons and actual usage when comparing output budgets.
- Our historical `/tokenize` endpoint undercounted native tool history; generated-request usage was the evidence used for long agent histories.
- Other operating systems, GPUs and a fresh cold installation were not qualified by this documentation release.

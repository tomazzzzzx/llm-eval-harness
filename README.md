# LLM Eval Harness

Comprehensive LLM evaluation harness covering MMLU, HumanEval, GSM8K, and more.

## Benchmarks
- **Knowledge**: MMLU, ARC, HellaSwag, Winogrande
- **Code**: HumanEval, MBPP, BigCodeBench
- **Math**: GSM8K, MATH, AQuA
- **Safety**: TruthfulQA, BBQ, BBH

## Usage
```bash
python eval.py --model meta-llama/Llama-3-8B --tasks mmlu,humaneval,gsm8k --output results/
```

## License: Apache 2.0

# Llm Eval Harness

Comprehensive LLM evaluation harness.

## Benchmarks
- MMLU, ARC, HellaSwag, Winogrande
- HumanEval, MBPP (code)
- GSM8K, MATH (math)
- TruthfulQA, BBH

## Usage
```bash
python eval.py --model meta-llama/Llama-3-8B --tasks mmlu,humaneval,gsm8k --output results/
```

## License
MIT

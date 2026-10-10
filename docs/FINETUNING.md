# Fine-Tuning Notes

The HealBot_Pro_Finetuning.ipynb notebook documents experiments with
fine-tuning smaller LLMs on medical Q&A data to reduce Groq API dependency.

## Dataset

- Source: MedQuAD (Medical Question Answer Dataset) + custom symptom–disease pairs
- Format: Instruction-following (system prompt + user message + assistant response)
- Size: ~12,000 training pairs after filtering

## Approach

| Experiment | Base Model | Method | Result |
|-----------|-----------|--------|--------|
| v1 | Mistral-7B | QLoRA (4-bit) | Decent symptom extraction, hallucinations on rare diseases |
| v2 | LLaMA-3-8B | QLoRA (4-bit) | Better factuality, slower inference |
| v3 (current) | LLaMA-3-8B | Full fine-tune on A100 | Best results; hosted on Groq not feasible ? use as-is |

## Outcome

Fine-tuned models showed improvement on the symptom-extraction task
(Step 1 of the pipeline) but the hosted Groq endpoints with the 70B model
outperformed all fine-tuned 7–8B models on report generation.

**Current decision:** Use Groq-hosted llama-3.3-70b-versatile for intake
and report generation; llama-3.1-8b-instant for fast symptom extraction.

## Reproducing Fine-Tuning

Open HealBot_Pro_Finetuning.ipynb in Google Colab (A100 runtime recommended):
1. Mount Google Drive for dataset storage
2. Install 	rl, peft, itsandbytes
3. Run all cells — training takes ~2 hours on A100

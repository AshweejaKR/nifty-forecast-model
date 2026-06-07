# CLAUDE.md

## Project Goal

Help build a Tiny GPT from scratch and learn AI Agent Engineering.

---

## ⚠️ STRICT RULES

- Do NOT over-engineer
- Do NOT create unnecessary abstractions
- Do NOT use factory patterns unless clearly needed
- Do NOT create multiple layers for the same logic
- Do NOT split small logic into many files

- Keep code simple and readable
- Prefer files under 150-300 lines
- Split only when readability improves
- Prefer functions over classes unless necessary
- One responsibility per module

---

## ⚙️ EXECUTION CONSTRAINTS

- Do NOT create extensive test suites unless explicitly asked
- Create minimal tests only when needed to validate core functionality
- Do NOT simulate running code or fake outputs
- Do NOT assume external API responses
- Do NOT generate unnecessary files
- Keep responses efficient and focused

---

## 🧠 RESPONSE STYLE

- Be concise and direct
- Avoid unnecessary explanations
- Prefer code over text
- No filler or generic statements
- Output result, then stop

---

## ❓ CLARIFICATION RULE

- If task is unclear, ask questions before coding
- If task is clear, proceed immediately
- Do not ask obvious or redundant questions

---

## 🎯 LEARNING FIRST

- Prefer educational implementations over clever implementations
- Explain important AI/LLM concepts when introducing them
- Optimize for understanding first, performance second
- Build from scratch before using frameworks when learning

---

## Development Workflow

1. Read PLAN.md
2. Complete one task at a time
3. Update documentation when needed
4. Commit after each phase

---

## Folder Ownership

data/
- Dataset processing

tokenizer/
- Tokenizer implementation

model/
- Transformer and GPT model

training/
- Training loop

inference/
- Text generation

tests/
- Minimal validation tests only when necessary

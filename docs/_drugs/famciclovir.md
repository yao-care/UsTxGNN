---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 9
---

# Famciclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Famciclovir: From Herpes Zoster/Genital Herpes to Post-infectious Neuralgia

## One-Sentence Summary

Famciclovir is an established oral antiviral (a prodrug of penciclovir) used for varicella-zoster and herpes simplex virus infections such as herpes zoster, genital herpes, and herpes labialis. The TxGNN model's top-ranked prediction for this drug is **Post-infectious Neuralgia** (essentially postherpetic neuralgia), but the evidence pack contains **0 literature records** and only **2 clinical trials, neither of which actually tests famciclovir** — both are graded "C" relevance (disease-population overlap only). This is currently a model-driven signal with mechanistic plausibility but no direct trial or literature support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this dataset (`original_indications` is empty; famciclovir is generically known as an antiviral for herpes zoster, genital herpes, and herpes labialis, but this dataset carries no confirmed regulatory-label text — see data gap below) |
| Predicted New Indication | Post-infectious Neuralgia (postherpetic neuralgia) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | **L5** (reassessed — see note below) |
| Market Status (Taiwan/TFDA) | 未上市 (Not marketed) |
| Number of Licenses | 0 (no license records) |
| Recommended Decision | **Hold** |

**Note on Evidence Level and Decision:** The evidence pack's internal `scoring` field labels this candidate L2/"Proceed with Guardrails." Applying the stated determination rules (≥2 completed Phase 3 RCTs = L1; 1 completed Phase 2/3 RCT = L2; observational/review = L3; preclinical/mechanism = L4; model-only = L5) to the *actual* evidence supplied — two trials, both testing other interventions (oxycodone; nerve block), neither completed nor evaluating famciclovir, zero literature — this candidate is more accurately **L5**, and the recommendation here is revised to **Hold**.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for famciclovir is not available in this dataset (data gap DG002). Based on established pharmacological knowledge, famciclovir is a prodrug of penciclovir: it is phosphorylated by viral (VZV/HSV) thymidine kinase and subsequently inhibits viral DNA polymerase, giving it direct antiviral activity against varicella-zoster virus (VZV) — the virus responsible for both chickenpox and, upon reactivation, herpes zoster (shingles).

Postherpetic neuralgia is the best-known complication of herpes zoster: persistent pain in the affected dermatome after the rash resolves. Because famciclovir suppresses VZV replication during the acute shingles episode, there is a plausible mechanistic pathway by which earlier/more effective antiviral treatment could reduce the incidence or severity of postherpetic neuralgia — an association also raised qualitatively in the evidence pack's own rationale text (citing, without including, the Tyring et al. Phase 3 literature).

However, the clinical trial evidence actually retrieved for this specific pairing does not test famciclovir: NCT03120962 evaluates oxycodone, and NCT06798662 evaluates nerve blockade/pulsed radiofrequency — both are disease-population matches only (relevance grade C), not drug evidence. By contrast, within the same evidence pack, "chickenpox" (rank 7, VZV infection broadly) has markedly stronger direct evidence — a completed Phase 3 RCT comparing famciclovir head-to-head against aciclovir (NCT01327144) and a completed Phase 3 pediatric PK/safety study (NCT00098046), plus 20 supporting literature records. That signal is closer to the drug's already-known antiviral spectrum than a genuinely novel indication, but it is far better substantiated than the top-ranked "post-infectious neuralgia" prediction and may warrant separate evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Tests early oxycodone (not famciclovir) during acute herpes zoster for PHN prevention; disease-population overlap only (relevance grade C) |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not yet recruiting | 120 | Tests multimodal nerve block/pulsed radiofrequency (liposomal bupivacaine, ropivacaine) for acute herpes zoster pain, not famciclovir; disease-population overlap only (relevance grade C) |

Neither trial evaluates famciclovir directly.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap in this evidence pack — DG001 — meaning a formal S1 safety screen cannot be completed until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and there is textbook-level mechanistic plausibility linking VZV-targeted antiviral therapy to reduced postherpetic neuralgia risk. However, none of the clinical trials retrieved for this pairing actually test famciclovir, and there is no supporting literature — the direct evidence base for *this specific* drug-disease pairing is effectively absent (L5).

**To proceed, the following is needed:**
- TFDA package insert / label warnings and contraindications (DG001, blocking — required before any safety screening)
- Confirmed original indication and mechanism-of-action data (DG002)
- Direct clinical evidence testing famciclovir specifically for postherpetic-neuralgia prevention (e.g., re-query literature to retrieve the Tyring et al. Phase 3 studies referenced qualitatively but not included in this evidence pack)
- Consider evaluating "chickenpox"/herpes zoster (rank 7) in parallel, given its substantially stronger direct evidence (completed Phase 3 head-to-head RCT vs. aciclovir, pediatric Phase 3 PK/safety study, 20 literature records)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


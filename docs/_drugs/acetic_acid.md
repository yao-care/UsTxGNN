---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 9
---

# Acetic Acid
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

The `txgnn-pipeline` skill confirms the project context. Now generating the evaluation report following the Drug Repurposing Evaluation Report Prompt (v5) specification.

---

# Acetic Acid: From Antimicrobial Agent to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a short-chain fatty acid (SCFA) with well-established use as a topical antimicrobial agent (e.g., dilute solutions for otitis externa and wound irrigation), though it carries no formally registered pharmaceutical indications in the current regulatory dataset.
The TxGNN model predicts it may have potential for **Post-Bacterial Disorder**, achieving a prediction score of **99.98%**.
However, no directly relevant clinical trials or published literature currently exist for this specific indication, yielding an **L5 evidence level** and a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of Registered Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetic acid (CH₃COOH) is a naturally occurring short-chain fatty acid produced endogenously by gut microbiota through anaerobic fermentation of dietary fiber. As an exogenous SCFA, dilute acetic acid (2–5%) lowers local pH and disrupts microbial membrane integrity, forming the basis of its decades-long clinical use as a topical antiseptic.

The theoretical bridge to post-bacterial disorder rests on the gut microbiome axis: acute bacterial infections frequently trigger severe gut dysbiosis, and SCFA levels — including acetate — are known to decline in post-infectious states. Restoring SCFA balance could, in principle, support microbiota recovery and modulate residual immune activation following bacterial infection. This is the network-level rationale the TxGNN model likely captures.

However, this mechanistic link is highly indirect and speculative. There is currently no established clinical pathway or controlled trial demonstrating that exogenous acetic acid administration benefits patients with post-bacterial disorder. The prediction should be interpreted as a hypothesis-generating signal rather than actionable clinical evidence.

---

## Clinical Trial Evidence

All retrieved trials carry **Grade C relevance** — none directly investigates acetic acid as a treatment for post-bacterial conditions. The table below lists the 10 closest related trials retrieved through keyword matching.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar (primary active: acetic acid) + Metformin vs. Metformin alone in newly diagnosed Type 2 Diabetics — the most direct acetic acid intervention retrieved |
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | Completed | 28 | SoftOx Biofilm Eradicator (hypochlorous acid, not acetic acid) safety & tolerability in chronic leg wounds; antimicrobial mechanism is analogous but agent differs |
| [NCT02872675](https://clinicaltrials.gov/study/NCT02872675) | N/A | Completed | 17 | HOST-DM059 prebiotic supplementation on gut bacterial metabolites and systemic inflammation in adults with/without exercise-induced bronchoconstriction; SCFA context indirectly relevant |
| [NCT04434365](https://clinicaltrials.gov/study/NCT04434365) | Phase 1/2 | Unknown | 24 | Berberine effects on gut microbiota remodeling and endothelial function in stable coronary artery disease; gut–SCFA pathway indirectly relevant |
| [NCT06612164](https://clinicaltrials.gov/study/NCT06612164) | N/A | Completed | 65 | Kefir consumption effects on gut health, immunity, and inflammation in healthy adults; fermented product contains acetic acid as a minor byproduct |
| [NCT07048028](https://clinicaltrials.gov/study/NCT07048028) | N/A | Recruiting | 90 | Chitosan vs. sodium hypochlorite as root canal irrigation antibacterials — antimicrobial theme relevant, no acetic acid involvement |
| [NCT04036318](https://clinicaltrials.gov/study/NCT04036318) | N/A | Completed | 3,022 | Presumptive periodic STI treatment in high-risk populations (Tanzania) — post-bacterial management context, no acetic acid use |
| [NCT07386795](https://clinicaltrials.gov/study/NCT07386795) | N/A | Not Yet Recruiting | 19 | Microbiota transplantation + prebiotics for functional constipation; indirect gut–SCFA relevance |
| [NCT06135116](https://clinicaltrials.gov/study/NCT06135116) | N/A | Completed | 60 | T-regulatory cells and related cytokines (IL-21/22/33) in periodontal disease progression; immune regulation background only |
| [NCT03619161](https://clinicaltrials.gov/study/NCT03619161) | N/A | Completed | 58 | Bleach baths vs. bubble baths for eczema — environmental antimicrobial control with distal relevance to antibacterial mechanisms |

---

## Literature Evidence

Currently no related literature available for post-bacterial disorder.

---

## Market Information

Acetic acid (DrugBank: DB03166) is not currently registered as a standalone pharmaceutical product. No approved indications, dosage forms, or license numbers are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is at L5 (model prediction only with no supporting clinical trials or literature), and the mechanistic link between acetic acid and post-bacterial disorder is highly indirect — current data cannot support advancement beyond hypothesis generation.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001:** Download and parse the regulatory package insert (TFDA/FDA) to obtain warnings, contraindications, and approved indications — currently blocking the S1 safety screening stage
- **Resolve Data Gap DG002:** Query the DrugBank API to retrieve full mechanism of action data, enabling mechanistic relevance analysis
- **Preclinical studies:** Direct in vivo SCFA/acetic acid supplementation studies in post-bacterial animal models are needed to establish proof of concept before clinical translation
- **Microbiome pathway mapping:** Identify measurable biomarkers (e.g., stool SCFA levels, microbiome diversity indices) that could serve as endpoints in a future pilot study
- **⚑ Consider reprioritizing to Tinea Corporis (Rank 9, L4):** This indication has substantially stronger evidence — a 2023 RCT comparing vinegar-based Terminalia chebula formulation vs. terbinafine 1% cream for tinea corporis ([PMID 37012894](https://pubmed.ncbi.nlm.nih.gov/37012894/)), plus multiple historical case series from the 1940s demonstrating efficacy of dilute acetic acid against related dermatophyte infections, plus a literature review on vinegar soak for tinea pedis/onychomycosis. This prediction carries a **Research Question** recommendation and may be a more productive near-term research focus
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


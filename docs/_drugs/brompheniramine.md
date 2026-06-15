---
layout: default
title: Brompheniramine
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 2
---

# Brompheniramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Brompheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation H1 receptor antagonist classically used for symptomatic relief of allergic rhinitis and common cold symptoms.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 clinical trials** and **0 publications** currently indexed in the query dataset — though this likely reflects data collection scope rather than a true evidence gap, as H1 antihistamines are first-line therapy for urticaria per international dermatology guidelines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, common cold symptoms (first-generation H1 antihistamine class) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (no NDA on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data inputs. Based on the drug class and repurposing rationale, brompheniramine is a first-generation H1 receptor antagonist — it works by competitively and reversibly blocking histamine H1 receptors, thereby preventing histamine-mediated vasodilation, increased vascular permeability, smooth muscle contraction, and pruritus.

Allergic urticaria (hives) is mechanistically driven by IgE-mediated mast cell degranulation, which releases large quantities of histamine that act on cutaneous microvascular H1 receptors — producing wheals (wind-rush plaques), flare, and itch. Brompheniramine directly blocks this pathway. The TxGNN score of 0.9987 (near perfect) is fully consistent with this mechanistic alignment; the model is essentially recognising a canonical drug-class effect rather than a novel repurposing leap.

It is important to note that zero clinical trial and literature hits in the query dataset almost certainly reflects data collection scope limitations rather than a genuine clinical evidence vacuum. H1 antihistamines — including first-generation agents such as brompheniramine, chlorpheniramine, and hydroxyzine — are the cornerstone first-line treatment for allergic urticaria in EAACI, AAD, and AAAAI guidelines. The prediction should therefore be interpreted as a confirmation of established pharmacology rather than a speculative repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the queried dataset for brompheniramine + allergic urticaria.

> **Note:** Absence of indexed trials reflects query scope. Broader searches using class-level terms (e.g., "first-generation antihistamine," "chlorpheniramine," "urticaria") would likely surface substantial Phase 3 evidence for the H1 antihistamine class as a whole.

---

## Literature Evidence

Currently no related literature available in the queried dataset for brompheniramine + allergic urticaria.

> **Note:** Same caveat as above — class-level PubMed queries for H1 antihistamines in urticaria management yield thousands of publications, including multiple systematic reviews and RCTs.

---

## US Market Information

No NDA records found for brompheniramine in the queried regulatory database.

> **Note:** Brompheniramine is widely available in the United States as an OTC ingredient in multi-symptom cold and allergy combination products (e.g., Dimetapp). It may be registered under OTC monograph frameworks rather than individual NDAs, which would explain the absence of records in an NDA-centric query.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All structured safety fields (key warnings, contraindications, drug–drug interactions) returned no data in this query cycle. As a first-generation antihistamine, known class-level concerns include sedation / CNS depression, anticholinergic effects (dry mouth, urinary retention, blurred vision), and potential QTc prolongation at high doses — prescribers should consult the current labelling before use.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN prediction is mechanistically sound and reflects established pharmacology; however, the current evidence pack contains no structured clinical trials, literature, or regulatory approval data for brompheniramine + allergic urticaria, yielding an L5 evidence level that is insufficient to support a formal repurposing recommendation without further documentation.

**To proceed, the following is needed:**

- **Expand literature search:** Run class-level PubMed queries (H1 antihistamines + urticaria) to confirm the expected body of clinical evidence and determine whether brompheniramine specifically has been studied versus class analogues only
- **Regulatory clarification:** Determine whether brompheniramine is covered under the US OTC antihistamine monograph (21 CFR Part 341) rather than individual NDAs, and document the relevant OTC approval pathway
- **MOA data:** Obtain full DrugBank MOA, pharmacodynamics, and toxicity profile to complete the mechanism-of-action analysis (DG002 remediation)
- **Safety data:** Download and parse the TFDA/FDA package insert to populate key warnings, contraindications, and drug interaction data (DG001 remediation)
- **Decision upgrade pathway:** If class-level evidence is confirmed (highly likely), this candidate could be upgraded to **Proceed with Guardrails** — the primary remaining gap is brompheniramine-specific trial data rather than a fundamental mechanistic question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


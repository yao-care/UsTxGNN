---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 1010
evidence_level: L5
indication_count: 10
---

# Paliperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

> Paliperidone (9-hydroxyrisperidone) is the active metabolite of risperidone and a D2/5-HT2A receptor antagonist already used as a standard antipsychotic for schizophrenia.
> The TxGNN model predicts it may extend to **Treatment-Refractory Schizophrenia**, a subpopulation of its own established indication,
> with **4 clinical trials** and **2 publications** currently supporting this direction.

**Note on screening:** TxGNN returned 10 candidate indications for this drug (ranks 1–10). Ranks 1–9 (e.g., retinal dystrophy, X-linked myopia, hydranencephaly, congenital glycosylation disorders) are rare structural/genetic disorders with **zero clinical trials, zero relevant literature, and no plausible mechanistic link** to paliperidone's D2/5-HT2A pharmacology — the evidence pack itself flags these as likely knowledge-graph artifacts (all scored **L5 / Hold**). Only **rank 10, treatment-refractory schizophrenia**, has actual supporting evidence and a mechanistically coherent rationale, so this report focuses on that candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (established use; per drug pharmacology — no Taiwan/US license record available in this pack) |
| Predicted New Indication | Treatment-Refractory Schizophrenia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa` = Data Gap). However, the evidence supporting rank 10 independently confirms that paliperidone is 9-hydroxyrisperidone, the active metabolite of risperidone, acting as a D2/5-HT2A receptor antagonist — a mechanism class already validated as first-line antipsychotic therapy.

This is not a conventional "old drug, new disease" repurposing case. Treatment-refractory schizophrenia is a **subpopulation of paliperidone's own existing indication (schizophrenia)**, not a mechanistically unrelated new disease. The prediction essentially asks whether an already-approved antipsychotic can be extended, with adequate monitoring, to patients who have failed standard therapy — a clinically familiar question rather than a novel mechanistic hypothesis.

By contrast, the other 9 TxGNN candidates for this drug (rare ophthalmic and neurogenetic structural disorders) have no biological rationale connecting D2/5-HT2A antagonism to their pathophysiology, and no trials or literature exist to support them. They are excluded from further consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating effectiveness of paliperidone palmitate across three schizophrenia patient groups |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared clozapine vs. non-clozapine antipsychotics (may include paliperidone) on inflammatory markers in treatment-resistant schizophrenia; terminated with very small sample |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates pharmacotherapy combined with new recovery-oriented programs for treatment-resistant schizophrenia and treatment-resistant bipolar disorder |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label multicenter RCT comparing aripiprazole vs. paliperidone/risperidone using multi-omics data in first-episode psychosis; status unconfirmed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews current psychopharmacology evidence for schizoaffective disorder, noting lack of specific treatment guidelines |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Reviews psychopharmacological interventions for early-onset schizophrenia spectrum disorders, including dosing and adverse effect management |

---

## US Market Information

PALIPERIDONE is currently **not marketed** under the licenses tracked in this evidence pack (0 NDAs on file, `market_status = 未上市`). No product/dosage-form records are available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DDI query status: not found; 0 interactions on record).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among the 10 TxGNN candidates, only treatment-refractory schizophrenia is supported by actual evidence (4 Phase 4 trials, 2 reviews) and a mechanistically coherent rationale, since it represents an extension of paliperidone's own approved use rather than an unrelated indication. However, no completed RCT specifically confirms superiority in the refractory subpopulation, and two of the four trials are terminated or of unknown status — evidence is directional, not conclusive.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (flagged as **Blocking** data gap — required before any S1 safety review)
- Formal mechanism-of-action documentation from DrugBank (High-priority data gap)
- Completion of DDI query and safety signal review
- Outcome data from NCT06060886 (status unknown) and completion of ongoing NCT07047651
- Confirmation of whether paliperidone (vs. only clozapine/other comparators) is specifically evaluated in NCT05741502
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Canakinumab
parent: Model Prediction Only (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Canakinumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Canakinumab: From Periodic Fever Syndromes to Hepatic Infarction

## One-Sentence Summary

Canakinumab is an anti-interleukin-1β (IL-1β) monoclonal antibody, originally used for autoinflammatory conditions such as cryopyrin-associated periodic syndrome, systemic juvenile idiopathic arthritis and gout.
The TxGNN model's top-ranked prediction is **hepatic infarction**, but this rests on model prediction alone, with **0 clinical trials** and **0 publications** supporting it.
The best-supported candidate among the top 10 predictions is **autosomal dominant familial Mediterranean fever** (3 Phase 3 trials and many publications), but this overlaps with an existing original indication and is not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory data. The knowledge graph lists gout, cryopyrin-associated periodic syndrome, systemic-onset juvenile idiopathic arthritis, juvenile idiopathic arthritis, mevalonate kinase deficiency, familial Mediterranean fever and related periodic fevers |
| Predicted New Indication | Hepatic infarction (rank 1) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, canakinumab is a monoclonal antibody that selectively neutralizes IL-1β. Its efficacy in IL-1-driven autoinflammatory diseases is established.

For hepatic infarction, the link is speculative. IL-1β blockade could plausibly reduce sterile inflammation after ischemic injury, but the data compiled for this report contains no trial, publication or mechanistic evidence directly connecting canakinumab to hepatic infarction. The same holds for the other top-ranked liver-related predictions (hepatic veno-occlusive disease, peliosis hepatis, liver angiosarcoma).

The most biologically coherent candidate is **familial Mediterranean fever, autosomal dominant** (rank 6, score 99.41%). The disease involves pyrin inflammasome dysregulation and excess IL-1β, which canakinumab directly targets. However, familial Mediterranean fever and autosomal dominant periodic fever are already among canakinumab's listed original indications, so this prediction largely confirms existing use.

Other predictions with some supporting literature:
- **Blau syndrome** (rank 8, L3): NOD2 gain-of-function granulomatous autoinflammation with IL-1β involvement, supported by case-level reports.
- **Syndrome with combined immunodeficiency** (rank 4, L4): only one infant case report in cryopyrin-associated periodic syndrome, an indirect link.
- **Monosomy X** (rank 9): the retrieved publications appear to be spurious matches.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (hepatic infarction). The table below shows trials for the best-supported candidate, familial Mediterranean fever, autosomal dominant (rank 6). Note that these trials enrolled cryopyrin-associated periodic syndrome (CAPS) patients, not FMF patients specifically.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | Open-label efficacy and safety study of canakinumab for 24 weeks in Japanese CAPS patients (FCAS, MWS, NOMID), with an extension phase |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Open-label extension study of long-term efficacy, safety and tolerability, plus childhood vaccination response, in CAPS |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Long-term open-label safety and efficacy study of canakinumab in CAPS; larger sample but not FMF-specific |

---

## Literature Evidence

Literature for the best-supported candidate, familial Mediterranean fever, autosomal dominant (rank 6), is shown below (selected). No literature was found for hepatic infarction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic review / meta-analysis | Rheumatology (Oxford) | Efficacy and safety of anti-IL-1 treatment in colchicine-resistant or -intolerant FMF |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic review | Front Immunol | Safety and efficacy of IL-1-targeted biologics (including canakinumab) in immune-mediated disorders |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Review | N Engl J Med | Canakinumab for recurrent fever syndromes including FMF, mevalonate kinase deficiency and TRAPS |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohort | Rheumatology (Oxford) | Feasibility of canakinumab withdrawal in paediatric colchicine-resistant FMF |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Real-life study | Rheumatol Int | Canakinumab effective in FMF resistant or intolerant to colchicine and/or anakinra |
| [42444147](https://pubmed.ncbi.nlm.nih.gov/42444147/) | 2026 | Real-world cohort | Rheumatology (Oxford) | AIDA Network data on effectiveness and probability of full disease control with canakinumab in FMF |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Review | Expert Rev Clin Immunol | Canakinumab in FMF: pyrin mutation, IL-1β regulation, use in colchicine-resistant patients |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Review | Clin Exp Rheumatol | IL-1 inhibition in FMF: clinical outcomes and expectations |

For Blau syndrome (rank 8), key items include a case report of clinical and transcriptional response to canakinumab in Blau-related uveitis ([23124805](https://pubmed.ncbi.nlm.nih.gov/23124805/), 2013) and a systematic review and meta-analysis of uveitis treatment ([40147219](https://pubmed.ncbi.nlm.nih.gov/40147219/), 2025).

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125319 | Ilaris (Novartis) | Injection, solution | Not stated in the data (status: cancelled) |
| Not available | GUNA-ANTI IL 1 (Guna spa) | Solution / drops | Not stated in the data (status: cancelled) |

Both authorizations are listed as cancelled; no currently valid license appears in the data compiled for this report.

---

## Safety Considerations

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Corticosteroids (Moderate):** hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone
- **Statin (Moderate):** simvastatin
- **Anticoagulants (Moderate):** apixaban, rivaroxaban, warfarin, dicoumarol
- **Radiopharmaceuticals / radioimmunotherapies (Moderate):** ibritumomab tiuxetan, iobenguane (I-131), tositumomab
- **Zinc salts (Minor):** zinc acetate, gluconate, sulfate

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, hepatic infarction)

**Rationale:**
Hepatic infarction and the other liver-related predictions have only model-based support (L5), with no trials, no literature and no established mechanistic link. The only prediction with strong evidence, familial Mediterranean fever (autosomal dominant), is essentially an existing indication, where a "Proceed with Guardrails" approach would apply (restrict to colchicine-resistant or intolerant patients and monitor for infections). Blau syndrome (L3) is a reasonable research question based on case-level evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism-of-action data for canakinumab
- Preclinical or mechanistic evidence linking IL-1β blockade to hepatic ischemic injury, if hepatic infarction is to be pursued
- Clarification of current US availability, since both licenses are cancelled
- For Blau syndrome, prospective or controlled data beyond case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


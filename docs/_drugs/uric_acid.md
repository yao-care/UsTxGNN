---
layout: default
title: Uric Acid
parent: Model Prediction Only (L5)
nav_order: 1277
evidence_level: L5
indication_count: 4
---

# Uric Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Uric Acid: From an Endogenous Metabolite (No Labeled Indication) to Rheumatoid Arthritis

## One-Sentence Summary

Uric acid is the end product of human purine metabolism. No original therapeutic indication is recorded for it in the US regulatory data.
The TxGNN model predicts it may be relevant to **rheumatoid arthritis** with a very high score, but the supporting literature treats uric acid only as a **biomarker**, never as a treatment, and **none of the retrieved clinical trials test uric acid as an intervention**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the US licenses) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 (association and biomarker studies only; no therapeutic study) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Uric acid is an endogenous purine metabolite with both antioxidant and pro-inflammatory properties. The direction of any effect in rheumatoid arthritis (RA) is unclear.

The literature links uric acid and its oxidation product allantoin to RA through oxidative stress, disease activity, RA-associated interstitial lung disease, cardiovascular risk and kidney stones. In every case uric acid is a marker or comorbidity signal, not an intervention. RA and gout also co-occur more often than once assumed, which may explain why the two diseases sit close together in the knowledge graph.

The high TxGNN score reflects graph proximity, not clinical support. Uric acid is not a plausible therapeutic agent for RA based on current data.

---

## Clinical Trial Evidence

None of the trials below test uric acid as an intervention. They matched on the disease term only. Most are RA studies of other agents (biologics, DMARDs, diet) or gout studies of other drugs.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03856190](https://clinicaltrials.gov/study/NCT03856190) | N/A | Terminated | 53 | Therapeutic fasting and specific diet in RA; uric acid is not the intervention |
| [NCT01258712](https://clinicaltrials.gov/study/NCT01258712) | Phase 3 | Completed | 86 | Tocilizumab plus methotrexate in moderate to severe RA |
| [NCT00048568](https://clinicaltrials.gov/study/NCT00048568) | Phase 3 | Completed | 1250 | Abatacept plus methotrexate vs methotrexate alone in RA |
| [NCT00461448](https://clinicaltrials.gov/study/NCT00461448) | Phase 1 | Completed | 36 | Potassium supplementation pilot in RA |
| [NCT05911880](https://clinicaltrials.gov/study/NCT05911880) | N/A | Unknown | 28 | Plant-based diet and RA activity |
| [NCT04033809](https://clinicaltrials.gov/study/NCT04033809) | N/A | Completed | 54 | High-fiber multigrain supplementation in RA |
| [NCT04953533](https://clinicaltrials.gov/study/NCT04953533) | N/A | Unknown | 800 | Gut microbiota and SNP study of intestinal uric acid excretion in gout and hyperuricemia (observational, not RA) |
| [NCT01078389](https://clinicaltrials.gov/study/NCT01078389) | Phase 2 | Completed | 314 | Febuxostat vs placebo on joint damage in hyperuricemic early gout (urate-lowering, not RA) |
| [NCT06186219](https://clinicaltrials.gov/study/NCT06186219) | Phase 1 | Completed | 2 | Rituximab pretreatment before methotrexate-pegloticase in tophaceous gout (not RA) |
| [NCT02332590](https://clinicaltrials.gov/study/NCT02332590) | Phase 3 | Completed | 369 | Sarilumab vs adalimumab monotherapy in RA |

---

## Literature Evidence

No randomized controlled trials were found. The papers are meta-analyses, reviews and observational cohorts of uric acid as a biomarker in RA.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37627564](https://pubmed.ncbi.nlm.nih.gov/37627564/) | 2023 | Meta-analysis | Antioxidants (Basel) | Systematic review of plasma/serum uric acid and allantoin levels in RA |
| [38699124](https://pubmed.ncbi.nlm.nih.gov/38699124/) | 2024 | Review | Cureus | Compares adenosine deaminase, CRP and uric acid biomarkers in RA vs non-arthritis patients |
| [39968300](https://pubmed.ncbi.nlm.nih.gov/39968300/) | 2025 | Review | Front Endocrinol | Links between serum urate and musculoskeletal disorders including RA, and the mechanisms behind them |
| [40710524](https://pubmed.ncbi.nlm.nih.gov/40710524/) | 2025 | Review | Metabolites | Uric acid, colchicine and cardiovascular risk in gout and RA |
| [21115462](https://pubmed.ncbi.nlm.nih.gov/21115462/) | 2011 | Review | Rheumatology (Oxford) | Uric acid and cardiovascular risk in RA (no abstract available) |
| [37650291](https://pubmed.ncbi.nlm.nih.gov/37650291/) | 2024 | Cohort | Clin Exp Rheumatol | Association of serum uric acid with all-cause and cardiovascular mortality in RA adults |
| [38026718](https://pubmed.ncbi.nlm.nih.gov/38026718/) | 2023 | Cohort | Open Access Rheumatol | Examines whether serum uric acid is associated with RA disease activity |
| [40837562](https://pubmed.ncbi.nlm.nih.gov/40837562/) | 2025 | Cohort | Front Med | Serum uric acid as a predictor of prognosis in RA-associated interstitial lung disease |
| [35314903](https://pubmed.ncbi.nlm.nih.gov/35314903/) | 2022 | Cohort | Inflammation | Serum uric acid as a diagnostic biomarker for RA-associated interstitial lung disease |
| [41582139](https://pubmed.ncbi.nlm.nih.gov/41582139/) | 2026 | Epidemiology/genetics | Arthritis Res Ther | RA and gout may coexist more often than assumed; epidemiological, genetic and molecular overlap |

---

## US Market Information

The five licenses are all liquid products, and none carries an approved indication text. License numbers are not listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Uric Acid (Professional Complementary Health Formulas) | Liquid | Not listed |
| Not listed | Bestmade Natural Products BM191 (Bestmade Natural Products) | Liquid | Not listed |
| Not listed | Bruise (Remedies Cure, LLC) | Liquid | Not listed |
| Not listed | Mycobacter/Mycoplasma Nosode (Professional Complementary Health Formulas) | Liquid | Not listed |
| Not listed | Large Joint Pain Drops (Professional Complementary Health Formulas) | Liquid | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on knowledge-graph proximity alone. The literature shows uric acid as an RA biomarker or comorbidity marker, with no interventional evidence and no plausible therapeutic mechanism. The other top predictions are weaker still. Colobomatous microphthalmia-rhizomelic dysplasia syndrome and brachydactyly-syndactyly syndrome have no trials or literature (L5), and bronchitis has only a keyword-driven match (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Mechanism of action data and the original indication for this record
- Evidence that raising or supplementing uric acid, rather than lowering it, has a therapeutic effect in RA
- Interventional studies of uric acid or urate modulation in RA, to replace the current association-only data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


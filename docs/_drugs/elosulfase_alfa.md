---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 647
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
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

# Elosulfase Alfa: From Morquio A Syndrome (MPS IVA) to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

> Elosulfase alfa (DrugBank DB09051) is a recombinant enzyme replacement therapy already known in the literature as the approved treatment for Morquio A syndrome (Mucopolysaccharidosis IVA, MPS IVA).
> Among 9 TxGNN-predicted indications reviewed, only **"lysosomal storage disease with skeletal involvement"** (TxGNN rank 2, score **99.59%**) maps mechanistically onto this known use, supported by **6 publications** (no registered clinical trials found under this exact disease label).
> The model's top-ranked candidate, Scheie syndrome, and five other high-scoring candidates (Hurler syndrome, Sanfilippo syndrome, and four ultra-rare congenital syndromes) were reviewed and found to lack any credible mechanistic or evidentiary link — most involve enzyme targets unrelated to GALNS, and several literature/trial hits are disease-label mismatches rather than genuine evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Morquio A Syndrome (MPS IVA) — per literature, not present in local regulatory license data |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement (clinically corresponds to MPS IVA/Morquio A) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L3 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured MOA data is not available in the regulatory data source (Data Gap DG002). However, based on the literature gathered for this evaluation, elosulfase alfa is a recombinant human N-acetylgalactosamine-6-sulfatase (GALNS) that directly replaces the enzyme deficient in Morquio A syndrome, breaking down the accumulated keratan sulfate and chondroitin-6-sulfate that drive the disease's progressive skeletal dysplasia.

The TxGNN-predicted label "lysosomal storage disease with skeletal involvement" is a broader disease-ontology term whose supporting literature is, in substance, entirely about MPS IVA/Morquio A — the drug's already-known approved use. This is therefore best read as a **confirmatory finding** (the model correctly recovering an established indication) rather than a novel repurposing opportunity, which is consistent with `original_indications` being an empty/unpopulated field in this evidence pack rather than a true absence of indication.

Of the other 8 predicted indications in this candidate set, none held up on review: Scheie syndrome, Hurler syndrome, and Sanfilippo syndrome are all caused by deficiencies in enzymes other than GALNS (alpha-L-iduronidase or heparan-sulfate-pathway enzymes), so there is no substrate or mechanistic overlap, and their attached literature/trial hits were found to be generic MPS cohort studies or unrelated Morquio A trial data rather than disease-specific evidence. The remaining four candidates (rare congenital ptosis/ocular-motility/Horner syndromes) are structural developmental disorders with no known link to GAG metabolism, no literature, and no trials — TxGNN score alone (L5, model prediction only).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41088244](https://pubmed.ncbi.nlm.nih.gov/41088244/) | 2025 | Review | Orphanet J Rare Dis | Reviews recent MPS IVA (Morquio A) treatment advances; confirms ERT with elosulfase alfa is currently the only approved treatment, noting its limited effect on bone pathology |
| [39541578](https://pubmed.ncbi.nlm.nih.gov/39541578/) | 2024 | Review (meta-analysis protocol) | JMIR Res Protocols | Protocol for phenotype-genotype correlation meta-analysis in Morquio A syndrome |
| [25496828](https://pubmed.ncbi.nlm.nih.gov/25496828/) | 2015 | Review/Clinical guidance | Mol Genet Metab | Diagnostic evaluation, monitoring, and perioperative management of spinal cord compression in Morquio syndrome |
| [38831290](https://pubmed.ncbi.nlm.nih.gov/38831290/) | 2024 | Cohort/Case series | BMC Med Genomics | Describes delayed diagnosis in mild/atypical MPS IVA presentations |
| [36000290](https://pubmed.ncbi.nlm.nih.gov/36000290/) | 2022 | Case report/genetic | Ann Hum Genet | Novel splicing variant identified in the GALNS gene in an MPS IVA patient |
| [25944767](https://pubmed.ncbi.nlm.nih.gov/25944767/) | 2015 | Diagnostic method study | Clin Chim Acta | Dried-leukocyte filter paper method for detecting Pompe, Gaucher, and Morquio A disease |

---

## US Market Information

Elosulfase alfa is not currently marketed in this jurisdiction (market status: 未上市, 0 licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN-predicted indication "lysosomal storage disease with skeletal involvement" is mechanistically direct and substantively corresponds to elosulfase alfa's known role as ERT for Morquio A syndrome/MPS IVA, but the evidence available here is limited to observational and mechanistic literature (L3) with no clinical trials retrieved under this exact disease label and no local regulatory or safety data. All other candidates in this evidence pack (Scheie, Hurler, Sanfilippo syndromes, and four rare congenital syndromes) failed mechanistic review and are recommended **Hold**.

**To proceed, the following is needed:**
- Confirm regulatory/label status for MPS IVA specifically (source: official prescribing information/TFDA equivalent), since `original_indications` is currently empty in this evidence pack
- Formal MOA field data from DrugBank (currently Data Gap DG002)
- TFDA warnings/contraindications (currently Blocking Data Gap DG001) before any safety assessment (S1) can proceed
- If pursuing skeletal-involvement LSDs beyond MPS IVA as a genuine new indication, disease-specific clinical trial search (current searches returned 0 trials)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


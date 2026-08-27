---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 836
evidence_level: L5
indication_count: 2
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase is a recombinant alpha-L-iduronidase enzyme replacement therapy, originally developed for mucopolysaccharidosis I (MPS I). The TxGNN model predicts it may also be relevant for **lysosomal storage disease with skeletal involvement**, but this predicted indication overlaps substantially with MPS I itself, and the current evidence base consists of **0 clinical trials** and **4 publications**, none of which directly study this as a distinct new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (MPS I) — derived from literature context; no TFDA license record exists (drug not marketed in Taiwan) |
| Predicted New Indication | Lysosomal Storage Disease with Skeletal Involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured DrugBank field (DG002). Based on the literature evidence collected, laronidase is a recombinant human alpha-L-iduronidase enzyme replacement therapy: it supplies the lysosomal enzyme that is deficient in MPS I, restoring the breakdown of accumulated glycosaminoglycans (GAGs) such as dermatan and heparan sulfate.

The predicted indication, "lysosomal storage disease with skeletal involvement," describes essentially the same disease process that laronidase already treats — MPS I itself is a lysosomal storage disorder with prominent skeletal manifestations (dysostosis multiplex, joint contractures, short stature). This is less a genuine repurposing signal than a related/overlapping disease-label match, which is consistent with the very high TxGNN score but limits its value as a "new" indication.

Note that the model's second-ranked candidate, Sanfilippo syndrome (MPS III), is caused by deficiency of different enzymes (heparan sulfate sulfatases, not alpha-L-iduronidase). Mechanistically, laronidase would not be expected to correct the enzymatic defect in Sanfilippo syndrome, so that candidate should be treated with more caution than the rank-1 prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15794739](https://pubmed.ncbi.nlm.nih.gov/15794739/) *(cross-referenced, rank-2 evidence set)* | — | — | — | *(not part of rank-1 evidence; see note below)* |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Drug profile of laronidase as recombinant alpha-L-iduronidase ERT for MPS I (Hurler syndrome); orphan drug/fast-track status, Phase I trial in 10 patients |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Overview of MPS I disease spectrum (Hurler, Scheie, Hurler/Scheie), diagnosis via urine GAGs and enzyme assay |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Preclinical | Biological & Pharmaceutical Bulletin | Laronidase uptake by MPS I fibroblasts/osteoblasts occurs via mannose-6-phosphate receptors, with lysosomal processing and substrate clearance — mechanistic basis for skeletal tissue effect |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Case report | Pediatric Neurology | 6.5-year follow-up of a Scheie syndrome patient on ERT; documented skeletal radiographs and disease progression despite treatment |

*(Note: only the 4 publications listed under predicted_indications[0] evidence are included above; the PMID 15794739 entry above was found only under the rank-2 Sanfilippo syndrome evidence set and is excluded from this table.)*

## Taiwan Market Information

Laronidase currently holds **no marketing authorization in Taiwan** (0 licenses on file; market status: 未上市 / Not marketed). No product name, dosage form, or approved indication text is available from TFDA records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TFDA warning/contraindication data is a blocking gap (DG001), and the predicted indication largely overlaps with the drug's already-established original indication (MPS I) rather than representing a clearly distinct repurposing opportunity — the evidence base is mechanistic/descriptive rather than trial-based for a genuinely new indication.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, blocking — required before any S1 safety review)
- Confirmed mechanism of action from DrugBank API (DG002)
- Clarification of whether "lysosomal storage disease with skeletal involvement" is clinically distinct from MPS I or a synonymous label
- If the rank-2 candidate (Sanfilippo syndrome) is pursued, mechanistic justification given the differing enzyme target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


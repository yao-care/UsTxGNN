---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 1194
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

# Tagraxofusp: From CD123+ Hematologic Malignancy to Pre-malignant Myeloid Neoplasm (MDS/CMML)

## One-Sentence Summary

Tagraxofusp is a CD123 (IL-3 receptor α)-targeted diphtheria toxin fusion protein used to eliminate CD123-expressing malignant cells, most notably in blastic plasmacytoid dendritic cell neoplasm (BPDCN) and AML blasts. Among the TxGNN candidates reviewed, the only prediction with actual clinical evidence is **pre-malignant neoplasm** (MDS/CMML), supported by **5 clinical trials** but **no dedicated publications**. The nine other top-ranked TxGNN predictions (esotropia, inner ear neoplasm, benign tongue neoplasm, etc.) have **no clinical trials and no relevant literature**, and are assessed as graph noise with no mechanistic plausibility — they are not carried forward in this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory data (drug not marketed in Taiwan); evidence-pack rationale text indicates approved use in CD123+ hematologic malignancies (BPDCN, AML) |
| Predicted New Indication | Pre-malignant neoplasm (MDS / CMML — CD123+ clonal disorders) |
| TxGNN Prediction Score | 99.73% (rank 2 of 10) |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for tagraxofusp is not yet available in our source database (flagged as a High-severity data gap). Based on information embedded in the evidence pack's own rationale text, tagraxofusp is a CD123 (IL-3Rα)-targeted diphtheria toxin fusion protein, designed to selectively kill CD123-expressing malignant cells such as BPDCN blasts and AML blasts.

Myelodysplastic syndrome (MDS) and chronic myelomonocytic leukemia (CMML) are widely regarded as pre-malignant/clonal myeloid disorders, and their blast populations frequently co-express CD123 — the same target exploited by tagraxofusp in its approved indications. This provides a mechanistically coherent rationale for extending tagraxofusp into earlier, pre-leukemic clonal disease, consistent with its established activity against CD123+ AML blasts.

By contrast, the model's top-ranked prediction (esotropia) and several other high-scoring candidates (inner ear neoplasm, benign tongue neoplasm, bronchial carcinoid, chondroid hamartoma, non-seminomatous lesion, cystic neoplasm, thyroglossal duct cyst) have no known CD123 biology and no supporting evidence — these should be treated as knowledge-graph artifacts rather than genuine repurposing signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06414681](https://clinicaltrials.gov/study/NCT06414681) | Early Phase 1 | Not Yet Recruiting | 20 | Tagraxofusp + pacritinib in intermediate-1+ myelofibrosis patients who failed/are unsuitable for JAK inhibitors; directly relevant to pre-malignant myeloid disease but not yet enrolling |
| [NCT05476770](https://clinicaltrials.gov/study/NCT05476770) | Phase 1 | Recruiting | 54 | Tagraxofusp ± chemotherapy in pediatric relapsed/refractory CD123+ hematologic malignancies; mechanism-relevant but population is confirmed malignancy, not strictly pre-malignant |
| [NCT03113643](https://clinicaltrials.gov/study/NCT03113643) | Phase 1 | Recruiting | 72 | SL-401 (tagraxofusp) + azacitidine in high-risk MDS, and + azacitidine/venetoclax in AML/BPDCN; MDS arm most directly supports the "pre-malignant" hypothesis |
| [NCT07148180](https://clinicaltrials.gov/study/NCT07148180) | Phase 1/2 | Recruiting | 31 | Tagraxofusp + azacitidine + venetoclax targeting measurable residual disease in AML; conceptually adjacent to early/subclinical disease but not a classic pre-malignant population |
| [NCT03386513](https://clinicaltrials.gov/study/NCT03386513) | Phase 1/2 | Active, Not Recruiting | 179 | Studies IMGN632 (a different CD123-targeted ADC), not tagraxofusp itself — mechanism-analogous evidence only |

---

## Literature Evidence

Currently no related literature available specifically addressing tagraxofusp in pre-malignant/MDS-CMML populations.

*(Note: 20 publications were retrieved under a separate TxGNN candidate, "ductular or ductular proliferation," but on review these concern hepatic ductular reaction/liver fibrosis biology and are unrelated to CD123/tagraxofusp mechanism — matched on the word "ductular" only. They are not included here.)*

---

## US Market Information

Tagraxofusp is not currently marketed in Taiwan — no license records are available for this drug in the regulatory database.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — CD123-targeted diphtheria toxin fusion protein (immunotoxin), distinct from conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a protein-toxin conjugate targeting malignant/pre-malignant hematologic cells, handling should follow institutional hazardous-drug protocols pending confirmation via official labeling |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data for tagraxofusp were not available in the source database at the time of this report (flagged as a Blocking data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only mechanistically plausible and evidence-supported prediction (pre-malignant neoplasm / MDS-CMML) is backed by just one not-yet-recruiting Early Phase 1 trial and two Phase 1 trials with indirect relevance (L2 evidence overall) — not sufficient to advance past a research-question stage. Critical safety data (TFDA/package-insert warnings and contraindications) is missing entirely, which blocks any S1 safety pre-assessment. The nine other top TxGNN-ranked indications lack any clinical or literature support and are assessed as graph noise.

**To proceed, the following is needed:**
- Package insert / official labeling data for warnings, contraindications, and drug interactions (DG001, Blocking)
- Confirmed mechanism-of-action and original-indication documentation from DrugBank or regulatory sources (DG002, High)
- Monitor enrollment status of NCT06414681 and maturation of NCT03113643 (MDS arm) for direct efficacy signal in pre-malignant disease
- Re-evaluate once literature specifically addressing tagraxofusp in MDS/CMML populations becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


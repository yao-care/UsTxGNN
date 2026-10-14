---
layout: default
title: Idelalisib
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# Idelalisib: From Chronic Lymphocytic Leukemia and B-Cell Lymphomas to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib is an oral PI3K-delta inhibitor, originally used for B-cell malignancies such as chronic lymphocytic leukemia/small lymphocytic lymphoma and follicular lymphoma.
The TxGNN model predicts it may be effective for **Mantle Cell Lymphoma**, with **5 clinical trials** (all early-phase) and **20 publications** (mostly reviews and preclinical studies) currently supporting this direction.
No confirmatory randomized trial exists for this indication, and the drug's only US license is now cancelled.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Follicular lymphoma, B-cell neoplasms, acute lymphoblastic leukemia, Richter syndrome, CLL/SLL (the US license text has no indication wording) |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 (as scored for this indication; see note below) |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* The mantle cell lymphoma trials are Phase 1 to Phase 2 studies, and the Phase 2 study was terminated. Under the strict rules (L2 requires a completed Phase 2/3 RCT), this evidence is closer to L3–L4. I therefore recommend Hold rather than advancing.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, idelalisib selectively inhibits the delta isoform of PI3K, which sits downstream of the B-cell receptor and supports the survival, proliferation and homing of malignant B cells.

Mantle cell lymphoma is a B-cell non-Hodgkin lymphoma that also depends on B-cell receptor and PI3K/AKT signaling. This is the same biology targeted in idelalisib's original indications (CLL/SLL and follicular lymphoma). Laboratory work shows idelalisib inhibits growth of mantle cell lymphoma cells through translation-regulatory mechanisms (PMID 27342398).

There are important caveats. Idelalisib shows intrinsic resistance in some mantle cell lymphoma models, and researchers are testing combinations (with P300/CBP inhibitors and CDK4/6 inhibitors) to overcome this. A resistance mechanism involving CBX5 loss has also been described.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Idelalisib combined with chemotherapy, immunomodulators and anti-CD20 antibody in relapsed/refractory indolent NHL, MCL or CLL; primary aim was safety |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1/2 | Completed | 106 | Idelalisib plus lenalidomide in relapsed/refractory MCL, with a randomized Phase 2 portion |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib plus idelalisib in relapsed/refractory hematologic malignancies including MCL; single-arm and stopped early |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 plus idelalisib in follicular lymphoma and MCL; dose-escalation safety study |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as maintenance after allogeneic stem cell transplant in B-cell malignancies; safety focus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | News/commentary | Cancer Discovery | Idelalisib was effective in heavily pretreated MCL patients |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clin Cancer Res | Idelalisib reduces MCL cell growth by inhibiting translation-regulatory mechanisms |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | p300/CBP inhibitor A-485 overcomes idelalisib resistance in MCL cells and in vivo |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Lett | Idelalisib enhances palbociclib's antitumor effect via PLK1 in B-cell lymphoma (DLBCL and MCL) |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ-inhibitor resistance in MCL; propolis restores sensitivity |
| [26841011](https://pubmed.ncbi.nlm.nih.gov/26841011/) | 2016 | Review | Cancer J | Idelalisib and PI3K pathway targeting in non-Hodgkin lymphoma |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Toxicity incidence and management with ibrutinib and idelalisib |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Current regimens and novel agents for MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opin Pharmacother | Treatment options for MCL |
| [36297673](https://pubmed.ncbi.nlm.nih.gov/36297673/) | 2022 | Preclinical | Pharmaceutics | ROR1 inhibitor and other agents, including idelalisib, tested alone and in combination in MCL cells |

No randomized controlled trial for mantle cell lymphoma appears in the literature retrieved.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205858 | Zydelig (Gilead Sciences) | Film-coated tablet | Not specified in the data; status: cancelled |

The product is oral only. One published review (PMID 36939665) notes that serious adverse effects reported in 2016 led to termination of post-marketing registry trials, and that Gilead voluntarily withdrew the drug for the accelerated approval indication in 2022.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-delta kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typical oncology monitoring includes CBC, liver function tests and assessment for diarrhea and respiratory symptoms |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

Related findings from the evidence: the data notes that the label carried serious toxicity warnings (hepatotoxicity, severe diarrhea/colitis, pneumonitis, infections). Several Phase 3 trials in earlier-line CLL and indolent NHL were stopped after the independent monitoring committee saw increased deaths and serious adverse events.

**Drug Interactions:** The interaction screen returned 100 interactions in total; the 20 listed in the data compiled for this report are mostly Moderate. The Major-level ones among them are:
- Loperamide
- Triamcinolone
- Budesonide
- Eliglustat

Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone), clarithromycin, aprepitant, bupropion, pioglitazone, acarbose, saxagliptin, doxycycline and minocycline. The full list should be reviewed before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mantle cell lymphoma evidence consists of early-phase combination studies (one terminated), plus preclinical and review literature, with no confirmatory randomized trial. Idelalisib's sole US license is cancelled, and it carries serious toxicity concerns (hepatotoxicity, colitis, pneumonitis, infections). Newer BTK inhibitors are already established in mantle cell lymphoma (e.g., ibrutinib), which weakens the case for a PI3K-delta inhibitor with this safety profile.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Efficacy and response-rate results from the MCL-specific trials (NCT01838434 in particular)
- A comparison against current standard MCL therapies, including BTK inhibitors
- A risk-benefit assessment given the withdrawal history and serious toxicity profile
- Regulatory feasibility review, since the NDA is cancelled

**Other predictions in this analysis (for reference):**
- **B-cell neoplasm** has the strongest evidence (multiple Phase 3 trials, including ASCEND and BRUIN CLL-321, which used idelalisib plus rituximab as a comparator). However, this is largely the drug's original indication class, so it is not true repurposing.
- **Hodgkin lymphoma, myeloid leukemia, chronic myelogenous leukemia, familial NHL, and colon adenocarcinoma** have only indirect, preclinical or very limited evidence.
- **CLL/SLL subtypes and small intestinal Burkitt lymphoma** are computational predictions with no supporting studies.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 1284
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor (VEGFR2/3, EGFR, RET) whose established oncology use is in medullary thyroid cancer, based on evidence found in this pack's literature set.
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**,
with **4 clinical trials** and **6 publications** currently supporting this direction — though two of the four trials were terminated early with very small enrollment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Medullary Thyroid Cancer (MTC) — no formal license record on file; inferred from literature evidence (PMID 24451769, 32691271) |
| Predicted New Indication | Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal `original_moa` record is not available (flagged as a High-severity data gap, DG002). Based on the mechanistic description captured in this evidence pack's repurposing rationale, vandetanib is a multi-target tyrosine kinase inhibitor that blocks VEGFR2/3, EGFR, and RET. VEGFR2 inhibition is a well-established anti-angiogenic strategy already used in RCC treatment (e.g., sunitinib, pazopanib, cabozantinib), so vandetanib's mechanism overlaps meaningfully with drugs already approved for this indication — a plausible "class effect" extension.

Clear cell RCC in particular is driven by VHL gene inactivation → HIF accumulation → VEGF overexpression, making it the RCC subtype with the strongest biological rationale for a VEGFR-targeted agent. This is reflected in the trial evidence: the largest completed study in this evidence set enrolled VHL-disease-associated renal tumor patients (NCT00566995, n=37).

However, mechanistic plausibility is undercut by execution: two of the four directly relevant trials were terminated with only 3 and 7 patients enrolled respectively, and the only trial with meaningful enrollment for a general RCC population (NCT01191892, n=82) was actually designed for urothelial cancer, raising disease-match uncertainty. Vandetanib itself has not demonstrated superiority over already-approved RCC TKIs in any completed trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in Von Hippel-Lindau disease and renal tumors; VEGFR2 mechanism highly relevant to VHL-driven RCC |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Directly targeted advanced clear cell RCC; terminated after only 3 patients, feasibility/safety signal unclear |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin in HLRCC/SDH-associated or sporadic papillary RCC; terminated with limited enrollment |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized carboplatin/gemcitabine ± vandetanib; designed for advanced urothelial cancer, not classic RCC — disease-match uncertain |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) | 2012 | Meta-analysis | Cancer Treat Rev | Treatment-related mortality risk across VEGFR-TKI class (including vandetanib) in solid tumors |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeted therapy approaches in fumarate hydratase-deficient RCC; no established standard regimen |
| [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/) | 2020 | Review/Meta-analysis | Expert Rev Clin Pharmacol | Proteinuria risk associated with VEGFR-TKIs including vandetanib |
| [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/) | 2014 | Review/Meta-analysis | Br J Clin Pharmacol | Hepatic toxicity incidence and risk across anti-angiogenic TKIs |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3-translocation RCC model identifies novel therapeutic targets and diagnostic marker |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Class overview of antiangiogenic TKIs (nintedanib, sunitinib, sorafenib, pazopanib, vandetanib) in solid tumors |

---

## US Market Information

No NDA or license records are currently on file for vandetanib in this jurisdiction (`total_licenses: 0`). The drug is not currently marketed here.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2/3, EGFR, RET) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Not directly reported in this evidence pack; literature-cited toxicities for this drug class center on hepatotoxicity, proteinuria, and treatment-related mortality rather than classic myelosuppression |
| Emetogenicity Classification | Low to Moderate (typical of oral small-molecule TKIs) |
| Monitoring Items | Liver function tests (per PMID 23981115), renal function/urinalysis for proteinuria (per PMID 32105149), general tolerability monitoring given class-wide treatment-related mortality signal (PMID 22651902) |
| Handling Protection | Standard oral oncology drug handling precautions recommended; not a conventional cytotoxic infusion agent |

---

## Safety Considerations

Please refer to the package insert for safety information — official warnings, contraindications, and DDI data are marked as a Blocking data gap (DG001) in this evidence pack and could not be retrieved.

**Literature-derived safety signals** (from class-wide TKI studies, not vandetanib-specific label data):
- Hepatotoxicity incidence across anti-angiogenic TKIs (PMID 23981115)
- Proteinuria risk associated with VEGFR-TKIs (PMID 32105149)
- Treatment-related mortality risk across the VEGFR-TKI class (PMID 22651902)
- One literature title in the broader search directly flags vandetanib toxicity concerns in its established oncology indication ("Vandetanib: too dangerous in medullary thyroid cancer", PMID 23185843), though this trial-related literature was surfaced for a different indication context and should be independently verified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The VEGFR2-driven mechanistic rationale for RCC is biologically sound and supported by one completed Phase 2 trial in VHL-associated renal tumors (n=37), but two of the four directly relevant trials terminated early with very small enrollment (n=3, n=7), and the drug's official safety documentation (warnings, contraindications, DDI) is a Blocking data gap that prevents completion of the required S1 safety review.

**To proceed, the following is needed:**
- Retrieve official label/regulatory safety documentation (warnings, contraindications, DDI) — currently Blocking (DG001)
- Retrieve a formal, sourced mechanism-of-action record rather than relying on inferred rationale text (DG002)
- Clarify the reasons NCT01372813 (n=3) and NCT02495103 (n=7) were terminated early — safety-driven vs. enrollment failure
- Confirm disease-population match for NCT01191892, which was designed for urothelial rather than classic RCC
- If advancing past Hold, prioritize newer, adequately powered trials specific to clear cell or VHL-driven RCC rather than relying on trials completed a decade or more ago
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


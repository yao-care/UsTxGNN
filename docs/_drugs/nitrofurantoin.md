---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 971
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

> Nitrofurantoin is a nitrofuran-class antibacterial generally used for urinary tract infections (specific original-indication text is not present in this evidence pack). The TxGNN model assigns its top-ranked candidate — **Rheumatoid Arthritis** — a raw score of **99.89%**, but the accompanying evidence review found **no clinical trials** and only indirect, largely safety-related literature, with the reviewer explicitly flagging the mechanistic link as implausible and in some respects contradictory to the treatment hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (`original_indications` empty; nitrofurantoin is generally used as a urinary tract antibacterial) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% (rank 3524) |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Nitrofurantoin's mechanism, as captured in the reviewer's rationale, relies on bacterial nitroreductase enzymes converting the drug into reactive intermediates that damage bacterial DNA and ribosomal machinery — a mechanism confined to bacterial cells, with no known immunomodulatory or anti-inflammatory activity relevant to autoimmune disease.

Rheumatoid arthritis is a systemic autoimmune/synovial inflammatory disease driven by cytokine dysregulation and autoantibody production. No pharmacological pathway connects nitrofurantoin's antibacterial action to RA pathogenesis, and the evidence reviewer explicitly classified this candidate as having **"no reasonable mechanism"** (無合理機轉).

More notably, the retrieved literature points in the *opposite* direction: several case reports and reviews document nitrofurantoin-induced pulmonary fibrosis and autoimmune hepatitis — including one case occurring specifically in an RA patient on concurrent methotrexate. Rather than supporting a therapeutic role, this body of evidence suggests nitrofurantoin may add risk in RA patients rather than benefit. The same pattern holds across the other nine ranked candidates in this evidence pack: none show a supportive mechanistic or clinical trial signal, and two (methemoglobinemia, alpha type / methemoglobinemia) are in fact **known adverse effects of nitrofurantoin**, meaning the model has surfaced its own toxicity profile as a "predicted indication." This is consistent with a high-confidence but low-plausibility TxGNN output — the model's score should not be read as clinical evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled case series | Scientific Reports | Examined antibiotic exposure and RA flare timing in 31,992 UK RA patients (CPRD GOLD); no nitrofurantoin-specific therapeutic signal for RA identified. |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Describes poor prognosis in RA patients hospitalized for interstitial lung fibrosis; unrelated to nitrofurantoin as a treatment. |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria in a middle-aged female population; no RA relevance (abstract unavailable). |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | Irreversible pulmonary fibrosis from a methotrexate–nitrofurantoin interaction in an RA patient — a documented safety hazard, not a therapeutic signal. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Reviews drug-induced pulmonary fibrosis; lists nitrofurantoin among causative agents and notes RA itself predisposes to fibrosis. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Reviews drug-induced interstitial lung disease; nitrofurantoin listed among causative antibiotics. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de dermatologie et de venereologie | Case of phenylbutazone-induced sialadenitis; nitrofurantoin mentioned only incidentally as another associated drug. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Autoimmune hepatitis case; nitrofurantoin listed among drugs to rule out as a cause, not as a treatment. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de pneumologie clinique | Gold-salt-induced pneumonitis case; no direct nitrofurantoin-RA treatment link. |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | General synopsis of alveolitis/pulmonary fibrosis (abstract unavailable). |

---

## US Market Information

Currently no marketing authorization records available. `taiwan_regulatory.total_licenses = 0`; the drug is recorded as **not marketed** (未上市) in this jurisdiction's regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information (`key_warnings`, `contraindications`, and DDI data are all unavailable in this evidence pack — flagged as **DG001, Blocking severity**).

Separately, the literature retrieved for this candidate (not sourced from the formal safety fields, but worth flagging) repeatedly documents nitrofurantoin-associated pulmonary fibrosis, autoimmune hepatitis, hemolytic anemia, and methemoglobinemia — these are adverse-reaction signals, not efficacy evidence, and should inform any future safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN raw score (99.89%), there is no clinical trial evidence, no mechanistic rationale, and the retrieved literature largely documents adverse/opposite-direction signals rather than therapeutic potential. This pattern holds across all 10 ranked candidates in this evidence pack — none reached beyond Evidence Level L5/L4 or moved past decision stage S0, and two other top-10 candidates (methemoglobinemia, alpha type; methemoglobinemia) are actually known nitrofurantoin toxicities rather than genuine indications. Additionally, TFDA safety/contraindication data (DG001) is a **Blocking** data gap that independently prevents any S1 safety screening regardless of efficacy evidence.

**To proceed, the following is needed:**
- A genuine mechanistic hypothesis linking nitrofuran antibacterial activity to RA/autoimmune inflammatory pathways (none currently exists)
- Prospective or controlled clinical data, rather than case reports and reviews, before this candidate could be re-scored
- Resolution of DG001 (TFDA warnings/contraindications) and DG002 (MOA) before any downstream safety or regulatory assessment can begin
- Given the consistently negative rationale across all 10 candidates, consider whether this candidate should be deprioritized from further TxGNN pipeline review entirely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Oxacillin
parent: 僅模型預測 (L5)
nav_order: 998
evidence_level: L5
indication_count: 4
---

# Oxacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxacillin: From Staphylococcal Infections to Epiglottitis

## One-Sentence Summary

Oxacillin is a narrow-spectrum, penicillinase-resistant penicillin used to treat infections caused by methicillin-susceptible *Staphylococcus aureus* (MSSA). The TxGNN model's top-ranked prediction points to a possible link with **Epiglottitis**, but this is currently supported only by **0 clinical trials** and **3 case-report-level publications**, indicating a mechanism-based, very preliminary signal rather than established evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Staphylococcal (MSSA) infections — narrow-spectrum, penicillinase-resistant penicillin (no formal approved-indication text on file; drug currently not marketed in Taiwan) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action documentation is not yet available for this candidate (flagged as a High-severity data gap, DG002). Based on pharmacological information captured in the evidence pack, oxacillin is an antistaphylococcal penicillin that inhibits penicillin-binding proteins (PBPs), blocking bacterial cell wall synthesis and producing a bactericidal effect against MSSA.

Epiglottitis is classically caused by *Haemophilus influenzae*, streptococci, and only occasionally by staphylococci. Oxacillin's mechanism is therefore only relevant in the subset of epiglottitis cases where a staphylococcal pathogen is confirmed — it is not a standard first-line treatment for epiglottitis in general, and the underlying literature reflects sporadic case reports rather than pathogen-directed treatment studies.

Notably, the same evidence pack contains a stronger, more clinically grounded signal further down the ranking: for **bacterial arthritis** (rank 3), oxacillin's role is described as "one of its historically core uses" for MSSA septic arthritis rather than a novel repurposing candidate, and it carries better evidence (L3, decision stage S2, "Research Question"). This is discussed further in the closing section.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3380744](https://pubmed.ncbi.nlm.nih.gov/3380744/) | 1988 | Case Report | Pediatric Emergency Care | Unusual epiglottitis case in a child with asthma; failed to respond to aggressive asthma therapy, intubation revealed acute epiglottitis requiring appropriate antibiotic management |
| [4999568](https://pubmed.ncbi.nlm.nih.gov/4999568/) | 1971 | Case Series/Review | British Medical Journal | Review of epiglottitis presentation and management in adults |
| [990756](https://pubmed.ncbi.nlm.nih.gov/990756/) | 1976 | Case Report | British Medical Journal | Acute epiglottiditis in an adult requiring tracheostomy |

---

## Taiwan Market Information

Oxacillin is currently **not marketed** in Taiwan (0 licenses on file). No NDA/registration records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications are pending retrieval — flagged as a Blocking data gap, DG001, required before any S1 safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (epiglottitis) is supported only by mechanistic plausibility and three case-report-level publications, with no clinical trials and no confirmation that staphylococcal pathogens drive typical epiglottitis presentations. Combined with the drug's non-marketed status in Taiwan and missing safety label data, evidence is insufficient to advance.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap DG001) before any safety screening
- Formal DrugBank MOA confirmation (High-priority gap DG002)
- Pathogen-confirmed (staphylococcal) case series or comparative studies specific to epiglottitis
- Regulatory feasibility assessment given oxacillin's current non-marketed status in Taiwan

**Note on alternative candidate:** Among the four indications predicted for this drug, **bacterial arthritis** (rank 3, L3, decision stage S2, "Research Question") is substantially better supported — it reflects oxacillin's established historical role in treating MSSA septic arthritis, with two relevant Phase 4 trials (NCT04141787, NCT04563325) and directly related cohort literature (e.g., PMID 25672426 on oxacillin-sensitive vs. -resistant *S. aureus* joint infections). This may warrant separate follow-up as a "confirm existing use" track rather than a novel repurposing hypothesis. The other two candidates (laryngitis, urinary tract infection) show weak, largely indirect evidence and are also recommended for **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


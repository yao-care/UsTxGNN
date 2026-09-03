---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 1099
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

> Pyrazinamide is a first-line anti-tuberculosis agent, standard therapy for pulmonary and extrapulmonary tuberculosis as part of multi-drug regimens.
> The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
> but this top-ranked prediction currently has **0 clinical trials** and **0 publications** supporting it directly — the score reflects graph proximity to the tuberculosis node only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (pulmonary and extrapulmonary) — no formal license text available; drug is not currently marketed in the evaluated jurisdiction |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on the mechanistic notes captured elsewhere in this evidence pack, pyrazinamide is a prodrug that is only active against *Mycobacterium tuberculosis* within the acidic environment of macrophage phagosomes, and it is used exclusively as part of standard multi-drug anti-tuberculosis regimens (typically with rifampicin and isoniazid). This mechanism is highly pathogen-specific and does not confer general antibacterial activity against the organisms that typically cause otitis media (e.g., *Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*).

The top-ranked prediction, "Infectious Otitis Media," has **no clinical trial or literature evidence** attached to it. According to the model's own rationale note, the mechanistic link is inferred purely from the graph's proximity to the tuberculosis node, without independent validation — this is explicitly flagged as unconfirmed.

Notably, several **adjacent, lower-ranked predictions** in this same evidence pack (rank 2 "middle ear disease," rank 4 "chronic otitis media," rank 5 "suppurative otitis media") are supported by case-report literature describing *tuberculous otitis media (TOM)* — a rare but recognized extrapulmonary manifestation of TB in which pyrazinamide is already used as part of standard anti-TB therapy (e.g., PMID 26785789 documents pyrazinamide 25 mg/kg alongside rifampicin and isoniazid for 9 months). This suggests the TxGNN model may be capturing a real but narrow signal — TB spreading to the middle ear — rather than a genuinely new mechanism for general infectious otitis media. The rank-1 prediction itself, however, remains unsupported and should not be conflated with this TB-specific subgroup.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorizations currently on record (`total_licenses = 0`). Pyrazinamide's status in the evaluated jurisdiction is recorded as **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug interaction data are all currently unavailable — flagged in this evidence pack as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Infectious Otitis Media) has zero clinical trial or literature support — it is a pure TxGNN graph-proximity score with no independent validation, and the model's own rationale acknowledges this. Combined with a Blocking gap on TFDA-equivalent label safety data (DG001) and missing MOA confirmation (DG002), the candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety evaluation
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Clarify whether "Infectious Otitis Media" is intended to capture the narrower, evidence-supported entity of *tuberculous otitis media* (see rank 2/4/5 predictions) — if so, re-scope the candidate around that better-validated extrapulmonary TB manifestation rather than general infectious otitis media
- Independent literature search specific to pyrazinamide (not just TB-otitis case reports as a class) before any evidence-level upgrade
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

The `txgnn-pipeline` skill covers pipeline operations rather than report writing — the detailed output format is already specified in this conversation's system prompt. I'll proceed with generating the evaluation report from the Evidence Pack.

---

# Acyclovir: From Herpes Simplex Virus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is a first-generation antiviral drug, established for treating herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections including genital herpes, cold sores, chickenpox, and shingles.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
with **0 clinical trials** and **2 publications** currently supporting this direction — an early-stage mechanistic signal that requires substantial further validation before clinical translation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HSV/VZV infections (no local license data available in this dataset) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed (Taiwan TFDA: 0 registered licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Acyclovir is a nucleoside analogue prodrug that requires activation by the herpesvirus-encoded thymidine kinase (TK). Once phosphorylated to acyclovir triphosphate by viral TK and host cell kinases, it competitively inhibits viral DNA polymerase — selectively blocking HSV-1, HSV-2, and VZV replication while posing minimal toxicity to host cells. This TK-dependent selectivity is both its strength and its limitation.

Punctate epithelial keratoconjunctivitis (PEK) is a condition characterized by scattered inflammatory lesions on the corneal surface and conjunctiva. HSV-1 and HSV-2 are recognized causative agents of PEK, and since Acyclovir directly targets HSV through the TK-activation pathway, there is a mechanistically coherent rationale for its use in **HSV-induced PEK specifically**. This is further supported by Acyclovir's proven efficacy in related HSV ocular conditions — herpetic dendritic keratitis, stromal keratitis, and iridocyclitis — documented in the landmark Herpetic Eye Disease Study (HEDS), suggesting a plausible extension within the same disease family.

However, the prediction carries a critical limitation: PEK is etiologically heterogeneous. Causative agents include adenovirus, microsporidia, toxic drug reactions, and dry eye disease — none of which Acyclovir can address. Neither supporting publication directly validates Acyclovir for PEK: PMID 7825685 describes drug-induced corneal lipidosis in AIDS patients (a distinct pathology), and PMID 21934222 documents microsporidial keratoconjunctivitis caused by a protozoan parasite rather than a virus. The TxGNN model likely captures the broader HSV–keratoconjunctivitis co-occurrence pattern rather than PEK-specific evidence. Pathogen confirmation is a prerequisite before any repurposing attempt.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Cohort/Case Series | American Journal of Ophthalmology | Two AIDS patients receiving opportunistic infection treatment developed bilateral ocular surface changes consistent with drug-induced corneal lipidosis; not a direct study of Acyclovir in PEK |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian Journal of Pathology & Microbiology | Case series of microsporidial keratoconjunctivitis (protozoan etiology) in immunocompetent individuals; illustrates that keratoconjunctivitis frequently has non-HSV causes, underscoring the need for pathogen-specific diagnosis before considering antivirals |

---

## Taiwan Market Information

No registered products found. The Taiwan TFDA database records 0 license entries for Acyclovir in this dataset.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No records available |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (99.67%), the evidence for Acyclovir in punctate epithelial keratoconjunctivitis is limited to 2 indirect publications (L4) and zero clinical trials. The mechanistic rationale applies only to the HSV-induced subset of PEK — a distinction the current evidence does not confirm — and no clinical data exists to establish efficacy or safety in this specific indication.

**To proceed, the following is needed:**
- **Etiology confirmation**: Prospective patients must have HSV-confirmed PEK (by PCR or viral culture) before Acyclovir is considered; adenoviral or microsporidial PEK should be excluded
- **Pilot clinical evidence**: A prospective case series or Phase 2 pilot study evaluating topical ophthalmic Acyclovir (or oral Acyclovir/Valacyclovir) in HSV-induced PEK
- **MOA documentation**: Retrieve DrugBank API data to formally document the TK-phosphorylation mechanism and close the existing data gap
- **Safety data**: Obtain Taiwan TFDA package insert to assess contraindications, renal monitoring requirements, and local prescribing restrictions

> **Note on higher-priority indications**: Other TxGNN predictions for Acyclovir carry substantially stronger evidence and should be prioritized for near-term evaluation: **Common Wart** (Rank 2 — L2, 6 clinical trials including a Phase 2/3 RCT [NCT06261684], 2 direct RCTs in the literature); **Post-infectious Neuralgia** (Rank 3 — L2, 12 trials via Valacyclovir/Acyclovir on postherpetic neuralgia prevention); and **Disease of Orbital Region** (Rank 9 — L1, anchored by the Herpetic Eye Disease Study Phase 3 landmark trials). These represent more actionable repurposing opportunities with established biological plausibility.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


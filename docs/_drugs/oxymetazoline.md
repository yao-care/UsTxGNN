---
layout: default
title: Oxymetazoline
parent: 僅模型預測 (L5)
nav_order: 1005
evidence_level: L5
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxymetazoline: From Nasal Congestion (OTC Decongestant) to Nasal Cavity Disease

## One-Sentence Summary

> Oxymetazoline is a topical α1/α2-adrenergic agonist widely known as an over-the-counter nasal decongestant, though a formal original indication text is not available in the current evidence pack.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
> with **18 clinical trials** and **5 publications** currently supporting this direction — several of which test oxymetazoline directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset; well-established clinical use is as a topical nasal decongestant (OTC) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on well-established pharmacological knowledge, oxymetazoline is a topical α1/α2-adrenergic receptor agonist that induces vasoconstriction of the nasal mucosal vasculature, reducing mucosal congestion and secretions. This is the same mechanism underlying its long-standing OTC use as a nasal decongestant.

The predicted new indication — "nasal cavity disease" — is mechanistically almost coextensive with this known pharmacological action: conditions involving nasal mucosal congestion, edema, and obstruction. Rather than representing a distant repurposing hypothesis, this prediction largely reaffirms the drug's existing pharmacological class effect, which is directly supported by clinical trial evidence (e.g., a completed Phase 2 RCT on nasal congestion relief, and a trial directly testing 0.05% oxymetazoline against epinephrine before sinus surgery).

Because no formal original indication or licensed product record exists in this jurisdiction (market status: Not Marketed, 0 licenses), this candidate should be treated as a potential new market-entry/repurposing target requiring formal regulatory documentation, rather than a novel mechanistic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Directly compares topical 0.05% oxymetazoline vs. 1:1000 epinephrine for blood loss and surgical field visualization prior to endoscopic sinus surgery |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, double-dummy, placebo-controlled, 4-way crossover study using nasal allergen challenge and acoustic rhinometry to assess nasal congestion relief |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | N/A | Completed | 16 | Acoustic rhinometry study using 0.05% oxymetazoline aerosol spray for nasal decongestion, evaluating rhinogram notches |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Compares co-phenylcaine nasal spray (decongestant + local anesthetic) vs. nebulization prior to rigid nasoendoscopy |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind study evaluating topical anesthesia and/or decongestant pretreatment for comfort during fiberoptic nasal pharyngoscopy/laryngoscopy |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple-crossover comparison of cocaine, lidocaine/xylometazoline (decongestant class), and saline for intranasal analgesia |
| [NCT00147940](https://clinicaltrials.gov/study/NCT00147940) | Phase 4 | Terminated | 20 | Correlates nasal volume/cross-sectional area with nasalance scores via acoustic rhinometry and nasometry |
| [NCT01974726](https://clinicaltrials.gov/study/NCT01974726) | NA | Terminated | 95 | Evaluates Eustachian tube function tests in patients with middle-ear disease related to nasal/nasopharyngeal pathology |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Compares Kovanaze (nasal mist anesthetic/decongestant combination) vs. articaine injection for dental pulpal anesthesia |
| [NCT00015795](https://clinicaltrials.gov/study/NCT00015795) | Phase 1 | Completed | 30 | Investigates laryngeal airflow/resistance in abductor spasmodic dysphonia vs. healthy volunteers |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Cohort | Annals of the New York Academy of Sciences | Assessed olfactory function changes and nasal volume (via acoustic rhinometry) during acute rhinitis |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohort | Journal of Plastic Surgery and Hand Surgery | Evaluated nasal patency by acoustic rhinometry in children with repaired cleft lip/palate vs. controls |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal (Preclinical) | Annals of Otology, Rhinology & Laryngology | Directly tested oxymetazoline nose drops' effect on local tissue defense in experimental rabbit sinusitis |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Global Pediatric Health | Rare pediatric case of rhinoscleroma presenting with nasal obstruction |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case series | American Journal of Rhinology & Allergy | Describes endoscopic coblation technique for nasal telangiectasias in hereditary hemorrhagic telangiectasia |

---

## US Market Information

Currently no marketing authorization or license records are available for this drug in this jurisdiction (market status: Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are flagged as a blocking data gap — DG001 — and drug interaction data was queried but not found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT and a trial directly testing oxymetazoline itself in a decongestant role provide L2-level evidence, and the mechanistic rationale is strong since the predicted indication overlaps closely with the drug's well-known pharmacological class effect. However, the absence of local market authorization, formal MOA documentation, and safety labeling data means the candidate cannot proceed without guardrails.

**To proceed, the following is needed:**
- TFDA (or equivalent local regulator) label warnings and contraindications (blocking gap, DG001)
- Formal mechanism of action documentation from DrugBank or equivalent source (DG002)
- Confirmed original indication text and licensing status for this jurisdiction
- Route/dosage-form compatibility assessment for the proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


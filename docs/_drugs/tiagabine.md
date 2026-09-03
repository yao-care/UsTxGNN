---
layout: default
title: Tiagabine
parent: 僅模型預測 (L5)
nav_order: 1226
evidence_level: L5
indication_count: 1
---

# Tiagabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Tiagabine: From Focal Epilepsy to Visual Epilepsy

## One-Sentence Summary

> Tiagabine is a selective GABA reuptake inhibitor established for adjunctive treatment of partial (focal) seizures.
> The TxGNN model predicts it may be effective for **Visual Epilepsy**,
> with **1 clinical trial** and **17 publications** currently associated with this prediction — though the literature raises an important safety caveat (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunctive treatment of partial (focal) seizures — inferred from literature (e.g., Cochrane review titles); no formal license/label data available in this dataset |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L3 |
| US Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal MOA data for tiagabine is not recorded in this evidence pack's `original_moa` field, but the associated literature and rationale consistently describe it as a **selective GABA transporter (GAT-1) inhibitor**: it blocks GABA reuptake into presynaptic neurons and glial cells, raising extracellular GABA concentration and enhancing inhibitory neurotransmission. This is tiagabine's well-established mechanism as an antiepileptic drug (AED), supported across multiple reviews (PMID 10530690, 9097364, 15094857, 8039477) and its Cochrane-reviewed use as add-on therapy for drug-resistant focal epilepsy (PMID 22592677, 31608990).

Mechanistically, enhancing GABAergic inhibition is broadly plausible for epilepsy in general, since GABA is the principal inhibitory neurotransmitter counterbalancing cortical excitability (PMID 11520315). However, "visual epilepsy" refers specifically to a **photosensitive/visually-triggered epilepsy subtype**, not general focal epilepsy. None of the current evidence (the single completed trial, or the 17 publications) directly studies tiagabine in this specific subtype — the trial (NCT00855738) evaluated tiagabine only as one of several AEDs in general focal epilepsy.

**Important caveat**: One literature item (PMID 12588906, "Vigabatrin, tiagabine, and visual fields") directly reports that tiagabine — like the mechanistically related drug vigabatrin — may be associated with **visual field constriction/defects** as an adverse effect, a concern echoed in a broader review of AEDs and visual function (PMID 17560495). This raises the possibility that the TxGNN signal linking tiagabine to "visual epilepsy" may partly reflect adverse-event literature co-occurrence rather than a genuine therapeutic indication signal, and warrants explicit disambiguation before further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study assessing effectiveness of newer AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice bitherapy in general focal epilepsy — not specific to visual/photosensitive epilepsy subtype |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22592677](https://pubmed.ncbi.nlm.nih.gov/22592677/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Efficacy of tiagabine add-on therapy for drug-resistant partial epilepsy |
| [31608990](https://pubmed.ncbi.nlm.nih.gov/31608990/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated Cochrane review of tiagabine add-on therapy for drug-resistant focal epilepsy |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES guideline update on efficacy/tolerability of newer AEDs for new-onset epilepsy |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Safety/Cohort | J Neurol Neurosurg Psychiatry | Reports visual field constriction associated with vigabatrin and tiagabine — direct safety signal relevant to "visual" indication |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatric Neurology | Reviews visual adverse effects (visual field/color vision deficits) across AEDs including tiagabine |
| [26210064](https://pubmed.ncbi.nlm.nih.gov/26210064/) | 2015 | Review | Epilepsy & Behavior | Discusses drug-induced status epilepticus, noting tiagabine among GABAergic drugs that can exacerbate seizures if misused |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Overview of mechanisms of action of currently used antiseizure drugs |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Review | Epilepsia | GABAergic mechanisms underlying seizure generation and control |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Review | Epilepsia | Comprehensive review of tiagabine's GABA reuptake inhibition mechanism and use as add-on therapy for partial seizures |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Review | Seminars in Pediatric Neurology | Reviews tiagabine pharmacokinetics, efficacy in partial seizures, and preliminary pediatric data |

---

## US Market Information

Tiagabine is currently **not marketed** in the jurisdiction covered by this dataset (0 licenses/NDAs recorded). No product authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — see DG001, a Blocking-severity gap requiring TFDA label retrieval before a full safety assessment can be completed. Independently, literature evidence above [PMID 12588906, 17560495] flags a possible visual field defect risk associated with tiagabine that should be reconciled with the "visual epilepsy" indication signal.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Tiagabine's GABAergic mechanism provides general biological plausibility for epilepsy, but no evidence directly supports efficacy in the specific "visual epilepsy" (photosensitive) subtype — the sole trial and most literature address general focal epilepsy. More critically, literature suggests tiagabine may cause visual field defects, creating a possible confound between an adverse-effect signal and a genuine indication signal. Combined with a Blocking data gap on TFDA warnings/contraindications and the drug's non-marketed status, this candidate should not advance past S1 review until clarified.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/product label warnings and contraindications) to complete S1 safety screening
- Confirm formal MOA documentation in DrugBank record (currently marked as data gap)
- Disease-mapping review to confirm whether "visual epilepsy" reflects a genuine TxGNN indication signal or an artifact of adverse-event co-mention in the literature
- Trials or case series specific to photosensitive/visually-triggered epilepsy, rather than general focal epilepsy
- Assessment of visual field monitoring requirements if this indication is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


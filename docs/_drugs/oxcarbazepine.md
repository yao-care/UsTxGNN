---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 1002
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepine: From Focal Epilepsy to Visual Epilepsy

## One-Sentence Summary

> Oxcarbazepine is a second-generation antiepileptic drug (AED), globally established for the treatment of partial-onset (focal) epilepsy, though it is not currently licensed in this jurisdiction.
> The TxGNN model predicts it may be effective for **Visual Epilepsy** (a photosensitive/reflex seizure subtype),
> with **1 clinical trial** and **19 publications** currently available as supporting context — though none are specific to this seizure subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in this jurisdiction (drug status: not marketed); globally established indication is focal (partial-onset) epilepsy, per literature evidence |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxcarbazepine belongs to the second-generation antiepileptic drug (AED) class — it is the keto-analogue of carbamazepine. Its efficacy in partial-onset (focal) epilepsy has been proven over decades of clinical use, and mechanistically it may be applicable to visual epilepsy.

Oxcarbazepine's active metabolite (10-monohydroxy derivative, MHD) acts as a voltage-dependent sodium channel blocker. This core antiseizure mechanism already covers essentially all focal seizure types. Visual (photosensitive/pattern-induced) epilepsy is considered a reflex seizure subtype within the broader focal/generalized seizure spectrum, so the mechanism can plausibly be extrapolated to this population.

It should be noted, however, that this represents largely an **extension of an already-established indication** rather than a genuinely novel repurposing target. As the evidence pack's own rationale states, the TxGNN model appears to be recovering a known drug-class relationship (AEDs treat reflex/visually-induced seizures as a matter of course) rather than surfacing an unexpected new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study assessing new AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice bitherapy in focal epilepsy. Relevance grade B — general focal-epilepsy population evidence, not specific to visual/photosensitive epilepsy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32129501](https://pubmed.ncbi.nlm.nih.gov/32129501/) | 2020 | Cochrane Systematic Review | Cochrane Database Syst Rev | Oxcarbazepine as add-on therapy for drug-resistant focal epilepsy. |
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | RCT | CNS Neurosci Ther | Multicenter, open-label, randomized study comparing oxcarbazepine vs. levetiracetam monotherapy in newly diagnosed focal epilepsy (China). |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | Overview of antiseizure medications for adults with epilepsy. |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Current role of carbamazepine and oxcarbazepine in epilepsy management. |
| [10530693](https://pubmed.ncbi.nlm.nih.gov/10530693/) | 1999 | Review | Epilepsia | Oxcarbazepine as first-line therapy for partial and generalized tonic-clonic seizures. |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Review | Pharmacogenomics | Pharmacogenomic variability in oxcarbazepine efficacy/safety across populations. |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review | Continuum (Minneap Minn) | Update on antiseizure medications, 2025. |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum (Minneap Minn) | Overview of antiepileptic drugs including oxcarbazepine's spectrum of use. |
| [1379159](https://pubmed.ncbi.nlm.nih.gov/1379159/) | 1992 | Review | Drugs | Pharmacology and therapeutic potential of oxcarbazepine in epilepsy, trigeminal neuralgia, and affective disorders. |
| [11772334](https://pubmed.ncbi.nlm.nih.gov/11772334/) | 2002 | Review | Expert Opin Pharmacother | Oxcarbazepine efficacy as adjunctive and monotherapy for partial-onset seizures. |

---

## US Market Information

The drug is currently **not marketed** in this jurisdiction (`market_status: 未上市`, `total_licenses: 0`), so no license/NDA records are available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: local label warnings, contraindications, and drug interaction data are currently a data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism of sodium-channel blockade is broadly applicable to reflex/focal seizure subtypes including visual epilepsy, and this is supported by one Phase 4 observational trial and multiple reviews on oxcarbazepine's established role in focal epilepsy — but no evidence specifically addresses visual/photosensitive epilepsy, and this candidate largely reflects a known indication extension rather than a novel repurposing signal.

**To proceed, the following is needed:**
- Local package insert warnings/contraindications (currently a **Blocking** data gap — required before safety pre-screening, S1)
- Detailed mechanism of action (MOA) documentation from DrugBank
- Visual-epilepsy-specific case series or trial evidence to confirm applicability beyond general focal-epilepsy population data
- Regulatory pathway assessment, since the drug is not currently marketed/licensed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 850
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

Using the report template supplied in the system prompt to generate the levetiracetam evaluation report. This is a self-contained content-generation task (no code, no repo work), so I'll write the report directly from the Evidence Pack JSON.

A few notes on how I resolved gaps in the data before the report:

- `drug.original_indications` is empty and `original_moa` is `[Data Gap]`, and `taiwan_regulatory.licenses` is empty (market_status = "未上市" / Not Marketed, 0 licenses) — so there is no TFDA-sourced original indication text to extract. I did **not** fabricate TFDA data; instead I grounded the "Original Indication" statement in the Evidence Pack's own trial descriptions (e.g. NCT00203216: "levetiracetam is FDA approved as an add-on medication in the treatment of partial onset seizures in adults with epilepsy... trade name Keppra®"), and flagged the missing TFDA-specific record as Data Gap DG001.
- Per the template's explicit extraction rule, "Predicted New Indication" = `predicted_indications[0]`, i.e. rank 1 "visual epilepsy" (score 0.9998, L2, Proceed with Guardrails) — not the strongest-evidence candidate in the list (rank 9 "status epilepticus" has L1/multiple RCTs), but the template instructs use of index 0, so the report follows that.
- Cytotoxicity section omitted (levetiracetam is an antiepileptic, not antineoplastic).
- Safety section collapsed to the fallback sentence since all safety fields are `[Data Gap]`/not found.

---

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is a broad-spectrum antiepileptic drug, established globally as add-on and monotherapy treatment for partial-onset seizures in patients with epilepsy. The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype), with **9 clinical trials** and **20 publications** currently identified in this evidence pack, though most of this evidence covers general epilepsy populations rather than the visually-induced subtype specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / partial-onset seizures (established global indication, per trial-reported labeling; Taiwan-specific TFDA approval record unavailable — see Data Gap DG001) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known information from the trial and literature records collected here, levetiracetam is a second-generation antiepileptic drug (marketed as Keppra®) whose established efficacy is in partial-onset seizures and, as adjunctive therapy, in myoclonic seizures of juvenile myoclonic epilepsy and primary generalized tonic-clonic seizures. Its pharmacology is generally understood to act via binding to synaptic vesicle protein 2A (SV2A), modulating neurotransmitter release and dampening abnormal neuronal synchronization — this mechanistic description appears consistently across the collected literature even though a formal MOA field was not returned by DrugBank in this pack.

Visual epilepsy (photosensitive/visually-induced seizures) is classified as a reflex epilepsy and is closely related to idiopathic generalized epilepsy (IGE) with photosensitive features. Because reflex and generalized epilepsies share overlapping cortical hyperexcitability mechanisms with the partial-onset and generalized seizure types levetiracetam already treats, the TxGNN prediction is mechanistically plausible. However, as the repurposing rationale notes, the identified trials and literature largely evaluate levetiracetam in general epilepsy, neurocritical-care, or pediatric seizure populations rather than in visually-induced/photosensitive epilepsy specifically — supporting a cautious "Proceed with Guardrails" rather than a stronger recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Prophylactic levetiracetam for functional outcome in acute intracerebral haemorrhage; seizures occur in up to 40% of ICH patients within 7 days. Grade C relevance — ICH population, not reflex/photosensitive epilepsy. |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for prophylactic treatment of migraine with/without visual aura. Grade C — general migraine prevention, not visual-epilepsy-specific. |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Levetiracetam for control of neonatal seizures. Grade C — neonatal population, different mechanism. |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | "Liceo" observational study of new AEDs (including levetiracetam) as first-line bitherapy for focal epilepsy. Grade B — may include reflex-epilepsy subgroups but not specific to them. |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam tested for reducing hippocampal hyperactivity in psychotic disorders using visual-scene-processing fMRI tasks. Grade C — psychiatric indication, not epilepsy. |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | Gene therapy (AVASPA) trial for Canavan Disease; not a levetiracetam efficacy trial. Grade C. |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Same hippocampal-hyperactivity/psychosis design as NCT04559529; terminated with only 1 participant. Grade C — very weak evidence. |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1649 | MAST trial: AED duration/choice (levetiracetam vs phenytoin) for post-traumatic-brain-injury seizure prevention. Grade C — different etiology. |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | 19-week double-blind, placebo-controlled safety study of cognitive/neuropsychological effects of levetiracetam in children with refractory partial-onset seizures. Grade B — design may include photosensitive subgroups but not confirmed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures — no FDA-approved therapy previously existed for this population; levetiracetam has proven efficacy/safety in older patients. |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care (ICH, TBI, SAH); efficacy, optimal dosing and adverse events remain unclear. |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy (including JME), compared with other ASMs for efficacy/safety. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review/Network Meta-analysis | Journal of Neurology | Antiseizure medications (including levetiracetam) for idiopathic generalized epilepsies — comparative efficacy and safety. |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guideline | Neurocritical Care | Neurocritical Care Society clinical practice guideline for seizure prophylaxis in adults with moderate-severe TBI. |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | Phase 3 RCT (PEACH trial) | The Lancet Neurology | Prophylactic levetiracetam to prevent epileptic seizures in acute intracerebral haemorrhage; double-blind, placebo-controlled. |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | Comparative Study (open-label RCT) | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome. |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Initial management of seizure in adults. |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Status epilepticus: diagnosis, monitoring and treatment overview. |
| [29037435](https://pubmed.ncbi.nlm.nih.gov/29037435/) | 2018 | Review (Veterinary) | Vet Clinics of North America: Small Animal Practice | Feline epilepsy management; notes levetiracetam may be useful for certain seizure types in cats. |

---

## US Market Information

Levetiracetam is currently recorded as **Not Marketed** in this regulatory dataset, with **0** license/NDA records returned. No product-level authorization data (dosage form, approved indication text) is available to populate a market information table. This should be independently verified against the official FDA Orange Book / NDA database, since the underlying TFDA/regulatory query in this evidence pack returned no results (query_log id 1, `result_status: success, result_count: 0`) rather than an explicit "not approved" determination.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in this evidence pack — key warnings, contraindications, and drug-drug interactions — returned no data; the DDI query status was "not_found".)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.98%) to visual epilepsy, and the mechanistic link (SV2A-mediated suppression of neuronal hyperexcitability, applicable to reflex/photosensitive epilepsy subtypes within the broader IGE spectrum) is plausible. However, the supporting clinical trial evidence (9 trials, evidence level L2) is drawn almost entirely from general epilepsy, neurocritical-care, or unrelated psychiatric populations rather than visual/photosensitive-epilepsy-specific studies — none of the identified trials directly enroll or report outcomes for this reflex subtype. This gap between a strong statistical signal and weak subtype-specific clinical evidence supports a guarded, evidence-gathering pathway rather than a full "Go."

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, precautions, contraindications) — currently a **Blocking** data gap (DG001) that must be resolved before any S1 safety review can proceed.
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source — currently a **High**-severity data gap (DG002) affecting mechanistic-relevance analysis.
- A treatment-outcome-specific literature or trial search restricted to reflex/photosensitive epilepsy (rather than general epilepsy) to confirm whether levetiracetam's benefit generalizes to this subtype.
- Drug-drug interaction (DDI) data, since the current DDI query returned no results.
- Confirmation of current US marketing/NDA status, since this dataset shows 0 license records despite levetiracetam (Keppra®) being a long-marketed drug in most regulatory jurisdictions — this discrepancy should be reconciled before relying on the "Not Marketed" status shown here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


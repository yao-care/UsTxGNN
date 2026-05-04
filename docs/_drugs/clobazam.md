---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Clobazam
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

Based on the Evidence Pack provided, here is the evaluation report for Clobazam:

---

# Clobazam: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine antiepileptic drug, established globally as adjunctive treatment for seizures associated with Lennox-Gastaut Syndrome and other refractory epilepsies, with FDA approval granted in 2011.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
with **0 clinical trials** and **2 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lennox-Gastaut Syndrome / refractory epilepsy (no US license record found in regulatory database) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| US Market Status | Not found (0 licenses recorded in registry) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this Evidence Pack. Based on established pharmacology, clobazam is a 1,5-benzodiazepine that potentiates GABA-A receptor-mediated chloride channel opening, thereby enhancing synaptic inhibition throughout the central nervous system. Its structural difference from 1,4-benzodiazepines confers relative selectivity for α2 subunit-containing GABA-A receptors, which reduces sedation while retaining broad antiseizure activity. This mechanism underpins its clinical role in Lennox-Gastaut Syndrome (FDA-approved, 2011) and Dravet syndrome, where it forms part of the stiripentol + clobazam + valproate triple regimen approved in the US and EU.

FIRES is a catastrophic epileptic encephalopathy triggered by a febrile infection in previously healthy individuals, characterized by super-refractory status epilepticus (SRSE). During the acute phase, GABAergic agents — particularly benzodiazepines — are the backbone of initial seizure control, providing a mechanistic rationale for the TxGNN model prediction that clobazam might be applicable here.

However, the clinical translation has important limitations. FIRES acute-phase management relies on intravenous benzodiazepines such as midazolam, lorazepam, and diazepam — not oral clobazam. During the chronic phase of FIRES, immune-mediated mechanisms dominate, and GABAergic modulation has limited independent efficacy. Neither of the 2 identified publications directly addresses clobazam in FIRES: one focuses on lorazepam weaning, the other on perampanel. The TxGNN prediction therefore appears to reflect a class-level benzodiazepine association rather than a clobazam-specific mechanistic finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | Perampanel reduced barbiturate dependency in a 13-year-old FIRES patient; illustrates the challenge of conventional AED failure in SRSE and the emerging role of adjunctive agents |
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Retrospective Case Series | Epileptic Disorders | Enteral lorazepam served as an effective weaning substitute for midazolam in FIRES patients; supports benzodiazepine class relevance in FIRES management but is not specific to clobazam |

---

## US Market Information

No FDA-registered licenses were identified in the regulatory database for Clobazam. This likely reflects a data retrieval gap — clobazam (brand name Onfi®) is known to hold FDA approval for adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome, based on the CONTAIN Phase 3 RCT program (approved October 2011). Regulatory record retrieval should be re-attempted directly via the FDA Orange Book or DailyMed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.82%), but the clinical fit is weak: intravenous benzodiazepines — not oral clobazam — are the standard of care in FIRES acute-phase super-refractory status epilepticus, and during the chronic phase, immune mechanisms dominate over GABAergic pathways. No clinical trials and no clobazam-specific publications were identified for this indication.

**To proceed, the following is needed:**
- Search for any published case reports or series where clobazam was specifically used in FIRES management — particularly during the transition from acute SRSE to chronic epilepsy maintenance
- Retrieve full MOA and safety data from DrugBank (DB00349), including GABA-A subunit binding profile and known drug interaction risk with commonly co-administered agents in FIRES (e.g., ketamine, phenobarbital, immunotherapeutics)
- Clarify whether clobazam has any role in FIRES chronic-phase adjunctive therapy alongside immunotherapy (IVIG, methylprednisolone, rituximab)
- Resolve the regulatory database discrepancy: confirm FDA license records for Onfi® to establish the correct US market status baseline
- Consider framing future investigation as a class-effect (benzodiazepine adjuncts in FIRES chronic phase) rather than a clobazam-specific hypothesis, given current evidence gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


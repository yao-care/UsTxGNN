---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic Bacterial/Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial generally used for anaerobic bacterial and protozoal infections (e.g., amoebiasis, trichomoniasis, giardiasis, anaerobic/IBD-related infections); this evidence pack's own regulatory and mechanism-of-action fields for the drug are marked as data gaps. The TxGNN model's top-ranked prediction is **Pneumocystosis**, with a 99.99% score, but the accompanying evidence review found **24 clinical trials** and **10 publications**, almost none of which support this specific indication — the pack itself flags this as a likely mismatch (Evidence Level **L5**, recommendation **Hold**).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` empty, no TFDA/US license on file); generally known as anaerobic bacterial & protozoal infections |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is marked as a data gap, and `original_indications` is empty). Based on general pharmacological knowledge not sourced from this pack, metronidazole is a nitroimidazole with established antibacterial activity against anaerobic bacteria and antiprotozoal activity (amoebiasis, trichomoniasis, giardiasis); it has no recognized antifungal activity.

For the top-ranked prediction, pneumocystosis (*Pneumocystis jirovecii* pneumonia), the evidence pack's own review finds no credible mechanistic basis. *Pneumocystis* is classified as a fungus, and metronidazole is not active against it — standard treatment is trimethoprim-sulfamethoxazole, pentamidine, or atovaquone. All 24 retrieved clinical trials were graded as unrelated to this indication (primary-care payment models, dementia caregiving technology, mobile depression therapy, etc.), and the 10 retrieved publications are general antiprotozoal/HIV-opportunistic-infection reviews or incidental case reports in which metronidazole and pneumocystosis co-occur in the same patient history without any direct treatment relationship.

TxGNN's high score most likely reflects a knowledge-graph co-occurrence signal — both entities frequently appear together in immunocompromised/HIV-related clinical contexts — rather than a genuine pharmacological mechanism. This is consistent with the evidence pack's own conclusion of Evidence Level L5 (model prediction only, no supporting studies) and a Hold recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02731716](https://clinicaltrials.gov/study/NCT02731716) | NA | Active, not recruiting | 117 | Primary care payment model study in Hawaii — unrelated to pneumocystosis (mismatched retrieval) |
| [NCT04631120](https://clinicaltrials.gov/study/NCT04631120) | NA | Withdrawn | 0 | Dementia caregiver technology study, withdrawn — unrelated |
| [NCT04463914](https://clinicaltrials.gov/study/NCT04463914) | NA | Completed | 649 | Mobile app for depression treatment — unrelated |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | Recruiting | 4000 | Comparison of walk-in clinic/PCP/ED care value — unrelated |
| [NCT05256303](https://clinicaltrials.gov/study/NCT05256303) | NA | Completed | 160 | Hospital-level home care RCT — unrelated to infection treatment |
| [NCT07203339](https://clinicaltrials.gov/study/NCT07203339) | NA | Recruiting | 610 | tDCS vs. duloxetine for fibromyalgia — relevance not yet graded, topic unrelated |
| [NCT04418232](https://clinicaltrials.gov/study/NCT04418232) | Phase 1 | Completed | 243 | Alzheimer's service-utilization feasibility study — unrelated (mismatched retrieval) |
| [NCT05340426](https://clinicaltrials.gov/study/NCT05340426) | Phase 1 | Withdrawn | 0 | Porcine kidney xenotransplantation trial, withdrawn — unrelated |
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | Completed | 65 | Head & neck cancer survivorship tool study — relevance not yet graded, topic unrelated |
| [NCT02972203](https://clinicaltrials.gov/study/NCT02972203) | NA | Completed | 87 | Mindfulness intervention pilot in primary care — relevance not yet graded, topic unrelated |

*Note: All 24 retrieved trials were reviewed by the evidence pipeline; none constitute a genuine metronidazole–pneumocystosis interventional trial.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Names metronidazole as drug of choice for amebic colitis/trichomoniasis, but names TMP-SMX (not metronidazole) as the drug of choice for pneumocystis pneumonia |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | Review of HIV-related opportunistic infections (background context only; no metronidazole-PCP efficacy data) |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Review of AIDS infectious complications (PCP is most common); no metronidazole treatment data for PCP |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | American Review of Respiratory Disease | Patient with PCP+CMV pneumonia who had separately received metronidazole for an unrelated diarrheal illness — incidental co-occurrence, not treatment evidence |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | AIDS patient treated with metronidazole for amebic dysentery who subsequently developed PCP — incidental co-occurrence, not causal/treatment evidence |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | General pharmacokinetic review of antiprotozoal therapy; no pneumocystosis-specific data |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | General review of antiparasitic agents; does not address metronidazole for pneumocystosis |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | Critique of antimicrobial prophylaxis trial design; unrelated to pneumocystosis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | Journal of the Formosan Medical Association | Colon perforation from CMV/amebic colitis in an AIDS patient; unrelated to pneumocystosis |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | General review of antiprotozoal drugs (no abstract available) |

## US Market Information

No marketing authorization records are present in this evidence pack. Market status: **Not Marketed**, with 0 licenses on file (`taiwan_regulatory.total_licenses = 0`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN assigns a very high score (99.99%) to pneumocystosis, but the evidence pack's own review found the clinical trials and literature retrieved to be largely unrelated or only incidentally co-occurring, with no direct treatment evidence and a mechanistic conflict (metronidazole lacks antifungal activity against *Pneumocystis jirovecii*). This is consistent with the assigned Evidence Level L5 (model prediction only).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001) preventing S1 safety screening
- Verified DrugBank MOA record — currently a High-severity data gap (DG002)
- Confirmed original approved indication(s) for metronidazole (currently empty/unrecorded in this pack)
- If pursuing a repurposing signal from this same candidate set, consider re-scoping toward the higher-evidence candidates already in this pack — e.g., **cap polyposis** (rank 9, L3, "Proceed with Guardrails," with an on-topic mechanistic case study, PMID 12141801) or **ulcerative proctosigmoiditis** / **ulceration of vulva** (rank 3/10, L3, "Research Question") — rather than pneumocystosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


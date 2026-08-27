---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 961
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# NEVIRAPINE: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose known pharmacology targets HIV-1 infection. The TxGNN model predicts a top-ranked association with **Simian Immunodeficiency Virus (SIV) Infection**, but the supporting evidence — **0 clinical trials** and **17 literature items**, none confirming activity against SIV in vivo — indicates this is likely a knowledge-graph artifact (HIV-1/SIV taxonomic proximity) rather than a real pharmacological signal, and SIV is not a human disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (per drug mechanism description in evidence pack; no formal license/indication record provided) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action record is available in this evidence pack (`original_moa` is unrecorded). Based on the mechanistic notes accompanying the prediction, nevirapine is an NNRTI whose binding pocket is highly specific to HIV-1 reverse transcriptase.

The predicted indication, SIV infection, belongs to a different lentivirus lineage. Multiple items in the literature set (e.g., PMID 7541200, PMID 15564466) show that wild-type SIV reverse transcriptase is **not** meaningfully inhibited by NNRTIs such as nevirapine — sensitivity has only been demonstrated in engineered SHIV chimeras where the SIV RT gene is replaced by HIV-1 RT. This suggests the TxGNN score reflects graph-level proximity between HIV-1 and SIV (both lentiviruses, both studied via shared reverse-transcriptase literature) rather than a genuine drug-disease pharmacological relationship.

Additionally, SIV infection is a disease of non-human primates used as an animal model for HIV research, not a human clinical indication. Even if the mechanistic signal were stronger, this candidate would not represent an actionable human repurposing opportunity without further translational justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review (human HIV PEP context, not SIV-specific) | Annals of Emergency Medicine | Discusses antiretroviral postexposure prophylaxis; SIV data cited only as indirect animal-model support for human HIV PEP |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro characterization | Journal of Virology | SIV/HIV chimera expressing HIV-1 RT was built specifically because native SIV RT is not effectively inhibited by NNRTIs |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model (SHIV transmission) | Virology | Characterizes an RT-SHIV chimera (HIV-1 RT inserted into SIV backbone) for vaginal transmission studies in macaques |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro resistance profiling | Biochemical and Biophysical Research Communications | Native SIV is inhibited only by nucleoside RT inhibitors, not NNRTIs; an RT-SHIV chimera was required for NNRTI sensitivity |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | In vivo animal model | AIDS Research and Human Retroviruses | Uses RT-SHIV (SIV with HIV-1 RT substitution) as a resistance-development model; underscores that native SIV is not an NNRTI target |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | In vitro antiviral screening | Chemical Biology & Drug Design | A novel small molecule (3G11) inhibited HIV-1 but explicitly did **not** block SIVmac or other non-HIV-1 retroviruses |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility panel | Antiviral Therapy | Evaluated 16 approved anti-HIV-1 drugs (including NNRTIs) against HIV-2, SIV, and SHIV strains to inform PEP/treatment guidance |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro combination study | Antimicrobial Agents and Chemotherapy | Nevirapine combined with an HIV-1 integrase inhibitor was tested against SIV(MAC251); combination effect was subsynergistic |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | In vitro virucide study | Virology | Nevirapine and other NNRTIs/NRTIs were tested for inactivation of HIV-1 and SIV virions via endogenous reverse transcription inhibition |
| [1283296](https://pubmed.ncbi.nlm.nih.gov/1283296/) | 1992 | In vitro antiviral screening | Antimicrobial Agents and Chemotherapy | A different nucleoside analog (FTC) — not nevirapine — showed activity against HIV-1/2, SIV, and FIV; included for cross-species susceptibility context |

---

## US Market Information

Nevirapine is not currently marketed in this jurisdiction (market status: 未上市); no NDA or license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature consistently indicates that native SIV reverse transcriptase is resistant to NNRTIs including nevirapine — sensitivity has only been shown in artificially engineered SHIV chimeras carrying HIV-1 RT. Combined with the absence of any clinical trial data and SIV not being a human disease, the evidence does not support advancing this candidate; the TxGNN score is more likely explained by lentivirus taxonomic proximity in the knowledge graph than by genuine drug-disease efficacy.

For reference, the two lower-ranked candidates in this evidence pack (feline immunodeficiency virus-related disease, rank 2; a rare pediatric neurodevelopmental disorder, rank 3) were also scored Hold — the former lacks in vivo efficacy data and is a veterinary indication, and the latter has no supporting literature or plausible mechanistic link at all.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed original mechanism-of-action record from DrugBank (currently a High-severity data gap)
- A specific molecular/pathway hypothesis connecting nevirapine's NNRTI activity to a genuine human disease target, rather than relying on SIV/FIV animal-model literature
- If pursuing further, in vivo efficacy data against wild-type (non-chimeric) target pathogens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 830
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamivudine: From Unspecified Original Indication to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lamivudine (DrugBank DB00709) is a nucleoside reverse transcriptase inhibitor (NRTI); this evidence pack does not contain data on its original approved indication(s) or mechanism of action. The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a disease that occurs only in non-human primates, not humans. Supporting evidence consists of **0 clinical trials** and **20 publications**, nearly all animal or in vitro virology studies with no direct human-disease relevance.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (evidence pack contains no `original_indications` data; drug not marketed in Taiwan) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lamivudine in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological class, Lamivudine is a cytidine-analog NRTI that inhibits retroviral reverse transcriptase — the enzyme class also used by SIV, a lentivirus closely related to HIV.

However, this mechanistic plausibility does not translate into a valid repurposing candidate. SIV infection is a veterinary/experimental condition confined to macaques and other non-human primates; it is not a human disease entity and has no corresponding clinical indication pathway. The supporting literature confirms this: essentially all 20 publications are animal-model or in vitro virology studies (e.g., SIV-infected macaque pharmacokinetics, M184V resistance mutation studies), not human trials. No clinical trials are registered for this "indication" at all. The TxGNN score is very high, but this reflects graph-embedding similarity (SIV and HIV share lentivirus/reverse-transcriptase biology) rather than a translatable clinical signal — consistent with the evidence pack's own scoring, which assigns Evidence Level L4 and a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review (unrelated drug, HIV context only) | Current Opinion in HIV and AIDS | Discusses islatravir, a different RT translocation inhibitor, for HIV-1; not specific to lamivudine or SIV |
| [39509655](https://pubmed.ncbi.nlm.nih.gov/39509655/) | 2024 | Epidemiology review (human HIV-1/2, not SIV) | AIDS Reviews | Reviews HIV-1/2 burden in Ivory Coast; SIV mentioned only as evolutionary precursor of HIV |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal study (macaque PEP model) | AIDS (London) | Zidovudine+lamivudine+indinavir post-exposure prophylaxis after vaginal SIV exposure in macaques |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal study | Journal of Virology | Bone marrow hematopoiesis defects in SHIV-infected macaques despite HAART viral suppression |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | In vitro/animal virology | Journal of Virology | M184V resistance mutation emergence in SIV-infected macaques treated with lamivudine/emtricitabine |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | Journal of Virology | Viral decay kinetics in SIV-infected macaques on quadruple antiretroviral therapy |
| [9237655](https://pubmed.ncbi.nlm.nih.gov/9237655/) | 1997 | In vitro pharmacology | FEBS Letters | Aryloxyphosphoramidate prodrugs of ddA/d4A potentiate anti-HIV/SIV/HBV activity vs. parent compounds |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | Animal study | Journal of Virology | Tenofovir selects M184V reversion in SIV reverse transcriptase even with concurrent lamivudine |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal study | Journal of Virology | HAART (efavirenz/lamivudine/tenofovir) suppresses viral load in RT-SHIV-infected rhesus macaques |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Animal study | Journal of Virology | Lymphocyte proliferation kinetics in SIV-infected macaques under early post-exposure HAART prophylaxis |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) is not a human disease entity, and its supporting literature is exclusively preclinical/veterinary. No clinical trials exist. This is consistent with the evidence pack's own S0/Hold scoring. Notably, all 5 TxGNN-ranked candidates in this pack were independently scored Hold: the remaining four are either a mismatched veterinary condition with human-trial evidence incorrectly attached via keyword collision (feline immunodeficiency syndrome — the 5 "supporting" trials are human HIV-1 Phase 3/4 studies unrelated to cats), a rare genetic neurodevelopmental disorder with zero mechanistic or empirical support, an obsolete/deprecated disease ontology term with no evidence, and chronic hepatitis C — a mechanistic mismatch, since HCV is an RNA virus replicating via RNA-dependent RNA polymerase (not reverse transcriptase), and the "supporting" trials/literature are almost entirely existing chronic hepatitis **B** evidence mislabeled under HCV. No candidate in this pack currently supports advancement past S0.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Correction of disease-label mapping errors observed in candidates 2 and 5 (FIV/HIV confusion; HBV/HCV confusion) before any evidence re-scoring
- Re-run of candidate generation restricted to valid human ICD/SNOMED disease entities, excluding obsolete ontology terms and non-human disease models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


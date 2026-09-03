---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 1106
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

> Raltegravir is an integrase strand transfer inhibitor (INSTI) originally developed for HIV-1 infection.
> The TxGNN model predicts a very high association with **Simian Immunodeficiency Virus (SIV) Infection**,
> but on closer review the supporting evidence consists of **1 withdrawn/irrelevant clinical trial** and **20 publications**, nearly all of which are non-human primate research-tool studies rather than evidence of a genuine new clinical indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (TFDA license data unavailable — drug is not marketed in this jurisdiction). Publicly known original indication: HIV‑1 infection, referenced indirectly throughout the evidence as background context. |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Raltegravir belongs to the integrase strand transfer inhibitor (INSTI) class of antiretrovirals; its efficacy in HIV‑1 infection is well established, and mechanistically this class may be applicable to other lentivirus infections, since both HIV and SIV are lentiviruses that require viral integrase to complete proviral DNA integration.

On this basis, the mechanistic link between HIV‑1 infection and SIV infection is biologically plausible — SIV-infected rhesus macaques are a long-standing model for studying HIV pathogenesis, and raltegravir has indeed been used experimentally in these animals as part of antiretroviral regimens.

However, the available evidence does not actually support SIV infection as a standalone new *clinical* indication. Nearly all cited studies use raltegravir as a **research tool within SIV/macaque models to study human HIV pathogenesis** (viral reservoir kinetics, resistance mutation emergence, metabolic side effects) rather than as a therapeutic intervention being developed for SIV infection itself. In addition, SIV infection is a veterinary/research-animal condition, not a human disease, which limits its relevance as a repurposing target in the conventional sense. The single associated clinical trial (NCT00863668) was withdrawn with zero enrollment and was itself a human HIV pharmacokinetics study, not an SIV trial — it was flagged as low relevance (Grade C). This prediction should be interpreted as a mechanistic signal generated from lentivirus taxonomic similarity in the knowledge graph, not as validated repurposing evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Studied HIV RNA decay kinetics in humans on antiretroviral therapy including raltegravir, referencing comparable decay estimates in SIV-infected macaques; trial was withdrawn with no enrollment and does not directly test raltegravir in SIV infection (relevance grade: C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Animal model | Retrovirology | First report of a raltegravir-containing ART regimen suppressing SIVmac251 in nonhuman primates, establishing an animal model for lentiviral persistence during ART. |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Animal model | J Virol | Analyzed 2-LTR circle dynamics in raltegravir-treated, SIV-infected rhesus macaques to study CD8+ cell effects on viral control. |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Animal model | J Virol | Evaluated intactness of persistent viral genomes in SIV-infected macaques after early ART initiation (including raltegravir-based regimens). |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Animal model | Clin Infect Dis | Found raltegravir and dolutegravir induce proadipogenic/profibrotic effects and insulin resistance in human/simian adipose tissue — a safety-relevant, not efficacy, finding. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Animal model | J Virol | Characterized drug resistance profiles of integrase inhibitors (including raltegravir) in SIVmac239 in vitro. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Animal model | PLoS One | Documented emergence of resistance mutations in SIV-infected macaques receiving non-suppressive raltegravir-containing ART. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal model | mBio | Investigated lentiviral persistence in the brain despite effective ART across lentivirus models. |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Animal model | Sci Transl Med | Tested topical integrase inhibitors for postexposure protection against vaginal SHIV infection in macaques. |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Animal model | Antimicrob Agents Chemother | Compared antiviral activity of bictegravir/cabotegravir against integrase-inhibitor-resistant SIVmac239 and HIV-1. |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Animal model | Antimicrob Agents Chemother | Used simian-tropic HIV as a model to study integrase inhibitor drug resistance. |

**Note:** All identified literature consists of preclinical/animal-model mechanistic and resistance studies (Tier 3); none are RCTs, human clinical trials, or systematic reviews of SIV infection as a treated condition.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings, contraindications, and drug-drug interaction data are currently unavailable for this candidate — see Data Gaps below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L4 (preclinical/mechanistic only), the single associated clinical trial is irrelevant and withdrawn, and the underlying literature primarily uses raltegravir as a research tool in SIV animal models rather than testing it as a therapy for SIV infection as a distinct indication. The other two TxGNN candidates for this drug (feline AIDS, a rare genetic neurodevelopmental disorder) were reviewed and identified as false-positive knowledge-graph associations with no supporting clinical or mechanistic evidence, reinforcing that this prediction set requires caution rather than advancement.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently a blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action data from DrugBank (currently missing)
- Clarification of whether "SIV infection" should be reframed as a research/veterinary-use case rather than a human repurposing candidate, given the absence of any human clinical evidence
- If pursued at all, purpose-designed studies distinguishing therapeutic use in SIV infection from its current role as a pharmacological tool in HIV/SIV comparative research
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


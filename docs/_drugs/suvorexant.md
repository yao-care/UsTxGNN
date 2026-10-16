---
layout: default
title: Suvorexant
parent: Model Prediction Only (L5)
nav_order: 1190
evidence_level: L5
indication_count: 1
monitor_inn: "SUVOREXANT"
predicted_indications: ["sleep disorder, initiating and maintaining sleep"]
last_modified_at: 2026-10-14
description: "Suvorexant: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
---

# Suvorexant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Suvorexant: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Suvorexant is a dual orexin receptor antagonist originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially a synonym or sub-phenotype of insomnia, so this is a confirmation of the existing use rather than a true repurposing.
No clinical trials are registered under this prediction, but **19 publications** support this direction, including several network meta-analyses and a clinical practice guideline.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (see note below) |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* No clinical trials are registered under this prediction in the data compiled for this report. The L1 level reflects the pivotal Phase 3 evidence on suvorexant for insomnia (two 3-month randomized trials, PMID 25526970) and the supporting meta-analyses. The trial registry details were not part of the compiled data, so this level could not be independently verified from registry records.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on established pharmacology, suvorexant is a dual orexin receptor antagonist (OX1R/OX2R). It suppresses wake-promoting orexin signaling, which reduces sleep-onset latency and improves sleep maintenance.

The predicted indication, difficulty initiating and maintaining sleep, describes the core features of insomnia. It is essentially the same condition as the drug's original indication, and the mechanism is identical. The model prediction therefore confirms an existing use and does not point to a new therapeutic area.

## Clinical Trial Evidence

Currently no related clinical trials registered under this prediction.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25526970](https://pubmed.ncbi.nlm.nih.gov/25526970/) | 2016 | RCT (two Phase 3 trials) | Biological Psychiatry | Results from two pivotal 3-month randomized trials of suvorexant in insomnia |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Network meta-analysis | Translational Psychiatry | Compared efficacy and safety of daridorexant, lemborexant and suvorexant in adults with insomnia |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Compared drug treatments for acute and long-term management of insomnia disorder in adults |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Network meta-analysis | Drugs | Network meta-analysis of 153 randomized trials on effectiveness, safety and tolerability of insomnia drugs |
| [37257468](https://pubmed.ncbi.nlm.nih.gov/37257468/) | 2023 | Network meta-analysis | Arquivos de Neuro-Psiquiatria | Compared dual orexin receptor antagonists for insomnia |
| [39277609](https://pubmed.ncbi.nlm.nih.gov/39277609/) | 2024 | Systematic review | Translational Psychiatry | Lemborexant and suvorexant for insomnia comorbid with psychiatric disorders |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical guideline | J Clin Sleep Med | AASM guideline on pharmacologic treatment of chronic insomnia in adults |
| [35972717](https://pubmed.ncbi.nlm.nih.gov/35972717/) | 2022 | Review | Current Psychiatry Reports | Review of orexin receptor antagonists for insomnia |
| [40943625](https://pubmed.ncbi.nlm.nih.gov/40943625/) | 2025 | Review | Int J Mol Sci | Orexin system targeting: suvorexant, lemborexant, daridorexant and experimental agents |
| [37229388](https://pubmed.ncbi.nlm.nih.gov/37229388/) | 2023 | Expert consensus | Frontiers in Psychiatry | Japanese expert consensus on treatment strategy for insomnia disorder |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204569 (cancelled) | BELSOMRA (Merck Sharp & Dohme LLC) | Tablet, film coated | Not specified in the compiled record |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text):** The knowledge graph links suvorexant to narcolepsy, narcolepsy-cataplexy syndrome, central nervous system disease, Balo concentric sclerosis and X-linked adrenoleukodystrophy. These should be verified against the official label.
- **Drug Interactions:** 100 interactions were found. Examples:
  - **Major:** aprepitant, morphine, clarithromycin
  - **Moderate:** dexamethasone, cimetidine, saxagliptin, simvastatin, metoclopramide, miconazole, clotrimazole, dronabinol, nabilone
  - **Minor:** naloxegol, prucalopride

  The major interactions with aprepitant and clarithromycin likely relate to CYP3A inhibition, and the one with morphine to additive CNS depression. Both are mechanistic inferences and were not confirmed in the compiled data.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is effectively the same as suvorexant's established insomnia use, and it is supported by pivotal randomized trials, network meta-analyses and a clinical guideline. Because this is not a new indication, the value lies in confirming existing use rather than in repurposing. The only US authorization on record is cancelled, and the label safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clarification of the US market status of BELSOMRA (the record shows the NDA as cancelled)
- Review of the DDI findings, particularly with CYP3A inhibitors and CNS depressants
- Review of the knowledge-graph contraindications, particularly narcolepsy, against the official label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


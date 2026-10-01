---
layout: default
title: Serotonin
parent: Model Prediction Only (L5)
nav_order: 1156
evidence_level: L5
indication_count: 10
---

# Serotonin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Serotonin: From No Labeled Indication to Insomnia

## One-Sentence Summary

Serotonin (DrugBank DB08839) is sold in the US as liquid preparations, but the records list no approved indication.
The TxGNN model predicts it may be useful for **insomnia** (score 99.90%), and the search returned **50 clinical trials** and **18 publications**.
None of them tests serotonin itself. The evidence covers serotonin-related drugs and pathways, so this is a model-driven hypothesis, not a clinically supported one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (all listed US product records have empty indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanistic/indirect evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 records (authorization numbers not recorded, so unverified as NDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Serotonin (5-HT) is a well-known neurotransmitter involved in sleep-wake regulation. Drugs that act on serotonin pathways, such as trazodone, mirtazapine and pimavanserin, affect sleep. This is the basis for the link to insomnia.

Serotonin has no documented original indication in the records. The prediction therefore rests on graph proximity in the TxGNN knowledge graph, not on extending a proven use.

There is also a major pharmacological caveat. Exogenous serotonin barely crosses the blood-brain barrier, so administering it is not equivalent to modulating central serotonin signaling. The high TxGNN score reflects graph proximity, not clinical support.

---

## Clinical Trial Evidence

No listed trial administers serotonin for insomnia. The most relevant of the retrieved trials are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04532749](https://clinicaltrials.gov/study/NCT04532749) | Phase 3 | Terminated | 212 | Seltorexant (orexin antagonist) added to antidepressants in depression with insomnia symptoms |
| [NCT06559306](https://clinicaltrials.gov/study/NCT06559306) | Phase 3 | Recruiting | 752 | Two-part seltorexant study of efficacy and maintenance of effect in depression with insomnia symptoms |
| [NCT03977441](https://clinicaltrials.gov/study/NCT03977441) | Phase 4 | Unknown | 240 | Agomelatine for sleep disorders and depression in Parkinson's disease |
| [NCT00765752](https://clinicaltrials.gov/study/NCT00765752) | N/A | Completed | 23 | Cortical GABA levels (MRS) in primary insomnia and depression with residual insomnia |
| [NCT05705830](https://clinicaltrials.gov/study/NCT05705830) | N/A | Unknown | 400 | Pulse magnetic therapy plus medication for anxiety with insomnia |
| [NCT07229976](https://clinicaltrials.gov/study/NCT07229976) | N/A | Not yet recruiting | 198 | Thumbtack needle for chronic insomnia in perimenopausal and menopausal women |
| [NCT06056258](https://clinicaltrials.gov/study/NCT06056258) | N/A | Completed | 48 | VL-NL-02 versus placebo on sleep quality and mood |
| [NCT05400005](https://clinicaltrials.gov/study/NCT05400005) | N/A | Active, not recruiting | 54 | Higher dietary protein and sleep quality in older adults |
| [NCT06893822](https://clinicaltrials.gov/study/NCT06893822) | N/A | Recruiting | 20 | Griffonia simplicifolia (5-HTP, a serotonin precursor) on pain modulation in healthy volunteers |
| [NCT03947216](https://clinicaltrials.gov/study/NCT03947216) | Phase 2 | Completed | 117 | Pimavanserin (5-HT2A inverse agonist) for impulse control disorders in Parkinson's disease; different drug and condition |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40135470](https://pubmed.ncbi.nlm.nih.gov/40135470/) | 2025 | RCT (design) | Age and Ageing | MIRAGE study: mirtazapine, which blocks serotonin and histamine receptors, for chronic insomnia in older adults; efficacy still to be shown |
| [34994734](https://pubmed.ncbi.nlm.nih.gov/34994734/) | 2021 | Review | Psychiatria Polska | Compares trazodone with hypnotics and reviews the evidence for trazodone in insomnia |
| [21537726](https://pubmed.ncbi.nlm.nih.gov/21537726/) | 2011 | Review | Rev Bras Psiquiatr | Sedative antidepressants and how serotonergic transmission links sleep and depression |
| [24685396](https://pubmed.ncbi.nlm.nih.gov/24685396/) | 2014 | Review | Sleep Med Rev | General insomnia research framework (3P model) |
| [30194544](https://pubmed.ncbi.nlm.nih.gov/30194544/) | 2019 | Review | Handb Exp Pharmacol | FDA-approved non-SSRI antidepressants (mirtazapine, trazodone and others) and their receptor targets |
| [41123484](https://pubmed.ncbi.nlm.nih.gov/41123484/) | 2025 | Review | Annals of Medicine | Circadian clock gene dysregulation as a molecular mechanism of insomnia |
| [37834999](https://pubmed.ncbi.nlm.nih.gov/37834999/) | 2023 | Observational | J Clin Med | Serotonin, its transporter and sleep/mood disorders in inflammatory bowel disease |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Retrospective | Medicine | Moxibustion, ear acupuncture and alprazolam: effects on neurotransmitters in coronary heart disease with insomnia |
| [41392764](https://pubmed.ncbi.nlm.nih.gov/41392764/) | 2026 | Preclinical (mouse) | Food & Function | Bifidobacterium Bbm-19 improved insomnia and restored GABA and serotonin signaling |
| [39519543](https://pubmed.ncbi.nlm.nih.gov/39519543/) | 2024 | Preclinical (mouse) | Nutrients | Lactobacillus plantarum reduced stress-induced insomnia and depression-like behavior |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | Serotonin (BioActive Nutritional) | Liquid | Not stated |
| Not recorded | Serotonin (BioActive Nutritional) | Liquid | Not stated |
| Not recorded | Serotonin Phenolic (Energique, Inc.) | Liquid | Not stated |
| Not recorded | Serotonin (BioActive Nutritional, Inc.) | Liquid | Not stated |
| Not recorded | Serotonin (Deseret Biologicals, Inc.) | Liquid | Not stated |

Ten records exist in total, and only five are shown above. All are liquid products with no authorization number or indication text on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any trial or publication that tests serotonin for insomnia. The supporting evidence concerns other serotonergic drugs or general biology, and exogenous serotonin barely crosses the blood-brain barrier. The market records also show no approved indication or authorization numbers, and safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Mechanism of action data (for example from DrugBank)
- Verified US regulatory status and authorization numbers for the listed liquid products
- Evidence that a serotonin-based product can reach the central nervous system, or a switch to a precursor or receptor-targeted approach
- Controlled clinical data in insomnia from a serotonin-based intervention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


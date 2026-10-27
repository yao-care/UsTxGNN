---
layout: default
title: Rivastigmine
parent: Moderate Evidence (L3-L4)
nav_order: 1131
evidence_level: L4
indication_count: 1
monitor_inn: "RIVASTIGMINE"
predicted_indications: ["glaucoma"]
last_modified_at: 2026-10-14
description: "Rivastigmine: predicted new indication Glaucoma (evidence level L4). Approved use: Alzheimer's disease"
---

# Rivastigmine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rivastigmine: From Alzheimer's Disease to Glaucoma
{: .text-alpha }

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor originally used to treat Alzheimer's disease and related dementias.
The TxGNN model predicts it may be effective for **glaucoma**,
but currently there are **0 registered clinical trials** and only **3 publications** (one animal study, two reviews) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (the data compiled for this report list no approved-indication text from US labels; the indication comes from knowledge-graph edges, which also include Alzheimer disease without neurofibrillary tangles, cerebellar degeneration, Reye syndrome and Pick disease) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 9 authorizations in total (1 NDA, 8 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on the known pharmacology of the drug class, rivastigmine inhibits both acetylcholinesterase and butyrylcholinesterase, which raises acetylcholine levels. Its efficacy in Alzheimer's disease comes from this cholinergic enhancement in the brain.

In the eye, higher acetylcholine acting on muscarinic receptors can contract the ciliary muscle and increase outflow through the trabecular meshwork, which lowers intraocular pressure (IOP). This is how established cholinergic agents such as pilocarpine and physostigmine work. A 2000 rabbit study found that topical rivastigmine lowered IOP, and a 2024 systems-genetics review supports a general cholinergic mechanism for IOP reduction.

Note that this link rests on class pharmacology and animal data, not on human glaucoma data. The very high TxGNN score is a computational prediction and does not count as clinical evidence. Also, the original forms of rivastigmine (oral capsules and transdermal patches) are designed for systemic delivery; a topical ocular formulation would be a new development, and route compatibility has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical animal study (rabbit) | J Ocul Pharmacol Ther | Topical rivastigmine, a selective acetylcholinesterase inhibitor, lowered intraocular pressure in normotensive rabbits |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review / computational systems genetics | Front Mol Biosci | Cholinergic signalling through M3 muscarinic receptors in the anterior eye regulates IOP; existing agonists are limited by systemic cholinergic side effects |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opin Ther Pat | Patent review of acetylcholinesterase inhibitors and reactivators; mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis and glaucoma |

## US Market Information

All nine US authorizations are cancelled. The data compiled for this report contain no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022083 | Exelon (Sandoz) | Extended-release patch | Not available |
| ANDA209063 | Rivastigmine Transdermal System (Breckenridge) | Extended-release patch | Not available |
| ANDA206318 | Rivastigmine (Zydus) | Extended-release patch | Not available |
| ANDA207308 | Rivastigmine (Amneal) | Patch | Not available |
| ANDA091689 | Rivastigmine Tartrate (Alembic) | Capsule | Not available |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, chronic obstructive pulmonary disease, asthma (including intrinsic and allergic forms), diarrheal disease, sudden cardiac arrest, heart conduction disease, sick sinus syndrome, atrioventricular block, anorexia nervosa, active peptic ulcer disease, urinary tract obstruction, and parkinsonian disorder / Parkinson disease. These reflect contraindication relationships in the knowledge graph and should be verified against the official label.
- **Drug Interactions:** 100 interactions were found in the DDI database. One is rated **Major**: **bupropion**. Many others are rated Moderate, including:
  - Anticholinergics and antispasmodics: atropine, hyoscyamine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate
  - Acid reducers: famotidine, ranitidine, cimetidine
  - Antibiotics: clarithromycin, levofloxacin, metronidazole
  - Others: loperamide, dolasetron, palonosetron, and bowel-preparation agents (picosulfuric acid, polyethylene glycol, sodium sulfate)

Please refer to the package insert for official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction is mechanistically plausible and supported by one rabbit study, but there are no human data or registered trials, and the evidence level is L4. The high TxGNN score is not clinical evidence. Label safety data are also missing, and all US licenses are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Assessment of an ocular formulation and route, including ocular and systemic safety, given the cholinergic adverse effects and the contraindication flags above
- Confirmatory preclinical work and, if supportive, an early-phase human IOP study
- Review of the bupropion interaction and other cholinergic or anticholinergic combinations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


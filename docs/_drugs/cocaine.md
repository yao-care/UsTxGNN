---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
monitor_inn: "COCAINE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "rhinitis", "irritable bowel syndrome", "anaphylaxis", "neurocirculatory asthenia", "atopic conjunctivitis", "food-dependent exercise-induced anaphylaxis", "pharyngitis"]
---

# Cocaine
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

# Cocaine: From Local Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine is a local anesthetic and vasoconstrictor historically used in nasal, oral and laryngeal surgery. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but this is a model prediction only: there are **0 clinical trials** and **1 publication** (a case report that does not involve cocaine), so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license data (pharmacology data describes use as a local anesthetic in nasal, oral and laryngeal surgery) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, cocaine is a local anesthetic that blocks sodium channels and also blocks reuptake of monoamines (including dopamine via DAT). Pharmacology records also list activity at 5-HT3 receptors.

There is no credible mechanistic link between these actions and cauda equina syndrome, which is a compressive neuropathy of the lumbosacral nerve roots, usually from disc pathology, and is treated surgically. The high TxGNN score appears to be a statistical artifact of the knowledge graph rather than a biologically grounded signal. The only retrieved paper is a case report on lumbosacral disc pathology and does not address cocaine.

Other predictions in the list (for example rhinitis, anaphylaxis, pharyngitis) also lack supporting evidence. For rhinitis and pharyngitis, the literature mostly shows cocaine as a cause of mucosal injury, not a treatment. The next-ranked predictions are not strong alternatives either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report/Review | Surgical Neurology International | Case report of distal cauda equina syndrome from lumbosacral disc pathology, with literature review. Does not address cocaine as a treatment. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209575 | Cocaine hydrochloride nasal (Omnivium Pharmaceuticals) | Solution | Not listed; license cancelled |
| NDA209963 | Cocaine hydrochloride (LXO US Inc.) | Solution | Not listed; license cancelled |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: epilepsy, sudden cardiac arrest, heart conduction disease, thyrotoxicosis, hyperthyroidism, Graves disease.
- **Pharmacological targets**: cocaine acts on 5-HT3A/5-HT3AB receptors and the dopamine transporter (DAT; rat data), which is consistent with its stimulant and cardiovascular effects.
- **Related literature**: the retrieved publications describe cocaine-associated harms, including mucosal necrosis, septal and palatal perforation, bronchospasm, allergic reactions, and upper airway injury. Cocaine also has high abuse potential.

Please refer to the package insert for full warnings, contraindications and drug interaction information, as this was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials, the single paper does not involve cocaine, no plausible mechanism links cocaine to cauda equina syndrome, and both US licenses are cancelled. The safety profile (cardiovascular risk, abuse potential, mucosal toxicity) is also unfavorable.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A credible preclinical or mechanistic rationale for cauda equina syndrome
- Evidence of benefit over existing treatments, with a risk-benefit assessment given cocaine's abuse potential and cardiovascular toxicity
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


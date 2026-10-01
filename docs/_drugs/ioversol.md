---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 807
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is an iodinated radiographic contrast agent, marketed in the US as Optiray injection.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (score 99.67%), but this is a model prediction with **0 supporting clinical trials and 0 publications** for that exact term.
The related term **osteoarthritis** has 4 registered trials and 1 publication, but they test an embolization procedure, not ioversol as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Radiographic contrast imaging (the source record lists no approved indication text) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (all under NDA019710) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ioversol is an iodinated contrast agent used to make blood vessels and tissues visible on imaging. It is considered pharmacologically inert, with no known disease-modifying or genetic-susceptibility activity.

The evidence does not show a plausible mechanistic link between the original use (diagnostic imaging) and osteoarthritis. The high TxGNN score most likely reflects proximity in the knowledge graph, not a real biological effect. Other top predictions include rare skeletal dysplasias (brachyolmia, acromesomelic dysplasia) and alopecia, which also have no plausible mechanism.

The only indirect signal is on the related term **osteoarthritis** (rank 2, score 99.63%). Several trials study genicular artery embolization (GAE) for knee osteoarthritis. Ioversol may at most serve as the angiographic contrast agent during the procedure. The trials do not show it is the intervention, and some use Lipiodol (ethiodized oil), a different agent.

---

## Clinical Trial Evidence

No trials are registered for "osteoarthritis susceptibility". The trials below come from the related prediction "osteoarthritis". They test embolization procedures, not ioversol.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Sham-controlled RCT of genicular artery embolization in symptomatic knee OA. The role of ioversol is not confirmed. |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | Pilot sham-controlled GAE trial for knee OA pain (NIH-NIAMS funded). The role of ioversol is unclear. |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Safety of Lipiodol embolization in hand OA. Lipiodol is a different agent. |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Lipiodol emulsion embolization for inflammatory hypervascularization in knee pain. The agent is not ioversol. |

---

## Literature Evidence

None of the retrieved papers tests ioversol as a therapy for the predicted indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Prospective clinical trial | Diagn Interv Imaging | LipioJoint-1: safety and efficacy of transient GAE with an ethiodized oil emulsion in knee OA. It is procedure-related and does not involve ioversol. |
| [22195536](https://pubmed.ncbi.nlm.nih.gov/22195536/) | 2012 | Retrospective cohort | Am J Med | Safety of intravenous iodinated contrast in sickle cell disease. It concerns diagnostic use, not therapeutic benefit (rank 5, hemoglobinopathy). |
| [23321839](https://pubmed.ncbi.nlm.nih.gov/23321839/) | 2013 | Case series / imaging review | J Comput Assist Tomogr | Craniofacial bone infarcts in sickle cell disease (rank 5, hemoglobinopathy). Imaging findings only. |
| [40137121](https://pubmed.ncbi.nlm.nih.gov/40137121/) | 2025 | Computational study | Metabolites | In silico screen of PAD4 inhibitors for rheumatoid arthritis (rank 3). It does not involve ioversol. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019710 | Optiray (Liebel-Flarsheim Company LLC) | Injection | Not specified in the source record |

The record contains three identical entries for this NDA, shown once above. The route is injectable only.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no plausible mechanism and no direct clinical support. The only related trials study embolization procedures, and ioversol is not confirmed to be the intervention. The evidence stays at L5 for the top-ranked term, and at most L4 for the related osteoarthritis term.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Confirmation of which contrast or embolic agent the GAE trials actually use, and whether ioversol plays any role
- A biological rationale linking ioversol to osteoarthritis, if one exists

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


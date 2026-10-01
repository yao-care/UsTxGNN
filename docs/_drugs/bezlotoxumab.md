---
layout: default
title: Bezlotoxumab
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: From Clostridioides difficile Infection Recurrence to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab (brand name ZINPLAVA) is a monoclonal antibody that neutralizes *C. difficile* toxin B. It is used to reduce recurrence of *C. difficile* infection; this indication does not appear in the input's license text and is stated from general drug knowledge.
The TxGNN model predicts it may be effective for **acute female pelvic peritonitis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is a graph-based score only and has no mechanistic or clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reducing recurrence of *C. difficile* infection (not listed in the input license text) |
| Predicted New Indication | Acute female pelvic peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761046) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input record. Bezlotoxumab is known to be a monoclonal antibody that binds and neutralizes *C. difficile* toxin B.

That mechanism does not extend to the predicted indication. Acute pelvic peritonitis is usually a polymicrobial ascending infection (for example *Chlamydia*, *Neisseria* and anaerobes), and toxin B is not a recognized driver. The high score (99.89%, rank 3466) reflects graph proximity in the knowledge graph, not a biological link.

The other nine top predictions do not help either. They include embryonic cyst of fallopian tube, tubal pregnancy, salpingitis isthmica nodosa, disease of uterine broad ligament, lumbar spinal stenosis, abdominal ectopic pregnancy, celiac trunk compression syndrome, abdominal cystic lymphangioma and pelvic varices. They are structural, obstetric or degenerative conditions with no toxin B pathway and form no coherent mechanistic theme, which suggests knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761046 | ZINPLAVA (Merck Sharp & Dohme LLC) | Injection, solution | Not listed in the input record |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism, so it stays at L5 (model prediction only). Its high score should not be read as a therapeutic signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Confirmed mechanism of action data and approved indication text from DrugBank or the label
- Any preclinical or clinical evidence linking toxin B neutralization to pelvic peritonitis; without it, the candidate should not advance
- Consideration of other indications, since none of the top 10 predictions has a plausible mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


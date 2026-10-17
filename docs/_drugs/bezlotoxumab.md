---
layout: default
title: Bezlotoxumab
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
monitor_inn: "BEZLOTOXUMAB"
predicted_indications: ["acute female pelvic peritonitis", "embryonic cyst of fallopian tube", "tubal pregnancy", "salpingitis isthmica nodosa", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "pelvic varices"]
last_modified_at: 2026-10-14
description: "Bezlotoxumab: predicted new indication Acute female pelvic peritonitis (evidence level L5). Approved use: Clostridium difficile colitis"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Bezlotoxumab: From Clostridium difficile Colitis to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab is a monoclonal antibody originally used to reduce recurrence of *Clostridium difficile* colitis.
The TxGNN model predicts it may be effective for **acute female pelvic peritonitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on a graph-based model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis (the approved indication text was not available in the data compiled for this report; this is taken from the knowledge-graph indication records) |
| Predicted New Indication | Acute female pelvic peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single license is cancelled) |
| Number of NDAs | 1 (BLA761046) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bezlotoxumab is, however, a well-established monoclonal antibody that neutralizes *C. difficile* toxin B. Its activity is specific to that toxin, and it is used to reduce recurrence of *C. difficile* infection.

The predicted indication, acute female pelvic peritonitis, is usually a polymicrobial infection and is not typically driven by toxin B. No credible mechanistic link between toxin B neutralization and this condition could be identified. The high TxGNN score (0.999) appears to be a graph-proximity result rather than a biologically grounded signal. The same pattern holds for the other nine top-ranked predictions (for example embryonic cyst of the fallopian tube, tubal pregnancy and lumbar spinal stenosis), which are also unsupported by trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761046 (cancelled) | ZINPLAVA (Merck Sharp & Dohme LLC) | Injection, solution | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found. Use of an antibody in pregnancy-related predicted conditions (such as tubal pregnancy and abdominal ectopic pregnancy among the other ranked predictions) would raise additional safety questions, and no supporting data exist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5), and no plausible mechanistic link exists between toxin B neutralization and acute female pelvic peritonitis. In addition, the only US license is cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A credible biological rationale, such as evidence of toxin B involvement in pelvic peritonitis
- Preclinical or observational evidence supporting the new indication
- Clarification of the cancelled license status and product availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


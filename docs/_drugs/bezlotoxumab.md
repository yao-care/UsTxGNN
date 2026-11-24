---
layout: default
title: Bezlotoxumab
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
monitor_inn: "BEZLOTOXUMAB"
predicted_indications: ["acute female pelvic peritonitis", "embryonic cyst of fallopian tube", "tubal pregnancy", "salpingitis isthmica nodosa", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "pelvic varices"]
last_modified_at: 2026-11-24
description: "Bezlotoxumab: predicted new indication acute female pelvic peritonitis (evidence level L5). In the US: 1 FDA application (1 active)"
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

## Bezlotoxumab: monoclonal antibody neutralizing C. difficile toxin B → acute female pelvic peritonitis
{: .text-alpha }

## One-Sentence Summary

Bezlotoxumab is a monoclonal antibody that neutralizes *Clostridium difficile* toxin B.
The TxGNN model predicts it may be relevant for **acute female pelvic peritonitis**,
but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acute female pelvic peritonitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the FDA-approved prescribing information for bezlotoxumab: "ZINPLAVA (bezlotoxumab) is a human monoclonal antibody that binds to C. difficile toxin B and neutralizes its effects. […] Bezlotoxumab is a human monoclonal antibody that binds C. difficile toxin B with an equilibrium dissociation constant (K d ) of &lt;1×10 -9 M. Bezlotoxumab inhibits the binding of toxin B and prevents its effects on mammalian cells. Bezlotoxumab does not bind to C. difficile toxin A. Activity In Vitro Bezlotoxumab binds to an epitope on toxin B that is conserved across reported strains of C. difficile, although amino acid sequence variation within the epitope does occur." ([DailyMed: Zinplava (bezlotoxumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f479bfe-2bfa-4cc5-9aee-1357364480b0), label version 2024-11-12; accessed 2026-11-19.) Bezlotoxumab is, however, a well-characterized antibody that binds and neutralizes *C. difficile* toxin B, so its activity is specific to that toxin.

Acute female pelvic peritonitis is usually polymicrobial infection and inflammation of the pelvic cavity, and it is not typically driven by toxin B. No credible mechanistic link between toxin B neutralization and this disease could be established. The high score of 0.9989 is a model output only; it is not backed by any trial or publication and likely reflects proximity to other pelvic-region predictions rather than biology.

Other lower-ranked predictions in the same list (for example embryonic cyst of fallopian tube and tubal pregnancy) likewise lack any mechanistic link or supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA761046 | ZINPLAVA | MERCK SHARP DOHME | Injectable; injection | Valid |

<!-- licenses:end -->

The licence record lists Merck Sharp & Dohme LLC as manufacturer. The product is administered as an injectable.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature, and no plausible mechanistic link exists between toxin B neutralization and acute female pelvic peritonitis. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A credible biological rationale, plus preclinical or clinical evidence that toxin B plays a role in this disease
- Confirmation of whether any toxin B-producing organism is implicated in pelvic peritonitis

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zinplava (bezlotoxumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f479bfe-2bfa-4cc5-9aee-1357364480b0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


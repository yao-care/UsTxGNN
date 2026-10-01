---
layout: default
title: Palifermin
parent: Model Prediction Only (L5)
nav_order: 1009
evidence_level: L5
indication_count: 6
---

# Palifermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Palifermin: From Approved Use (Not Recorded in the Data) to Primary Release Disorder of Platelets

## One-Sentence Summary

Palifermin is a recombinant keratinocyte growth factor (KGF/FGF7) sold in the US as KEPIVANCE. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but only **1 loosely related clinical trial** and **0 publications** exist, and neither tests this idea. This is a model-only prediction with no supporting evidence, so we recommend **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (the approved indication text is blank) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125103) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Palifermin acts on epithelial cells through the FGFR2b receptor. The Evidence Pack does not include a detailed mechanism-of-action entry or the original indications, so the prediction cannot be checked against known label pharmacology.

The evidence review found **no plausible mechanistic link** to the predicted disease. Primary release disorders of platelets are intrinsic defects in platelet granule secretion, and no known KGF pathway acts on that process. The score of 99.94% is most likely an artifact of the knowledge-graph topology. Several inherited platelet disorders cluster together in the graph and receive similarly high scores, so the score does not reflect a real pharmacological signal.

The same pattern holds for the other five predictions for this drug, all of which are inherited platelet or bleeding disorders:

| Rank | Predicted Disease | TxGNN Score | Why There Is No Link |
|------|------|------|------|
| 2 | Glanzmann thrombasthenia | 99.93% | Defect of the integrin αIIbβ3 receptor; KGF signaling does not correct or bypass it |
| 3 | Pseudo-von Willebrand disease | 99.91% | Gain-of-function defect of platelet GPIb-alpha; unrelated to epithelial KGF signaling |
| 4 | Hemorrhagic disorder due to a constitutional thrombocytopenia | 99.50% | Inherited defect of platelet production; palifermin is not a thrombopoietic agent |
| 5 | Bleeding diathesis due to a collagen receptor defect | 99.48% | Defective platelet collagen receptors (GPVI or α2β1); KGF does not restore them |
| 6 | Scott syndrome | 99.38% | Defective phosphatidylserine exposure (ANO6/TMEM16F); not addressed by an epithelial growth factor |

None of these five has any clinical trial or literature support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol comparing post-transplant cyclophosphamide-based drug combinations to prevent graft-versus-host disease (GVHD) after mismatched unrelated donor stem cell transplant. It does not test a platelet function disorder, and palifermin's role in the trial was not verified. Relevance grade: C (no direct or indirect evidence for the predicted indication). |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125103 | KEPIVANCE (Swedish Orphan Biovitrum AB) | Lyophilized powder for injection | — (not stated in the data) |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) and stops at the first screening stage (S0). The single related trial addresses GVHD prophylaxis rather than platelet disorders, there are no publications, and there is no plausible mechanistic link between epithelial KGF signaling and platelet secretion defects. The high score is likely a graph artifact.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- The drug's mechanism of action and original indications, so the prediction can be cross-checked
- Any preclinical or clinical evidence linking KGF/FGFR2b signaling to platelet function or production
- Route and formulation compatibility assessment, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


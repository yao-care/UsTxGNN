---
layout: default
title: Paromomycin
parent: Model Prediction Only (L5)
nav_order: 1016
evidence_level: L5
indication_count: 8
---

# Paromomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Paromomycin: From Luminal Antimicrobial Use to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Paromomycin is a poorly absorbed oral aminoglycoside that acts in the gut lumen as an antibacterial and amebicide.
The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**, but **0 clinical trials** and **0 publications** support this prediction, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Paromomycin is an aminoglycoside antibiotic that acts on ribosomes and stays mostly in the gut lumen after oral dosing. Its established use is as a luminal antimicrobial and amebicide.

The reviewed evidence does not support a link between this use and idiopathic copper-associated cirrhosis. Paromomycin has no known role in copper metabolism or copper-related liver injury. The TxGNN score (0.999) is identical across five liver and portal diseases: idiopathic copper-associated cirrhosis, hepatoportal sclerosis, hepatopulmonary syndrome, early-onset familial noncirrhotic portal hypertension, and primitive portal vein thrombosis. This pattern suggests a graph-neighborhood artifact rather than a disease-specific signal.

The prediction should be treated as a low-confidence computational hypothesis. Its high score reflects the model's graph structure, not biological or clinical support.

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
| ANDA065173 | Humatin (Waylis Therapeutics LLC) | Capsule (oral) | — |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings and contraindications. Aminoglycosides as a class carry a nephrotoxicity concern, which would need attention in any liver-disease population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score that is identical across five unrelated liver and portal diseases. There are no trials or literature, and no plausible mechanism has been identified. Paromomycin's poor systemic absorption and class nephrotoxicity also argue against use in this setting.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, and a testable hypothesis linking paromomycin to copper-associated liver injury
- Any preclinical or clinical signal specific to this disease
- Route compatibility and similarity-to-original-indication analysis, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


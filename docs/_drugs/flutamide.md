---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 729
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "FLUTAMIDE"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
description: "Flutamide: predicted new indication Fibroma of prostate (evidence level L5). Approved use: Not recorded in the local data"
---

# Flutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Flutamide: Fibroma of prostate
{: .text-alpha }

## One-Sentence Summary

Flutamide is an oral antiandrogen originally used to treat prostate cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibroma of prostate |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Flutamide is a nonsteroidal androgen receptor (AR) antagonist. Its efficacy in prostate cancer is established, and mechanistically it may be applicable to androgen-driven prostate disease.

The predicted entry combines prostate cancer with brain cancer susceptibility. It describes an inherited predisposition, not a disease state a drug can treat. There is no plausible mechanistic link to brain cancer, and no trials or literature support this entry.

Other predictions for flutamide have more support, though none is a clear new indication:
- **Male reproductive organ cancer** has the most trial and literature evidence, but it is essentially the original prostate cancer indication rather than true repurposing.
- **Benign reproductive system neoplasm** is supported mainly by small, older human studies of flutamide's effects on prostate tissue (for example in benign prostatic hyperplasia).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075298 | Eulexin (Waylis Therapeutics LLC) | Capsule (oral) | Not specified in the license record; status: valid |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal antiandrogen), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Generally low for oral hormonal agents; please refer to the package insert |
| Monitoring Items | Liver function (hepatic safety is a key concern for this drug); other parameters per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from drug-disease relationships in the knowledge graph, not from label text): liver failure, liver disease, gallbladder disease, methemoglobinemia, sulfhemoglobinemia, hyperbilirubinemia, hereditary hyperbilirubinemia, Gilbert syndrome, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Drug interactions**: 100 interactions were found in total. The main ones are:
  - **Major**: dolasetron, cisapride.
  - **Moderate**: clarithromycin, levofloxacin, ondansetron, palonosetron, naltrexone, famotidine, loperamide, obeticholic acid, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate, lactulose, lactitol, castor oil, glycerin).
  - **Minor**: metronidazole.
- **Hepatotoxicity**: the compiled assessment flags this as a concern, consistent with the liver-related signals above. It would matter especially in populations already taking hepatotoxic drugs.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted entry is a genetic susceptibility label with no supporting trials or literature (L5, model prediction only). The high score appears to reflect flutamide's existing prostate cancer association. In addition, the only US license on record is cancelled.

**To proceed, the following is needed:**
- A clearer, treatable disease definition in place of the susceptibility label
- Direct clinical or preclinical evidence for the predicted indication
- Mechanism of action data (MOA)
- The full package insert warnings and contraindications, especially hepatotoxicity
- Re-verification of US regulatory status, since only a cancelled license is on record
- Consideration of the better-supported alternative predictions (male reproductive organ cancer, benign reproductive system neoplasm) as separate evaluations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


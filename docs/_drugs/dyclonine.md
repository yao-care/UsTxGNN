---
layout: default
title: Dyclonine
parent: Model Prediction Only (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "DYCLONINE"
predicted_indications: ["bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "gastroduodenitis", "peptic ulcer disease", "irritable bowel syndrome"]
description: "Dyclonine: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Dyclonine
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

## Dyclonine: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Dyclonine is a local anesthetic.
The TxGNN model predicts it may be effective for **Bronchitis** (top-ranked prediction), but **0 clinical trials** and **0 publications** currently support this specific prediction.
The only indication with any supporting literature among the top 10 predictions is irritable bowel syndrome (1 mechanistic study).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, dyclonine is a local anesthetic that is understood to block voltage-gated sodium channels. This could theoretically dampen the activity of airway sensory nerves and suppress cough.

The link between dermatitis and bronchitis is weak. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Dyclonine would at most relieve symptoms (such as cough or irritation); there is no basis to expect it to treat the underlying airway inflammation or infection. This rationale is speculative and not supported by data.

Other top predictions show the same pattern. Most are skin diseases (dermatomyositis, acrodermatitis chronica atrophicans, acne keloid, hydroa vacciniforme) or other conditions for which no plausible disease-modifying mechanism exists. For these, symptomatic relief of pain or itch is the most that could be argued.

The one prediction with some biological plausibility is **irritable bowel syndrome (IBS)**. Visceral hypersensitivity is a recognized IBS mechanism, and local anesthesia of sensory nerves could theoretically reduce visceral pain signaling.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis or for any of the other top 10 predicted indications.

---

## Literature Evidence

No literature is available for bronchitis. For the tenth-ranked prediction, irritable bowel syndrome, one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8907258](https://pubmed.ncbi.nlm.nih.gov/8907258/) | 1996 | Mechanistic study | The Journal of the Oklahoma State Medical Association | Studied mucosal application of dyclonine (40 ml enema, versus saline) before rectosigmoid distension in IBS patients and volunteers (n = 10), investigating visceral hypersensitivity. Cutaneous pain thresholds did not differ between groups, whereas IBS patients had a lower pain threshold. The abstract is truncated, so the effect of dyclonine itself cannot be confirmed from the available text. |

This study supports biological plausibility only and is not evidence of efficacy.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA200480 | DycloPro (Septodont Inc) | Solution | Not available (valid) |
| M022 | Sucrets Sore Throat Wild Cherry (Insight Pharmaceuticals LLC) | Lozenge | Not available (valid) |
| M003 | Leader Liquid Bandage (LEADER / Cardinal Health 110, Inc.) | Liquid | Not available (valid) |

The drug is marketed in the US, with 3 valid licenses.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph links dyclonine with epilepsy, sudden cardiac arrest, heart conduction disease, and respiratory failure. These are graph-derived associations and should be verified against official labeling.
- **Drug Interactions**: No interactions were found in the queried database.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a model score alone, with no clinical trials, no literature, and only a speculative mechanistic link. The drug's US licenses are all cancelled, and mechanism-of-action and label safety data are missing. Of the top 10 predictions, only irritable bowel syndrome has any supporting study, and it is a single 1996 mechanistic study that does not demonstrate efficacy.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence that dyclonine affects airway sensory nerve activity or cough, if bronchitis is to be pursued
- A literature and trial search focused on IBS and visceral pain, as this is the most plausible secondary direction (a research question rather than a development candidate at this stage)
- Assessment of route and formulation feasibility, since the available products were topical or oral-mucosal and none is designed for airway or gastrointestinal delivery
- Review of the graph-derived contraindications (epilepsy, cardiac conduction disease, respiratory failure), especially relevant for any airway-targeted use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


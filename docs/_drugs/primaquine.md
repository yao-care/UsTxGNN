---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 1082
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "PRIMAQUINE"
predicted_indications: ["myiasis", "creeping myiasis", "furuncular myiasis", "wound myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
description: "Primaquine: predicted new indication Myiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Primaquine: Myiasis
{: .text-alpha }

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used for the radical cure of *Plasmodium vivax* malaria.
The TxGNN model predicts it may be effective for **myiasis** (fly-larva infestation) with a very high score, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on model output alone and has no biological rationale behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of FDA Applications | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primaquine acts on protozoan parasites, notably the liver stages and dormant hypnozoites of *P. vivax*/*P. ovale* and mature *P. falciparum* gametocytes, probably through oxidative stress mechanisms.

Myiasis is a different kind of disease. It is an infestation by fly larvae, which are multicellular arthropods rather than protozoa. Treatment is normally larval removal, occlusion or debridement, with ivermectin sometimes used. Primaquine has no known activity against fly larvae.

The high TxGNN score therefore likely reflects similarities the model learned between related diseases, not biological evidence, and is probably driven by generic antiparasitic associations. The related subtypes (creeping, furuncular and wound myiasis) received nearly identical scores, which supports this reading. No mechanistic link between primaquine and myiasis could be identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All three US authorizations for primaquine are valid.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| NDA008316 | Primaquine Phosphate | Tablet, film coated | Sanofi-Aventis U.S. LLC | Valid |
| ANDA206043 | Primaquine Phosphate | Tablet, film coated | Ingenus Pharmaceuticals, LLC | Valid |
| ANDA204476 | Primaquine Phosphate | Tablet | Unichem Pharmaceuticals (USA), Inc. | Valid |

---

## Safety Considerations

- **Contraindication signals (from drug–disease knowledge graph, not label text)**: neutropenia, agranulocytosis, G6PD deficiency, hemolytic anemia, methemoglobinemia due to methemoglobin reductase deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency.
- **Drug Interactions**: 100 interactions were recorded. Examples from the first 20 returned:
  - **Major**: dolasetron.
  - **Moderate**: clarithromycin, levofloxacin, ondansetron, palonosetron, granisetron, famotidine, alosetron, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, sodium sulfate, magnesium citrate, glycerin, castor oil).
  - **Minor**: metronidazole.

Please refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction has no clinical trials, no literature and no plausible mechanism. Its Evidence Level is L5, and all three US licenses are valid. The hemolysis risk in G6PD deficiency adds further caution, so there is no basis for advancing this indication.

**To proceed, the following is needed:**
- Any preclinical or mechanistic evidence of primaquine activity against fly larvae. Without it, further investment is not justified.
- Detailed mechanism of action data for primaquine.
- Full package insert warnings and contraindications.
- Verification of current product availability in the US.

Other predictions for this drug are better supported and may deserve review first. **Malaria** (L1, 40 registered trials) is essentially an on-label or extension use. **Pneumocystosis** (L1) is supported by older Phase 3 data on clindamycin plus primaquine as a second-line regimen. Both would need G6PD screening as a guardrail.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


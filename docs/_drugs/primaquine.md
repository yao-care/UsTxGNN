---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 1082
evidence_level: L5
indication_count: 8
---

# Primaquine
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

# Primaquine: From Malaria to Myiasis

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, used for radical cure of *P. vivax*/*P. ovale* malaria and to block *P. falciparum* transmission.
The TxGNN model ranks **myiasis** (a fly-larvae infestation of tissue) as its top new-indication prediction.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only and no supporting evidence was found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (the US license records contain no indication text; this is based on primaquine's established use as described in the evidence pack) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primaquine is an 8-aminoquinoline whose efficacy against *Plasmodium* parasites (liver-stage hypnozoites and mature gametocytes) is well established. The pack has no mechanistic link to fly larvae.

Myiasis is an infestation by dipteran (fly) larvae, which are arthropods, not protozoa. Primaquine has no known activity against arthropods. The very high score (99.76%) most likely reflects the drug sitting close to antiparasitic drugs in the knowledge graph, not a pharmacological reason.

The same reasoning applies to the closely related predictions creeping myiasis, furuncular myiasis and wound myiasis (each about 99.7%). None has any trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA008316 | Primaquine Phosphate | Tablet, film coated | Sanofi-Aventis U.S. LLC |
| ANDA206043 | Primaquine Phosphate | Tablet, film coated | Ingenus Pharmaceuticals, LLC |
| ANDA206043 | Primaquine Phosphate | Tablet, film coated | AvKARE |
| ANDA204476 | Primaquine Phosphate | Tablet | Unichem Pharmaceuticals (USA), Inc. |
| ANDA204476 | Primaquine Phosphate | Tablet | PD-Rx Pharmaceuticals, Inc. |

All products are oral tablets. The official label warnings and contraindications were not captured in this pack.

## Safety Considerations

Please refer to the package insert for safety information.

Safety points from the supporting evidence for other primaquine indications (not from the label):
- **Hemolysis in G6PD deficiency**: G6PD testing before use is emphasized throughout the literature and trials.
- **Methemoglobinemia**: reported in the literature, including a 2025 case report.
- **Pregnancy and lactation**: use is restricted. A Phase 2/3 pharmacokinetic study in lactating women (NCT07060404) has not yet started recruiting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction is model-only (L5): no trials, no literature, and no plausible mechanism, because primaquine acts on *Plasmodium* and not on arthropod larvae. It should not be advanced.

**Other predictions in the pack:**

| Predicted Indication | Score | Evidence Level | Decision | Note |
|------|------|------|------|------|
| Pneumocystosis | 99.32% | L1 | Proceed with Guardrails | Clindamycin plus primaquine is an established second-line regimen. It is supported by a completed Phase 3 trial (NCT00000640, n=290) and by systematic reviews and guidelines. |
| Malaria | 99.38% | L2 | Proceed with Guardrails | This is primaquine's on-label core use, not true repurposing. |
| Toxoplasmosis | 99.64% | L4 | Hold | Only indirect review mentions. |
| Nocardiosis | 99.42% | L5 | Hold | Bacterial infection, no mechanism and no evidence. |

Pneumocystosis is the only genuine repurposing candidate with strong evidence.

**To proceed, the following is needed:**
- Do not pursue the myiasis group unless independent preclinical or clinical evidence appears.
- Obtain the FDA package insert (warnings and contraindications) to fill the label safety gap.
- Obtain mechanism of action data from DrugBank.
- If pursuing pneumocystosis, define guardrails: second-line use only when TMP-SMX cannot be used, mandatory G6PD screening, and methemoglobin monitoring.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


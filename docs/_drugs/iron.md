---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 811
evidence_level: L5
indication_count: 6
---

# Iron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Iron: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Iron is an essential micronutrient used to treat and prevent iron deficiency anemia. The TxGNN model additionally flags **Plummer-Vinson syndrome** — a rare disorder whose classic diagnostic triad already includes iron deficiency anemia — as a strong-scoring candidate, supported by **19 publications** documenting iron repletion as the standard, causal treatment for this condition. No dedicated clinical trials exist for this pairing, largely because withholding iron from an anemic patient for a placebo-controlled design raises ethical concerns in this rare disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (general medical use; no Taiwan license on file — drug not marketed) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iron is an essential trace element required for hemoglobin synthesis and erythropoiesis; its efficacy in correcting iron deficiency anemia is well established, and mechanistically this extends directly to conditions in which iron deficiency anemia is a core pathological feature.

Plummer-Vinson syndrome (also called Paterson-Kelly syndrome) is defined by a classic triad: dysphagia, iron deficiency anemia, and esophageal webs. Because iron deficiency anemia is one of the three defining diagnostic components, iron repletion is not a speculative new mechanism but a direct, causal intervention — multiple case series report that iron supplementation resolves anemia and, in many patients, improves or eliminates dysphagia symptoms.

It should be noted transparently: this is best understood as an **established clinical practice being surfaced by the model**, rather than a genuinely novel repurposing hypothesis. The evidence base consists of reviews, case reports, and case series rather than randomized controlled trials, largely because the rarity of the syndrome and the ethical difficulty of withholding iron from an anemic patient make RCTs impractical.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Review | Journal of Blood Medicine | Overview of Plummer-Vinson syndrome (PVS) as a triad of dysphagia, iron deficiency anemia, and esophageal web; notes declining prevalence, possibly linked to improved nutrition |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet Journal of Rare Diseases | Classical PVS/Paterson-Kelly triad description; epidemiology poorly characterized due to rarity |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Review | Diseases of the Esophagus | Two PVS cases in middle-aged women; iron supplementation resulted in elimination of dysphagia symptoms |
| [39760192](https://pubmed.ncbi.nlm.nih.gov/39760192/) | 2025 | Systematic Review | Oral Diseases | Systematic review of head and neck cancer manifestations and oral comorbidities in PVS patients |
| [34651287](https://pubmed.ncbi.nlm.nih.gov/34651287/) | 2022 | Case Report/Review | Immunologic Research | Case-based review of PVS occurring in a patient with primary Sjögren syndrome; shared disease mechanisms discussed |
| [38034443](https://pubmed.ncbi.nlm.nih.gov/38034443/) | 2023 | Case Report | JPGN Reports | 4-year-old child with PVS treated via endoscopic balloon dilatation of esophageal webs with iron deficiency correction |
| [41756818](https://pubmed.ncbi.nlm.nih.gov/41756818/) | 2026 | Case Report | Case Reports in Hematology | 26-year-old woman with 5-year progressive dysphagia and long-standing iron deficiency diagnosed with PVS |
| [39391408](https://pubmed.ncbi.nlm.nih.gov/39391408/) | 2024 | Case Report | Cureus | Case exploring potential overlap between xanthogranulomatous pyelonephritis and PVS in a single patient |
| [40248609](https://pubmed.ncbi.nlm.nih.gov/40248609/) | 2025 | Case Report | Clinical Case Reports | PVS presenting with coexistent thyro-cardiac disease and acute decompensated heart failure |
| [20890819](https://pubmed.ncbi.nlm.nih.gov/20890819/) | 2010 | Review | La Tunisie Medicale | Summary description of PVS as dysphagia, iron-deficiency anemia, and esophageal webbing, predominantly in white women |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Iron deficiency anemia is a defining component of the Plummer-Vinson syndrome triad, making iron repletion a mechanistically direct and well-documented intervention rather than a speculative hypothesis. However, the evidence base is limited to reviews and case reports/series (no RCTs), and this candidate represents an extension of an already-recognized clinical use rather than a genuinely novel discovery — both facts warrant guardrails before any formal positioning.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings/contraindications for iron (currently a blocking data gap — DG001)
- Formal mechanism of action (MOA) documentation (currently a data gap — DG002)
- Route compatibility and available dosage form data (marked "pending" in the evidence pack)
- Explicit labeling of this candidate internally as "known standard-of-care extension" rather than "novel repurposing hypothesis," to avoid overstating the TxGNN model's contribution
- Local Taiwan regulatory/market status confirmation, since the drug currently shows 0 licenses and "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


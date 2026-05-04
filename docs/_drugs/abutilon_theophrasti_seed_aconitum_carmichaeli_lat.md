---
layout: default
title: Abutilon Theophrasti Seed Aconitum Carmichaeli Lat
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Abutilon Theophrasti Seed Aconitum Carmichaeli Lat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Six-Herb Combination Formula: Repurposing Evaluation Incomplete — No Prediction Data Available

## One-Sentence Summary

This submission covers a complex herbal combination comprising six botanical and zoological ingredients — including *Artemisia annua*, Asian Ginseng, *Aconitum carmichaeli*, and cantharidin-containing *Lytta vesicatoria* — with no registered indication and no Taiwan market approval.
The TxGNN pipeline returned **no predicted indications** for this compound, and key inputs including mechanism of action and regulatory safety data are absent.
A complete repurposing evaluation cannot be performed at this stage; a **Hold** decision is recommended pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | None (no TxGNN prediction returned) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no actual studies; model returned no output |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this formula, so no mechanistic repurposing rationale can be constructed. This section instead documents what is pharmacologically known about the six individual components, to support a future re-run with disaggregated inputs.

The formula contains six active ingredients spanning highly divergent pharmacological classes:

| Component | Known Pharmacological Class | Key Active Compound |
|---|---|---|
| *Abutilon theophrasti* seed (苘麻子) | TCM — clearing heat, promoting urination | Mucilage, flavonoids |
| *Aconitum carmichaeli* lateral root (附子) | Analgesic, cardiotonic; **highly toxic** | Aconitine, mesaconitine |
| *Artemisia annua* flowering top (青蒿) | Antimalarial; emerging oncology/autoimmune evidence | Artemisinin |
| Asian Ginseng (人參) | Adaptogenic, immunomodulatory | Ginsenosides |
| *Lytta vesicatoria* (斑蝥) | Cytotoxic (protein phosphatase inhibitor) | Cantharidin |
| *Salix alba* bark (白柳皮) | Anti-inflammatory, analgesic | Salicin (aspirin precursor) |

Because no original indication is registered and TxGNN returned no scored candidates, a pharmacological bridge between this combination and a new disease target cannot currently be established. Notably, *Artemisia annua* (artemisinin) and *Lytta vesicatoria* (cantharidin) are each individually mappable to DrugBank nodes and have published repurposing evidence — disaggregating the formula and re-running those components individually is the recommended next step.

---

## Safety Considerations

The extracted safety fields contain no usable data. However, several components of this formula carry well-documented safety concerns that any future evaluation must address:

- **Aconitum carmichaeli lateral root**: Contains cardiotoxic and neurotoxic aconitine alkaloids. Overdose causes life-threatening ventricular arrhythmia and peripheral neuropathy. Traditional processing (炮制, e.g., prolonged heating) is required to reduce aconitine content; raw root is considered highly toxic in all regulatory jurisdictions.
- **Lytta vesicatoria (cantharidin)**: Extremely narrow therapeutic window. Causes severe mucosal irritation, renal tubular toxicity, and hemorrhagic cystitis. Classified as a controlled or restricted substance in many countries.
- **Salix alba bark**: Contraindicated in patients with salicylate hypersensitivity, peptic ulcer disease, and in children under 12 (risk of Reye's syndrome). May potentiate anticoagulant effects of warfarin and NSAIDs.
- **Artemisia annua**: Generally well-tolerated at therapeutic doses. Inhibits CYP3A4 and may alter plasma levels of co-administered drugs metabolized by this pathway.

Please refer to each component's individual package insert and safety monographs for a comprehensive assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This combination formula has no registered indication, no DrugBank ID, and returned zero TxGNN predictions. The data inputs required for a valid repurposing evaluation are either missing or unmapped, making it impossible to assess mechanistic plausibility, evidence strength, or safety-benefit ratio.

**To proceed, the following is needed:**

- **Disaggregate the formula**: Re-run TxGNN individually for *Artemisia annua* (artemisinin, DrugBank DB13132), cantharidin (*Lytta vesicatoria*, DrugBank DB04571), and ginsenosides (Asian Ginseng) — each has a known DrugBank node and existing repurposing literature.
- **Define the formula's original intended use**: Determine whether this is a registered traditional medicine formulation in any jurisdiction (e.g., China NMPA, Taiwan TFDA traditional medicine track) and extract the approved indication.
- **Obtain MOA data**: Query DrugBank API and ChEMBL for each active ingredient to build a mechanistic profile.
- **Safety data remediation**: Download any available TFDA or NMPA product monographs and extract key warnings and contraindications, especially for aconitine and cantharidin content.
- **Assess cytotoxicity classification**: If the formula is intended for oncological use (cantharidin and artemisinin both have anti-tumor evidence), a Cytotoxicity section per antineoplastic drug handling standards should be completed prior to any clinical consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


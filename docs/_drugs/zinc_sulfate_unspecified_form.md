---
layout: default
title: Zinc Sulfate Unspecified Form
parent: 僅模型預測 (L5)
nav_order: 1309
evidence_level: L5
indication_count: 5
---

# Zinc Sulfate Unspecified Form
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Zinc Sulfate: From Trace-Element Supplementation to Multiple Predicted Indications

## One-Sentence Summary

> This evidence pack does not contain documented original-indication or regulatory data for zinc sulfate (unspecified form) — it is not currently marketed in Taiwan or reflected with any Taiwan NDA. TxGNN has generated **5 predicted new indications** for this candidate, but the strength of supporting evidence varies enormously: only **dermatitis** (zinc-deficiency / radiation-induced subtypes) reaches RCT-level evidence (**L2**), one indication (**bronchitis**) has mixed/indirect literature (**L3**), and the remaining three (severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract) are supported by mechanistic reasoning alone (**L5**), with little to no zinc-sulfate-specific literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` is empty; zinc sulfate is generally known as a trace-element/mineral supplement) |
| Number of Predicted Indications Evaluated | 5 |
| Best-Supported Indication | **Dermatitis** (zinc-deficiency and radiation-induced subtypes) — TxGNN score 99.15%, Evidence Level **L2** |
| US/Taiwan Market Status | Not marketed (0 licenses) |
| Number of NDAs | 0 |
| Overall Recommended Decision | **Proceed with Guardrails** (dermatitis subtypes only) / **Hold** for all other predicted indications |

### Summary of All Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Severe nonproliferative diabetic retinopathy | 99.84% | L5 | S0 | Hold |
| 2 | Diabetic retinopathy | 99.76% | L5 | S0 | Hold |
| 3 | Bronchitis | 99.61% | L3 | S1 | Research Question |
| 4 | Diabetic cataract | 99.35% | L5 | S0 | Hold |
| 5 | Dermatitis | 99.15% | **L2** | **S2** | **Proceed with Guardrails** |

Note: TxGNN prediction score does not correlate with evidence strength here — the highest-ranked prediction (severe NPDR) has zero supporting literature, while the lowest-ranked (dermatitis) has the strongest clinical evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (`original_moa: [Data Gap]`, flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, zinc is an essential trace element and cofactor for Cu/Zn-superoxide dismutase (SOD), metallothionein, and numerous enzymes involved in immune regulation, epithelial differentiation, and antioxidant defense. This general mechanistic role underlies all five TxGNN predictions, but the strength of the underlying rationale differs sharply by indication:

**Dermatitis (strongest candidate):** Zinc deficiency is a well-established, direct cause of a specific dermatitis subtype (acrodermatitis enteropathica), for which zinc replacement is the accepted standard of care — this is fundamentally a deficiency-correction indication rather than a novel repurposing mechanism. Separately, zinc's anti-inflammatory and keratinocyte-modulating properties have RCT support for **prevention of radiation-induced dermatitis**. However, many of the retrieved literature results concern veterinary/agricultural dermatitis (cattle, sheep, poultry) and are not applicable to human general dermatitis (eczema, contact dermatitis) — species and subtype mismatches should be excluded during evidence curation.

**Bronchitis:** Zinc's immunomodulatory and mild antiviral activity provides a plausible mechanistic basis for airway anti-inflammatory effects. One double-blind placebo-controlled RCT exists, but it evaluated **acute bronchiolitis in children**, not bronchitis broadly, and definitional mismatch with the target indication should be resolved before further evaluation.

**Diabetic retinopathy / severe NPDR / diabetic cataract:** These three predictions rest solely on zinc's role as a cofactor for antioxidant enzymes in ocular tissue (Cu/Zn-SOD, metallothionein), a theoretical extrapolation with **no direct clinical or preclinical zinc-sulfate studies** identified. The two literature hits retrieved for diabetic retinopathy concern a vanadium compound and a PAI-1 transgenic mouse model respectively — neither studies zinc sulfate directly, and neither should be treated as supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the five predicted indications (`clinical_trials` and `ictrp_trials` are empty across all entries).

---

## Literature Evidence

### Dermatitis (L2 — strongest evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28168533](https://pubmed.ncbi.nlm.nih.gov/28168533/) | 2017 | RCT | Biol Trace Elem Res | Zinc sulfate ± growth hormone reduced radiation-induced skin injury in a placebo-controlled rat model |
| [1090826](https://pubmed.ncbi.nlm.nih.gov/1090826/) | 1975 | Clinical study | NEJM | Oral zinc sulfate resolved acrodermatitis enteropathica in an adult patient with confirmed zinc deficiency |
| [12383101](https://pubmed.ncbi.nlm.nih.gov/12383101/) | 2002 | Case report | Pediatr Dermatol | Zinc sulfate 40 mg/day resolved acrodermatitis enteropathica in a 21-month-old with low plasma zinc |
| [16960696](https://pubmed.ncbi.nlm.nih.gov/16960696/) | 2007 | Case series | Eur J Pediatr | Zinc-deficiency dermatitis in 10 breast-fed preterm infants, often misdiagnosed as eczema/impetigo |
| [6886096](https://pubmed.ncbi.nlm.nih.gov/6886096/) | 1983 | Case series/review | J Am Acad Dermatol | Acrodermatitis enteropathica case in pregnancy; markedly decreased zinc levels |
| [30038513](https://pubmed.ncbi.nlm.nih.gov/30038513/) | 2018 | Open-label study | Clin Cosmet Investig Dermatol | Dermo-cosmetic product containing zinc sulfate improved hand eczema over 21 days |
| [37308289](https://pubmed.ncbi.nlm.nih.gov/37308289/) | 2023 | RCT (veterinary — species mismatch) | Vet Rec | Zinc sulfate footbath vs. topical oxytetracycline for ovine digital dermatitis (not applicable to humans) |
| [38670340](https://pubmed.ncbi.nlm.nih.gov/38670340/) | 2024 | Study (veterinary — species mismatch) | J Dairy Sci | Zinc sulfate footbath for digital dermatitis in dairy cattle (not applicable to humans) |

**Caution:** Several additional hits (acrodermatitis enteropathica reviews/case reports, e.g. PMID 18328205, 37214014, 1990299, 2621529) reinforce the deficiency-correction indication but do not represent novel repurposing evidence. Veterinary studies (cattle/sheep) should be excluded from human indication assessment.

### Bronchitis (L3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28011970](https://pubmed.ncbi.nlm.nih.gov/28011970/) | 2016 | RCT (double-blind, placebo-controlled) | Infez Med | Oral zinc sulfate in 100 children with acute bronchiolitis (not bronchitis) showed effects on symptom recovery timeline |
| [2063340](https://pubmed.ncbi.nlm.nih.gov/2063340/) | 1991 | Clinical-experimental study | Ter Arkh | Trace element (zinc/copper) correction studied in chronic obstructive bronchitis, rat and human data |
| [6966823](https://pubmed.ncbi.nlm.nih.gov/6966823/) | 1980 | Occupational cohort study | Scand J Work Environ Health | Occupational zinc/cobalt exposure study; cobalt (not zinc) associated with increased asthma risk |
| [33347551](https://pubmed.ncbi.nlm.nih.gov/33347551/) | 2020 | Animal study (poultry) | Avian Dis | Zinc/manganese feed additives tested against infectious bronchitis coronavirus in chickens (not human-applicable) |
| [10774827](https://pubmed.ncbi.nlm.nih.gov/10774827/) | 2000 | Animal model | Toxicol Sci | Rat bronchitis model used to study particulate matter exposure, not zinc treatment |

### Diabetic Retinopathy (L5 — non-specific)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12203906](https://pubmed.ncbi.nlm.nih.gov/12203906/) | 2002 | Review/mechanistic | Chem Rec | Discusses vanadium (not zinc) complexes for diabetes management, mentions retinopathy as a complication |
| [10892876](https://pubmed.ncbi.nlm.nih.gov/10892876/) | 2000 | Basic research (animal model) | Invest Ophthalmol Vis Sci | PAI-1 overexpression study in transgenic mice; not a zinc study |

Neither publication studies zinc sulfate directly; both were retrieved on disease-term relevance only.

### Severe Nonproliferative Diabetic Retinopathy / Diabetic Cataract (L5)

Currently no related literature available for either indication.

---

## US Market Information

Zinc sulfate (unspecified form) is **not currently marketed** in Taiwan under this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No NDA/license records are available for review.

---

## Safety Considerations

Two data gaps are flagged for this candidate, one of which is **Blocking**:

- **TFDA label warnings/contraindications (Blocking gap, DG001):** Not yet retrieved — this is required before any Stage 1 (S1) safety screening can proceed.
- **Mechanism of action (High-severity gap, DG002):** Not yet retrieved from DrugBank.
- Drug-drug interaction query returned no results (`query_status: not_found`, 0 interactions found) — this should be treated as "not yet searched," not as "no interactions exist."

Please refer to the official package insert (once available) for complete safety information.

---

## Conclusion and Next Steps

**Decision by indication:**

| Indication | Decision |
|------------|----------|
| Dermatitis (zinc-deficiency / radiation-induced subtypes) | **Proceed with Guardrails** |
| Bronchitis | **Hold — Research Question** (definitional mismatch: existing RCT is in bronchiolitis, not bronchitis) |
| Severe NPDR, Diabetic retinopathy, Diabetic cataract | **Hold** (L5, mechanism-only, no zinc-specific evidence) |

**Rationale:**
Dermatitis is the only indication with RCT-level evidence (radiation-induced dermatitis prevention) plus well-established deficiency-correction precedent (acrodermatitis enteropathica), justifying guarded progression. However, this is arguably not true "repurposing" but restoration-of-normal-physiology in a deficiency state, and should be scoped narrowly (zinc-deficiency and radiation-induced dermatitis subtypes) rather than general dermatitis. Bronchitis has only indirect/mismatched pediatric bronchiolitis data. The three ophthalmic/diabetic-complication predictions have no zinc-sulfate-specific evidence and rest entirely on theoretical antioxidant-cofactor reasoning.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain TFDA/FDA label warnings and contraindications before any indication can clear S1 safety screening.
- Resolve **DG002**: obtain confirmed MOA from DrugBank to validate mechanistic rationale.
- For dermatitis: narrow scope to zinc-deficiency and radiation-induced subtypes; exclude veterinary studies from the evidence base; seek human RCTs in general/atopic/contact dermatitis if broader indication is intended.
- For bronchitis: clarify whether bronchiolitis evidence can be extrapolated to bronchitis, or seek trials specific to bronchitis.
- For the three L5 ocular/diabetic-complication predictions: no further action recommended until direct zinc-sulfate preclinical or clinical data emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


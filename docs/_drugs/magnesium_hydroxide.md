---
layout: default
title: Magnesium Hydroxide
parent: Moderate Evidence (L3-L4)
nav_order: 883
evidence_level: L3
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

# Magnesium Hydroxide: From Antacid/Laxative Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium hydroxide is a long-established over-the-counter antacid and laxative, sold in the US mainly as Milk of Magnesia.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but there are **0 registered clinical trials** and **20 publications** behind this direction. Most of the publications are older studies of aluminum/magnesium combination antacids or preclinical work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antacid / laxative (inferred from product types; the label indication text is not provided in the data) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed authorizations, mostly OTC monograph M007) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology and the retrieved literature, magnesium hydroxide neutralizes gastric acid and raises intragastric pH. Preclinical studies of aluminum/magnesium antacids also point to mucosal protection through endogenous prostaglandins (PMID 2595273, 22950493) and to upregulation of EGF signaling in gastric mucosa (PMID 10791688).

The original use (acid neutralization) and the predicted use (ulcer healing) are closely related, because gastric acid and pepsin drive ulcer injury. This makes the prediction plausible, but it is **largely a rediscovery of the established antacid class use rather than a novel repurposing**.

Three caveats apply:
- Most human evidence involves Al/Mg combination antacids, not magnesium hydroxide alone.
- The studies predate proton pump inhibitors (PPIs) and *H. pylori* eradication therapy, which are now the standard of care.
- Any use should be adjunctive only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial in 72 patients with duodenal or prepyloric ulcers. Cimetidine reached 67% healing at 3 weeks (p<0.005 vs placebo). The antacid/anticholinergic arm reached 50%; its comparison with placebo is cut off in the available abstract. |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | RCT | J Clin Gastroenterol | In duodenal ulcer patients, compared the postprandial acid-buffering duration of sodium bicarbonate versus aluminum-magnesium hydroxide (Maalox). |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Cohort | Drugs Exp Clin Res | Retrospective study of 267 children with peptic symptoms, assessing peptic disease incidence and the efficacy of various drugs in acute phases and relapses. |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacids help in peptic ulcer disease by neutralizing gastric acid and inhibiting pepsin. Adequate dosing is needed 1 and 3 hours after meals. |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clin Gastroenterol | Reviews antacids and anticholinergics in duodenal ulcer treatment. |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | Updates the cellular and molecular mechanisms of antacid-related mucosal protection and ulcer healing. |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Animal | Scand J Gastroenterol | In rats, an Al/Mg hydroxide antacid (Maalox 70) dose-dependently prevented gastric lesions from ethanol, aspirin and stress. The effect was similar to a PGE2 analog and involved endogenous prostanoids. |
| [10791688](https://pubmed.ncbi.nlm.nih.gov/10791688/) | 2000 | Mechanistic | J Physiol Paris | The antacid talcid activated genes for EGF and its receptor in gastric mucosa, a proposed basis for ulcer healing. |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical | Aliment Pharmacol Ther | Reports that H2-receptor antagonists and antacids (including Al/Mg hydroxide) have an aggravating effect on *H. pylori* gastritis in duodenal ulcer patients. This is a caution signal. |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro | Med Pharm Rep | Evaluated the acid-neutralizing capacity of antacids marketed in Morocco. |

---

## US Market Information

The source data lists 20 authorizations in total; the 5 main ones are shown below. Approved indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M007 | Milk of Magnesia Cherry | Liquid | CVS |
| M007 | Milk of Magnesia Mint | Suspension | Cardinal Health |
| M007 | Milk of Magnesia Mint | Liquid | Preferred Pharmaceuticals Inc. |
| M007 | Milk of Magnesia Mint | Liquid | Geri-Care Pharmaceuticals, Corp |
| 505G(a)(3) | Dulcolax | Liquid | Chattem, Inc. |

Chewable tablets (oral) are also recorded among the dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information.

- **Drug Interactions**: No interactions were found in the interaction database query. A Phase 1 study in healthy volunteers (NCT00446316) examined the effect of Mg-Al antacids on imatinib pharmacokinetics. It is a co-medication signal worth checking, but the results are not provided here.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically sensible, but it mainly restates the established antacid class effect. There are no registered trials, and the human evidence is old, uses combination antacids, and predates PPIs and *H. pylori* eradication. Magnesium hydroxide alone is not shown to heal active ulcers, so at most it is an adjunct for symptom relief.

**To proceed, the following is needed:**
- Mechanism of action data for magnesium hydroxide alone
- Package insert warnings and contraindications
- Evidence isolating magnesium hydroxide from aluminum-containing combinations
- Comparison against current standard therapy (PPIs, *H. pylori* eradication), or a defined adjunct-only use case

This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Hyoscyamine
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 1
---

# Hyoscyamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Hyoscyamine: From Original Indication (Not Listed) to Gastroduodenitis

## One-Sentence Summary

Hyoscyamine is an anticholinergic (muscarinic antagonist) marketed in the US as tablets, extended-release tablets, orally disintegrating tablets, an elixir and an injection. The supplied data do not list its approved indications.
The TxGNN model predicts it may be useful for **Gastroduodenitis**, but there are currently **0 clinical trials** and **1 publication**, and that publication is not about hyoscyamine.
This is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (approved indication text is empty for all listed products) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only; the only publication is an unrelated endoscopy sedation review) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank record supplied. The following is inferred from general pharmacology, not from the supplied data. Hyoscyamine is a non-selective muscarinic antagonist. Blocking muscarinic receptors reduces gastrointestinal smooth-muscle spasm and motility, and it lowers gastric acid and secretory output.

For gastroduodenitis (inflammation of the stomach and duodenum), this gives a plausible symptomatic rationale. The drug could act as an adjunct for cramping and hypersecretion. It would not treat the underlying inflammation or its causes, such as *H. pylori* infection or NSAID use.

The high TxGNN score (0.996) reflects a model-based association. It is not clinical evidence. The supplied data also give no original indication to compare against, so the similarity between the original and new indication cannot be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review | Endoscopy | Review of premedication, sedation (e.g., propofol) and surveillance practice around endoscopy and colonoscopy. It does not address hyoscyamine or gastroduodenitis treatment, so its relevance is low. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Hyoscyamine Sulfate (ANI Pharmaceuticals) | Tablet, extended release | Not listed |
| Not listed | Hyoscyamine Sulfate (Bryant Ranch Prepack) | Tablet | Not listed |
| Not listed | Hyoscyamine Sulfate (Westminster Pharmaceuticals) | Tablet | Not listed |
| Not listed | Hyoscyamine Sulfate TAB (QPharma) | Tablet | Not listed |
| Not listed | Hyoscyamine Sulfate (Bryant Ranch Prepack) | Tablet | Not listed |

There are 20 authorizations in total. The other dosage forms on the US market are orally disintegrating tablets, an elixir and an injectable solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and general anticholinergic pharmacology. There are no clinical trials, and the single retrieved publication is unrelated to the drug. Safety data are also missing, so the candidate cannot yet pass safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking safety screening)
- The approved indications and mechanism of action from DrugBank or the labels
- Targeted literature and trial searches on hyoscyamine or anticholinergics in gastritis and duodenitis
- A route and formulation compatibility assessment for the proposed use
- A check of the clinical rationale, since symptom relief alone may not justify a new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


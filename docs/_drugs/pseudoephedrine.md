---
layout: default
title: Pseudoephedrine
parent: Model Prediction Only (L5)
nav_order: 1098
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "PSEUDOEPHEDRINE"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
description: "Pseudoephedrine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Pseudoephedrine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Pseudoephedrine is an oral nasal decongestant, originally used for allergic rhinitis, vasomotor rhinitis, the common cold and related upper airway conditions.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, but there are currently **0 registered clinical trials** and only **7 publications** (mostly preclinical models and a review) linked to this prediction.
This is largely an extension of existing use rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of FDA Applications | at least 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, pseudoephedrine is an indirect sympathomimetic that releases norepinephrine and activates alpha-adrenergic receptors on nasal mucosal blood vessels. This causes vasoconstriction, reducing mucosal swelling and congestion.

"Nasal cavity disease" is a broad category that overlaps heavily with the drug's existing indications (allergic rhinitis, vasomotor rhinitis, rhinitis, common cold). The decongestant mechanism applies to nasal congestion across allergic and non-allergic conditions, so the prediction is plausible. However, the benefit would be symptomatic relief of congestion, not treatment of the underlying disease.

One other prediction was also generated: allergic urticaria (score 0.9914, no supporting evidence for pseudoephedrine, Hold). It has no convincing mechanistic link. Urticaria is histamine-driven, and pseudoephedrine has no antihistamine activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | Overview of nonallergic rhinitis (inflammatory and noninflammatory causes) with nasal congestion as a shared symptom |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Clinical study (design not confirmed) | Am J Rhinol | Compared oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions using acoustic rhinometry |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Preclinical (dog) | Am J Rhinol | Model of allergic nasal congestion in ragweed-sensitized dogs using acoustic rhinometry |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Preclinical (dog) | J Pharmacol Toxicol Methods | Pharmacological characterization of a chronic dog model of nasal congestion for studying decongestants |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Preclinical (dog) | Am J Rhinol | Dog model of compound 48/80-induced nasal congestion measured by acoustic rhinometry |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Preclinical (cat) | Am J Rhinol Allergy | Loratadine plus montelukast produced decongestion in a feline model; d-pseudoephedrine was also studied as a comparator |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Preclinical | J Pharmacol Exp Ther | Selective α2c-adrenergic agonists evaluated in animal models of nasal congestion (not pseudoephedrine) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075153 | Leader 12 Hour Sinus Nasal Decongestant (Cardinal Health) | Film-coated extended-release tablet | Not available (valid) |
| M012 | Nasal Decongestant (CVS Pharmacy) | Film-coated tablet | Not available (valid) |
| ANDA077442 | Pseudoephedrine Hydrochloride (Publix Super Markets) | Film-coated extended-release tablet | Not available (valid) |

All three authorizations are currently valid, and the drug is marketed. All listed forms are oral.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text, so they need verification against the package insert): hypertension, coronary artery disease, congestive heart failure, stroke and cerebrovascular disorders, kidney disease, liver disease and liver failure, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, epilepsy, COPD, peptic ulcer disease, benign prostatic hyperplasia, inflammatory bowel disease, pancreatitis, gallbladder disease, blood coagulation disease, rhabdomyolysis, and substance abuse/dependence. The cardiovascular and metabolic conditions are the most clinically relevant.
- **Drug Interactions**: 100 interactions were found; the 20 retrieved are mostly Moderate. They involve antidiabetic agents (acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, glimepiride, glipizide, glyburide, insulins, exenatide, dulaglutide, albiglutide) and the anorectic diethylpropion. Ascorbic acid is a Minor interaction.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (nasal cavity disease) is biologically plausible but overlaps with existing indications, so it adds little new value. Evidence is limited to preclinical models, one review and one comparative clinical study, with no registered trials. The drug is marketed in the US with 3 valid licenses, and label safety data are missing. The other prediction (urticaria) lacks supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (safety screening cannot proceed without them)
- Mechanism of action data from DrugBank
- A defined, specific nasal condition beyond existing rhinitis and cold indications, with controlled clinical data
- Confirmation of current US regulatory and marketing status
- A review of cardiovascular and metabolic risk for the target population, given the knowledge-graph contraindications and antidiabetic interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


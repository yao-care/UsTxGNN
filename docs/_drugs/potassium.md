---
layout: default
title: Potassium
parent: Model Prediction Only (L5)
nav_order: 1066
evidence_level: L5
indication_count: 5
monitor_inn: "POTASSIUM"
predicted_indications: ["hypertensive disorder", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant renovascular hypertension", "malignant hypertensive renal disease"]
last_modified_at: 2026-10-14
description: "Potassium: predicted new indication Hypertensive disorder (evidence level L5). Approved use: Not available"
---

# Potassium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Potassium: From an Unspecified Original Indication to Hypertensive Disorder

## One-Sentence Summary

Potassium is an essential mineral and electrolyte. The data compiled for this report list no approved original indication for it, and all 7 US licenses are cancelled.
The TxGNN model predicts it may be effective for **hypertensive disorder**.
This direction is supported by **25 registered clinical trials** (only a few directly test potassium) and **20 publications**, including **2 meta-analyses of randomized trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the license records) |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L1 (per the compiled scoring; see the note below) |
| US Market Status | Cancelled only |
| Number of NDAs | 7 (all cancelled; the records are mostly ANDA or unlisted) |
| Recommended Decision | Proceed with Guardrails |

**Note on the evidence level:** Most Phase 3 trials retrieved are losartan potassium or other potassium-salt drugs matched by name, so they are not evidence for potassium itself. The directly relevant support comes from meta-analyses of RCTs and a small number of potassium-specific trials. The L1 label should be read cautiously.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Based on the published literature, however, increased potassium intake lowers blood pressure through several mechanisms:
- Natriuresis and reduced sodium retention
- Vasodilation through hyperpolarization of vascular smooth muscle (Kir channels, Na+/K+-ATPase)
- Reduced sympathetic activity
- Improved endothelial function

Two meta-analyses of randomized trials (a dose-response analysis, PMID 32500831, and a systematic review, PMID 23558164) show a consistent blood pressure reduction with higher potassium intake. This gives the prediction a plausible biological basis and human evidence.

Because no original indication is recorded, the link to an existing use cannot be assessed. The product form and dose must also be defined, either dietary or supplement, because the US market records are cancelled and mix potassium citrate with unrelated products.

**Other predicted indications** have much weaker support and are all rated Hold:
- *Pulmonary hypertension owing to lung disease and/or hypoxia* (99.05%, L4): the literature is basic science on oxygen-sensitive potassium channels, which does not show that potassium supplementation treats the disease.
- *Pulmonary hypertension with unclear multifactorial mechanism* (99.05%, L5): only the model score supports it.
- *Malignant renovascular hypertension* (99.02%, L4): potassium appears in the literature as a biomarker or a consequence (hypokalemia), not as a treatment.
- *Malignant hypertensive renal disease* (99.02%, L5): only the model score supports it, and hyperkalemia risk in renal disease is a safety concern.

---

## Clinical Trial Evidence

Only the trials judged most relevant to potassium itself are listed. Trials of losartan potassium or other potassium-salt drugs, where potassium is only a counter-ion, are excluded because they are not evidence for potassium.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000509](https://clinicaltrials.gov/study/NCT00000509) | Phase 3 | Completed | Not reported | Dietary sodium reduction with and without potassium supplementation for blood pressure control in hypertensive men |
| [NCT03809884](https://clinicaltrials.gov/study/NCT03809884) | Phase 3 | Completed | 7 | Diet vs. supplement to increase potassium intake; very small sample, little efficacy information |
| [NCT02959931](https://clinicaltrials.gov/study/NCT02959931) | N/A | Completed | 33 | Acute vascular effects of a high-potassium meal in hypertensive patients |
| [NCT00949585](https://clinicaltrials.gov/study/NCT00949585) | N/A | Completed | 29 | Two levels of potassium intake in chronic kidney disease; informs blood pressure effect and safety in a high-risk group |
| [NCT00000501](https://clinicaltrials.gov/study/NCT00000501) | Phase 2 | Completed | Not reported | Feasibility of sodium reduction with or without increased potassium intake to prevent hypertension |
| [NCT02697708](https://clinicaltrials.gov/study/NCT02697708) | Phase 1/2 | Unknown | 40 | Potassium sources (supplement, potatoes, French fries) and effects on potassium retention, acid-base balance, and blood pressure |
| [NCT01074918](https://clinicaltrials.gov/study/NCT01074918) | Phase 1/2 | Withdrawn | 0 | Potassium magnesium citrate vs. potassium chloride on blood pressure; never enrolled |

The other registered trials are mostly losartan potassium or similar potassium-salt drugs matched by name, bioequivalence studies, or unrelated hypertension studies, so they are not listed.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Meta-analysis of RCTs | J Am Heart Assoc | Dose-response analysis of potassium supplementation and blood pressure in trials lasting 4 weeks or more |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic review and meta-analysis | BMJ | Effect of increased potassium intake on cardiovascular risk factors and disease |
| [28024910](https://pubmed.ncbi.nlm.nih.gov/28024910/) | 2017 | Systematic review and meta-analysis | Int J Cardiol | Effect of potassium supplementation on blood pressure in hypertensive subjects |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Review | Am J Hypertens | State-of-the-art review of potassium and hypertension |
| [10979053](https://pubmed.ncbi.nlm.nih.gov/10979053/) | 2000 | Guideline review | Arch Intern Med | National Council guidelines on potassium replacement in clinical practice |
| [35045721](https://pubmed.ncbi.nlm.nih.gov/35045721/) | 2022 | Clinical study | Hypertension | Potassium-induced natriuresis in 19 hypertensive postmenopausal women, compared with hydrochlorothiazide |
| [41263071](https://pubmed.ncbi.nlm.nih.gov/41263071/) | 2026 | Trial analysis | Hypertension | Consistency of blood pressure response to potassium-enriched salt in the China Salt Substitute Study |
| [39543422](https://pubmed.ncbi.nlm.nih.gov/39543422/) | 2025 | Commentary | Hypertens Res | Potassium considerations when combining antihypertensive drugs |
| [24721891](https://pubmed.ncbi.nlm.nih.gov/24721891/) | 2015 | Review | Clin J Am Soc Nephrol | Regulation of potassium homeostasis |
| [27194424](https://pubmed.ncbi.nlm.nih.gov/27194424/) | 2017 | Review | Pediatr Nephrol | Risks of both low and high serum potassium |

---

## US Market Information

All licenses are cancelled, and no approved indication text is recorded. Some entries are unrelated products (for example, a homeopathic pellet and a clorazepate salt) that match the name only.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212779 | Potassium Citrate | Tablet, extended release | Not recorded (cancelled) |
| ANDA203546 | Potassium Citrate | Tablet, extended release | Not recorded (cancelled) |
| ANDA214420 | Potassium Citrate | Tablet, extended release | Not recorded (cancelled) |
| ANDA209758 | Potassium Citrate | Tablet, extended release | Not recorded (cancelled) |
| ANDA206813 | Potassium Citrate | Tablet | Not recorded (cancelled) |

---

## Safety Considerations

Safety data from the package insert are not available in the data compiled for this report, and no drug-interaction or knowledge-graph contraindication records were found. Please refer to the package insert for safety information.

Based on the literature and trial review, the main risk is **hyperkalemia**, with particular caution for:
- Renal impairment
- Concurrent RAAS inhibitors (ACE inhibitors, ARBs) or potassium-sparing diuretics

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For hypertension, two meta-analyses of randomized trials show a consistent blood pressure reduction with higher potassium intake, and the mechanism is plausible. Direct potassium-specific trials are small or old, the market records are cancelled with no recorded indication, and safety label data are missing, so progress should be conditional. The other four predicted indications are not supported and should remain on Hold.

**To proceed, the following is needed:**
- Define the product form and dose (dietary vs. supplement)
- Obtain the package insert warnings and contraindications (a blocking data gap)
- Obtain mechanism of action data from DrugBank
- Develop a hyperkalemia monitoring plan, with exclusion or close monitoring of patients with renal impairment or on RAAS inhibitors or potassium-sparing diuretics
- Review the potassium-specific trials for efficacy at defined doses, since many of the registered trials are name matches to potassium-salt drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


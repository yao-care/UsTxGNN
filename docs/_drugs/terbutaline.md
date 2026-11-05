---
layout: default
title: Terbutaline
parent: Model Prediction Only (L5)
nav_order: 1212
evidence_level: L5
indication_count: 2
monitor_inn: "TERBUTALINE"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
last_modified_at: 2026-11-06
description: "Terbutaline: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Terbutaline
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

## Terbutaline: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Terbutaline is a beta-2 adrenergic agonist. The TxGNN model predicts it may be relevant for **respiratory malformation**, but support is weak: **1 registered clinical trial** (a general pediatric pharmacokinetics study) and **13 publications**, none of which show that terbutaline works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 6 of 15) |
| Number of FDA Applications | 15 (active: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Terbutaline is known as a beta-2 adrenergic agonist, a class that relaxes airway smooth muscle and relieves bronchospasm.

In theory, this action could ease secondary bronchospasm or airflow limitation in people with structural airway anomalies. It cannot correct the malformation itself. The literature retrieved concerns mostly asthma, bronchitis, airway stenosis differential diagnosis, and unrelated topics such as fetal heart block, feline lung disease and autism. None of it demonstrates a benefit of terbutaline for respiratory malformation.

The high TxGNN score (0.9952) most likely reflects network proximity to airway disease rather than a specific therapeutic link. It should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | General pharmacokinetics and safety study of understudied drugs in children; not specific to respiratory malformation and does not test efficacy for it |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3281307](https://pubmed.ncbi.nlm.nih.gov/3281307/) | 1988 | RCT | Thorax | Subcutaneous adrenaline vs terbutaline in acute severe asthma (20 patients) |
| [1629507](https://pubmed.ncbi.nlm.nih.gov/1629507/) | 1992 | RCT | J Allergy Clin Immunol | Inhaled budesonide vs terbutaline on airway inflammation in newly diagnosed asthma (14 patients) |
| [42303000](https://pubmed.ncbi.nlm.nih.gov/42303000/) | 2026 | Cohort | Respiratory Medicine | Lung function and HRCT changes during long-term treatment of infants with post-infectious bronchiolitis obliterans |
| [12061354](https://pubmed.ncbi.nlm.nih.gov/12061354/) | 2002 | Cohort | Acta Paediatrica | Central airway stenosis in school-aged children and how to tell it from asthma |
| [1620986](https://pubmed.ncbi.nlm.nih.gov/1620986/) | 1992 | Cohort | Respiration | Inhaled terbutaline reversed abnormal respiratory impedance in chronic bronchitis |
| [19254906](https://pubmed.ncbi.nlm.nih.gov/19254906/) | 2009 | Cohort | Arch Dis Child | Budesonide improved airway conductance in infants with respiratory symptoms |
| [11813927](https://pubmed.ncbi.nlm.nih.gov/11813927/) | 2001 | Case report | Cardiology in the Young | Oral terbutaline in fetal complete heart block (unrelated to the airway) |
| [9628312](https://pubmed.ncbi.nlm.nih.gov/9628312/) | 1998 | Case report | Acta Paediatrica | Multiple anomalies with hypokalaemic paralysis and partial relief by terbutaline |
| [19793774](https://pubmed.ncbi.nlm.nih.gov/19793774/) | 2009 | Review | Toxicol Ind Health | Terbutaline- and mold-associated brain and lung impairment in relation to autism |
| [8327281](https://pubmed.ncbi.nlm.nih.gov/8327281/) | 1993 | Methodological | Pediatr Pulmonol | Flow-volume analysis of lung mechanics in intubated premature infants after terbutaline |

None of these studies directly examines terbutaline for respiratory malformation.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017849 | Terbutaline Sulfate (ANI Pharmaceuticals) | Tablet | Not available |
| ANDA075877 | Terbutaline Sulfate (Amneal) | Tablet | Not available |
| ANDA211832 | Terbutaline Sulfate (Upsher-Smith) | Tablet | Not available |
| ANDA077152 | Terbutaline Sulfate (Chartwell RX) | Tablet | Not available |
| ANDA078630 | Terbutaline Sulfate (Henry Schein) | Injection | Not available |

Five of the six licences are currently valid, and one is cancelled.

## Safety Considerations

Label warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

- **Conditions flagged as contraindication-related in the data compiled** (not label text): hypertension, epilepsy, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, sudden cardiac arrest, heart conduction disease, respiratory failure, hyperthyroidism, thyrotoxicosis, pulmonary edema, myocardial ischemia, coronary artery disease and placental abruption.
- **Drug interactions**: 100 interactions were recorded. Examples at moderate level include epinephrine, acarbose, pioglitazone, canagliflozin, clarithromycin, famotidine and loperamide. Minor-level examples include corticosteroids such as hydrocortisone, dexamethasone and budesonide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only registered trial is a general pediatric pharmacokinetics study, and no cited study addresses terbutaline in respiratory malformation. Beta-2 agonism could at best relieve secondary bronchospasm, not treat the malformation.

**To proceed, the following is needed:**
- Mechanism-of-action data and a clearer account of which malformation-related airway problem terbutaline would address
- Studies that directly examine terbutaline in patients with respiratory malformation
- Label warnings and contraindications reviewed against the cardiovascular, metabolic and potassium-related risks above
- Safety evaluation for the pediatric populations in which these malformations typically present

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


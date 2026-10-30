---
layout: default
title: Doxapram
parent: Model Prediction Only (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
monitor_inn: "DOXAPRAM"
predicted_indications: ["vascular disease", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "angiodysplasia of stomach", "blue toe syndrome", "hemangioendothelioma", "atheroembolism of kidney", "neurogenic thoracic outlet syndrome", "visceral calciphylaxis", "lymphangiectasis"]
last_modified_at: 2026-10-30
description: "Doxapram: predicted new indication Vascular disease (evidence level L4). Approved use: Respiratory failure"
---

# Doxapram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Doxapram: From Respiratory Failure to Vascular Disease
{: .text-alpha }

## One-Sentence Summary

Doxapram is a respiratory stimulant, originally used to treat respiratory failure.
The TxGNN model predicts it may be effective for **vascular disease**, but there are currently **no registered clinical trials** and only **12 publications**, none of which show that it treats vascular disease. This prediction is best regarded as a model artifact rather than a supported direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Respiratory failure |
| Predicted New Indication | Vascular disease |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Doxapram is a respiratory stimulant that acts on the peripheral carotid chemoreceptors and the brainstem respiratory centers. Currently, detailed mechanism of action data is not available in the data compiled for this report, so this description is based on general pharmacological knowledge.

The retrieved literature shows only indirect hemodynamic effects: pressor responses in hypovolemic or hemorrhagic hypotension (in dogs and humans), and modulation of hypoxic pulmonary vasoconstriction. None of it supports treating an underlying vascular disease. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other nine top-ranked predictions (for example thoracic outlet syndromes, blue toe syndrome, hemangioendothelioma, visceral calciphylaxis and lymphangiectasis) are model predictions only. They have no trials or literature, and no plausible mechanistic link to a respiratory stimulant.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Most items are animal studies, case reports, or safety reports. None tests doxapram as a treatment for vascular disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8737758](https://pubmed.ncbi.nlm.nih.gov/8737758/) | 1996 | Clinical study (adverse events) | Eur J Clin Pharmacol | Randomized double-blind trial of doxapram vs placebo against late postoperative hypoxaemia; adverse events with continuous infusion |
| [11743509](https://pubmed.ncbi.nlm.nih.gov/11743509/) | 2001 | Cohort | J Pediatr | Prolonged doxapram therapy for apnea associated with isolated mental delay in very low birth weight infants |
| [18371030](https://pubmed.ncbi.nlm.nih.gov/18371030/) | 2008 | Veterinary retrospective cohort | J Vet Intern Med | Caffeine vs doxapram for hypercapnia in foals with hypoxic-ischemic encephalopathy |
| [35318792](https://pubmed.ncbi.nlm.nih.gov/35318792/) | 2022 | Veterinary retrospective cohort | J Vet Emerg Crit Care | Cardiopulmonary arrest and resuscitation in hospitalized birds |
| [10704775](https://pubmed.ncbi.nlm.nih.gov/10704775/) | 2000 | Animal study | Neurosci Lett | Doxapram accentuated white matter injury in neonatal rats after bilateral carotid artery occlusion |
| [8870121](https://pubmed.ncbi.nlm.nih.gov/8870121/) | 1996 | Animal study | Semin Perinatol | Modulators of hypoxic pulmonary vasoconstriction and response to inhaled nitric oxide in piglets |
| [4398848](https://pubmed.ncbi.nlm.nih.gov/4398848/) | 1971 | Animal study | Anesth Analg | Hemodynamic responses to doxapram in normovolemic and hypovolemic dogs |
| [4397240](https://pubmed.ncbi.nlm.nih.gov/4397240/) | 1971 | Clinical study | Proc Soc Exp Biol Med | Doxapram in hemorrhagic hypotension |
| [4706757](https://pubmed.ncbi.nlm.nih.gov/4706757/) | 1973 | Case report | Anesthesiology | Recovery from central respiratory failure and doxapram administration in a patient with a brainstem lesion |
| [4388361](https://pubmed.ncbi.nlm.nih.gov/4388361/) | 1966 | Human physiology study | Acta Anaesthesiol Scand Suppl | Electroencephalographic effect of doxapram in humans |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA014879 | DOXAPRAM HYDROCHLORIDE (HF Acquisition Co LLC, DBA HealthFirst) | Injection | Not listed (license valid) |

---

## Safety Considerations

- **Drug Interactions**: 55 interactions were recorded. Major-level interactions include bupropion, methylene blue, iobenguane (I-131), iohexol, iopamidol and tramadol. Moderate-level interactions include sympathomimetics and beta-agonists such as epinephrine, ephedrine, phenylephrine, pseudoephedrine, salbutamol, formoterol and arformoterol, as well as isometheptene, amifampridine, lindane, and some bowel preparations (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).
- **Disease-related cautions from the knowledge graph** (not label text): epilepsy, COPD, asthma, kidney disease, liver disease, gallbladder disease, brain edema, hypotensive disorder, stroke and cerebrovascular disorders, cerebral infarction, pulmonary embolism, coronary artery disease, atherosclerosis, sudden cardiac arrest, heart conduction disease, and pheochromocytoma/paraganglioma. Several of these are vascular conditions, which directly conflicts with the predicted new indication.
- **Safety signals in the literature**: adverse events with continuous infusion, white matter injury in neonatal rats after carotid occlusion, and an association between prolonged therapy and developmental delay in very low birth weight infants.

Please also refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trial or relevant literature, and the mechanism does not plausibly fit vascular disease. Several vascular conditions appear among the knowledge-graph cautions, and the only US license is cancelled. Evidence is limited to indirect, mostly preclinical or safety-related findings (L4).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Detailed mechanism of action data, to test whether any mechanistic link to vascular disease exists
- A specific, clinically defined vascular indication, with supporting preclinical or clinical data
- A review of the contraindicated vascular conditions against the proposed use
- Clarification of the regulatory and route situation, given that the only US license is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


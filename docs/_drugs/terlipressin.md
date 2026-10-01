---
layout: default
title: Terlipressin
parent: Model Prediction Only (L5)
nav_order: 1216
evidence_level: L5
indication_count: 7
---

# Terlipressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Terlipressin: From Hepatorenal Syndrome to Open-Angle Glaucoma

## One-Sentence Summary

Terlipressin is a vasopressin analog marketed in the US as Terlivaz, an injectable used for complications of cirrhosis and portal hypertension. The TxGNN model predicts it may be effective for **open-angle glaucoma**, but **no clinical trials or publications** support this prediction, and vasoconstriction could theoretically worsen ocular perfusion. The best-supported alternative prediction in this record is **pulmonary hypertension** (Evidence Level L3, small hemodynamic studies and case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied license record. Terlivaz's US labeling is for hepatorenal syndrome (background knowledge, not in the pack). |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Terlipressin is known to be a prodrug of a vasopressin V1a-receptor agonist with strong vasoconstrictor effects. Its use is concentrated in cirrhosis-related conditions such as variceal bleeding, hepatorenal syndrome and portal hypertension.

For open-angle glaucoma, **no plausible mechanism is documented**. The condition involves impaired aqueous outflow and raised intraocular pressure, which is unrelated to portal or splanchnic hemodynamics. Systemic vasoconstriction could in theory reduce ocular perfusion rather than help. The high score (rank 6201) most likely reflects knowledge-graph proximity to related glaucoma nodes, not a real pharmacological link.

The same applies to the other low-evidence predictions:

- **Primary hereditary glaucoma:** a developmental outflow-pathway disorder with no rationale for a vasopressin analog.
- **Glaucoma 1, open angle:** a duplicate ontology node of the top prediction.
- **Esotropia:** an ocular motility disorder with no vasopressin-pathway link.
- **Kyphoscoliotic heart disease:** inferred only from the weak pulmonary hypertension signal.
- **Headache disorder:** more likely a side-effect association than a treatment target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for open-angle glaucoma.

For reference, the most biologically plausible alternative prediction is **pulmonary hypertension** (rank 3). None of its 4 matched trials tests terlipressin in pulmonary hypertension. All were graded C (indirect context only).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06027970](https://clinicaltrials.gov/study/NCT06027970) | Phase 3 | Unknown | 165 | Continuous terlipressin after endoscopic ligation in acute variceal hemorrhage |
| [NCT03584087](https://clinicaltrials.gov/study/NCT03584087) | Phase 4 | Completed | 74 | Terlipressin after endoscopic ligation in acute variceal hemorrhage |
| [NCT05315557](https://clinicaltrials.gov/study/NCT05315557) | N/A | Unknown | 100 | Vasopressin vs terlipressin as second vasopressor in cirrhotic septic shock |
| [NCT06256432](https://clinicaltrials.gov/study/NCT06256432) | Phase 2 | Active, not recruiting | 54 | Ambrisentan in hepatorenal syndrome, with terlipressin only as background or comparator therapy |

---

## Literature Evidence

Currently no related literature available for open-angle glaucoma.

For the pulmonary hypertension prediction, the most relevant publications are below. They are small hemodynamic studies and case reports, with no RCT in pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Clinical hemodynamic study | Hepatobiliary Pancreat Dis Int | In 7 cirrhotic patients with pulmonary hypertension, the first terlipressin dose lowered pulmonary vascular resistance |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Clinical hemodynamic study | Angiology | Terlipressin had differential effects on pulmonary and systemic hemodynamics in cirrhosis with pulmonary hypertension (echo study) |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | Clinical study | Ann Card Anaesth | Terlipressin vs norepinephrine for milrinone-induced systemic hypotension in cardiac surgery patients with pulmonary hypertension |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | Case report | J Hepatol | Significant improvement of portopulmonary hypertension after 1 week of terlipressin |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | Echocardiographic study | World J Gastroenterol | Effect of terlipressin on systolic pulmonary artery pressure in cirrhosis |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case report | Indian Pediatr | Rescue terlipressin for persistent pulmonary hypertension and refractory shock in a preterm infant |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | Case report | J Pediatr Surg | Rescue therapy for refractory pulmonary hypertension in a neonate with congenital diaphragmatic hernia |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | Report | Paediatr Anaesth | Terlipressin in severe pulmonary hypertension with congenital diaphragmatic hernia |
| [40190717](https://pubmed.ncbi.nlm.nih.gov/40190717/) | 2025 | RCT (portal hypertension, indirect) | JHEP Rep | Hepatic and cardiopulmonary hemodynamics of bolus vs continuous terlipressin and octreotide |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | Systematic review protocol | BMJ Paediatr Open | Planned review of vasopressin and terlipressin in preterm neonates, including persistent pulmonary hypertension |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022231 | Terlivaz (Mallinckrodt Hospital Products Inc.) | Injection, powder, lyophilized, for solution | Not listed in the supplied record |

---

## Safety Considerations

Please refer to the package insert for safety information.

One caution comes from the pulmonary hypertension rationale: terlipressin carries a labeled risk of serious respiratory failure, especially with volume overload. Any study in this area would need strict fluid and oxygenation monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, open-angle glaucoma, is supported only by the model score. It has no trials or literature, no documented mechanism, and a theoretical safety concern from vasoconstriction. The pulmonary hypertension prediction has more plausible support (L3) but rests on small hemodynamic studies and case reports. It should be treated as a research question, not a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, and the approved indication text (these are blocking gaps)
- Mechanism of action data from DrugBank
- For glaucoma: a mechanistic rationale showing benefit rather than harm to ocular perfusion, plus preclinical data
- For pulmonary hypertension: a controlled study in pulmonary hypertension patients, with respiratory-failure risk mitigation
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


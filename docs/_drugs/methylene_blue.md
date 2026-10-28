---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 915
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "METHYLENE BLUE"
predicted_indications: ["bronchitis"]
description: "Methylene Blue: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Methylene Blue: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Methylene blue was originally used to treat methemoglobinemia and sulfhemoglobinemia.
The TxGNN model predicts it may be effective for **bronchitis**, but the evidence is very thin: **0 clinical trials** are registered and the **8 publications** retrieved are mostly indirect (preclinical, diagnostic staining, or unrelated studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of NDAs | 10 (all cancelled; most are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methylene blue is not available in the data compiled for this report. Based on general pharmacology, methylene blue is known to inhibit nitric oxide synthase and guanylate cyclase, and it is a redox-cycling agent with some anti-inflammatory properties. In theory, these could be relevant to airway inflammation.

Its established use is in methemoglobinemia, where it is reduced to leucomethylene blue and then converts methemoglobin back to hemoglobin. This mechanism has no obvious link to bronchitis, a respiratory tract inflammatory or infectious condition. The TxGNN score is very high, but none of the retrieved literature tests methylene blue as a treatment for bronchitis. The prediction therefore cannot be grounded in the data supplied and should be treated as a model-generated hypothesis.


---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic staining | Zhonghua Wai Ke Za Zhi | Methylene blue staining during bronchoscopy in 47 patients stained 97% of central malignant bronchial tumours and 8% of bronchitis cases; a diagnostic aid, not a treatment |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic staining | Terapevticheskii Arkhiv | Chromoendoscopy with methylene blue to distinguish benign from malignant GI and bronchial neoplasms |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological | Am Rev Respir Dis | Methylene blue used as one of five markers to quantify intraalveolar fluid in lavage; not a therapeutic study |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Pharmacology | Int J Clin Pharmacol Ther Toxicol | Methylene blue used as an indicator-dilution tracer in a beta-blocker study; unrelated to bronchitis therapy |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical | J Ethnopharmacol | Plant essential oil relaxes guinea-pig trachea; bronchitis mentioned only as folk-medicine use |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical | J Ethnopharmacol | Plant extract with antidepressant-like effects; bronchitis mentioned only as traditional use |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical chemistry | Anal Chim Acta | Electrochemical aptasensor for theophylline detection; not relevant |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case report | Mikrobiyol Bul | Moraxella catarrhalis endocarditis case; not relevant |

None of these publications shows therapeutic benefit of methylene blue in bronchitis.

---

## US Market Information

All 10 US authorizations are listed as valid, the drug is marketed, and no approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204630 | PROVAYBLUE (American Regent) | Injection | Not recorded |
| ANDA216959 | Methylene blue (Hikma) | Injection, solution | Not recorded |
| ANDA217561 | Methylene Blue (Nexus) | Injection, solution | Not recorded |
| ANDA215636 | Methylene blue (Zydus) | Injection | Not recorded |
| ANDA216955 | Methylene blue (Steriscience) | Injection, solution | Not recorded |

Five further authorizations (including ANDA219550, ANDA219363, ANDA217380, and 505G(a)(3)) are also cancelled. All available forms are injectable or topical solution, which may not suit a respiratory indication such as bronchitis.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** G6PD deficiency (hemolysis risk), hypertension, liver failure, kidney disease, liver disease, congestive heart failure, coronary artery disease, cirrhosis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, hemophilia, anemia, sudden cardiac arrest, heart conduction disease, and myasthenia gravis, among others.

**Drug Interactions:** 100 interactions were recorded. Major ones include serotonergic and sympathomimetic agents and related drugs such as bupropion, morphine, ondansetron, granisetron, palonosetron, dolasetron, fenfluramine, phentermine, lorcaserin, ephedrine, and isometheptene. Epinephrine products are rated Moderate. The combination with serotonergic drugs is a known concern because methylene blue inhibits MAO.

Package insert warnings were not available in the data compiled for this report, so the label should be reviewed before any safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for bronchitis is very high, but there are no clinical trials, no therapeutic literature, and no clear mechanistic link. The evidence level is L5, and the US licenses are all cancelled with injectable-only forms.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale linking methylene blue to airway disease
- Preclinical studies in bronchitis or airway inflammation models
- FDA package insert warnings and contraindications for a formal safety screen
- Assessment of a suitable route of administration (for example, inhaled) and current availability
- Consideration of the methemoglobin reductase deficiency indication (L4, case reports and veterinary data) as a more coherent repurposing direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


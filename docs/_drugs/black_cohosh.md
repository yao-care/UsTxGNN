---
layout: default
title: Black Cohosh
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
monitor_inn: "BLACK COHOSH"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "Jeune syndrome situs inversus", "orofacial clefting syndrome", "disorder of fucoglycosan synthesis", "pulmonary valve disease", "interventricular septum aneurysm"]
last_modified_at: 2026-10-30
description: "Black Cohosh: predicted new indication Heart disease (evidence level L4). Approved use: Not available"
---

# Black Cohosh
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

## Black Cohosh: From an Unspecified Original Indication to Heart Disease
{: .text-alpha }

## One-Sentence Summary

Black cohosh (*Cimicifuga racemosa*) is a botanical product, and the data compiled for this report list no approved indication for it in the United States. The TxGNN model predicts it may be effective for **heart disease**, but there are **0 clinical trials** and no literature that supports the prediction. The only cardiac-specific publication is a **case report of bradycardia and heart block**, which is a safety signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only listed license has no indication text; black cohosh is commonly used for menopausal symptoms) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 0.9919 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 1) |
| Number of FDA Applications | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Black cohosh is a botanical extract traditionally used for menopausal symptoms such as hot flashes. The data compiled for this report show no established cardioprotective mechanism.

The retrieved literature concerns menopause management and hormone replacement therapy alternatives. One review notes that hormone therapy carries cardiovascular risk, and one preclinical paper suggests that black cohosh extract may reduce inflammation linked to postmenopausal cardiovascular risk. Neither paper tests heart disease outcomes. The one cardiac-specific publication, a 2010 case report, describes reversible complete heart block in a woman who had recently started a black cohosh supplement.

The high TxGNN score of 0.9919 is a computational prediction. Clinical data do not corroborate it, so the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below were retrieved for the heart disease prediction. None tests black cohosh for heart disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39829189](https://pubmed.ncbi.nlm.nih.gov/39829189/) | 2024 | Meta-analysis | J Menopausal Med | Evening primrose oil for menopausal hot flashes. It is a different agent, and the paper notes that hormone therapy raises coronary heart disease risk |
| [16181020](https://pubmed.ncbi.nlm.nih.gov/16181020/) | 2005 | Review | J Womens Health | Botanical and dietary supplements for menopausal symptoms. Scientific evidence of efficacy is limited |
| [15813159](https://pubmed.ncbi.nlm.nih.gov/15813159/) | 2005 | Review | South Med J | Integrative therapies for menopause as alternatives to hormone therapy |
| [16115005](https://pubmed.ncbi.nlm.nih.gov/16115005/) | 2005 | Survey/Cohort | J Womens Health | Menopausal symptom management and prevention counseling after the Women's Health Initiative |
| [20955128](https://pubmed.ncbi.nlm.nih.gov/20955128/) | 2010 | Case report | Med J Aust | Reversible complete heart block in a woman who recently began black cohosh. This is a safety signal, not supporting evidence |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Cimicifuga Racemosa (Hahnemann Laboratories, Inc.) | Pellet | Not stated |

Other dosage forms recorded for black cohosh products are tablet (soluble), globule and liquid.

## Safety Considerations

Safety signals come from the retrieved literature, not from a package insert:
- **Cardiac**: a case report of reversible complete heart block and bradycardia (PMID 20955128).
- **Liver**: a causality assessment of nine suspected black cohosh hepatotoxicity cases (PMID 19339903) and a liver biopsy analysis (PMID 24657312).
- **Hematologic**: a mouse toxicology study found hematologic alterations with black cohosh extract (PMID 36373576).
- **Metabolism**: an in vitro study identified reactive quinoid metabolites (PMID 12870886).

Please refer to the package insert for formal warnings, contraindications and drug interaction information. No interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supportive clinical literature, and no cardioprotective mechanism is established. The only cardiac-specific report is a safety signal, and the hepatotoxicity literature adds further concern. The US license is cancelled, and there is no package insert warning data, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (download and parse the label)
- Mechanism of action data (for example from the DrugBank API) to test for a plausible cardiovascular link
- Preclinical cardiovascular studies, including a review of cardiac conduction safety
- A formal assessment of liver and cardiac safety risks

### Other Predictions (Reference Only)

The other nine predictions have TxGNN scores from 0.9911 to 0.9916. They are Laubry-Pezzi syndrome (0.9916), Pierre Robin syndrome with a chromosomal anomaly (0.9916), genetic syndromic Pierre Robin syndrome (0.9915), partial deletion of the long arm of chromosome 7 (0.9915), Jeune syndrome situs inversus (0.9914), orofacial clefting syndrome (0.9913), disorder of fucoglycosan synthesis (0.9912), pulmonary valve disease (0.9912) and interventricular septum aneurysm (0.9911). All have evidence level L5 and a recommendation of Hold. None has clinical trials, and none has a plausible pharmacological link to black cohosh. The literature retrieved for the fucoglycosan disorder concerns menopause, animal studies and toxicity rather than that disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


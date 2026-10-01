---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 915
evidence_level: L5
indication_count: 3
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Methylene Blue: From Acquired Methemoglobinemia to Bronchitis

## One-Sentence Summary

Methylene blue is a marketed injectable drug best known as the standard antidote for acquired methemoglobinemia. The TxGNN model predicts it may be effective for **bronchitis**, with a score of 99.97%. There are **0 clinical trials** and **10 retrieved publications**, none of which tests methylene blue as a treatment for bronchitis, so the score is very likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license data (established clinical use: acquired methemoglobinemia) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Its known actions are inhibition of nitric oxide synthase and guanylate cyclase, redox cycling, and MAO inhibition. Its best-established therapeutic effect is reducing methemoglobin back to hemoglobin via leucomethylene blue.

**No credible mechanistic link to bronchitis was identified.** None of these actions establishes an anti-bronchitic effect. In the retrieved literature, methylene blue appears only as a diagnostic stain (bronchoscopy) or as a laboratory marker. Several hits are unrelated to both methylene blue and bronchitis, such as a guinea-pig trachea assay, an aptasensor paper, beta-blocker pharmacology, and an endocarditis case report. They were retrieved mainly because they mention the word "bronchitis".

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below evaluates methylene blue as a treatment for bronchitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic study | Zhonghua Wai Ke Za Zhi | Methylene blue staining during fiberoptic bronchoscopy: 97.14% of central malignant bronchial tumors stained versus 8.33% of bronchitis cases. It is a diagnostic aid, not a treatment. |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic study | Terapevticheskii Arkhiv | Methylene blue chromoendoscopy to differentiate benign from malignant GI and bronchial neoplasms. No abstract available. |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodology | Am Rev Respir Dis | Compares five markers, including methylene blue, for quantifying intraalveolar fluid in bronchoalveolar lavage. |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Preclinical pharmacology (unrelated drug) | Int J Clin Pharmacol Ther Toxicol | A beta-blocker study that used methylene blue only as a circulation-time indicator. |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | Laboratory study | Tsitologiia | Methemoglobin content in erythrocytes. Not related to bronchitis. |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical (ex vivo) | J Ethnopharmacol | Lippia alnifolia essential oil relaxes guinea-pig trachea. Bronchitis is mentioned only as a folk-medicine use of the plant. |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical (animal) | J Ethnopharmacol | Antidepressant-like effects of Aloysia gratissima. Bronchitis is mentioned only as a traditional use. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Anal Chim Acta | Electrochemical aptasensor for theophylline. Unrelated. |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case report (unrelated) | Mikrobiyol Bul | Moraxella catarrhalis endocarditis. Unrelated. |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | Case report (unrelated) | Eur J Pediatr | Isolated tracheoesophageal fistula in a child. Unrelated. |

## US Market Information

The source data lists 20 authorizations. The approved indication text is empty for all of them, so that column is omitted. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216959 | Methylene blue | Injection, solution | Hikma Pharmaceuticals USA Inc. |
| ANDA217561 | Methylene Blue | Injection, solution | Nexus Pharmaceuticals, LLC |
| ANDA215636 | Methylene blue | Injection | Zydus Lifesciences Limited |
| 505G(a)(3) | Arthcal 1% Methylene Blue | Solution | Beijing JUNGE Technology Co., Ltd. |
| Not listed | Methylene Blue | Injection | BPI Labs LLC |

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no drug-interaction records and no package-insert warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.97% TxGNN score is not supported by any evidence: there are no trials, and the literature shows only diagnostic-staining use. There is no mechanistic basis for treating bronchitis with methylene blue, so this indication should not be pursued.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the blocking safety gap)
- Mechanism of action data from DrugBank, and any preclinical evidence of an anti-inflammatory or airway effect
- Original indication data for the US licenses

**Other predictions from the same run are more credible and are better candidates for follow-up:**
- **Methemoglobinemia due to deficiency of methemoglobin reductase** (score 99.36%, L4, Proceed with Guardrails). Methylene blue bypasses the impaired NADH-dependent pathway via NADPH-dependent methemoglobin reductase. Support is limited to human case reports and veterinary data, with no prospective human trials. Guardrails are to exclude G6PD deficiency (hemolysis risk), screen for serotonergic drug interactions (serotonin syndrome), and monitor methemoglobin levels and hemolysis. Type II disease (neurologic involvement) is not expected to respond.
- **Methemoglobinemia, alpha type** (score 99.36%, L4, Research Question). "Alpha type" likely refers to HBA1/HBA2 hemoglobin M variants, which generally respond poorly to methylene blue. The disease mapping and the specific variant need verification before this counts as supportive.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


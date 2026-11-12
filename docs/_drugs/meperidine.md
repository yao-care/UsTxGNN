---
layout: default
title: Meperidine
parent: Model Prediction Only (L5)
nav_order: 898
evidence_level: L5
indication_count: 2
monitor_inn: "MEPERIDINE"
predicted_indications: ["Tourette syndrome", "trichotillomania"]
last_modified_at: 2026-11-12
description: "Meperidine: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not available in the compiled data"
---

# Meperidine
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

## Meperidine: From Pain Management to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Meperidine is a synthetic opioid analgesic whose original approved indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a computational signal only and is not backed by any real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the approved indication text of all licenses is empty) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 49) |
| Number of FDA Applications | 49 (active: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, meperidine is a synthetic mu-opioid receptor agonist with weak serotonin reuptake inhibition and anticholinergic-like properties. This general description is not drawn from the compiled mechanism data, so it should be verified against DrugBank.

Tourette syndrome involves dysregulated cortico-striato-thalamo-cortical circuits, mainly dopaminergic, with GABAergic and glutamatergic contributions. A link through opioid-system modulation of dopaminergic tone is speculative. Some opioid-modulating agents have been explored in tic disorders, but nothing supports meperidine specifically.

The high TxGNN score (0.9946) is a computational prediction only. The mechanistic rationale is weak, and the safety profile (serotonin syndrome risk with serotonergic agents, which are common in Tourette and comorbid psychiatric treatment; seizure risk from the neurotoxic metabolite normeperidine) is unfavorable for a chronic neuropsychiatric indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261105-meperidine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All five licenses are valid and the drug is marketed in the US, and no approved indication text is available for any of them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 49 FDA applications or NDC listings for this drug, 7 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-meperidine-1 -->

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA021171 | DEMEROL (Hospira, Inc.) | Injection, solution | Valid |
| ANDA088744 | Meperidine Hydrochloride (Hikma) | Solution | Valid |
| ANDA080445 | Meperidine Hydrochloride (Hikma) | Injection | Valid |
| ANDA040331 | Meperidine Hydrochloride (Epic Pharma) | Tablet | Valid |
| ANDA040893 | Meperidine Hydrochloride (Genus Lifesciences) | Tablet | Valid |

## Cytotoxicity

Not applicable. Meperidine is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: The knowledge graph links meperidine to many conditions, including:
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
  - Respiratory: COPD, respiratory failure, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome
  - Hepatic and biliary: liver failure, liver disease, gallbladder disease, hyperbilirubinemia, Gilbert syndrome
  - Endocrine: hypothyroidism, myxedema, Addison disease
  - Other: peptic ulcer disease, benign prostatic hyperplasia, hypotensive disorder, substance abuse/dependence, sickle cell anemia, thrombophlebitis, angle-closure glaucoma
- **Drug Interactions**: 100 interactions were found. Major-level examples include:
  - Alvimopan
  - Bupropion
  - Morphine
  - Lorcaserin
  - Dolasetron
  - Palonosetron

  Moderate-level examples include:
  - Hyoscyamine
  - Loperamide
  - Atropine
  - Glycopyrronium
  - Cimetidine
  - Naloxone
  - Phentermine
- **Mechanism-related risks (from the repurposing assessment)**: Serotonin syndrome with serotonergic agents, seizures from the metabolite normeperidine, and abuse liability.

Please refer to the package insert for warnings and contraindications, which are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no clinical trials or publications. The mechanistic link is speculative, and the safety profile (serotonin syndrome, normeperidine neurotoxicity, abuse liability, many contraindication signals) is unfavorable for a chronic indication, although the drug is marketed in the US. Tourette syndrome is a chronic condition, so these safety concerns weigh heavily.

<!-- review:begin us-lic-20261106-meperidine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The mechanistic link is speculative, and the safety profile (serotonin syndrome, normeperidine neurotoxicity, abuse liability, many contraindication signals) is unfavorable for a chronic indication, although the drug is marketed in the US with 5 of 5 licenses valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 49 FDA applications or NDC listings for this drug, 7 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-meperidine-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text
- Preclinical or mechanistic evidence for a role in tic disorders
- A review of safer alternatives within the same predicted-indication space

---

*Additional predicted indication (for reference):* The second-ranked prediction, **trichotillomania** (TxGNN score 0.9939), is also Evidence Level L5 with no trials or literature, and is likewise on Hold. Its biological rationale is weak or even contradictory, because a mu-opioid agonist acts opposite to the opioid-antagonist approach (naltrexone) studied for this condition, and the same safety concerns apply.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All five licenses are valid and the drug is marketed in the US, and no approved indication text is available for any of them" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 5 of 5 licenses valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


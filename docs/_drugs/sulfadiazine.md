---
layout: default
title: Sulfadiazine
parent: Model Prediction Only (L5)
nav_order: 1186
evidence_level: L5
indication_count: 2
monitor_inn: "SULFADIAZINE"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-12
description: "Sulfadiazine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfadiazine
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

## Sulfadiazine: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Sulfadiazine is a sulfonamide antibiotic, originally used mainly for toxoplasmosis and related infections.
The TxGNN model predicts it may be effective for **Pneumocystosis**,
but there are currently **0 clinical trials** and only **indirect literature (20 publications, mostly general reviews and case reports)** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 8) |
| Number of FDA Applications | 8 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sulfadiazine is a sulfonamide that inhibits dihydropteroate synthase (DHPS) in the folate biosynthesis pathway. Its efficacy in toxoplasmosis is established.

*Pneumocystis jirovecii* also depends on the folate pathway. Sulfonamides, notably sulfamethoxazole combined with trimethoprim, are established therapy for Pneumocystis pneumonia. This gives a plausible class-level mechanistic link. Both toxoplasmosis and pneumocystosis are also common opportunistic infections in patients with AIDS, and the literature often discusses them together.

However, the supplied literature contains no direct data on sulfadiazine for pneumocystosis. The evidence is extrapolated from trimethoprim-sulfamethoxazole. The high TxGNN score is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications is a randomized trial; all are reviews, case reports or retrospective studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Not classified | Clinical Pharmacy | Pyrimethamine-sulfadiazine for Pneumocystis carinii pneumonia and toxoplasmosis in AIDS (no abstract available); the closest title match, but findings cannot be assessed |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including Pneumocystis and Toxoplasma |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Antiparasitic drugs of choice; quinine-pyrimethamine-sulfadiazine for resistant malaria, trimethoprim-sulfamethoxazole for pneumocystis pneumonia |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Review | Annals of Internal Medicine | Management of AIDS-related opportunistic infections |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Treatment of infectious complications of AIDS, with Pneumocystis pneumonia the most common |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Review | Primary Care | Protozoan infections in AIDS, including Pneumocystis pneumonia and CNS toxoplasmosis |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Review | Seminars in Respiratory Infections | Toxoplasma pneumonia in AIDS and other immunodeficiency |
| [15673759](https://pubmed.ncbi.nlm.nih.gov/15673759/) | 2005 | Not classified | Antimicrob Agents Chemother | DHPS mutations in P. jirovecii confer cross-resistance to sulfa drugs, supporting the shared target |
| [2060528](https://pubmed.ncbi.nlm.nih.gov/2060528/) | 1991 | Not classified | Eur J Clin Microbiol Infect Dis | Chart review of 35 AIDS patients on toxoplasmosis maintenance therapy; relapses of both toxoplasmosis and pneumocystosis occurred |
| [21273373](https://pubmed.ncbi.nlm.nih.gov/21273373/) | 2011 | Not classified | J Med Microbiol | Retrospective study of Pneumocystis pneumonia in mainland China over 50 years |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040091 | SULFADIAZINE | EPIC PHARMA LLC | Tablet; oral | Valid |
| ANDA080081 | SULFADIAZINE | IMPAX LABS | Tablet; oral | Discontinued in Drugs@FDA |
| ANDA080084 | SULFADIAZINE | CHARTWELL MOLECULAR | Tablet; oral | Discontinued in Drugs@FDA |
| ANDA080088 | SULFADIAZINE | EVERYLIFE | Tablet; oral | Discontinued in Drugs@FDA |
| NDA004054 | SULFADIAZINE | LEDERLE | Tablet; oral | Discontinued in Drugs@FDA |

Showing 5 of 8 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication edges, not package insert text): porphyria (including inherited porphyria and porphyrin metabolism disease), G6PD deficiency, kidney disease, liver disease, gallbladder disease, hematologic diseases (thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anemia including macrocytic and folic acid deficiency anemia, aplastic anemia), asthma (intrinsic and allergic), slow acetylation, urinary tract obstruction, cystinuria, galactosemia, glycogen storage disease, and superimposed infection.
- **Drug interactions**: 82 interactions were identified; 20 are shown in the data, all rated Moderate. The main groups are:
  - Antidiabetic agents (risk of altered glucose control): sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide), meglitinides (repaglinide, nateglinide), and many insulin products.
  - Others: balsalazide, picosulfuric acid, naltrexone.

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link (folate pathway inhibition, class-level precedent with trimethoprim-sulfamethoxazole) is plausible, but there are no clinical trials and no direct literature for sulfadiazine in pneumocystosis. Established alternatives already exist.

<!-- review:begin us-lic-20261106-sulfadiazine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Established alternatives already exist, and both US licenses are cancelled, which limits practical availability." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 8 FDA applications or NDC listings for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-sulfadiazine-1 -->

**To proceed, the following is needed:**
- Direct clinical or comparative data for sulfadiazine in Pneumocystis pneumonia
- Package insert warnings and contraindications (FDA label)
- Mechanism of action data confirmed from DrugBank
- Assessment of current US availability
- Safety review for the hematologic, renal and G6PD-related risks listed above

<!-- review:begin us-lic-20261106-sulfadiazine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Assessment of current US availability, given that both licenses are cancelled" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 8 FDA applications or NDC listings for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-sulfadiazine-2 -->

---

### Note on the Second Predicted Indication

The second prediction, **punctate epithelial keratoconjunctivitis** (TxGNN score 0.9936, evidence level L5), has no clinical trials or literature. This condition is often viral, so the antibacterial/antiprotozoal mechanism of sulfadiazine gives no clear rationale. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. **Decision: Hold.**

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and both US licenses are cancelled, which limits practical availability" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given that both licenses are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


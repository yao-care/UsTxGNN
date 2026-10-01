---
layout: default
title: Nitrofurantoin
parent: Moderate Evidence (L3-L4)
nav_order: 971
evidence_level: L4
indication_count: 10
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran antibacterial marketed in the US as generic capsules and suspensions, used for urinary tract infection.
The TxGNN model predicts it may be effective for **rheumatoid arthritis** with a very high score (99.89%), but there are **0 clinical trials** and only observational or case-level publications.
Most of these publications describe **harm or co-occurrence**, not benefit, so the prediction is not supported by therapeutic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (taken from the prediction rationale; the license indication text is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nitrofurantoin is a nitrofuran antibacterial used for urinary tract infection. It has no known anti-rheumatic activity, so no therapeutic mechanism linking it to rheumatoid arthritis can be established from the available data.

The literature attached to this prediction is about co-occurrence and harm, not treatment:
- Antibiotic exposure was associated with RA flares in a UK cohort.
- Nitrofurantoin has been reported to cause pulmonary toxicity and, combined with methotrexate, irreversible pulmonary fibrosis in an RA patient.

The very high TxGNN score probably reflects knowledge-graph proximity, such as shared links to lung toxicity and RA-associated conditions, rather than a real treatment signal. This prediction should be treated as a computational hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | In about 32,000 newly diagnosed RA patients, the study examined the association between antibiotic exposure and RA flares. The framing suggests antibiotic use may be linked to flares, not benefit. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis review. Nitrofurantoin is listed as a cause, and RA is listed as a predisposing systemic disease. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease review. Nitrofurantoin is named among the implicated antibiotics. |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | Overview of alveolitis and pulmonary fibrosis (no abstract available). |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | In 57 RA patients hospitalized for interstitial lung fibrosis, the prognosis was poor. This is not about nitrofurantoin treatment. |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin for recurrent UTI. This is a harmful interaction. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury. Nitrofurantoin is listed as a drug to rule out. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonitis with CD4 alveolitis. This is not about nitrofurantoin treatment. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis. Nitrofurantoin is only mentioned as another possible cause of sialadenitis. |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Short-term nitrofurantoin for bacteriuria in middle-aged women (no abstract available). It is not an RA study. |

No RCTs were found. Most items are only loosely related to the predicted indication.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA073652 | Nitrofurantoin | Capsule | Bryant Ranch Prepack |
| ANDA217272 | Nitrofurantoin macrocrystals | Capsule | NorthStar Rx LLC |
| ANDA217272 | Nitrofurantoin Macrocrystals | Capsule | American Health Packaging |
| ANDA203233 | Nitrofurantoin macrocrystals | Capsule | Lupin Pharmaceuticals, Inc. |
| ANDA205005 | Nitrofurantoin macrocrystals | Capsule | Zydus Pharmaceuticals (USA) Inc. |

Available forms across all licenses: oral capsule, suspension and for-suspension. Indication text is not populated in the license records.

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the Evidence Pack. Please refer to the package insert for safety information.

The retrieved literature raises these signals:
- **Pulmonary toxicity**: Nitrofurantoin is a recognized cause of drug-induced interstitial lung disease and pulmonary fibrosis. RA itself also predisposes to lung disease.
- **Methotrexate combination**: A case report describes irreversible pulmonary fibrosis when nitrofurantoin was given to an RA patient on long-term methotrexate. This matters because methotrexate is a mainstay RA drug.
- **Liver injury**: Nitrofurantoin is a known cause of drug-induced liver injury and must be considered in autoimmune hepatitis workups.
- **Methemoglobinemia and hemolytic anemia**: Supported by an animal study and neonatal case reports.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no therapeutic mechanism for rheumatoid arthritis. The literature points mainly to harm, especially pulmonary toxicity with methotrexate, which is a mainstay RA drug. The other nine predicted indications (all rated Hold) have either no evidence or only safety-direction or irrelevant evidence.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence of anti-inflammatory or anti-rheumatic activity
- A safety review of nitrofurantoin use in RA patients, especially those on methotrexate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


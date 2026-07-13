---
layout: default
title: Dexrazoxane
parent: 僅模型預測 (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Dexrazoxane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dexrazoxane: From Anthracycline Cardioprotection to Sclerosing Cholangitis

## One-Sentence Summary

Dexrazoxane is a cardioprotective agent used globally to prevent anthracycline-induced cardiomyopathy and treat anthracycline extravasation injuries. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis** (top-ranked of 10 predicted indications), currently supported by **0 clinical trials** and **0 publications** for this specific indication. Notably, the 10th-ranked prediction — **Cystitis** — carries the strongest mechanistic rationale in this batch (L4 evidence), grounded in the ferroptosis-mediated bladder injury pathway.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anthracycline-induced cardiotoxicity prevention (global approvals; absent from local database) |
| Predicted New Indication (Rank 1) | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not found in database (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Dexrazoxane is an iron chelator and catalytic topoisomerase II inhibitor. It is hydrolyzed intracellularly to its active form (ADR-925), which chelates free iron and prevents iron-catalyzed Fenton reactions — the central mechanism by which anthracyclines (e.g., doxorubicin) generate reactive oxygen species and damage cardiomyocytes. This positions dexrazoxane as a broadly applicable antioxidant agent wherever iron-mediated oxidative stress drives tissue injury.

The rank-1 prediction of sclerosing cholangitis is theoretically conceivable: iron chelation could in principle reduce oxidative stress in bile duct epithelium. However, sclerosing cholangitis is predominantly driven by bile acid toxicity and autoimmune mechanisms rather than iron metabolism dysregulation. The mechanistic link is indirect and speculative, and no clinical or preclinical evidence supports this direction. The algorithm's high confidence score (99.99%) reflects graph topology similarity rather than biological plausibility.

**The most mechanistically coherent prediction in this batch is Cystitis (rank 10, L4).** Recent preclinical research has established ferroptosis — an iron-dependent regulated cell death triggered by lipid peroxidation — as a key driver of cyclophosphamide (CYP)-induced hemorrhagic cystitis and interstitial cystitis/bladder pain syndrome. Since dexrazoxane chelates Fe²⁺ and disrupts the Fenton reaction that initiates ferroptosis, it could theoretically protect bladder epithelium from CYP-metabolite (acrolein)-induced ferroptotic injury. This would be complementary to, rather than competitive with, the current standard bladder protectant mesna, which neutralizes acrolein directly by a different mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Sclerosing Cholangitis or any of the 10 predicted indications.

---

## Literature Evidence

No publications directly linking Dexrazoxane to Sclerosing Cholangitis were identified.

**Supplementary — Cystitis Evidence (Rank 10, Highest Evidence Level in This Batch)**

The following publications support the ferroptosis-based repurposing rationale for cystitis and are the most relevant literature across all 10 predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41999537](https://pubmed.ncbi.nlm.nih.gov/41999537/) | 2026 | Systematic Review (Preclinical) | Int Urology Nephrology | Comprehensive review establishing ferroptosis (iron-dependent lipid peroxidation) as a pathogenic mechanism in interstitial cystitis/bladder pain syndrome; suggests iron-targeting therapy as a potential intervention |
| [37690746](https://pubmed.ncbi.nlm.nih.gov/37690746/) | 2023 | Preclinical Mechanistic Study | Chem-Biol Interactions | Demonstrated that cyclophosphamide-induced hemorrhagic cystitis is mediated via acrolein-triggered ferroptosis in bladder tissue; confirmed the Fe²⁺-Fenton pathway as essential to the injury cascade |
| [10193684](https://pubmed.ncbi.nlm.nih.gov/10193684/) | 1999 | Narrative Review | Drugs | Pharmacology review of chemoprotectants including dexrazoxane; covers cardioprotection and broader chemoprotective utility in oncology settings |
| [7811398](https://pubmed.ncbi.nlm.nih.gov/7811398/) | 1994 | Narrative Review | Drug Safety | Early review of chemotherapy-induced toxicities (including hemorrhagic cystitis and anthracycline cardiotoxicity) and the protective role of agents such as dexrazoxane and mesna |

---

## US Market Information

No regulatory authorization records were retrieved for Dexrazoxane in the current database. This is likely a data retrieval gap rather than true market absence — Dexrazoxane holds multiple international approvals (e.g., Zinecard®/Cardioxane® for cardioprotection; Totect®/Savene® for extravasation) that should appear upon querying the drugs@FDA database directly.

---

## Cytotoxicity

Dexrazoxane is not itself cytotoxic — it is classified as a **chemoprotectant** and **cardioprotective adjunct** used exclusively in conjunction with anthracycline chemotherapy. The following applies given its exclusive oncology context:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Chemoprotectant — Catalytic Topoisomerase II inhibitor / Iron chelator (non-cytotoxic) |
| Myelosuppression Risk | Low at standard cardioprotective doses; additive myelosuppression possible with anthracycline combinations |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (baseline and periodic), hepatic function, renal function; cardiac monitoring when co-administered with anthracyclines |
| Handling Protection | Standard oncology suite precautions apply due to co-administration context with cytotoxic anthracyclines |

---

## Safety Considerations

Please refer to the package insert for safety information. All safety data fields (key warnings, contraindications, drug-drug interactions) returned no data in this dataset, and formal safety evaluation cannot be completed until the package insert is retrieved and parsed (see Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of the 10 TxGNN-predicted indications are at Evidence Level L5 (model prediction only) with no supporting clinical trials or literature, and the top-ranked indication (sclerosing cholangitis) has an extremely weak mechanistic basis; proceeding to clinical evaluation without addressing fundamental data gaps and obtaining at least preclinical proof-of-concept would not be justified.

**To proceed, the following is needed:**

- **Retrieve US FDA records**: Query drugs@FDA for Zinecard® and Totect® NDAs to restore original approved indication data — this is essential for the mechanistic similarity analysis
- **Retrieve MOA data**: Pull full mechanism of action from DrugBank API (Data Gap DG002) to enable formal mechanistic linkage scoring
- **Retrieve safety data**: Download and parse the US prescribing information (Data Gap DG001) for complete warnings, contraindications, and drug interaction profile before any safety stage evaluation
- **Prioritize Cystitis (Rank 10) as the lead repurposing hypothesis**: Commission a targeted systematic literature review on dexrazoxane + ferroptosis + bladder protection; this is the only indication in the current batch with a mechanistically coherent and biologically plausible rationale
- **Commission preclinical study**: Design an *in vivo* mouse model of cyclophosphamide-induced hemorrhagic cystitis to test dexrazoxane (alone and in combination with mesna) for bladder protection, generating the minimum data package needed to advance to an L3 evidence level
- **Deprioritize ranks 1–9** (except cystitis): Sclerosing cholangitis, bronchitis, paratyphoid fever, conjunctivitis, epiglottitis, laryngitis, UTI, and pyelonephritis all lack mechanistic rationale and evidence; these should not consume research resources at this stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


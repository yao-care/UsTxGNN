---
layout: default
title: Carisoprodol
parent: Model Prediction Only (L5)
nav_order: 500
evidence_level: L5
indication_count: 1
monitor_inn: "CARISOPRODOL"
predicted_indications: ["insomnia (disease)"]
---

# Carisoprodol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Carisoprodol: From Muscle Relaxation to Insomnia

## One-Sentence Summary

Carisoprodol is a centrally acting skeletal muscle relaxant that was marketed in the US as tablets, including the brand product Soma.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and only **1 indirectly related publication** supporting this direction.
This is a computational prediction without direct clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available US license records (carisoprodol is generally known as a muscle relaxant) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 authorizations in total (1 NDA, 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, carisoprodol is a centrally acting muscle relaxant. It is metabolized to meprobamate, which modulates GABA-A receptors and has barbiturate-like sedative and anxiolytic effects. This gives a plausible biological reason why the drug could promote sleep. Note that this link comes from general pharmacological knowledge, not from the supplied data.

The relationship between the original use and insomnia is indirect. Muscle spasm and pain can disrupt sleep, and sedation is a known effect of the drug. However, sedation as a side effect is not the same as proven efficacy and safety for treating insomnia.

The only linked publication is a review on nocturnal leg cramps, a sleep-disrupting muscle condition. It does not evaluate carisoprodol for insomnia. The very high TxGNN score therefore reflects a model-based association, not clinical confirmation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review | American Family Physician | Review of nocturnal leg cramps, which are common in adults and can cause severe insomnia. It does not directly evaluate carisoprodol for insomnia. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA011792 | Soma (Viatris Specialty LLC) | Tablet | Not stated; status cancelled |
| ANDA040188 | Carisoprodol (Bryant Ranch Prepack) | Tablet | Not stated; status cancelled |
| ANDA040792 | Carisoprodol (Bryant Ranch Prepack) | Tablet | Not stated; status cancelled |
| ANDA040245 | Carisoprodol (Chartwell RX, LLC) | Tablet | Not stated; status cancelled |
| ANDA203374 | Carisoprodol (Asclemed USA, Inc.) | Tablet | Not stated; status cancelled |

One further authorization (ANDA211789, Carisoprodol Tablets, USP, 350 mg, Bryant Ranch Prepack) is also cancelled.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not label text): epilepsy, kidney disease, liver disease, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, benign prostatic hyperplasia, hypotensive disorder, gout, substance abuse/dependence, hemophilia, anemia, respiratory failure, sudden cardiac arrest, heart conduction disease, and adrenal insufficiency (including Addison disease). Other related conditions are also listed in the graph.
- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: Morphine, liposomal morphine (additive central nervous system and respiratory depression)
  - **Moderate**: Dronabinol, Metoclopramide, Nabilone, Opium, Sibutramine, Difenoxin, Diphenoxylate
  - Several others have unknown severity (e.g., Phentermine, Pantoprazole, Glimepiride, Metformin, Omeprazole).
- **General pharmacological concerns**: abuse and dependence potential, withdrawal syndrome, and additive sedation with other sedatives and opioids. These are especially important for a drug considered for sleep use. They come from general pharmacology, not from the supplied label data.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no clinical trials and no literature directly testing carisoprodol for insomnia. Abuse and dependence potential, a large interaction burden, and the fact that all US licenses are cancelled further weaken the case for repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Direct clinical or preclinical evidence of carisoprodol or meprobamate for insomnia
- A benefit-risk comparison against approved insomnia treatments, including an abuse and dependence assessment
- Clarification of the regulatory pathway, given that no US licenses are currently valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


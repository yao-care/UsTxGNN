---
layout: default
title: Siponimod
parent: Model Prediction Only (L5)
nav_order: 1165
evidence_level: L5
indication_count: 8
monitor_inn: "SIPONIMOD"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "Prinzmetal angina", "rheumatoid arthritis", "atrophoderma vermiculata"]
last_modified_at: 2026-10-14
description: "Siponimod: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the compiled data"
---

# Siponimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Siponimod: From an Unspecified Original Indication to Pulmonary Hypertension

## One-Sentence Summary

Siponimod is an oral sphingosine-1-phosphate (S1P) receptor modulator. The data compiled for this report do not list an original indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the approved indication text on the US license is empty) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Siponimod is an S1P1/S1P5 receptor modulator. S1P signalling is involved in lymphocyte trafficking, pulmonary vascular remodelling and endothelial barrier function, so a link to pulmonary vascular disease is biologically conceivable.

The direction of effect is uncertain, however. S1P receptor modulation has also been associated with bradycardia and vasoconstriction, which could worsen rather than improve pulmonary vascular conditions. Detailed mechanism of action data are not available in the compiled data, and no trials or literature were found for this indication. The prediction therefore rests only on the model score.

The other predicted indications are weaker or less coherent:

- **Migraine disorder, migraine with brainstem aura, and migraine susceptibility (ranks 2, 4, 5):** The literature hits are a generic neurology review series and a case report in which migraine remitted in a patient with multiple sclerosis (MS) after starting interferon β1a. None tests siponimod as a migraine treatment. The scores likely reflect proximity between related migraine nodes in the knowledge graph.
- **Rheumatoid arthritis (rank 7):** This has the most plausible indirect support (L4). S1P modulation limits lymphocyte egress from lymphoid organs, and a review covers S1P signalling in immune-mediated diseases beyond MS. No RA-specific siponimod trial was found.
- **Kyphoscoliotic heart disease, Prinzmetal angina, atrophoderma vermiculata (ranks 3, 6, 8):** No plausible mechanistic link or evidence was found. For Prinzmetal angina, the cardiac liabilities of S1P modulators suggest a safety concern more than a benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension.

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

For context, the literature found for other predicted indications (not for the lead indication) is limited to reviews and one case report:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33983615](https://pubmed.ncbi.nlm.nih.gov/33983615/) | 2021 | Review | Drugs | Reviews S1P signalling in immune-mediated diseases beyond MS (relevant to rheumatoid arthritis) |
| [29500302](https://pubmed.ncbi.nlm.nih.gov/29500302/) | 2019 | Review | Cold Spring Harb Perspect Med | Overview of oral MS therapies; only indirectly relevant |
| [35382764](https://pubmed.ncbi.nlm.nih.gov/35382764/) | 2022 | Case report | BMC Anesthesiology | Migraine remission in an MS patient after starting interferon β1a; not a test of siponimod for migraine |
| [30629375](https://pubmed.ncbi.nlm.nih.gov/30629375/) | 2019 | Review | Rev Med Suisse | Annual neurology update; notes siponimod reduces disability progression in secondary progressive MS |
| [28703543](https://pubmed.ncbi.nlm.nih.gov/28703543/) | 2017 | Review | Rev Med Suisse | Annual neurology update; no siponimod-specific evidence for migraine |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209884 | MAYZENT (Novartis Pharmaceuticals Corporation) | Tablet, film coated | Not available (status: cancelled) |

## Safety Considerations

**Drug Interactions:** The compiled data list 100 interactions in total; the first 20 are shown here. Many are rated Major, including:

- Famotidine, ranitidine, cimetidine
- Corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide)
- Aprepitant
- Clarithromycin
- Dolasetron, palonosetron
- Oxandrolone
- Levofloxacin

Moderate interactions include loperamide, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate and naltrexone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction has a high model score but no trials, no literature and an uncertain direction of effect. The evidence level is L5. The US license is cancelled, and warnings and contraindications have not been reviewed.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic and safety assessment of S1P modulation in pulmonary vascular disease, including cardiac effects such as bradycardia and AV conduction
- A targeted literature and trial search for pulmonary hypertension
- Consideration of rheumatoid arthritis (L4, indirect immunological support) as a better-supported research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Pregabalin
parent: Model Prediction Only (L5)
nav_order: 1079
evidence_level: L5
indication_count: 6
monitor_inn: "PREGABALIN"
predicted_indications: ["tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-30
description: "Pregabalin: predicted new indication Tendinitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Pregabalin: Tendinitis
{: .text-alpha }

## One-Sentence Summary

Pregabalin is an alpha2-delta calcium channel ligand, used for neuropathic and musculoskeletal pain conditions such as postherpetic neuralgia, fibromyalgia and myofascial pain.
The TxGNN model predicts it may be effective for **tendinitis**, but there are **0 clinical trials** and **no directly relevant publications** on this use. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 10) |
| Number of FDA Applications | 11 (1 NDA and 10 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pregabalin binds the alpha2-delta subunit of voltage-gated calcium channels and reduces the release of excitatory neurotransmitters. This can relieve neuropathic and nociceptive pain. Detailed mechanism data were not available beyond this general description.

The link to tendinitis is indirect. Tendinitis is a painful musculoskeletal condition, and pregabalin's known uses (fibromyalgia, myofascial pain) are also musculoskeletal pain syndromes. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There is no evidence that pregabalin affects tendon inflammation, degeneration or healing. At most, it might relieve the pain component. It is not expected to modify the disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved papers tests pregabalin as a treatment for tendinitis. The two closest are postoperative pain studies after rotator cuff repair, which is a tendon surgery setting.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Compared perioperative oral pregabalin with single-shot interscalene brachial plexus block after arthroscopic rotator cuff repair. The title reports equivalent postoperative pain scores. This is a surgical pain setting, not tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Evaluated analgesic efficacy and opioid-sparing effect of pregabalin after arthroscopic rotator cuff repair. Prior evidence on opioid sparing is conflicting. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement after a marathon, with hamstring tendonitis as the cause. Not about pregabalin efficacy. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Fluoroquinolone-associated disability after ciprofloxacin, including tendinopathy as a side effect. Not relevant to pregabalin treatment. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Commentary on piriformis syndrome and its surgical treatment. Not relevant to pregabalin. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical (rat) | Adv Pharmacol Pharm Sci | A plant extract in vincristine-induced neuropathy in rats. Not relevant to pregabalin or tendinitis. |

## US Market Information

The drug is marketed in the US, with 11 valid licenses. The records list no approved indication text. The five main authorizations are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021446 | Lyrica (Viatris Specialty LLC) | Capsule | Not specified |
| ANDA212988 | Pregabalin (Eskayef Pharmaceuticals) | Capsule | Not specified |
| ANDA216197 | Pregabalin (Marksans Pharma) | Capsule | Not specified |
| ANDA206912 | Pregabalin (NorthStar Rx) | Capsule | Not specified |
| ANDA215249 | Pregabalin (Advagen Pharma) | Extended-release film-coated tablet | Not specified |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text):
  - Psychiatric and mood: anxiety disorder, neurotic disorder, dysthymic disorder
  - Hematologic: thrombocytopenia
  - Angioedema: angioedema and its acquired, hereditary, non-histaminic and RAAS-blocker-induced forms
  - Muscle: myopathy, muscular and skeletal muscle disease, familial periodic paralysis, rhabdomyolysis, nodular fasciitis
  - Renal and cardiac: impaired renal function, atrioventricular block
- **Drug Interactions**: 100 interactions were found. The most significant are:
  - **Major:** morphine and liposomal morphine, which carry additive central nervous system and respiratory depression risk.
  - **Moderate:** pioglitazone, rosiglitazone and troglitazone; opioid-type antidiarrheals (diphenoxylate, difenoxin) and opium; cannabinoids (dronabinol, nabilone); metoclopramide; sibutramine.

The muscle-related signals (myopathy, rhabdomyolysis) deserve attention in a musculoskeletal indication. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trial or paper tests pregabalin for tendinitis, and there is no mechanism by which it would treat tendon pathology. It might help the pain symptoms at most. The drug is marketed in the US, with 11 valid licenses.

**To proceed, the following is needed:**
- Direct clinical evidence, such as a pilot RCT of pregabalin for tendinitis pain against standard care.
- Mechanism data on whether pregabalin affects tendon inflammation or healing.
- Review of the current package insert for warnings and contraindications.
- A safety assessment of the muscle-related contraindication signals and the opioid interaction.

**Alternative candidate:** Among the other predictions for this drug, **migraine disorder** (score 0.9947) has the strongest support. It has two pediatric randomized trials, one against propranolol and one against sodium valproate, plus preclinical data on cortical spreading depression. Its Phase 3 trial (NCT00447369) was withdrawn, and adult evidence is lacking. It is better framed as a research question than as a ready candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


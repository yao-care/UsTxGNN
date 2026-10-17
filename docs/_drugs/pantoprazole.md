---
layout: default
title: Pantoprazole
parent: High Evidence (L1-L2)
nav_order: 1013
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Pantoprazole: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Peptic ulcer disease, GERD, esophagitis, Zollinger-Ellison syndrome"
monitor_inn: "PANTOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **6** 
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

# Pantoprazole: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease (GERD), and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **1 directly relevant Phase 3 clinical trial** and **20 publications** retrieved for this prediction.
This prediction is essentially label-consistent (on-label) rather than a true repurposing of a new disease area.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, GERD, esophagitis, Zollinger-Ellison syndrome (the approved-indication text is not available in the US license records) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| US Market Status | Cancelled only (all 8 listed authorizations are cancelled) |
| Number of NDAs | 8 (7 ANDAs and 1 NDA) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured drug record. However, the mechanism is well established in the literature: pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (the proton pump) in parietal cells. This suppresses gastric acid secretion and allows ulcers to heal.

Active peptic ulcer disease is essentially the same condition as the drug's original indication, so the prediction is very plausible. Older randomized trials found that pantoprazole healed acute duodenal ulcers faster than ranitidine and comparably to omeprazole.

Because this is an on-label use, the main value of this prediction is confirmatory. It does not point to a new therapeutic area.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomized, double-blind trial of ilaprazole vs pantoprazole triple therapy for 7 days for H. pylori eradication in gastric/duodenal ulcer patients |

Other pantoprazole trials related to ulcer disease (for example, prevention of recurrent ulcers versus famotidine, and PPI therapy for bleeding ulcers) were retrieved under the duodenal ulcer prediction and are not repeated here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review/network meta-analysis | Am J Gastroenterol | Compares P-CAB vs PPI for healing severe (grade C/D) esophagitis; indirect for ulcers |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Tegoprazan for endoscopic-resection-induced artificial ulcers; indirect |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole review; no drug-drug interactions identified in numerous interaction studies |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Comparative study | Am J Gastroenterol | Pantoprazole vs ranitidine for duodenal ulcer in Brazil |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepatogastroenterology | Lansoprazole vs pantoprazole for active duodenal ulcer and H. pylori eradication |
| [15989651](https://pubmed.ncbi.nlm.nih.gov/15989651/) | 1997 | Review | Expert Opin Investig Drugs | Pantoprazole gives faster pain relief and ulcer healing than H2 antagonists |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Review | Int J Clin Pharmacol Ther | Impact of CYP2C19 polymorphism on PPI action |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Animal study | Inflammopharmacology | Pantoprazole plus mesenchymal stem cells in rat gastric ulcer |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077619 | Pantoprazole (Dr. Reddy's) | Delayed-release tablet | Not available (cancelled) |
| ANDA219087 | Pantoprazole Sodium (Rising Pharma) | Delayed-release tablet | Not available (cancelled) |
| ANDA202038 | Pantoprazole Sodium (Aurobindo) | Delayed-release tablet | Not available (cancelled) |
| ANDA217416 | Pantoprazole Sodium (American Health Packaging) | For suspension | Not available (cancelled) |
| NDA020988 | Protonix (Cardinal Health 107) | Powder for injection solution | Not available (cancelled) |

All 8 authorizations in the compiled data are cancelled, so none is currently listed as valid. These are repackager and manufacturer listings, and this does not necessarily reflect the overall US market availability of pantoprazole.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: osteoporosis, postmenopausal osteoporosis, bone fracture, and pernicious anemia are flagged as contraindication-related conditions.
- **Drug Interactions**: 100 interactions were found in the interaction database. Major-level examples include **acalabrutinib** and **atazanavir**. Moderate-level examples include hydrochlorothiazide, atorvastatin, fenofibrate, bosutinib, alpelisib, apalutamide, amphetamine, amphotericin B, amikacin, and bumetanide. Minor-level examples include aspirin, axitinib, bortezomib, brivaracetam, and cyanocobalamin.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Direct randomized evidence supports pantoprazole for ulcer healing, including Phase 3 data and older double-blind comparisons with ranitidine and omeprazole. However, this is essentially an on-label use, so it offers little repurposing novelty. The US license records show all authorizations as cancelled, and label safety data is missing.

**To proceed, the following is needed:**
- Obtain and review the FDA package insert for warnings and contraindications (a blocking gap for safety screening)
- Verify current US marketing status and approved indication text, since all listed authorizations are cancelled
- Confirm the comparator and arm structure of NCT02084420
- Review the bone-health (fracture, osteoporosis) and vitamin B12 (pernicious anemia) flags, and the major drug interactions, for long-term use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


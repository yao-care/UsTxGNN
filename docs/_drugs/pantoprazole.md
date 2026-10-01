---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 1013
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Pantoprazole: From Acid-Suppressing PPI Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) that reduces stomach acid. The TxGNN model predicts it may be effective for **active peptic ulcer disease**. This direction is supported by **3 clinical trials** (1 completed Phase 3) and **20 publications**, including several randomized trials. The evidence is direct, so this may already be a labeled use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 by the strict trial rule (1 completed Phase 3 RCT in the registry). The pack lists L1 because several published pantoprazole RCTs support it. |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the licenses shown are generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured record. The pack's repurposing rationale describes the mechanism as direct and well established. Pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (the proton pump), which suppresses acid secretion and lets ulcers heal.

Peptic ulcers are acid-mediated, so lowering acid is the standard treatment logic. Pantoprazole-based triple therapy with antibiotics is also used to eradicate *H. pylori*, a major cause of ulcers. The literature includes head-to-head trials against omeprazole, lansoprazole and ranitidine.

The original indications are missing from the record, so this prediction may match an existing labeled use. Check the current US label before treating it as a new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomized, double-blind, active-controlled trial. It compares ilaprazole and pantoprazole triple therapy (7 days) for *H. pylori* eradication in gastric and/or duodenal ulcer patients. The title is truncated, so the exact arms need confirmation. |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Studies how statins and PPIs affect clopidogrel's antiplatelet effect after coronary stenting. It is a drug-interaction study and does not address ulcer treatment. |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Identifies risk factors to decide who needs second-look endoscopy in bleeding peptic ulcers after hemostasis and high-dose PPI infusion. It is a management-strategy study and does not test pantoprazole efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Compares intermittent vs continuous pantoprazole infusion for preventing rebleeding in peptic ulcer bleeding after endoscopic therapy. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Tests pantoprazole infusion as an add-on to endoscopic treatment in peptic ulcer bleeding. |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Compares three pantoprazole-based triple therapies for *H. pylori* eradication and gastric ulcer healing. |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | Compares amoxycillin and clarithromycin with either sucralfate or pantoprazole for *H. pylori* eradication in duodenal ulcer. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepato-gastroenterology | Compares lansoprazole and pantoprazole for active duodenal ulcer treatment and *H. pylori* eradication. |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Clinical study | Aliment Pharmacol Ther | Tests pantoprazole and amoxycillin with azithromycin or clarithromycin for *H. pylori* eradication in duodenal ulcer. |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | Clinical study | Aliment Pharmacol Ther | Evaluates a 2-week pantoprazole course with 1 week of amoxycillin and clarithromycin for *H. pylori* eradication and duodenal ulcer healing. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | Compares P-CABs with PPIs for grade C/D esophagitis. It is indirect evidence for this indication. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Reviews pantoprazole as a PPI. It notes long duration of action and no drug interactions identified in the interaction studies it covers. |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (rat) | Inflammopharmacology | Studies pantoprazole combined with mesenchymal stem cells in experimental gastric ulcer, looking at oxidative stress, inflammation and apoptosis. |

---

## US Market Information

The 5 licenses below are a sample of the 20 on record. The record contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077619 | Pantoprazole | Tablet, delayed release | Dr. Reddy's Laboratories Limited |
| ANDA219087 | Pantoprazole Sodium | Tablet, delayed release | Rising Pharma Holdings, Inc. |
| ANDA077619 | Pantoprazole | Tablet, delayed release | NorthStar Rx LLC |
| ANDA078281 | Pantoprazole Sodium | Tablet, delayed release | AvPAK |

Other dosage forms on the market include oral delayed-release tablets, granules for suspension, and injectable powder for solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

Published literature includes a Phase 4 study of PPI effects on clopidogrel (NCT00930670) and a 2022 review of PPI drug interactions (PMID 35787720). Check these before use alongside antiplatelet drugs.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pantoprazole's mechanism directly fits acid-mediated ulcer disease. The evidence includes a completed Phase 3 trial and multiple published RCTs of pantoprazole-based regimens. However, the original indications are missing, so this may be an existing labeled use rather than new repurposing. Safety data is also incomplete.

**To proceed, the following is needed:**
- Verify the current US label for peptic ulcer indications to confirm whether this is new or already approved.
- Download and parse the package insert for warnings and contraindications.
- Confirm the arms of NCT02084420 (is pantoprazole a comparator arm?).
- Retrieve structured mechanism-of-action data from DrugBank.
- Consider the duodenal ulcer prediction, which has more direct evidence than several other predicted indications for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


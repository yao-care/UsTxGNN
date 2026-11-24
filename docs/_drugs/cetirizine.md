---
layout: default
title: Cetirizine
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 3
monitor_inn: "CETIRIZINE"
predicted_indications: ["nasal cavity disease", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
last_modified_at: 2026-11-24
description: "Cetirizine: predicted new indication nasal cavity disease (evidence level L5). In the US: 79 FDA applications (54 active), plus 1 OTC monograph/unapproved NDC listing"
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Cetirizine: H1 antihistamine → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Cetirizine is an H1-receptor antihistamine. The TxGNN model predicts it may be effective for **nasal cavity disease**, but the data compiled for this report contain **0 clinical trials** and only **5 publications**, none of which directly tests cetirizine in this broad category.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 54 of 79; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 79 (active: 54) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for cetirizine: "Cetirizine hydrochloride, a human metabolite of hydroxyzine, is an antihistamine; its principal effects are mediated via selective inhibition of peripheral H 1 -receptors. The antihistaminic activity of cetirizine hydrochloride has been clearly documented in a variety of animal and human models." ([DailyMed: Quzyttir (cetirizine hydrochloride) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=573770f6-b76e-f6ba-e063-6294a90aa54d), label version 2026-09-22; accessed 2026-11-19.) Based on what is known, cetirizine belongs to the H1-receptor antagonist class. The class works mainly by competitively blocking histamine binding at H1 receptors on nerve endings, smooth muscle and glandular cells. Reviews suggest H1 antagonists may also have additional anti-allergic and anti-inflammatory effects.

"Nasal cavity disease" is a very broad, non-specific category. The high score most likely reflects cetirizine's existing use in allergic nasal conditions rather than a distinct new use. The literature offers indirect support (antihistamine effects on nasal inflammation, mucosal swelling and mucus), but nothing that points to a new indication beyond what is already established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11291777](https://pubmed.ncbi.nlm.nih.gov/11291777/) | 2000 | Review | Allergy | Describes H1 antagonism as the main antihistamine mechanism and discusses possible additional anti-allergic effects in allergic rhinitis |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Pathogenesis-based treatment of inflammatory diseases of the nose and paranasal sinuses, aiming to reduce hyperemia, swelling and mucus |
| [35818943](https://pubmed.ncbi.nlm.nih.gov/35818943/) | 2022 | Review | Vestnik otorinolaringologii | Modern H1 antihistamines in allergic rhinitis patients with comorbid acute respiratory infections |
| [36116201](https://pubmed.ncbi.nlm.nih.gov/36116201/) | 2022 | Preclinical (mouse) | Phytomedicine | Shufeng Jiedu capsule, a traditional Chinese medicine (not cetirizine), improved olfactory dysfunction in allergic rhinitis mice |
| [9301130](https://pubmed.ncbi.nlm.nih.gov/9301130/) | 1997 | Preclinical | Arerugi | Betotastine (a different drug) in experimental allergic rhinitis; cetirizine and terfenadine were comparators that dose-dependently inhibited the response |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076047 | CETIRIZINE HYDROCHLORIDE ALLERGY | CONTRACT PHARMACAL | Tablet; oral | Valid |
| ANDA076601 | CETIRIZINE HYDROCHLORIDE | TARO | Solution; oral | Valid |
| ANDA076677 | CETIRIZINE HYDROCHLORIDE HIVES | MYLAN | Tablet; oral | Valid |
| ANDA077498 | CETIRIZINE HYDROCHLORIDE HIVES | SUN PHARM INDS LTD | Tablet; oral | Valid |
| ANDA077829 | CETIRIZINE HYDROCHLORIDE HIVES | UNIQUE | Tablet; oral | Valid |

Showing 5 of 80 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The data compiled for this report list at least 13 licences, and this list may be partial.

## Safety Considerations

Please refer to the package insert for safety information. Package-insert warnings and contraindications were not available in the data compiled for this report.

**Drug Interactions**: 100 interacting drugs were identified. Those listed with a Moderate severity level include:
- Bupropion
- Dronabinol
- Loperamide
- Metoclopramide
- Morphine (including liposomal)
- Nabilone
- Opium
- Sibutramine
- Difenoxin
- Diphenoxylate

Several others (e.g. calcitriol, vitamin A, phentermine, pantoprazole, glimepiride) have an unknown severity level. Many of the moderate interactions involve other central nervous system depressants, so additive sedation should be considered.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9977), but no clinical trials exist and no cited study directly examines cetirizine for this broad category. The evidence is therefore model prediction only (L5), and the category is too non-specific to guide a development decision.

**To proceed, the following is needed:**
- A more specific nasal condition to test, instead of the broad "nasal cavity disease" category
- Clinical or observational studies of cetirizine in that specific condition
- Mechanism of action data and package-insert safety information
- Confirmation of current licence status and approved indications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Quzyttir (cetirizine hydrochloride) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=573770f6-b76e-f6ba-e063-6294a90aa54d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


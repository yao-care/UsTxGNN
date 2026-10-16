---
layout: default
title: Alosetron
parent: Model Prediction Only (L5)
nav_order: 226
evidence_level: L5
indication_count: 6
monitor_inn: "ALOSETRON"
predicted_indications: ["migraine disorder", "leprosy", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "migraine with or without aura, susceptibility to"]
---

# Alosetron
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

# Alosetron: From Irritable Bowel Syndrome to Migraine Disorder

## One-Sentence Summary

Alosetron is a selective 5-HT3 receptor antagonist. The US approved-indication text is not available in the data compiled for this report, so its original use is not confirmed here.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. The only literature linked to related headache and migraine predictions is a tolerability review and a safety case report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 3 (all cancelled ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alosetron is a selective 5-HT3 receptor antagonist. 5-HT3 signaling plays a plausible role in nausea and in peripheral and visceral pain signaling. This gives a loose biological rationale for migraine, which involves both nausea and altered pain processing.

However, this link is weak. 5-HT3 antagonists such as ondansetron are used in migraine mainly as antiemetics. There is no established efficacy for them as preventive or abortive migraine therapy. The high TxGNN score is a computational prediction only, and no clinical trials or literature were found for this indication.

Detailed mechanism-of-action data is not currently available in the compiled data. The relationship between the original indication and migraine has not been assessed.

Other predictions from the model show the same weakness:
- **Leprosy**, **nephrogenic syndrome of inappropriate antidiuresis**: no credible mechanistic link to 5-HT3 antagonism was identified. These are likely graph-based artifacts.
- **Migraine with brainstem aura**: a rare migraine subtype with the same loose rationale and no specific evidence.
- **Headache disorder**: the only linked paper is a 2004 review of 5-HT3 antagonist use and tolerability. Headache is a commonly reported adverse effect of this drug class, so the review likely addresses tolerability, not benefit.
- **Migraine with or without aura, susceptibility to**: a genetic susceptibility phenotype, not a treatable indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports alosetron in migraine disorder. The two items below are linked to related predictions (headache disorder and migraine susceptibility). Neither provides efficacy evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15515406](https://pubmed.ncbi.nlm.nih.gov/15515406/) | 2004 | Review | Scandinavian Journal of Rheumatology. Supplement | Overview of 5-HT3 antagonists (tropisetron, ondansetron, granisetron, dolasetron, palonosetron). They are mainly used for chemotherapy-induced and postoperative nausea and vomiting. Addresses use and tolerability, not headache treatment. |
| [24442762](https://pubmed.ncbi.nlm.nih.gov/24442762/) | 2014 | Case report/Review | Drug Safety | Sumatriptan-associated ischemic colitis in a migraine patient, with a literature and FAERS review. Concerns a different drug. Relevant as a safety signal, since ischemic colitis is also a known alosetron risk. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206647 | Alosetron Hydrochloride (Amneal Pharmaceuticals LLC) | Tablet, film coated | Not available (status: cancelled) |
| ANDA213614 | Alosetron (Lifestar Pharma LLC) | Tablet | Not available (status: cancelled) |
| ANDA211621 | Alosetron Hydrochloride (Eywa Pharma Inc) | Tablet | Not available (status: cancelled) |

---

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): contraindication links were found with liver failure, liver disease, gallbladder disease, Crohn disease, inflammatory bowel disease, Crohn's colitis, thrombophlebitis, thrombophilia, colitis, ulcerative colitis, toxic megacolon, constipation disorder, and ischemic bowel disease.
- **Drug Interactions**: 100 interactions were identified. Examples of **Major** interactions:
  - Fluvoxamine
  - Apomorphine
- Examples of **Moderate** interactions: caffeine, cimetidine, ciprofloxacin, clarithromycin, aprepitant, fosaprepitant, atazanavir, amprenavir, fosamprenavir, alpelisib, anagrelide, apalutamide, capmatinib, deferasirox, delavirdine, fostamatinib, echinacea, and topical abametapir.
- **Class-related concern**: the review of related predictions notes ischemic colitis and severe constipation as known alosetron risks. This weighs against repurposing without strong efficacy data.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or supporting efficacy literature, and the mechanistic link to migraine is weak. All US licenses are cancelled, and the known gastrointestinal safety risks (ischemic colitis, severe constipation) and the graph-derived contraindications make the risk-benefit case unfavorable without efficacy data.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications, and approved indications
- Detailed mechanism-of-action data
- Preclinical or clinical evidence that 5-HT3 antagonism provides migraine benefit beyond antiemetic effect
- A risk-benefit assessment addressing ischemic colitis and severe constipation in a non-GI population
- Clarification of the current US regulatory and marketing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


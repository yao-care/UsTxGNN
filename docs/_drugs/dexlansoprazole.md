---
layout: default
title: Dexlansoprazole
parent: Model Prediction Only (L5)
nav_order: 593
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "DEXLANSOPRAZOLE"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
description: "Dexlansoprazole: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Dexlansoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Dexlansoprazole: Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Dexlansoprazole is a proton pump inhibitor (PPI) originally used for peptic ulcer disease, gastroesophageal reflux disease (GERD) and esophagitis.
Currently **2 completed Phase 3 trials** (in erosive esophagitis, so indirect evidence for this indication) and **3 publications** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (based on the data compiled for this report; the Phase 3 trials enrolled erosive esophagitis patients, so applicability to ulcer healing is indirect) |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of FDA Applications | 4 (valid: 4) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. However, dexlansoprazole belongs to the well-established proton pump inhibitor class. These drugs irreversibly block the H+/K+ ATPase in gastric parietal cells and suppress gastric acid secretion. Raising gastric pH allows ulcerated mucosa to heal.

This prediction is therefore effectively an on-label or near-label indication rather than true repurposing. The high TxGNN score mainly reflects this close relationship.

An important caveat: the large Phase 3 trials of dexlansoprazole enrolled patients with erosive esophagitis, not ulcer patients. They support acid-suppression efficacy and safety, but they are indirect evidence for ulcer healing specifically.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2054 | Dexlansoprazole MR 60/90 mg vs lansoprazole 30 mg for 8-week healing of erosive esophagitis (indirect for ulcer) |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2038 | Companion trial to NCT00251719 with the same design and population |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | Compares P-CAB vs PPI for healing Los Angeles grade C/D esophagitis (indirect) |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | Development overview of dexlansoprazole, a modified-release enantiomer of lansoprazole, for reflux esophagitis |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclinical / mechanistic | J Chin Med Assoc | Studies how PPIs, including dexlansoprazole, suppress vacuolar-type ATPase and induce endoplasmic reticulum stress, in the context of long-term PPI use and gastric cancer risk |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022287 | Dexlansoprazole (A-S Medication Solutions) | Delayed-release capsule | Not available (valid) |
| ANDA202294 | Dexlansoprazole (A-S Medication Solutions) | Delayed-release capsule | Not available (valid) |
| ANDA202666 | Dexlansoprazole (Upsher-Smith Laboratories, LLC) | Delayed-release capsule | Not available (valid) |
| ANDA219115 | Dexlansoprazole (Alembic Pharmaceuticals Inc.) | Delayed-release capsule | Not available (valid) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from a knowledge graph, not from label text): liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture.
- **Drug Interactions**: The interaction query found 100 potential interactions. Examples:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: fosamprenavir, foscarnet, fostamatinib, furosemide, gefitinib, hydrochlorothiazide, amphotericin B, amikacin, amphetamine, ampicillin, bosutinib, bumetanide
  - **Minor**: acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

  Several of these (for example atazanavir, acalabrutinib and gefitinib) are probably related to acid-dependent absorption, which should be confirmed against the label.

Please refer to the package insert for the official warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acid suppression is a well-established mechanism for ulcer healing, and this indication is already close to the drug's original uses. Two large completed Phase 3 trials support efficacy and safety of the drug.

**To proceed, the following is needed:**
- Ulcer-specific efficacy data, for example results from the recruiting Phase 4 trial [NCT07344506](https://clinicaltrials.gov/study/NCT07344506) (n=942, comparing dexlansoprazole, lansoprazole and vonoprazan with H. pylori eradication therapy)
- FDA package insert warnings and contraindications
- Mechanism of action data confirmed from DrugBank
- A review of the 100 known drug interactions, especially the Major ones
- Clarification of the cancelled US market status and any re-licensing plan

---

### Other Predicted Indications (Brief Notes)

Other high-ranking predictions, summarized for reference:

| Predicted Indication | Evidence Level | Recommendation | Note |
|------|------|------|------|
| Gastric ulcer | L1 | Proceed with Guardrails | Same indirect Phase 3 trials plus the recruiting Phase 4 trial NCT07344506 |
| Duodenal ulcer | L1 | Proceed with Guardrails | Shared indirect Phase 3 evidence; no literature retrieved |
| Gastrojejunal ulcer | L3 | Research Question | Only trial is a withdrawn Phase 4 absorption study (n=0); absorption after gastric bypass is unresolved |
| Peptic ulcer perforation, gastroduodenitis, duodenal obstruction, duodenogastric reflux, leather-bottle stomach | L5 | Hold | Network-proximity predictions with no trials or literature |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


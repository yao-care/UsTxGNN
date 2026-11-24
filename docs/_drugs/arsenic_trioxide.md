---
layout: default
title: Arsenic Trioxide
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
monitor_inn: "ARSENIC TRIOXIDE"
predicted_indications: ["unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "partial deletion of the long arm of chromosome 5", "myelodysplastic syndrome", "Ewing sarcoma", "dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
last_modified_at: 2026-11-24
description: "Arsenic Trioxide: predicted new indication unclassified myelodysplastic syndrome (evidence level L5). In the US: 12 FDA applications (11 active), plus 720 OTC monograph/unapproved NDC listings"
---

# Arsenic Trioxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Arsenic Trioxide: Arsenic-based antineoplastic agent → unclassified myelodysplastic syndrome
{: .text-alpha }

## One-Sentence Summary

Arsenic trioxide is an arsenic-based anticancer drug used in leukemia treatment.
The TxGNN model predicts it may be effective for **unclassified myelodysplastic syndrome**, but **no clinical trials and no publications** were linked to this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | unclassified myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 11 of 12; OTC monograph / unapproved listings: 720) |
| Number of FDA Applications | 12 (active: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for arsenic trioxide: "The mechanism of action of TRISENOX is not completely understood. Arsenic trioxide causes morphological changes and DNA fragmentation characteristic of apoptosis in NB4 human promyelocytic leukemia cells in vitro. Arsenic trioxide also causes damage or degradation of the fusion protein promyelocytic leukemia (PML)-retinoic acid receptor (RAR)-alpha." ([DailyMed: Trisenox (arsenic trioxide) prescribing information, Cephalon, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=101fc347-d0ad-4aee-8b06-9feb187fd741), label version 2022-06-30; accessed 2026-11-19.) Based on general knowledge, arsenic trioxide induces apoptosis and promotes differentiation of malignant blood cells, and these effects have been explored across the broader group of myelodysplastic syndromes (MDS).

The TxGNN score for this prediction is very high (0.9993). However, no trial or publication directly studies the unclassified subtype. The mechanistic argument therefore comes only from activity seen in the wider MDS category and remains a hypothesis for this specific entity.

For context, the broader disease "myelodysplastic syndrome" is a separate prediction in the same list, with many Phase 1/2 trials of arsenic trioxide combinations. That work does not directly establish benefit in the unclassified subtype, and it is not used here to raise the evidence level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for unclassified myelodysplastic syndrome.

---

## Literature Evidence

Currently no related literature available for unclassified myelodysplastic syndrome.

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA206228 | ARSENIC TRIOXIDE | ZYDUS PHARMS | Injectable; injection | Valid |
| ANDA208231 | ARSENIC TRIOXIDE | FRESENIUS KABI USA | Injectable; injection | Valid |
| ANDA209315 | ARSENIC TRIOXIDE | INGENUS PHARMS LLC | Injectable; injection | Valid |
| ANDA209780 | ARSENIC TRIOXIDE | NEXUS | Injectable; injection | Valid |
| ANDA209873 | ARSENIC TRIOXIDE | PENN LIFE | Injectable; injection | Valid |

Showing 5 of 732 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The local records list at least 5 licences and may be partial.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic / antineoplastic (arsenic-based) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; given the contraindicated conditions listed below, ECG/QT monitoring, electrolytes (potassium, magnesium), and liver and renal function are relevant |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Conditions flagged as contraindicated in the reference data**: long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, liver disease, gallbladder disease, potassium deficiency disease, atrioventricular block. These come from relationship data, not from label text.
- **Drug Interactions** (100 interactions found; examples):
  - Major: hydrocortisone, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), cisapride, clarithromycin, dolasetron, granisetron, levofloxacin
  - Moderate: famotidine, loperamide, bisacodyl, castor oil, glycerin, lactitol, lactulose, magnesium citrate, magnesium hydroxide
  - Minor: metronidazole

  Many of the major interactions involve QT-prolonging or electrolyte-depleting drugs.

Package insert warnings and contraindications were not available in the compiled data; please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trial or publication studies unclassified myelodysplastic syndrome directly, so the evidence level is L5. The drug also carries notable cardiac and electrolyte-related safety concerns.

**To proceed, the following is needed:**
- Disease-specific clinical or preclinical evidence in this MDS subtype
- Review of the evidence in broader MDS and whether it applies to this subtype
- Mechanism of action data
- Full package insert warnings and contraindications
- A QT/ECG and electrolyte monitoring plan

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Trisenox (arsenic trioxide) prescribing information, Cephalon, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=101fc347-d0ad-4aee-8b06-9feb187fd741) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


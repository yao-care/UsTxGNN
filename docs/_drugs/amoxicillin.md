---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 8
monitor_inn: "AMOXICILLIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-30
description: "Amoxicillin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, infectious otitis media…"
---

# Amoxicillin
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

## Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic originally used to treat bacterial infections such as urinary tract infection, otitis media, pneumonia, and pharyngitis.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**, but **no clinical trials and no publications** currently support this prediction. The high score appears to be a TxGNN model (deep learning) artifact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, pharyngitis and other bacterial infections |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of FDA Applications | 11 (all are ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Amoxicillin is a member of the beta-lactam antibacterial class, which acts by inhibiting bacterial cell wall synthesis. Its efficacy in bacterial infections is well established.

For the predicted indication, however, no plausible mechanistic link was identified. Polyclonal hyperviscosity syndrome arises from elevated polyclonal immunoglobulins, which is not an infectious process, so an antibacterial would have no clear target. The high TxGNN score (0.9963) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Similarly high scores were assigned to several other unrelated predictions (for example hyperamylasemia at 0.9963 and congenital analbuminemia at 0.9959).

For context, the highest-ranked prediction with a biologically plausible antibacterial rationale is **septicemic plague** (score 0.9913), caused by *Yersinia pestis*. Evidence there is limited to animal-model and in vitro studies. Beta-lactams are not first-line for plague, and the intracellular localization of the organism may limit their efficacy. It is flagged as a research question only.

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## US Market Information

All 11 US authorizations are generic applications (ANDAs) with cancelled status. The data compiled for this report do not include approved indication text. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065271 | Amoxicillin | Capsule | American Health Packaging |
| ANDA064076 | Amoxicillin | Capsule | REMEDYREPACK INC. |
| ANDA065334 | Amoxicillin | Powder for suspension | Proficient Rx LP |
| ANDA065387 | Amoxicillin | Powder for suspension | NuCare Pharmaceuticals, Inc. |
| ANDA065325 | Amoxil | Powder for suspension | DirectRx |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not label text): long QT syndrome, torsades de pointes, ventricular tachycardia, liver failure and liver disease, cholestasis, porphyria, kidney disease, gallbladder disease, osteoporosis, bone fracture, *Clostridium difficile* colitis, necrotizing enterocolitis, myasthenia gravis, and infectious mononucleosis. These come from the knowledge graph and should be verified against the official package insert.
- **Drug Interactions** (100 interactions recorded; main examples):
  - **Major**: Methotrexate; live cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
  - **Moderate**: Doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, balsalazide, entecavir, mycophenolate mofetil, live probiotics (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*), indium In-111 oxyquinoline
  - **Minor**: Allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials, no literature, and no plausible mechanistic link between an antibacterial and a non-infectious immunoglobulin disorder. In addition, all US authorizations for amoxicillin are currently cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking amoxicillin to hyperviscosity
- FDA package insert warnings and contraindications for a full safety review
- Any preclinical or clinical data for the predicted indication
- Consideration of alternative candidates, such as septicemic plague, as a research question, noting that animal and in vitro data suggest beta-lactams are not first-line
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


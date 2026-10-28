---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 1218
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "TETRACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
description: "Tetracaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Not recorded in the local data"
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tetracaine: Acrodermatitis chronica atrophicans
{: .text-alpha }

## One-Sentence Summary

Tetracaine is a local ester anesthetic.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but **no clinical trials and no publications** support this prediction.
The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so this prediction should be treated as unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tetracaine is generally known as a local ester anesthetic that blocks voltage-gated sodium channels.

Acrodermatitis chronica atrophicans is a late-stage skin infection caused by Borrelia. Tetracaine has no known antimicrobial or anti-inflammatory activity relevant to this disease. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a real mechanistic link.

**This prediction is not considered mechanistically plausible.**

## Clinical Trial Evidence

Currently no related clinical trials registered for acrodermatitis chronica atrophicans.

## Literature Evidence

Currently no related literature available for acrodermatitis chronica atrophicans.

## Other Predictions Reviewed

Eight other predictions were generated for tetracaine. None has therapeutic evidence, and all are rated **Hold**.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Neonatal dermatomyositis | 0.9992 | L5 | No plausible mechanism for an autoimmune disease. Neonatal use also raises systemic absorption and methemoglobinemia concerns. |
| 3 | Bronchitis | 0.9992 | L5 | Tetracaine is used as airway mucosal anesthesia (e.g., bronchoscopy), which is procedural and not treatment of bronchitis. |
| 4 | Secondary childhood interstitial lung disease (connective tissue disease) | 0.9992 | L5 | No mechanistic link. Pediatric use adds safety concerns. |
| 5 | Acne keloid | 0.9991 | L5 | Indirect evidence only (see below). |
| 6 | Hydroa vacciniforme, familial | 0.9991 | L5 | No mechanistic rationale. |
| 7 | Amyopathic dermatomyositis | 0.9990 | L5 | No plausible mechanism. |
| 8 | Cauda equina syndrome | 0.9955 | L4 | Safety signal, not a therapeutic one (see below). |
| 9 | Irritable bowel syndrome | 0.9941 | L5 | Speculative. No established route or formulation for this use. |

**Acne keloid (rank 5).** The only trial is [NCT02372786](https://clinicaltrials.gov/study/NCT02372786), a completed Phase 4 randomized, double-blind study (n=30). It compared 7% lidocaine/7% tetracaine cream with 2.5% lidocaine/2.5% prilocaine cream for pain control during laser treatment of acne keloidalis nuchae and tattoo removal. The related RCT report is [PMID 27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/) (Br J Dermatol, 2017). Both evaluate procedural anesthesia, not treatment of the disease itself.

**Cauda equina syndrome (rank 8).** The literature, made up of case reports, reviews and preclinical studies, describes this condition as an adverse effect of intrathecal tetracaine and other local anesthetics. Examples are [PMID 30625770](https://pubmed.ncbi.nlm.nih.gov/30625770/), [PMID 11685003](https://pubmed.ncbi.nlm.nih.gov/11685003/) and [PMID 8982894](https://pubmed.ncbi.nlm.nih.gov/8982894/). This is a safety flag, not a repurposing opportunity.

## US Market Information

All five licenses are valid, and the data contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208135 | Tetracaine Hydrochloride (Alcon Laboratories) | Solution | Not available |
| ANDA217227 | Tetracaine Hydrochloride (Somerset Therapeutics) | Solution | Not available |
| M017 | BLT 3 (Centura Pharmaceuticals) | Ointment | Not available |
| NDA210821 | Tetracaine Hydrochloride (Bausch & Lomb) | Solution/Drops | Not available |
| Not available | Tetracaine HCL (BPI Labs) | Injection | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication associations** (not label text) include:
  - Neurologic: epilepsy, myasthenia gravis, neuromuscular junction disease, butyrylcholinesterase deficiency
  - Cardiac and respiratory: heart disease, cardiovascular disease, sudden cardiac arrest, heart conduction disease, respiratory failure
  - Organ disease: kidney, liver and gallbladder disease
  - Thyroid: hyperthyroidism, Graves disease, thyrotoxicosis
  - Eye: uveitis, iris disease, ciliary body disease, panuveitis, eye infectious disease, conjunctivitis
- **Drug interactions**: 32 interactions were identified, and 20 are listed in the data compiled for this report.
  - **Major**: nitrous acid, liposomal bupivacaine
  - **Moderate**: other local anesthetics (lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine), benzodiazepines (alprazolam, chlordiazepoxide, clobazam, clonazepam, clorazepic acid, diazepam, estazolam), and sulfonamides (sulfasalazine, sulfamethoxazole)
  - **Minor**: hyaluronidase
- **Safety signal**: intrathecal tetracaine has been associated with cauda equina syndrome and neurotoxicity in case reports and preclinical studies.
- Neonatal or pediatric use raises concerns about systemic absorption and methemoglobinemia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature. Tetracaine has no plausible mechanism against a Borrelia skin infection, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. None of the other eight predictions has therapeutic evidence. All five US licenses are valid.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Any preclinical or clinical evidence linking tetracaine to the predicted indication
- Confirmation of a viable route and formulation for the predicted indication
- Review of whether the TxGNN model (deep learning) prediction reflects a true therapeutic association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Armodafinil
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 1
---

# Armodafinil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Armodafinil: From Narcolepsy to Insomnia

## One-Sentence Summary

Armodafinil is a wakefulness-promoting agent (the R-enantiomer of modafinil), originally used for narcolepsy and related sleep and central nervous system conditions.
The TxGNN model predicts it may be effective for **insomnia**,
with **3 clinical trials** and **2 publications** currently supporting this direction. This support is indirect, because armodafinil promotes wakefulness and is the opposite of a hypnotic.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (listed with narcolepsy-cataplexy syndrome, central nervous system disease, Balo concentric sclerosis and X-linked adrenoleukodystrophy in the knowledge graph; the US label indication text was not available) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (see note below) |
| US Market Status | Cancelled only (all 4 authorizations cancelled) |
| Number of NDAs | 4 (1 NDA and 3 ANDAs, all cancelled) |
| Recommended Decision | Hold |

*Evidence level note:* The level is L2 because the data show completed Phase 2 trials. However, none of the trials has results available, and none shows armodafinil treating insomnia itself, so the real strength is closer to the lower end of L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Armodafinil is generally described as a dopamine reuptake inhibitor that increases wakefulness. This is pharmacologically opposite to a hypnotic effect, so the mechanistic link to insomnia is weak.

The link is indirect. In the trials found, armodafinil is used to treat daytime fatigue and sleepiness that occur together with insomnia. Examples are cancer survivors after chemotherapy and people with sleep-disordered breathing. It is usually combined with cognitive behavioral therapy for insomnia (CBT-I), and it is not used as the treatment for insomnia itself.

The very high TxGNN score (99.89%) is a computational prediction. It should not be read as clinical validation. The mechanistic rationale needs to be clarified before any recommendation is made.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm randomized trial of CBT-I with or without armodafinil for insomnia and fatigue after chemotherapy in female breast cancer patients. It is the most direct and largest trial, but no results were available. |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Brief behavioral therapy or CBT-I, with or without armodafinil 150 mg/day, for insomnia in breast cancer patients. The contribution of armodafinil is unclear, and no results were available. |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | Not applicable | Completed | 39 | Armodafinil, CBT-I, or both for insomnia with obstructive sleep apnea, looking at sleep continuity and adherence to CBT-I and CPAP. Small, comorbid population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Review | Postgraduate Medicine | Overview of emerging theories and therapies for shift work disorder, which involves excessive sleepiness during work and/or insomnia during scheduled sleep. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Burden of illness and management approaches for shift work sleep disorder. The condition is common but under-recognised and undertreated. |

Both publications are reviews of shift work disorder. They address sleepiness and sleep disruption in shift workers, not insomnia treatment with armodafinil directly.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021875 | Nuvigil (Golden State Medical Supply, Inc.) | Tablet | Not available; status cancelled |
| ANDA206069 | Armodafinil (Direct_Rx) | Tablet | Not available; status cancelled |
| ANDA202768 | Armodafinil (Natco Pharma USA LLC) | Tablet | Not available; status cancelled |
| ANDA200043 | Armodafinil (Mylan Pharmaceuticals Inc.) | Tablet | Not available; status cancelled |

All four authorizations are for oral tablets and all are listed as cancelled.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): hypertension and hypertensive disorder, liver failure, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, mitral valve prolapse (including familial forms), congenital mitral valve insufficiency, and postural orthostatic tachycardia syndrome.
- **Drug Interactions**: The interaction query returned 100 interactions in total, and the first 20 are shown here.
  - **Moderate**: rabeprazole, esomeprazole, cisapride, dexamethasone, eliglustat, linagliptin.
  - **Minor**: hydrocortisone, pioglitazone, aprepitant, triamcinolone, betamethasone, cimetidine, clarithromycin, clotrimazole, dronabinol, granisetron, miconazole, naldemedine, naloxegol, nitisinone.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism of armodafinil (wakefulness-promoting) is opposite to what insomnia treatment needs. The trials use it for comorbid fatigue and sleepiness alongside CBT-I, and none has available results showing benefit for insomnia itself. The high model score is not sufficient on its own. All US authorizations are also cancelled.

**To proceed, the following is needed:**
- Results from NCT01091974, NCT01011218 and NCT02552303, to see whether armodafinil improved insomnia outcomes or only fatigue and sleepiness
- Mechanism-of-action data and a clear explanation of how a wakefulness-promoting drug could benefit insomnia
- FDA package insert warnings and contraindications for a full safety screening
- Review of the knowledge-graph contraindication signals (cardiovascular, psychiatric, liver) against a population with insomnia
- Clarification of the US regulatory status, since all four authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


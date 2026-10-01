---
layout: default
title: Nefazodone
parent: Moderate Evidence (L3-L4)
nav_order: 959
evidence_level: L4
indication_count: 2
---

# Nefazodone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Nefazodone: From Depression to Migraine Disorder

## One-Sentence Summary

Nefazodone is an oral antidepressant. The Evidence Pack does not state its original indication, so "depression" here comes from general pharmacology.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 registered clinical trials** and only **3 narrative reviews** behind this direction. The evidence is preliminary, and the drug carries a serious liver-safety concern.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all under ANDA076037, a generic application) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, nefazodone is a potent 5-HT2A antagonist with weak serotonin and norepinephrine reuptake inhibition. This link therefore rests on general knowledge and not on data supplied here.

Blocking 5-HT2A/2C receptors is a recognized rationale for migraine prevention. Other antidepressants, such as amitriptyline and venlafaxine, are already used for prophylaxis. This makes the prediction mechanistically plausible but unconfirmed. A 2004 review lists nefazodone among the emerging preventive options for migraine.

The model also gave a similar score (99.60%) to **migraine with brainstem aura**, a rare subtype. There are no trials or publications for it. The score most likely reflects its proximity to the parent migraine node in the knowledge graph and is not an independent signal, so it is not evaluated further here.

The TxGNN score is a model prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Current Pain and Headache Reports | Reviews emerging migraine preventive options. Nefazodone is among the agents discussed, alongside topiramate, levetiracetam, zonisamide, botulinum toxin, tizanidine, lisinopril and candesartan. |
| [15549532](https://pubmed.ncbi.nlm.nih.gov/15549532/) | 2004 | Review | Neurological Sciences | Reviews new migraine prevention drugs. Some data come from double-blind controlled studies and some only from open, uncontrolled trials. |
| [15926007](https://pubmed.ncbi.nlm.nih.gov/15926007/) | 2005 | Review | Neurological Sciences | Overview of current and emerging migraine preventive treatments. The abstract does not name nefazodone specifically. |

All three are narrative reviews from 2004–2005. None is a controlled trial of nefazodone in migraine.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076037 | Nefazodone Hydrochloride | Tablet (oral) | Teva Pharmaceuticals USA, Inc. |
| ANDA076037 | Nefazodone Hydrochloride | Tablet (oral) | Bryant Ranch Prepack |

The Evidence Pack lists 5 entries under the same authorization number (4 Teva, 1 Bryant Ranch Prepack), with no approved-indication text.

## Safety Considerations

- **Key Warnings**: Nefazodone carries a boxed warning for hepatotoxicity (liver failure). This comes from the Pack's rationale notes, not from parsed label data.
- **Drug Interactions**: Nefazodone is a strong CYP3A4 inhibitor, so clinically significant interactions are likely. The DDI query returned no results, which is probably a data gap and not evidence of no interactions.
- Migraine is a chronic condition treated long-term and has many safer alternatives, so this risk weighs heavily against use.

Please refer to the package insert for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model prediction and three older narrative reviews, with no registered trials. The hepatotoxicity boxed warning and strong CYP3A4 inhibition make the risk-benefit balance unfavorable for a chronic, preventive use with many safer alternatives.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A full DDI profile
- Controlled clinical data of nefazodone in migraine prevention
- A risk-benefit comparison against existing prophylactic agents (e.g., amitriptyline, venlafaxine)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


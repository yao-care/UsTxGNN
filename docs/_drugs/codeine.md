---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Codeine: From Approved Opioid Use to Nasal Cavity Disease (Prediction Not Supported)

## One-Sentence Summary

Codeine is an opioid that is marketed in the US as oral tablets, among other forms. The TxGNN model predicts it may be effective for **nasal cavity disease**, with a very high score (99.93%). However, there are **0 clinical trials** and only **2 case reports**, and both describe harm from opioid misuse rather than treatment benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided label data (the approved-indication text for the listed products is empty) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (2 case reports only, no therapeutic studies) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is a marketed opioid. Its use in the original indications is established, but the provided data does not describe those indications or a mechanism that would apply to nasal cavity disease.

The evidence does not support a therapeutic link. The two retrieved papers describe **harm**: necrosis of the nasal cavity and pharynx after intranasal hydrocodone-acetaminophen abuse, and a rhinolith formed around a hardened codeine-opium mixture (an "opioma"). The high TxGNN score most likely reflects proximity in the knowledge graph, since codeine and nasal conditions are linked through misuse and adverse effects. It does not indicate a treatment benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case report | The Laryngoscope | Intranasal abuse of hydrocodone-acetaminophen tablets caused necrosis of the nasal cavity and pharynx. The drug is a different opioid, and the paper describes harm, not treatment. |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose, & Throat Journal | A young man had a unilateral rhinolith formed around an impacted foreign body, which was a hardened mixture of codeine and opium. The paper describes a complication, not a treatment effect. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022402 | Codeine sulfate (Hikma Pharmaceuticals USA Inc.) | Tablet | Not provided in the source data |
| ANDA203046 | Codeine Sulfate (Lannett Company, Inc.) | Tablet | Not provided in the source data |

The pack lists 20 authorizations in total, but only 5 records were supplied, and they represent just the 2 unique authorizations above. Other forms in the pack include solution, liquid and syrup.

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature raises a safety signal for this indication. Misuse of opioids by the intranasal route is associated with tissue necrosis, and a codeine-opium mixture was found in a rhinolith. No drug interaction records were found for codeine in the source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is high, but there are no clinical trials and the only literature consists of two case reports of misuse-related harm. The available evidence points to adverse effects, not benefit, so there is no basis to advance this indication.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) to test whether any plausible link to nasal cavity disease exists
- Any controlled study evaluating codeine as a treatment for a nasal cavity condition
- Route compatibility assessment, since the available oral forms do not match a nasal-targeted indication

Two other predicted indications also do not currently support advancement. Acute laryngopharyngitis (score 99.92%) has no retrieved evidence, and the only rationale is an unverified cough-relief inference. Allergic urticaria (score 99.37%) is mechanistically contradicted, because codeine triggers mast-cell histamine release and is used as a skin-test provocation agent.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


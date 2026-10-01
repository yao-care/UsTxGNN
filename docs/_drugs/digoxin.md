---
layout: default
title: Digoxin
parent: Moderate Evidence (L3-L4)
nav_order: 608
evidence_level: L4
indication_count: 6
---

# Digoxin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Digoxin: From Cardiac Indications to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside (Na+/K+-ATPase inhibitor) marketed in the US as tablets, injection, and oral solution. The US license records provided contain no indication text.
The TxGNN model predicts it may be effective for **Prinzmetal angina** with a score of 99.81%. However, there are **0 clinical trials** and only **2 loosely related publications**, and the mechanism argues against benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided license records (digoxin is a cardiac glycoside used in cardiac conditions) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the Evidence Pack. Digoxin is a cardiac glycoside that inhibits Na+/K+-ATPase and raises intracellular calcium.

This mechanism does not plausibly treat Prinzmetal angina, which is caused by coronary vasospasm. Increased intracellular calcium and vascular tone could theoretically worsen vasospasm. The high graph score therefore looks like a knowledge-graph association rather than a mechanistic signal, and it should be read as a hypothesis-generating output only.

The other five predictions are also weak:
- **Duodenal obstruction:** one unrelated case report.
- **Duodenal ulcer:** the literature shows drug-interaction and toxicity signals, not efficacy.
- **Duodenogastric reflux:** no evidence retrieved.
- **Obsolete susceptibility to ischemic stroke:** an obsolete ontology term, so not actionable.
- **Hypoalphalipoproteinemia:** no evidence retrieved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review (as classified) | Chinese Medical Sciences Journal | Study of 30 hospitalized patients with angina decubitus. It found severe coronary obstruction and increased myocardial oxygen consumption before attacks. It does not evaluate digoxin for vasospastic angina. |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | Overview of chronopharmacology and circadian rhythms in antihypertensive treatment. It has no direct evidence for digoxin in Prinzmetal angina. |

Neither publication supports digoxin efficacy for Prinzmetal angina.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA215307 | Digoxin (American Health Packaging) | Tablet |
| ANDA215307 | Digoxin (Marlex Pharmaceuticals, Inc.) | Tablet |
| ANDA215307 | Digoxin (ANI Pharmaceuticals, Inc.) | Tablet |
| ANDA083391 | Digoxin (Hikma Pharmaceuticals USA Inc.) | Injection |
| ANDA215209 | Digoxin (Amici Pharma, Inc) | Solution |

The 20 licenses cover oral (tablet), injectable, and solution forms.

---

## Safety Considerations

- **Theoretical concern for this indication:** Digoxin's calcium-raising action and effect on vascular tone could aggravate coronary vasospasm. This is a potential harm rather than a benefit.

No package-insert warnings, contraindications, or drug-interaction records were retrieved. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. There are no clinical trials, the two publications are not relevant to efficacy, and digoxin's known mechanism suggests possible harm in vasospastic angina.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data (DrugBank) to test whether any plausible link exists
- Confirmation of the original approved indications from the labels
- Any clinical or mechanistic evidence for digoxin in coronary vasospasm

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


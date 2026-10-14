---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Mannitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Mannitol: From Intracranial Hypertension and Brain Edema to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain edema, intracranial hypertension, ocular hypertension, and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but there are currently **0 clinical trials** and only **1 general review article** that does not support this use, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain edema, intracranial hypertension, ocular hypertension, pseudotumor cerebri, congestive heart failure, cystic fibrosis (from the knowledge graph; no approved indication text is available) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 7 authorizations in total (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Mannitol is known as an osmotic diuretic: it is filtered by the kidney but poorly reabsorbed, so it draws water into the urine and promotes water diuresis. In theory this could influence free-water balance, which is the only link to NSIAD.

On closer inspection the mechanistic fit is weak. NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), leading to water retention and hyponatremia. Osmotic diuresis does not correct this underlying receptor defect. Mannitol can also worsen hyponatremia through osmotic water shifts out of cells. The high model score therefore appears to reflect network proximity in the knowledge graph rather than a biologically supported treatment effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes ten common pitfalls in evaluating hyponatremia; it is a general review and does not address mannitol as a treatment for NSIAD |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016269 | Mannitol (Henry Schein) | Injection, solution | Not available (cancelled) |
| ANDA080677 | Mannitol (Fresenius Kabi) | Injection, solution | Not available (cancelled) |
| NDA020006 | Mannitol (B. Braun) | Injection, solution | Not available (cancelled) |
| NDA019603 | Mannitol (ICU Medical) | Injection, solution | Not available (cancelled) |
| NDA013684 | Osmitrol (Baxter) | Injection, solution | Not available (cancelled) |

Two further cancelled authorizations are not shown: QR PAIN (cream) and Sorbitol-Mannitol (irrigant).

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text)**: The knowledge graph links mannitol to contraindications or cautions in several conditions. The most relevant are:
  - Renal and hepatic: anuria, impaired renal function, liver failure, liver disease, hepatic coma, hepatic encephalopathy
  - Cardiopulmonary and neurological: pulmonary edema, intracranial hemorrhage
  - Haematological: anemia, thrombocytopenia, neutropenia, agranulocytosis
  - Others: porphyria, sleep apnea syndromes, substance abuse or dependence, anxiety and mood disorders
- **Drug Interactions**: The interaction screen returned 100 records. Examples:
  - **Major**: amikacin
  - **Moderate**: lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, canagliflozin, dapagliflozin, carbamazepine, citalopram, desvenlafaxine, cisatracurium, amifostine, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid, diatrizoate
  - **Minor**: doxycycline
- **Context-specific concerns from the literature**: A case report describes pulmonary edema after hypertonic saline and mannitol were given for water intoxication. For other predicted conditions, osmotic diuresis could worsen polyuria in nephrogenic diabetes insipidus, and mannitol can aggravate hyponatremia.

Please refer to the package insert for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no registered trials and no supportive literature. The mechanism is implausible, since osmotic diuresis does not correct the AVPR2 defect and may worsen hyponatremia. All US authorizations are also cancelled. The other nine predicted indications are no stronger: most are Hold with L4–L5 evidence, and several (hypokalemic periodic paralysis, nephrogenic diabetes insipidus, acute pulmonary heart disease) point to possible harm rather than benefit.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that an osmotic agent can benefit NSIAD
- A safety assessment of hyponatremia and volume-expansion risks in this population
- Clarification of whether any active US product remains, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


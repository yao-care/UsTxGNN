---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 1083
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Primidone: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including generalized tonic-clonic seizures…"
monitor_inn: "PRIMIDONE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Primidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Primidone: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Primidone is an anticonvulsant originally used to treat epilepsy, including generalized tonic-clonic and partial seizures.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **0 clinical trials** and **0 publications** currently support this prediction.
The score is a model output only, with no actual study behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including generalized tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | 8 (1 NDA and 7 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Primidone is an anticonvulsant that is metabolized to phenobarbital and phenylethylmalonamide (PEMA), and its efficacy in epilepsy is well established.

For trigeminal nerve neoplasm, however, the data compiled for this report supports no mechanistic link. There is no rationale for antitumor activity from an antiseizure drug. The very high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as trigeminal neuralgia or epilepsy, not biological evidence of an effect on the tumor.

**Other predictions in the same list.** Several other predicted indications are more plausible, though still weakly supported:
- **Startle epilepsy** and other reflex seizures (orgasm-induced, micturition-induced, thinking, eating, audiogenic, reading seizures): a general antiseizure rationale applies. These are close to the existing epilepsy indications and are arguably extensions rather than true repurposing. Evidence consists only of old case reports, animal studies, and general antiepileptic reviews.
- **Trigeminal neuralgia**: anticonvulsants such as carbamazepine are standard treatment, so a class-level rationale exists. No direct primidone trial evidence was found, and established first-line options are available.
- **Beta-ketothiolase deficiency**: an inborn error of metabolism with no supported mechanistic link to primidone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For reference, the strongest literature attached to the other predicted indications is limited to:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs are used for non-epilepsy conditions, mostly based on case series and small trials that need confirmation (trigeminal neuralgia) |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case report | Zhonghua Yi Xue Za Zhi | Startle epilepsy presenting as drop attacks in a 3.5-year-old boy; the available text does not confirm primidone use |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clin Neurosci | Primidone (500–1,000 mg/day) is among the useful drugs for cortical myoclonus (reading seizures context) |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Animal study | Neurol Psychiatr | Effects of phenobarbital, diphenylhydantoin and primidone on brain enzyme activity in mice with audiogenic epilepsy |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA009170 | Mysoline (Bausch Health US, LLC) | Tablet | Valid |
| ANDA040862 | Primidone (Dr. Reddy's Laboratories Limited) | Tablet | Valid |
| ANDA040866 | Primidone (Bryant Ranch Prepack) | Tablet | Valid |
| ANDA214896 | Primidone (Advagen Pharma Limited) | Tablet | Valid |
| ANDA040586 | Primidone (Bryant Ranch Prepack) | Tablet | Valid |

Three more cancelled ANDAs (083551, 218366, 084903) are not shown. All 8 authorizations in the data compiled for this report are cancelled, and none contains approved indication text.

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

**Contraindications suggested by the knowledge graph** (not label text):
- Porphyria and other porphyrin metabolism diseases
- Liver disease, kidney disease, gallbladder disease
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, leukopenia, pancytopenia, anaemia (including macrocytic anaemia), and congenital neutropenia syndromes
- Sleep apnoea and hypoventilation syndromes
- Substance abuse/dependence
- Anxiety, neurotic and dysthymic disorders

**Drug Interactions** (100 interactions found; examples):
- **Major**: morphine, eliglustat
- **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), doxycycline, metronidazole, bupropion, aprepitant, pioglitazone, canagliflozin, saxagliptin, vitamin D analogues (cholecalciferol, calcifediol, calcitriol), diphenoxylate, difenoxin, dronabinol
- **Minor**: cimetidine

Primidone is metabolized to phenobarbital, an enzyme inducer, which likely explains the many interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for trigeminal nerve neoplasm is very high, but there are no clinical trials, no literature, and no plausible mechanism for antitumor activity. The prediction is model output only (L5). The drug is marketed in the US, with 8 valid licenses, and label safety data is missing.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and any biological rationale linking primidone to trigeminal nerve tumours
- FDA package insert warnings and contraindications, which block safety screening
- Preclinical evidence of antitumour activity, if the neoplasm indication is pursued
- Consider redirecting effort to the more plausible predictions (startle epilepsy and other reflex seizures, trigeminal neuralgia), which need disease-specific clinical evidence and a comparison against established first-line therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


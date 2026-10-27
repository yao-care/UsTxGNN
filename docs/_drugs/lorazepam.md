---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 870
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lorazepam: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Anxiety disorder, status epilepticus, Lennox-Gastaut syndrome…"
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
---

# Lorazepam
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

## Lorazepam: From Anxiety and Seizure Disorders to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Lorazepam is a benzodiazepine, originally used for anxiety disorders and seizure conditions such as status epilepticus.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** (top-ranked prediction), but there are **0 clinical trials** and **0 publications** supporting this direction, so it rests on the model score alone.
Among the other predictions, **insomnia** has the most supporting literature (17 publications, including older clinical studies of lorazepam as a hypnotic), though this is closer to an already-recognized use than a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, status epilepticus, Lennox-Gastaut syndrome, absence epilepsy (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 authorizations in total (2 NDAs, 5 ANDAs; all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Lorazepam is generally known as a positive allosteric modulator of the GABA-A receptor, which gives it anxiolytic, sedative and anticonvulsant effects. These effects are established in anxiety and seizure emergencies.

For trigeminal nerve neoplasm, the data supports **no mechanistic link**. Lorazepam has no known antineoplastic activity. Any realistic use would be symptom control (for example anxiety or seizures in a patient with a tumour), not treating the tumour itself. The very high model score (99.87%) is not backed by any trial or publication, so it should be read as a statistical artefact of the knowledge graph, not as a biological signal.

Several lower-ranked predictions are mostly extensions of lorazepam's known anticonvulsant role:

- **Insomnia (rank 2, L3):** GABA-A enhancement produces sedative-hypnotic effects, which is biologically plausible. However, benzodiazepine concerns (dependence, tolerance, cognitive effects, falls) argue against long-term use.
- **Reflex seizure types (ranks 3-9):** Reading, thinking, orgasm-induced, audiogenic, startle, eating and micturition-induced seizures. Support is indirect: general seizure reviews, animal withdrawal studies, and a few case-type reports. Most of this likely reflects a generic seizure-treatment association rather than a distinct repurposing signal.
- **Acute encephalopathy with biphasic seizures (rank 10):** Model score only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm. No registered trials were found for any of the other top-10 predicted indications either.

---

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For reference, the most relevant literature for the next-ranked prediction, **insomnia**, is shown below. It supports a hypnotic use, not the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Comparative clinical study | J Clin Pharmacol | Double-blind crossover in 8 chronic insomniacs: 2 mg lorazepam performed better than 30 mg flurazepam on most sleep parameters |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical study | Int Clin Psychopharmacol | Tested lorazepam 0.5 mg TID (24-hour) versus 1.5 mg at bedtime in primary insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm | Reviewed tranquilizer use, doses and adverse effects in elderly patients with chronic non-communicable diseases |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Overview of drugs for chronic insomnia |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Observational | Clin Ther | Benzodiazepine and sedative-hypnotic use among older seriously ill veterans, in the context of Choosing Wisely cautions |

---

## US Market Information

All seven US authorizations are cancelled. Approved-indication text is not available in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018140 | Lorazepam (Hikma) | Injection | Not available |
| NDA214826 | LOREEV XR (Almatica) | Extended-release capsule | Not available |
| ANDA072926 | Lorazepam (PD-Rx) | Tablet | Not available |
| ANDA078203 | Lorazepam (Proficient Rx) | Tablet | Not available |
| ANDA072928 | Lorazepam (Golden State Medical Supply) | Tablet | Not available |

Two further cancelled ANDAs (ANDA203572, Preferred Pharmaceuticals; ANDA076045, PD-Rx) are not shown.

---

## Safety Considerations

No package-insert warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for label safety information.

The following comes from the knowledge graph and is not label text.

- **Disease contraindications (knowledge graph):** liver failure, liver disease, hepatic encephalopathy/coma, kidney disease, gallbladder disease, porphyria (inherited porphyria, porphyrin metabolism disease), angle-closure and open-angle glaucoma, respiratory failure, sleep apnea (obstructive sleep apnea, congenital central hypoventilation syndrome), substance-related disorder/substance abuse and dependence, and several psychiatric conditions (neurotic disorder, dysthymic disorder, anxiety disorder).
- **Drug interactions:** 100 interactions were found in total. Notable ones:
  - **Major:** Morphine, liposomal morphine (additive CNS and respiratory depression is the expected concern).
  - **Moderate:** Bupropion, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide.
  - **Minor:** Antacids (aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide).
  - Only the first 20 entries were returned in detail.
- **Class concerns noted in the literature:** dependence, tolerance, cognitive effects and falls, especially in older adults; propylene glycol toxicity has been reported with intravenous lorazepam infusion.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has a very high model score but no trials, no literature and no plausible antitumour mechanism for lorazepam, so the evidence level is L5. All US authorizations are cancelled, and label safety data is missing.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any preclinical or clinical evidence of a tumour-related effect (none exists in the current data); without it, the prediction should be de-prioritised
- If a different direction is of interest, treat insomnia (L3) as a separate research question. It is already a recognized sedative-hypnotic use, so it is better framed as an existing use than a novel repurposing, and it requires weighing dependence and fall risk.
- Clarification of why all US authorizations are cancelled, and whether any route or formulation is available for a new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


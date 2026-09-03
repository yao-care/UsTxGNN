---
layout: default
title: Tranylcypromine
parent: 僅模型預測 (L5)
nav_order: 1249
evidence_level: L5
indication_count: 10
---

# Tranylcypromine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tranylcypromine: From Depression to Melancholia and Related Mood/Anxiety Disorders

## One-Sentence Summary

> Tranylcypromine (DrugBank DB00752) is a classic irreversible monoamine oxidase inhibitor (MAOI), historically used to treat major depressive disorder — particularly treatment-resistant and atypical depression.
> This Evidence Pack screens **10 TxGNN-predicted indications**; after filtering out several implausible high-score predictions (rare pediatric/genetic syndromes with no mechanistic link), the strongest repurposing signal converges on **Melancholia** and the broader depression/anxiety spectrum (dysthymic disorder, agoraphobia, neurotic depression),
> supported by **0 registered clinical trials but 19 relevant publications**, including two controlled trials and one meta-analysis specific to tranylcypromine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (classic MAOI antidepressant; particularly treatment-resistant/atypical depression) |
| Predicted New Indication | Melancholia (melancholic subtype of major depression) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Candidate Indication Landscape (Multi-Prediction Screening)

This Evidence Pack contains 10 TxGNN predictions for tranylcypromine. Four of the top-10-scored predictions are rare pediatric/genetic syndromes (benign paroxysmal torticollis of infancy, Ohdo syndrome and variants ×2, ligneous conjunctivitis, Keppen-Lubinsky syndrome) that the evidence pack's own rationale flags as **knowledge-graph embedding artefacts with no mechanistic plausibility and zero supporting evidence** — these are excluded from further consideration (Hold, L5). The credible signal clusters around the depression/anxiety spectrum:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 5 | Melancholia | 99.58% | L2 | S3 | Proceed with Guardrails |
| 6 | Neurotic depression | 99.58% | L2 | S3 | Proceed with Guardrails |
| 4 | Agoraphobia | 99.62% | L3 | S2 | Proceed with Guardrails |
| 3 | Dysthymic disorder | 99.63% | L4 | S1 | Research Question |
| 8 | Neurotic disorder | 99.50% | L4 | S1 | Research Question |
| 1, 2, 7, 9, 10 | Rare pediatric/genetic syndromes | 99.38–99.67% | L5 | S0 | Hold (noise) |

Melancholia and neurotic depression share the top evidence level (L2) in this pack. Melancholia is selected as the lead candidate because it remains an actively used clinical construct (a recognized DSM/ICD depression specifier), whereas "neurotic depression" is a largely retired diagnostic term.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured evidence pack (flagged as a High-severity data gap, DG002). Based on information drawn from the literature evidence itself, tranylcypromine is described as a classic **irreversible, non-selective monoamine oxidase (MAO-A/MAO-B) inhibitor** that raises synaptic concentrations of serotonin, norepinephrine, and dopamine — the pharmacological basis for its established antidepressant effect (e.g., PMID 28579071, 37989204, 401000).

Melancholia is a severe subtype within the major depressive disorder spectrum — the same disease category tranylcypromine's original indication belongs to. Multiple sources in this pack directly evaluate tranylcypromine (rather than the antidepressant class generically) in this population: a double-blind RCT against moclobemide (PMID 8127928), a controlled trial combining tranylcypromine with amitriptyline (PMID 6342565), and a two-part meta-analysis of controlled tranylcypromine studies in depression (PMID 28579071). This is a materially stronger evidentiary basis than the "melancholia-specific placebo-controlled RCT" bar required for L1, but well above prediction-only (L5).

The parallel, consistently high-scoring predictions for dysthymic disorder, agoraphobia, and neurotic depression reinforce this pattern: MAOIs have a long documented clinical history in mood and anxiety-spectrum disorders (agoraphobia with panic, atypical/neurotic depression), which is consistent with the pharmacological rationale rather than an isolated artefact — unlike the four rare-syndrome predictions, which have no literature or trial support at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for melancholia.

*(Note: no ClinicalTrials.gov or ICTRP records were returned for any of the depression/anxiety-spectrum predictions in this pack; supporting evidence is literature-only.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8127928](https://pubmed.ncbi.nlm.nih.gov/8127928/) | 1993 | Double-blind RCT | Pharmacopsychiatry | Compared moclobemide vs. tranylcypromine (79 patients) in depression; established tranylcypromine as an efficacy/safety comparator for newer MAOIs |
| [6342565](https://pubmed.ncbi.nlm.nih.gov/6342565/) | 1983 | Controlled Trial | Archives of General Psychiatry | Amitriptyline + tranylcypromine combination vs. either alone in 60 major depression patients; all three arms improved equally, no added combo benefit |
| [28579071](https://pubmed.ncbi.nlm.nih.gov/28579071/) | 2017 | Meta-analysis | Eur Neuropsychopharmacology | Two-part review with meta-analysis of controlled tranylcypromine studies in depression; covers pharmacodynamics, interactions, and place in therapy |
| [35837681](https://pubmed.ncbi.nlm.nih.gov/35837681/) | 2023 | Review (Prescriber's Guide) | CNS Spectrums | Consensus clinical guide (>70 international experts) on classic MAOIs incl. tranylcypromine for treatment-resistant depression |
| [37989204](https://pubmed.ncbi.nlm.nih.gov/37989204/) | 2025 | Review | Fortschritte der Neurologie-Psychiatrie | Contemporary assessment of tranylcypromine psychopharmacotherapy; cites meta-analyses confirming established efficacy |
| [34369903](https://pubmed.ncbi.nlm.nih.gov/34369903/) | 2021 | Case Series | J Clin Psychopharmacology | Tranylcypromine + mirtazapine combination in difficult-to-treat depression; addresses serotonin syndrome risk of common combos |
| [3522559](https://pubmed.ncbi.nlm.nih.gov/3522559/) | 1986 | Retrospective Cohort | J Clin Psychiatry | Analysis of 58 patients from 2 controlled trials; identifies predictors of favorable tranylcypromine response (severity, psychomotor retardation, weight loss) |
| [23359339](https://pubmed.ncbi.nlm.nih.gov/23359339/) | 2013 | Systematic Review | Pharmacopsychiatry | Systematic review of withdrawal/discontinuation phenomena after abrupt tranylcypromine cessation |
| [34283390](https://pubmed.ncbi.nlm.nih.gov/34283390/) | 2021 | Retrospective Cohort | CNS Drugs | Cardiovascular effects of combining (es)ketamine with tranylcypromine in treatment-resistant depression |
| [36482163](https://pubmed.ncbi.nlm.nih.gov/36482163/) | 2023 | Pharmaceutical Development | Drug Delivery Transl Res | Development of a transdermal tranylcypromine delivery system to reduce oral GI/hepatic side effects |

**Supporting evidence for related predictions:** Agoraphobia is directly supported by a case report (PMID 20703987) and reviews on MAOIs in anxiety disorders (PMID 3050061); Dysthymic disorder is supported by a class-level meta-analysis of antidepressants (PMID 21527126, drug-nonspecific).

---

## US Market Information

Tranylcypromine currently holds **no active NDA on file** in this evidence pack (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). No dosage form or approved-indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information (`key_warnings`, `contraindications`, and `DDI` fields are all unpopulated in this evidence pack — flagged as **Blocking data gap DG001**, which must be resolved before any safety pre-assessment can proceed).

**Literature-derived risk signals** (not official labeling, drawn from evidence pack citations):
- Hypertensive crisis with tyramine-containing foods, including a historical fatality (PMID 14132611)
- Serotonin syndrome risk with serotonergic combinations (PMID 1636815, 34369903)
- Acute blood pressure elevation shortly after dosing (PMID 2738182)
- Withdrawal/discontinuation syndrome after abrupt cessation (PMID 23359339)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia (and the broader depression/anxiety spectrum: agoraphobia, neurotic depression) is supported by tranylcypromine-specific controlled trials and a dedicated meta-analysis (L2), a materially stronger and mechanistically coherent evidence base than the top TxGNN-ranked but mechanistically implausible rare-syndrome predictions, which should be disregarded (Hold).

**To proceed, the following is needed:**
- Official label warnings and contraindications (DG001, Blocking — required before any safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- A melancholia-specific placebo-controlled RCT to advance evidence level from L2 to L1
- Formal DDI review given known MAOI-class interaction risks (tyramine, serotonergic agents, sympathomimetics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


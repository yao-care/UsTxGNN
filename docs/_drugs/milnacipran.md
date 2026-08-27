---
layout: default
title: Milnacipran
parent: 僅模型預測 (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
---

# Milnacipran
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

# Milnacipran: From Fibromyalgia/Depression to Migraine Disorder

## One-Sentence Summary

Milnacipran (DrugBank DB04896) is a serotonin-norepinephrine reuptake inhibitor (SNRI), used elsewhere for fibromyalgia and depression, though it is not currently marketed in Taiwan and no official Taiwan indication text is on record. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **2 clinical trials** and **5 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from official regulatory record — literature references describe milnacipran as indicated for fibromyalgia/depression (see MOA data gap below) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the evidence pack's repurposing rationale, milnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI), in the same pharmacological class as venlafaxine and duloxetine. SNRIs already have an established mechanistic hypothesis for migraine prevention, acting through central monoamine modulation and descending pain-inhibitory pathways — though this is not a first-line mechanism for migraine.

Supporting this, cited literature (PMID 26798881) notes that SNRIs and tricyclic antidepressants are recognized as preventive medications for chronic migraine headaches, and that milnacipran is one of three FDA-approved drugs for fibromyalgia (alongside pregabalin and duloxetine) — a condition that shares pain-modulation pathophysiology with migraine. This provides a plausible mechanistic bridge between milnacipran's known pharmacology and the TxGNN-predicted new indication, though it should be noted the drug's own MOA record is currently a data gap and this rationale is inferred from class effects rather than milnacipran-specific mechanistic studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01393522](https://clinicaltrials.gov/study/NCT01393522) | Not Applicable | Completed | 37 | Randomized, double-blind, placebo-controlled trial testing twice-daily milnacipran for reduction of migraine headache pain |
| [NCT01319825](https://clinicaltrials.gov/study/NCT01319825) | Phase 4 | Unknown | 45 | Open-label pilot study evaluating whether milnacipran reduces headache frequency in episodic and chronic migraine |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21377931](https://pubmed.ncbi.nlm.nih.gov/21377931/) | 2011 | Review | Current Opinion in Pharmacology | Overview of 5-HT receptor ligands for pain (including migraine), noting SNRIs like milnacipran may exert analgesic effects via serotonergic modulation |
| [24030685](https://pubmed.ncbi.nlm.nih.gov/24030685/) | 2014 | Cohort (open-label prospective) | Neurological Sciences | 3-month pilot study in 45 patients with episodic/chronic migraine; anecdotal clinical observation that milnacipran reduced headache incidence prompted the study |
| [26798881](https://pubmed.ncbi.nlm.nih.gov/26798881/) | 2015 | Review | Journal of the California Dental Association | Evidence-based pharmacologic approaches for chronic orofacial/migraine pain; lists milnacipran among SNRIs relevant to preventive treatment, though notes efficacy for fibromyalgia indication is "not robust" |
| [31804357](https://pubmed.ncbi.nlm.nih.gov/31804357/) | 2019 | Case Report | Medicine | Case report on reversible cerebral vasoconstriction syndrome presenting with thunderclap headache, discussed as a differential diagnosis challenge versus migraine |
| [22967190](https://pubmed.ncbi.nlm.nih.gov/22967190/) | 2012 | Pharmacovigilance/Safety signal analysis | Drug Safety | Methodological analysis of competition bias in spontaneous adverse-event reporting databases; not migraine-specific but relevant to signal-detection context |

## US Market Information

Milnacipran is currently not marketed in Taiwan — no active licenses are on record (0 NDAs found).

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data for milnacipran are currently a **Blocking** data gap (TFDA label not yet retrieved), and a DDI database query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (missing TFDA warnings/contraindications) prevents this candidate from entering the S1 safety pre-assessment stage, and the drug is not currently marketed in Taiwan. While the migraine indication has L2-level supporting evidence (a completed double-blind RCT, albeit with a small n=37 sample, plus a Phase 4 open-label pilot and five supporting publications), efficacy evidence alone is insufficient to advance without the safety data.

**To proceed, the following is needed:**
- TFDA-equivalent or manufacturer package insert (warnings, contraindications, DDI profile) to clear the Blocking data gap
- Confirmed mechanism of action data from DrugBank to strengthen the mechanistic rationale
- Larger, phase-designated controlled trials for migraine given the current largest study has only 45 participants
- Clarification of milnacipran's actual approved indication(s) in reference markets, since Taiwan regulatory records show no licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


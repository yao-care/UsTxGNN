---
layout: default
title: Serotonin
parent: Moderate Evidence (L3-L4)
nav_order: 1156
evidence_level: L4
indication_count: 9
monitor_inn: "SEROTONIN"
predicted_indications: ["insomnia (disease)", "anxiety disorder", "migraine disorder", "anxiety", "agoraphobia", "migraine with brainstem aura", "benign paroxysmal torticollis of infancy", "manic bipolar affective disorder", "atrophoderma vermiculata"]
last_modified_at: 2026-10-28
description: "Serotonin: predicted new indication Insomnia (disease) (evidence level L4). Approved use: Not recorded in the local data"
---

# Serotonin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Serotonin: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Serotonin is an endogenous neurotransmitter, and the only US listing in the data compiled for this report is a cancelled liquid product with no approved indication on file.
The TxGNN model predicts it may be effective for **insomnia**, but none of the **2 clinical trials** found actually tests serotonin itself, and the **18 publications** are mostly reviews and mechanistic papers about serotonin-related drugs.
The prediction is a network-based signal, not clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L4 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this compound are not available in the data compiled for this report. Serotonin (5-HT) is a well-known neurotransmitter involved in sleep-wake regulation, mood and anxiety circuitry. Serotonergic drugs such as trazodone and mirtazapine are used for their effects on sleep. This likely explains why the network model links serotonin to insomnia.

However, this supports the serotonin pathway, not the administration of serotonin itself. Exogenous serotonin does not cross the blood-brain barrier well, and it has peripheral cardiovascular and gastrointestinal effects. Evidence for serotonin-modulating drugs (SSRIs, trazodone, triptans) therefore cannot be transferred to this compound. The TxGNN score of 0.999 is a model output, not clinical proof.

Other top predictions (all with the same limitation) include anxiety disorder, anxiety, agoraphobia, migraine disorder and related subtypes, and manic bipolar affective disorder. Two lower-ranked predictions have no supporting trials or literature at all: benign paroxysmal torticollis of infancy and atrophoderma vermiculata. The bipolar prediction also carries a safety concern, because enhancing serotonergic tone may precipitate antidepressant-associated switch to mania.

## Clinical Trial Evidence

Trials for the top predicted indication (insomnia). Neither tests serotonin.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06559306](https://clinicaltrials.gov/study/NCT06559306) | Phase 3 | Recruiting | 752 | Seltorexant as adjunctive therapy to antidepressants in major depressive disorder with insomnia symptoms; the investigational drug is not serotonin |
| [NCT05705830](https://clinicaltrials.gov/study/NCT05705830) | N/A | Unknown | 400 | Pulse magnetotherapy plus medication for anxiety disorder with insomnia; a non-drug intervention trial |

## Literature Evidence

Publications for insomnia (most relevant first). No randomized trial of serotonin in insomnia was found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40135470](https://pubmed.ncbi.nlm.nih.gov/40135470/) | 2025 | RCT (protocol) | Age and Ageing | Mirtazapine (blocks serotonin and histamine receptors) for chronic insomnia in older adults; a different drug |
| [34994734](https://pubmed.ncbi.nlm.nih.gov/34994734/) | 2021 | Review | Psychiatria Polska | Compares trazodone and hypnotics for sleep effects; indirect support for serotonergic agents |
| [41123484](https://pubmed.ncbi.nlm.nih.gov/41123484/) | 2025 | Review | Annals of Medicine | Circadian clock genes and insomnia mechanisms |
| [37834999](https://pubmed.ncbi.nlm.nih.gov/37834999/) | 2023 | Observational | Journal of Clinical Medicine | Serotonin transmission linked to depressive and insomnia symptoms in inflammatory bowel disease |
| [41392764](https://pubmed.ncbi.nlm.nih.gov/41392764/) | 2026 | Preclinical | Food & Function | A probiotic strain improved insomnia in mice by restoring GABA and serotonin signaling |
| [38645778](https://pubmed.ncbi.nlm.nih.gov/38645778/) | 2024 | Review | Tzu Chi Medical Journal | Role of the GABAergic system in insomnia |
| [40102888](https://pubmed.ncbi.nlm.nih.gov/40102888/) | 2025 | Observational | Cell Communication and Signaling | Neurotransmitter levels and sleep disorders in early Parkinson's disease |

Several other retrieved papers (on acupuncture, aspartame, and similar topics) were only loosely related and are omitted.

For the other top predictions, the evidence is similar in nature. Anxiety has one Phase 2 sertraline trial (NCT06081348) and several guideline and meta-analysis papers on SSRIs/SNRIs. Migraine has reviews on serotonin's role and on triptans and lasmiditan, which are selective receptor agonists rather than serotonin.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Serotonin (BioActive Nutritional) | Liquid | Not available; status: cancelled |


## Safety Considerations

No label warnings, contraindications or drug-interaction data were found in the data compiled for this report. Please refer to the package insert for safety information, which is itself a blocking data gap.

Based on the rationale compiled for the predictions, the following concerns should be noted:
- Exogenous serotonin may cause peripheral cardiovascular and gastrointestinal effects and vasoconstriction.
- Increasing serotonergic tone may precipitate a switch to mania in people with bipolar disorder.
- Use in infants (for example, the infantile torticollis prediction) would raise significant safety concerns.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a network score alone (evidence level L4 for insomnia, L5 for the weakest predictions). No trial tests serotonin itself, and the supporting literature concerns other serotonergic drugs. The only US license is cancelled, and the safety label data needed for screening is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism-of-action data from DrugBank
- Confirmation of the investigational product in NCT06559306
- Evidence that serotonin, or a suitable prodrug or precursor, can reach the relevant target (CNS penetration, route of administration)
- A clear definition of the original indication and dosage form, since no approved indication is on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


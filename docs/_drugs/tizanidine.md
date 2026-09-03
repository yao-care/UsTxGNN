---
layout: default
title: Tizanidine
parent: 僅模型預測 (L5)
nav_order: 1236
evidence_level: L5
indication_count: 6
---

# Tizanidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using no additional skill — this is a direct content-generation task following the explicit v5 report template already provided in the prompt.

---

# Tizanidine: From Muscle Spasticity to Migraine Disorder

## One-Sentence Summary

Tizanidine is a centrally-acting alpha-2 adrenergic agonist traditionally used to manage muscle spasticity. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **2 clinical trials** (including an actively recruiting Phase 3 RCT) and **18 publications** currently supporting this direction — though most of the literature is older, indirect (class-level) evidence rather than tizanidine-specific pivotal trial data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasticity (globally established use; no TFDA license record — drug not marketed in Taiwan) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of NDAs (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tizanidine is a centrally-acting alpha-2 adrenergic receptor agonist, mechanistically related to clonidine, which reduces presynaptic release of excitatory neurotransmitters. This mechanism is relevant to the central sensitization and muscle-tension-related pathophysiology implicated in migraine and chronic daily headache. Clinically, low-dose tizanidine combined with NSAIDs has already been used in practice for detoxification from analgesic-overuse (rebound) headache, providing an established real-world precedent for its use in headache disorders.

The original indication (spasticity) and the predicted indication (migraine) share a common pharmacological thread: alpha-2 agonists as a drug class (clonidine, guanfacine, tizanidine) modulate central noradrenergic/excitatory tone, and several agents in this class have documented use in neurological and headache-related conditions. This makes the repurposing hypothesis a reasonable pharmacological extrapolation rather than a novel, unprecedented mechanism — a conclusion reinforced by decades-old open-label and placebo-controlled studies of tizanidine in chronic daily headache prophylaxis (see literature below).

Currently, detailed formal mechanism-of-action documentation from DrugBank is flagged as a data gap in this evidence pack (DG002); the mechanistic description above is derived from the model's repurposing rationale rather than a structured MOA record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Recruiting | 189 | Multicenter, randomized, double-blind, placebo-controlled trial evaluating oral tizanidine for prevention of migraine attacks (with/without aura) in adults 18–65; no results reported yet |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completed | 300 | 24-week observational study on topical NSAIDs for pain relief; not tizanidine-specific, only broadly relevant to analgesic efficacy research |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Double-blind, placebo-controlled, multicenter trial of tizanidine as adjunctive prophylaxis for chronic daily headache (incl. chronic migraine) |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Open-label study | Headache | Open-label dose-titration study of tizanidine tablets for prophylaxis of chronic daily headache |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | Cohort | Headache | Outpatient regimen using low-dose tizanidine with NSAIDs for detoxification from analgesic rebound headache |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | Preclinical/Formulation | J Control Release | Supramolecular cocrystal of tizanidine + meloxicam shows synergistic anti-migraine efficacy in preclinical formulation study |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | Reviews muscle-tone-modifying agents (baclofen, tizanidine, botulinum toxin A) as preventive treatments for migraine and tension-type headache |
| [21770931](https://pubmed.ncbi.nlm.nih.gov/21770931/) | 2011 | Review | Headache | Reviews chronic migraine prophylactic agents (incl. tizanidine) in the context of medication-overuse trials |
| [23293866](https://pubmed.ncbi.nlm.nih.gov/23293866/) | 2013 | Review | Headache | Rational approach to chronic migraine management, listing tizanidine among established prophylactic options |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | Review of chronic daily headache prophylaxis, citing tizanidine evidence alongside topiramate/gabapentin |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | Reviews emerging migraine prophylactic treatments, including tizanidine |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | Review | Neurol Sci | Systematic review of double-blind, placebo-controlled pharmacological prophylaxis trials for chronic migraine |

---

## Taiwan Market Information

Tizanidine currently holds **no TFDA license** and is **not marketed in Taiwan** (`market_status: 未上市`, `total_licenses: 0`). No product/dosage-form data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (TFDA label data is flagged as a **blocking** data gap, DG001), and the DDI database query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alpha-2 agonist mechanism and older placebo-controlled/open-label studies provide plausible, but dated and indirect, support for tizanidine in chronic daily headache/migraine prophylaxis. The one directly relevant, adequately powered study (NCT05484349, Phase 3) is still recruiting with no results yet, and a blocking safety data gap (TFDA warnings/contraindications) prevents even an initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — blocking gap, DG001
- Structured mechanism-of-action data from DrugBank — DG002
- Results of NCT05484349 upon completion
- DDI dataset re-query, as current search returned no interactions on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


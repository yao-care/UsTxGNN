---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 1137
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease/Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Rotigotine is a non-ergot dopamine receptor agonist reported in the literature as being used to treat Parkinson's disease and restless legs syndrome (no confirmed original indication is available in the structured regulatory data for this candidate).
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> with **0 clinical trials** and only **3 tangentially related publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory license data; literature (PMID 37221270) references Parkinson's disease and restless legs syndrome as rotigotine's known uses |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (mechanistic/preclinical evidence only) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap (DG002). Based on the available literature within this evidence pack, rotigotine is a non-ergot dopamine receptor agonist active across the D1–D3 subtypes (one structural study, PMID 37221270, further characterizes it as a "pan-agonist" across all five human dopamine receptor subtypes, D1R–D5R). It is described in the literature as being used clinically for Parkinson's disease and restless legs syndrome (RLS).

The mechanistic rationale for ADHD rests on the dopamine-deficiency hypothesis: ADHD is associated with reduced dopaminergic signaling in prefrontal-striatal circuits, and existing ADHD pharmacotherapies (stimulants, atomoxetine) act — directly or indirectly — to increase dopaminergic tone. A direct dopamine receptor agonist such as rotigotine could theoretically address this deficit.

However, the supporting literature retrieved for this candidate is weak and largely indirect: two of the three papers are general reviews of RLS (not ADHD), and only one (PMID 34182128) discusses a mechanism potentially relevant to ADHD — heteromerization between α2A-adrenoceptors and dopamine D4 receptor variants — without testing rotigotine itself in an ADHD model or population. No ADHD-specific preclinical, clinical trial, or case-report evidence exists in the current evidence pack. The prediction should therefore be treated as a mechanism-driven research hypothesis rather than clinically supported repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Mechanistic/Receptor Study | Pharmacological research | Describes heteromerization between α2A-adrenoceptors and dopamine D4 receptor variants, a pathway implicated in ADHD; does not test rotigotine directly in ADHD models |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | Review of pharmacological options for restless legs syndrome in children; not ADHD-specific |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | General review of restless legs syndrome pathophysiology and treatment; not ADHD-specific |

---

## US Market Information

No approved licenses or NDA records found for this candidate (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available for this candidate (structured safety fields are all data gaps, including a **blocking** gap: DG001 — TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction is supported only by mechanistic/preclinical-tier literature (L4) with zero clinical trials, and the retrieved publications are largely about a different indication (RLS) rather than ADHD. Combined with a blocking safety data gap (no TFDA label data available) and the theoretical risk that a full D2/D3 dopamine agonist could carry a distinct adverse-effect profile in a psychiatric population (e.g., impulse-control disorders), the evidence does not currently support proceeding beyond a research question.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TFDA/official label warnings, contraindications, and precautions
- Resolve DG002: confirm mechanism of action via DrugBank API
- Confirm the drug's actual approved original indication(s) through official regulatory sources (current structured data has no license records)
- Generate or identify ADHD-specific preclinical data (in vivo/in vitro) for rotigotine before considering clinical investigation
- Assess safety signals specific to non-Parkinsonian, non-elderly populations (e.g., impulse-control disorder risk, cardiovascular tolerability in children/adolescents if pursuing pediatric ADHD)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


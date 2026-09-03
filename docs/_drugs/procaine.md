---
layout: default
title: Procaine
parent: 僅模型預測 (L5)
nav_order: 1086
evidence_level: L5
indication_count: 10
---

# Procaine
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

# Procaine: From Local Anesthesia to Methemoglobinemia

## One-Sentence Summary

Procaine is a classic ester-type local anesthetic (confirmed by the associated literature, which repeatedly references "local anaesthetics," "regional anesthesia," and "novocaine block").
TxGNN's top-ranked prediction links procaine to **Methemoglobinemia**, but review of the underlying literature shows this reflects procaine's well-documented **risk of causing** methemoglobinemia as a toxicity — not a therapeutic effect. Evidence level is **L4** (case reports and reviews only), and no clinical trials exist.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in this dataset — 0 approved licenses on file. Per the associated literature (e.g., "Rational use of local anaesthetics," "Local-regional dental anesthesia"), procaine's established use is as a local/regional anesthetic |
| Predicted New Indication | Methemoglobinemia — **flagged as a reverse-causality adverse-effect signal, not a therapeutic candidate** (see rationale below) |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on the literature associated with this prediction, procaine is an ester-type local anesthetic used for infiltration and peripheral nerve block. Its ester hydrolysis produces para-aminobenzoic acid (PABA) and diethylaminoethanol, and oxidative stress from these metabolites is documented to induce methemoglobinemia as an **adverse reaction** — this is the mechanistic link TxGNN is picking up on.

However, the direction of this relationship matters: every piece of supporting literature (e.g., PMID 5529388 "Methemoglobinemia due to intravenous procaine," PMID 705003 neonatal methemoglobinemia after subcutaneous novocaine infiltration) describes procaine **causing** methemoglobinemia, not treating it. TxGNN's knowledge graph appears to have captured a drug-adverse-event co-occurrence pattern from toxicology/case-report literature and surfaced it as a drug-disease association, without distinguishing causal direction. This is a known failure mode of graph-embedding repurposing models and should be treated as a **safety signal**, not a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of local anesthetic pharmacology and clinical use; no procaine-specific methemoglobinemia data |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review (unclassified) | Laval Medical | General review of local anesthetics |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Cohort/Observational | Zhonghua Wai Ke Za Zhi (Chinese J Surgery) | Effect of IV procaine anesthesia on methemoglobin levels in surgical patients |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case Report | Acta Physiologica Latino Americana | IV procaine reported to cause methemoglobinemia |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case Report | Revista Española de Anestesiología y Reanimación | Neonatal methemoglobinemia after subcutaneous novocaine infiltration during general anesthesia |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Unclassified | American Journal of Obstetrics and Gynecology | Studied transplacental passage of procaine HCl and PABA — the metabolite implicated in methemoglobin formation |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Unclassified | Lancet | Methemoglobinemia following lignocaine (a structurally related local anesthetic), supporting a class effect |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Unclassified | Fundamental and Applied Toxicology | Mechanistic discussion of organophosphate interactions altering metabolism/toxicity of ester- and amide-containing xenobiotics (not procaine-specific) |

---

## US Market Information

No marketing authorizations found. Procaine is not currently marketed in this jurisdiction (0 licenses on file, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Blocking data gap (DG001)**: TFDA/label warnings and contraindications for procaine could not be retrieved. This blocks any Stage-1 safety evaluation and must be resolved before any repurposing decision — including for the more promising candidates below (fibromyalgia, tendinitis) — can proceed.

---

## Other Predicted Signals (Ranks 2–10)

The evidence pack contains 9 additional TxGNN predictions for procaine. Only two show any evidence base worth further tracking; the rest are model-only (L5) or reflect the same reverse-causality pattern as the headline prediction.

| Rank | Disease | Score | Evidence | Stage | Recommendation | Note |
|------|---------|-------|----------|-------|------|------|
| 2 | Methemoglobinemia, alpha type | 99.43% | L5 | S0 | Hold | No literature; likely graph-neighborhood artifact of rank 1 |
| 3 | Tourette syndrome | 99.34% | L5 | S0 | Hold | No literature/mechanistic plausibility (peripheral vs. central action) |
| 4 | Anaphylaxis | 99.29% | L4 | S0 | Hold | 20 papers, but describe procaine/procaine-penicillin **causing** anaphylactoid reactions (Hoigné's syndrome) — same reverse-causality problem |
| 5 | Methemoglobin reductase deficiency | 99.27% | L5 | S0 | Hold | No literature; mechanistically procaine would worsen, not treat, this condition |
| 6 | Hyperthyroidism | 99.25% | L4 | S0 | Hold | Historic "procaine esterase test" (diagnostic, not therapeutic) and obsolete "neural therapy" case series |
| 7 | Fibromyalgia | 99.23% | L3 | S1 | **Research Question** | Plausible MOA (trigger-point/peripheral nerve blockade); only 1950s–70s case series, linked to the controversial Gerovital H3 anti-aging context |
| 8 | Tendinitis | 99.20% | L3 | S2 | **Research Question** | Strongest candidate: includes a 2022 comparative trial (PMID 35480510, supraspinatus tendinopathy) plus comparator studies vs. corticosteroid injection |
| 9 | Idiopathic granulomatous myositis | 99.18% | L5 | S0 | Hold | No literature; no known mechanism |
| 10 | Myositis fibrosa | 99.18% | L5 | S0 | Hold | Identical score to rank 9 — likely a knowledge-graph clustering artifact, not independent signal |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline TxGNN prediction (methemoglobinemia) is a reverse-causality artifact — every supporting citation describes procaine **inducing** this condition, not treating it — and should be reclassified as a safety signal rather than a repurposing lead. A blocking data gap (missing label warnings/contraindications, DG001) also prevents any Stage-1 safety review for procaine in general. Among the 10 predictions, only tendinitis (L3, S2) and fibromyalgia (L3, S1) have any plausible mechanistic and clinical support, but both rely almost entirely on historical case series plus a single 2022 comparative trial.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/FDA label warnings and contraindications for procaine
- Resolve DG002: obtain DrugBank mechanism-of-action data
- If pursuing the tendinitis signal: independently appraise PMID 35480510 (2022 supraspinatus tendinopathy trial) for quality and replication, and search for additional modern comparative studies
- If pursuing the fibromyalgia signal: separate the historical "intradermal procaine therapy" literature from its association with the discredited Gerovital H3 anti-aging product before further evaluation
- Add a causal-direction check to the prediction pipeline so adverse-event co-occurrence (methemoglobinemia, anaphylaxis) is not surfaced as a repurposing candidate in future TxGNN runs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


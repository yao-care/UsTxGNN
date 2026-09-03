---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 1110
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

> Ranitidine is a histamine H2-receptor antagonist historically used to treat peptic ulcer disease and other gastric acid-related conditions.
> The TxGNN model's top prediction — **Active Peptic Ulcer Disease** — is essentially a re-identification of its long-established original indication rather than a novel repurposing signal,
> supported by **1 directly linked clinical trial** and **20 literature references**, though the drug currently carries **zero active US market authorizations**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / gastric acid hypersecretion (based on ranitidine's known pharmacological class as an H2-receptor antagonist; no formal license text is present in the evidence pack) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002). Based on known pharmacological information, ranitidine is a competitive histamine H2-receptor antagonist that blocks H2 receptors on gastric parietal cells, thereby inhibiting basal and stimulated gastric acid secretion. This is a well-characterized, decades-old mechanism.

Critically, the top-ranked TxGNN prediction — active peptic ulcer disease — is **not a genuine new indication**. As the model's own rationale notes, this is ranitidine's original, already-approved use; the knowledge graph is essentially confirming an existing, well-validated drug-disease relationship rather than surfacing an underexplored one. The remaining candidates in this evidence pack (peptic ulcer perforation, gastrojejunal ulcer, duodenogastric reflux, duodenal obstruction, gastroduodenitis) represent more plausible "adjacent" repurposing opportunities via the same acid-suppression mechanism, though evidence for these is indirect (retrospective/review-level) rather than purpose-designed trials.

The dominant issue limiting this candidate is not efficacy but **safety/supply**: ranitidine was withdrawn from markets globally in 2019–2020 after detection of N-nitrosodimethylamine (NDMA), a probable human carcinogen, in the active ingredient and finished products. This is reflected in the US market status of "Not Marketed" with zero active NDAs, and is the primary reason all ten predicted indications in this evidence pack are scored **Hold** or **Research Question** despite several having strong (L1) clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the influence of statins and proton pump inhibitors (PPIs) on clopidogrel antiplatelet effects in PCI patients; ranitidine/acid-suppression relevance is indirect (Relevance grade C) rather than a direct efficacy trial for peptic ulcer disease. |

*Note: The top-ranked indication (active peptic ulcer disease) has only 1 directly linked trial in this evidence pack. Stronger, directly relevant Phase 3 head-to-head trials (e.g., esomeprazole vs. ranitidine for NSAID-associated gastric ulcer, NCT00633412/NCT00633672) are associated with the closely related "peptic ulcer disease" candidate (rank 7) rather than this specific term.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Compared nocturnal rioprostil (prostaglandin E1 analogue) vs. ranitidine 300mg in duodenal ulcer healing. |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Ranitidine 300mg/day showed 4-week healing rates of 91% (duodenal), 68% (prepyloric), 81% (gastric corporeal) ulcers; maintenance therapy reduced relapse vs. placebo. |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | Prospective controlled study | Hepato-gastroenterology | Compared ranitidine and ecabet for inhibition of peptic ulcer relapse independent of H. pylori eradication. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | Multicenter RCT | Clinical Therapeutics | 160 patients with active duodenal ulcer randomized to famotidine 40mg vs. ranitidine 300mg nightly; 8-week healing rates 94% vs. 80% respectively. |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Reviewed the role of prostaglandins and H2-receptor antagonists (including ranitidine) in peptic ulcer pathophysiology and treatment. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Reviewed the role of acid suppression (H2-antagonists) in peptic ulcer pathogenesis and healing. |
| [9506245](https://pubmed.ncbi.nlm.nih.gov/9506245/) | 1998 | Review | Drugs | Reviewed rabeprazole (PPI) pharmacodynamics, referencing comparative antisecretory potency vs. H2-antagonists such as ranitidine. |
| [8736619](https://pubmed.ncbi.nlm.nih.gov/8736619/) | 1996 | Review | Drugs | Reviewed ebrotidine, an H2-antagonist with gastroprotective activity, noting antisecretory potency similar to ranitidine. |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Reviewed nizatidine, comparing its antisecretory activity to cimetidine and other H2-antagonists including ranitidine. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intelligence & Clinical Pharmacy | Early review of ranitidine following its FDA approval for short-term treatment of active duodenal ulcers and gastric hypersecretory conditions. |

---

## US Market Information

Currently no active US marketing authorization (NDA) is recorded for ranitidine — market status is **Not Marketed**, consistent with its global withdrawal in 2019–2020 due to NDMA contamination.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, drug-drug interactions) are not populated in this evidence pack (DG001, Blocking severity) — a formal TFDA/FDA label review has not yet been completed for this candidate.

However, the evidence pack's repurposing rationale independently documents a critical safety event: ranitidine products were found to contain **N-nitrosodimethylamine (NDMA)**, a probable human carcinogen, leading to a **global market withdrawal in 2019–2020**. This is not an efficacy issue but a manufacturing/impurity issue, and it is the primary driver of the "Hold" recommendation across all predicted indications in this evidence pack, overriding an otherwise strong (L1) mechanistic and clinical evidence base.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for acid-suppression indications is strong (L1, multiple Phase 3/4 RCTs), but the drug is not currently marketed anywhere due to a global withdrawal over NDMA (probable carcinogen) contamination — a blocking safety/supply issue that must be resolved before any repurposing pathway (including the top-ranked "active peptic ulcer disease," which is not a true novel indication) can be clinically actionable.

**To proceed, the following is needed:**
- Formal FDA/TFDA label data (warnings, contraindications) to close DG001 (Blocking)
- Documented mechanism of action from DrugBank to close DG002
- Resolution status of the NDMA impurity issue (reformulation, alternative synthesis route, or confirmation that no compliant supply chain exists)
- Clarification of which candidates represent genuine novel indications vs. restatement of the original approved use, before allocating further review effort to lower-evidence candidates (ranks 4, 5, 8–10, currently L4–L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


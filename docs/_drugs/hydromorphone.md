---
layout: default
title: Hydromorphone
parent: 僅模型預測 (L5)
nav_order: 777
evidence_level: L5
indication_count: 6
---

# Hydromorphone
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

# Hydromorphone: From Opioid Pain Management to Acute Migraine (Headache Disorder)

## One-Sentence Summary

Hydromorphone is a semi-synthetic opioid analgesic established for moderate-to-severe pain. Of the six indications TxGNN surfaced, only **Headache Disorder (acute migraine)** is backed by substantive clinical evidence — **6 clinical trials and 17 publications**, including Phase 4 RCTs directly testing hydromorphone against active comparators in the emergency department. The model's top-ranked candidate by raw score, pharyngitis, has no disease-specific evidence and is judged an artifact of pain-management co-occurrence rather than a real signal.

*Note on candidate selection*: TxGNN ranked pharyngitis first by score (99.81%), but every supporting trial for it involves post-surgical opioid analgesia (tonsillectomy, foot/ankle surgery) or unrelated agents (palifermin), none of which treat pharyngitis itself. This report therefore leads with headache disorder — the only candidate with a genuine treat-relationship evidence base — and summarizes the other five separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe pain (established opioid/μ-receptor agonist use; Taiwan-specific label text unavailable — 0 TW licenses on file) |
| Predicted New Indication | Headache Disorder (acute migraine) |
| TxGNN Prediction Score | 99.65% (rank 8998 of candidate pool) |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

**Other TxGNN candidates (all Hold, L4–L5, no disease-specific evidence):**

| Disease | TxGNN Score | Evidence Level | Note |
|---------|------------|-----------------|------|
| Pharyngitis (top score) | 99.81% | L4 | All 6 trials are post-surgical analgesia, not pharyngitis treatment |
| Allergic Urticaria | 99.81% | L5 | Opioids are known to *cause* pruritus/urticaria via mast cell degranulation — directional conflict with "treatment" |
| Nasal Cavity Disease | 99.80% | L5 | No trials, literature, or plausible mechanism |
| Acute Laryngopharyngitis | 99.75% | L5 | No trials or literature; viral etiology has no opioid-relevant mechanism |
| Trigeminal Autonomic Cephalalgia | 99.58% | L5 | No trials/literature; opioids are generally considered *ineffective* for this headache class |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a flagged gap (DG002, High severity). Based on known pharmacology, hydromorphone is a semi-synthetic phenanthrene-class opioid and potent μ-opioid receptor agonist, used clinically for moderate-to-severe acute and chronic pain.

Migraine is a pain syndrome, and opioids — including hydromorphone — have historically been used as rescue analgesia in emergency departments when first-line agents (triptans, antiemetics/dopamine antagonists) fail or are contraindicated. This gives the prediction a plausible non-specific mechanistic basis: μ-receptor-mediated analgesia can blunt migraine pain even without acting on the disease-specific CGRP/5-HT1 pathways that dedicated anti-migraine drugs target.

However, this same literature base shows the clinical field is moving *away* from opioids for migraine. A head-to-head Phase 4 RCT (NCT02389829) and its associated publications found hydromorphone comparable to or worse than dopamine-antagonist regimens, with added concerns about euphoria-driven return ED visits and medication-overuse headache (MOH). The most recent evidence — the 2025/2026 American Headache Society guideline update (PMID 41321235) — reflects this shift. The mechanistic plausibility is real, but it argues for "opioid as a studied-and-largely-discouraged option" rather than a novel repurposing opportunity.

---

## Clinical Trial Evidence (Headache Disorder)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02389829](https://clinicaltrials.gov/study/NCT02389829) | Phase 4 | Completed | 127 | Direct RCT comparing hydromorphone vs. prochlorperazine+diphenhydramine for acute migraine in the ED; disease-specific and highest-relevance trial in this set. |
| [NCT00261495](https://clinicaltrials.gov/study/NCT00261495) | Phase 3 | Completed | 504 | OROS hydromorphone vs. sustained-release oxycodone in chronic non-cancer pain; supports general analgesic efficacy but not headache-specific. |
| [NCT03766269](https://clinicaltrials.gov/study/NCT03766269) | Phase 2 | Unknown | 280 | Opioid-sparing effect of dronabinol co-administered with opioids (incl. hydromorphone) in chronic pain; indirect relevance. |
| [NCT06453447](https://clinicaltrials.gov/study/NCT06453447) | N/A | Recruiting | 40 | Prednisone for CRPS after wrist fracture; opioid-context only, not hydromorphone-specific. |
| [NCT02152514](https://clinicaltrials.gov/study/NCT02152514) | Phase 4 | Terminated | 34 | Intrathecal morphine/sufentanil vs. placebo for post-VATS analgesia; not headache-related. |
| [NCT02417298](https://clinicaltrials.gov/study/NCT02417298) | N/A | Terminated | 12 | Ketamine + opioid therapy for sickle cell pain crisis; not headache-related. |

---

## Literature Evidence (Headache Disorder)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17981511](https://pubmed.ncbi.nlm.nih.gov/17981511/) | 2008 | RCT | The Journal of Pain | Retrospective cohort/RCT comparing metoclopramide vs. hydromorphone for ED migraine treatment. |
| [29046364](https://pubmed.ncbi.nlm.nih.gov/29046364/) | 2017 | RCT | Neurology | Pivotal RCT: IV hydromorphone vs. IV prochlorperazine+diphenhydramine for migraine outcomes. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 AHS update on acute ED migraine treatment; evidence assessment of parenteral pharmacotherapies (post-dates and reframes opioid use). |
| [27300483](https://pubmed.ncbi.nlm.nih.gov/27300483/) | 2016 | Guideline | Headache | Prior AHS evidence assessment on injectable migraine therapies in the ED. |
| [34363617](https://pubmed.ncbi.nlm.nih.gov/34363617/) | 2021 | Post-hoc RCT analysis | Headache | Post hoc analysis of the same hydromorphone vs. prochlorperazine+diphenhydramine trial, focused on migraine-associated symptoms. |
| [29516486](https://pubmed.ncbi.nlm.nih.gov/29516486/) | 2018 | Cohort | Headache | Opioid-induced "likeability"/euphoria not associated with return ED visits among IV-hydromorphone migraine patients — but raises misuse-risk questions. |
| [22795050](https://pubmed.ncbi.nlm.nih.gov/22795050/) | 2012 | RCT (pooled) | J Pain Symptom Manage | Safety/tolerability of once-daily OROS hydromorphone ER across 11 pooled studies (chronic cancer/non-cancer pain, not headache-specific). |
| [39924451](https://pubmed.ncbi.nlm.nih.gov/39924451/) | 2025 | Review (SR/meta-analysis) | Addiction | Relative adverse-effect risks across opioid agonist treatments. |
| [30059368](https://pubmed.ncbi.nlm.nih.gov/30059368/) | 2018 | Commentary | Adv Emerg Nurs J | Practice commentary on the prochlorperazine+diphenhydramine vs. hydromorphone migraine RCT. |
| [29461426](https://pubmed.ncbi.nlm.nih.gov/29461426/) | 2018 | Review | Curr Opin Neurol | Review of current acute-care treatment approaches for primary headache. |

---

## Taiwan Market Information

Hydromorphone is **not currently marketed in Taiwan** — 0 approved licenses are on file (`taiwan_regulatory.total_licenses = 0`, `market_status = 未上市`). No NDA/license records are available to summarize.

---

## Safety Considerations

- **Data gap flagged as blocking (DG001)**: TFDA label warnings and contraindications for hydromorphone have not been retrieved. This blocks the S1 safety pre-screen and must be resolved (via TFDA label PDF or equivalent, e.g. FDA label given TW non-marketing status) before any further evaluation.
- **Drug interaction data**: DDI query returned no results (`query_status: not_found`); no interaction profile is currently available.
- **Known class-level risk (not in structured safety fields, but noted in the evidence pack's own rationale)**: opioids, including hydromorphone, can trigger mast-cell degranulation causing pruritus/urticaria — directly relevant given "allergic urticaria" appears as a (rejected) predicted indication. Separately, opioid use for migraine carries recognized risk of dependency and medication-overuse headache, a concern echoed in the 2025/2026 AHS guideline.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Headache disorder is the only candidate with real disease-specific evidence (Phase 4 RCTs, guideline coverage), but hydromorphone is unmarketed in Taiwan, lacks any retrievable TFDA safety/label data (blocking gap), and the most current guideline (2025/2026 AHS) reflects a field-wide move away from opioids for migraine due to MOH and dependency risk. The remaining five TxGNN candidates (pharyngitis, allergic urticaria, nasal cavity disease, acute laryngopharyngitis, trigeminal autonomic cephalalgia) have no disease-specific evidence and in some cases run mechanistically counter to a "treatment" relationship.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA (or FDA, given no TW marketing) label warnings/contraindications to complete the S1 safety pre-screen
- Resolve DG002: confirm mechanism-of-action detail via DrugBank API
- If pursuing the headache/migraine angle: formally weigh the 2025/2026 AHS guideline's stance against opioids as first-line ED migraine therapy, and assess misuse/diversion risk
- Given zero existing Taiwan licenses, determine the correct regulatory pathway (new drug application, not label extension) before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


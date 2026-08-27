---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 814
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

> Isoniazid is a first-line antituberculosis agent, most commonly used alone or in isoniazid-rifapentine combination regimens (e.g. 3HP/1HP) for active and latent tuberculosis.
> The TxGNN model predicts it may be effective for **Conjunctivitis**,
> with **1 clinical trial** and **20 publications** currently associated with this direction — though, as detailed below, the supporting evidence is largely indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (active and latent TB infection) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Market Status (Taiwan) | 未上市 (Not currently marketed) |
| Number of NDAs/Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacology, isoniazid inhibits mycolic acid synthesis in the mycobacterial cell wall, an action specific to *Mycobacterium tuberculosis* and related organisms. This mechanism has no established direct pharmacological action on the conjunctiva or on common causes of conjunctivitis (allergic, viral, or bacterial).

The literature association between isoniazid and "conjunctivitis" almost entirely reflects a narrow clinical subgroup: **tuberculous or phlyctenular keratoconjunctivitis**, an ocular manifestation of underlying tuberculosis infection. In these cases, isoniazid improves the conjunctivitis indirectly, by treating the causative TB infection — not by acting on conjunctivitis as a general disease category. Two publications (PMID 14253168, PMID 5103251) do describe isoniazid used specifically for phlyctenular keratoconjunctivitis, but both are historical papers pertaining to TB-associated disease, not general conjunctivitis.

Given this, the TxGNN model's high score (99.36%) most likely reflects the knowledge graph picking up a strong co-occurrence between isoniazid, tuberculosis, and conjunctivitis (as a TB complication), rather than a genuine, generalizable pharmacological effect on conjunctivitis. The one associated clinical trial (NCT04094012) is a Phase 3 safety comparison of latent TB regimens and was not designed to evaluate conjunctivitis outcomes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic adverse drug reaction rates between 3HP (rifapentine+isoniazid weekly ×12) and 1HP regimens for latent TB infection. Not designed to evaluate conjunctivitis efficacy; ocular findings, if any, would only appear as incidental adverse events (relevance grade C — low relevance to this indication). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case Report | Annales d'oculistique | Describes local (topical) use of isoniazid in treatment of ocular tuberculosis. |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Case Report | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Alaskan Eskimos — the most direct isoniazid–conjunctivitis link identified. |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Review of ocular side effects of systemic drugs; conjunctivitis noted as an adverse effect associated with several drug classes (not specific to isoniazid). |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye (conjunctival TB). |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Report | Can J Ophthalmol | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case Report | Oftalmologia | 28 cases of tuberculous/phlyctenular keratoconjunctivitis, mostly in children with primary TB. |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | Case Report | Arch Ophtalmol Rev Gen Ophtalmol | Tuberculosis of the bulbar conjunctiva. |

All identified literature concerns **tuberculous/phlyctenular conjunctivitis** specifically, not conjunctivitis of other etiologies. No RCTs supporting isoniazid for general conjunctivitis were found.

---

## US Market Information

No TFDA/FDA marketing authorization records are currently available — isoniazid is recorded as **未上市 (not marketed)** in this dataset, with 0 licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (data gap DG001, Blocking severity) and must be obtained before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence supports isoniazid's role in treating *tuberculous* conjunctivitis (a TB complication), not conjunctivitis as a general disease category — the TxGNN prediction likely reflects a co-occurrence artifact in the knowledge graph rather than a broad pharmacological effect. No RCT-level evidence and no trial specifically designed to test isoniazid for conjunctivitis exists.
- A Blocking-severity data gap (missing TFDA label/warnings, DG001) also prevents any Stage 1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — DG001
- Detailed mechanism of action data from DrugBank — DG002
- Clarification of target population: should this be re-scoped specifically to *tuberculous/phlyctenular keratoconjunctivitis* rather than conjunctivitis broadly, given the evidence base
- If re-scoped, prospective data comparing isoniazid-treated vs. untreated TB-conjunctivitis outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


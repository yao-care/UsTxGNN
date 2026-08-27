---
layout: default
title: Hydroxyzine
parent: 僅模型預測 (L5)
nav_order: 782
evidence_level: L5
indication_count: 5
---

# Hydroxyzine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Hydroxyzine: From Antihistamine/Antipruritic Use to Allergic Urticaria

## One-Sentence Summary

> Hydroxyzine is a first-generation H1-antihistamine historically used for allergic and pruritic conditions (as reflected in the literature evidence collected here).
> The TxGNN model predicts it may be effective for **Allergic Urticaria**,
> with **1 clinical trial** and **20 publications** currently identified, though most of this literature centers on related second-generation antihistamines (cetirizine, levocetirizine) rather than hydroxyzine directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory license data (drug currently unlicensed in this market); literature in this pack identifies hydroxyzine as a first-generation H1-antihistamine used for allergic/pruritic conditions |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available for hydroxyzine (flagged as a High-severity data gap, DG002). Based on the literature evidence collected, hydroxyzine is a first-generation H1 histamine receptor antagonist; cetirizine, one of its well-known carboxylated metabolites, is explicitly noted in PMID 1981354 and PMID 11034010 as being derived from hydroxyzine.

Allergic urticaria is mediated by mast-cell histamine release causing the classic wheal-and-flare reaction, which is the direct pharmacological target of H1-receptor blockade. Multiple reviews in this evidence set (PMID 31582993, PMID 28913986) explicitly note that hydroxyzine has historically been used alongside diphenhydramine as a first-generation antihistamine option for chronic and allergic urticaria, though current guidelines favor newer, less-sedating second-generation agents as first-line therapy due to a more favorable safety profile.

Mechanistically, the prediction is reasonable and consistent with hydroxyzine's known antihistaminic pharmacology. However, the clinical trial and literature evidence gathered for this specific candidate predominantly involves related but distinct molecules (cetirizine, levocetirizine, bilastine, desloratadine) rather than head-to-head data on hydroxyzine itself in allergic urticaria — this is an indirect, class-based evidentiary link rather than a direct one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter pilot study comparing IV cetirizine injection (10 mg) to IV diphenhydramine (50 mg) for acute urticaria in emergency/urgent-care settings. Note: relevance graded "C" — the tested drug is cetirizine, not hydroxyzine, so this is only an indirect, same-class reference. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position Statement/Review | Allergy Asthma Clin Immunol | CSACI position statement — explicitly names hydroxyzine (with diphenhydramine) as a first-generation antihistamine historically used for urticaria, but recommends newer agents as safer first-line therapy |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria treatment review; notes hydroxyzine (Atarax) and diphenhydramine were historically used at high doses before step-up to omalizumab |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Review of cetirizine, described as a piperazine derivative and carboxylated metabolite of hydroxyzine, in allergic rhinitis and chronic urticaria |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Review of oral antihistamine efficacy/safety for allergic rhinitis and chronic idiopathic urticaria |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case Report | J Clin Gastroenterol | Case of cetirizine-induced cholestasis; notes cetirizine is a human metabolite of hydroxyzine, approved for chronic urticaria |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | Review of H1-antihistamines in children, including allergic conditions |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics/pharmacodynamics of desloratadine, fexofenadine, and levocetirizine in allergic rhinitis and chronic idiopathic urticaria |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine review in allergic rhinitis and urticaria |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Levocetirizine as a treatment option for allergic rhinitis and chronic idiopathic urticaria |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine for allergic rhinitis and chronic idiopathic urticaria in adults and children |

---

## US Market Information

No marketing authorization records are available in this evidence pack — hydroxyzine's regulatory status is recorded as "未上市" (not marketed), with 0 licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not retrievable at the time of this evaluation — flagged as Blocking data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The H1-antagonist mechanism is pharmacologically plausible for allergic urticaria, and hydroxyzine is already referenced in the literature as historically used for this class of condition. However, the specific evidence assembled here (1 low-relevance Phase 3 trial, 20 reviews mostly about other antihistamines) does not directly establish efficacy for hydroxyzine itself in allergic urticaria — it does not yet meet the bar for a Go or even a guarded Proceed decision.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action data from DrugBank (High-priority gap, DG002)
- Direct clinical evidence (trials or studies) evaluating hydroxyzine specifically — not related metabolites — in allergic urticaria
- Drug-drug interaction data, currently unresolved (query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


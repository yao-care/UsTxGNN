---
layout: default
title: Streptomycin
parent: 僅模型預測 (L5)
nav_order: 1182
evidence_level: L5
indication_count: 10
---

# Streptomycin
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

# Streptomycin: From Bacterial Infections (Tuberculosis) to Conjunctivitis

## One-Sentence Summary

> Streptomycin is a first-generation aminoglycoside antibiotic historically used to treat tuberculosis and other bacterial infections, though it is **not currently marketed** in this jurisdiction (0 registered licenses).
> The TxGNN model predicts it may be effective for **Conjunctivitis**, supported by **0 modern clinical trials** and **20 pieces of literature**, most dating from the 1940s–1950s era of early antibiotic use.
> Evidence is largely historical (field trials, case reports); no controlled modern studies exist for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in regulatory data (0 licenses); historically used systemically for tuberculosis and other bacterial infections as a class-defining aminoglycoside |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data (DrugBank MOA field) is not available for streptomycin in this evidence pack. However, the model's own rationale confirms streptomycin's well-established pharmacology: it is an aminoglycoside antibiotic that inhibits bacterial 30S ribosomal protein synthesis, producing bactericidal activity against a range of gram-negative and gram-positive organisms.

Bacterial conjunctivitis can be caused by many of the same pathogen classes streptomycin has historically targeted — including *Haemophilus* species, *Brucella*, *Mycobacterium tuberculosis*, and *Francisella tularensis* (the causative agent of tularemia-associated oculoglandular/Parinaud syndrome). This provides a plausible mechanistic bridge between streptomycin's antibacterial spectrum and the proposed new indication.

That said, streptomycin is **not the modern standard of care** for ophthalmic infection. As the literature itself notes (PMID 3317953), streptomycin was the first aminoglycoside discovered (1943) but has since been clinically superseded in ophthalmology by newer aminoglycosides such as tobramycin and gentamicin, which have better local tolerability and safety profiles. The supporting evidence for streptomycin specifically in conjunctivitis is almost entirely from the 1940s–1950s (field trials in Morocco, experimental *Hemophilus* conjunctivitis studies, TB/Brucella case reports), predating modern trial design and safety standards.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for conjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13075256](https://pubmed.ncbi.nlm.nih.gov/13075256/) | 1953 | Field trial | Rev Int Trachome | Prophylaxis/treatment of seasonal conjunctivitis in rural Morocco via streptomycin and chloramine eye instillations, compared for effect |
| [13075257](https://pubmed.ncbi.nlm.nih.gov/13075257/) | 1953 | Field trial | Rev Int Trachome | Prevention of seasonal conjunctivitis in southern Morocco: streptomycin eye-wash vs. aureomycin salve, comparative effects |
| [18132879](https://pubmed.ncbi.nlm.nih.gov/18132879/) | 1949 | Historical clinical study | Am J Ophthalmol | Streptomycin effective in experimental conjunctivitis caused by *Hemophilus* sp. |
| [15442493](https://pubmed.ncbi.nlm.nih.gov/15442493/) | 1950 | Case report | La Semana Medica | Primary tuberculous conjunctivitis with fistulized submaxillary adenopathy treated with systemic and local streptomycin |
| [6789462](https://pubmed.ncbi.nlm.nih.gov/6789462/) | 1981 | Case report | S Afr Med J | Occupational Brucella keratoconjunctivitis treated with systemic tetracycline/co-trimoxazole/streptomycin plus topical chloramphenicol |
| [5289718](https://pubmed.ncbi.nlm.nih.gov/5289718/) | 1971 | Laboratory study | J Hygiene | Streptomycin (and neomycin) effective at suppressing bacterial contamination during isolation of trachoma (TRIC) agent from conjunctival scrapings |
| [38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/) | 2024 | Case report | Am J Case Rep | *Francisella tularensis* causing Parinaud oculoglandular syndrome (granulomatous conjunctivitis) via conjunctival entry |
| [19584516](https://pubmed.ncbi.nlm.nih.gov/19584516/) | 2009 | Case series/Review | Indian J Med Microbiol | Familial tularaemia cases, including oculoglandular (conjunctivitis) presentation |
| [38298538](https://pubmed.ncbi.nlm.nih.gov/38298538/) | 2023 | Review | Front Microbiol | Review of tularemia treatment (experimental and clinical data); oculoglandular form frequently presents as conjunctivitis |
| [3317953](https://pubmed.ncbi.nlm.nih.gov/3317953/) | 1987 | Review | Surv Ophthalmol | Historical review noting streptomycin as the first aminoglycoside (1943), superseded in ophthalmology by tobramycin/gentamicin |

---

## US Market Information

Streptomycin is **not currently marketed** in this jurisdiction — no NDA/license records are on file (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data for streptomycin were not available in this evidence pack (flagged as a **Blocking** data gap — DG001: TFDA label warnings/contraindications must be obtained before any S1 safety evaluation can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for streptomycin in conjunctivitis is limited to historical field trials and case reports from the 1940s–1950s (Evidence Level L3), with no modern controlled trials. Progression to a formal safety evaluation (S1) is also blocked by a missing TFDA label/warnings dataset (DG001, Blocking severity), and the drug is not currently marketed in this jurisdiction (0 licenses), which limits regulatory pathways for repurposing.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert/label data — warnings, contraindications, DDI (DG001, Blocking)
- Structured mechanism-of-action confirmation from DrugBank (DG002, High)
- Modern comparative safety data given streptomycin's known ototoxicity/nephrotoxicity profile relative to newer aminoglycosides already used ophthalmically (e.g., tobramycin)
- Clarification of a viable regulatory pathway given the drug's current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


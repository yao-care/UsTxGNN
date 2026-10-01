---
layout: default
title: Isoniazid
parent: Model Prediction Only (L5)
nav_order: 814
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a long-established anti-tuberculosis antibiotic. The US label text is not included in the Evidence Pack, so this rests on general drug knowledge.
The TxGNN model predicts it may be effective for **conjunctivitis**, but the support is weak: **1 clinical trial** (not about conjunctivitis) and **20 publications**, mostly case reports on tuberculosis-related eye disease.
The prediction most plausibly applies only to rare mycobacterial (tuberculous or phlyctenular) conjunctivitis, not to conjunctivitis in general.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (general drug knowledge; approved indication text is empty in all listed US licenses) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 (no efficacy studies in conjunctivitis; only case reports and mechanistic plausibility) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 (the five listed are all ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Isoniazid is known to block mycolic acid synthesis in *Mycobacterium tuberculosis* (via InhA), which weakens the bacterial cell wall. This action is specific to mycobacteria.

The plausible link to conjunctivitis is therefore narrow. Tuberculosis can involve the eye, causing tuberculous conjunctivitis and phlyctenular keratoconjunctivitis (an allergic-type reaction to TB antigens). The literature includes reports of these conditions, an older isoniazid prophylaxis study in phlyctenular keratoconjunctivitis (1965), and a report on local isoniazid for ocular TB (1971). Isoniazid has no known activity against the common causes of conjunctivitis (bacterial, viral, allergic).

The very high TxGNN score most likely reflects knowledge-graph proximity to tuberculosis-related eye disease, not a general anti-conjunctivitis effect. Some papers are also confounded. Rifampicin, often given with isoniazid, is the drug associated with ocular and conjunctival irritation, and several papers describe conjunctivitis as a side effect of drugs or of BCG therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compares systemic drug reactions under 3HP (rifapentine + isoniazid, 12 weekly doses) and 1HP regimens for latent TB infection. Conjunctivitis is not a target or endpoint; it offers isoniazid safety data only, not efficacy (relevance grade C). |

---

## Literature Evidence

Titles are reported as classified in the Evidence Pack. Most entries are not classified as RCTs, and none tests isoniazid for conjunctivitis in a controlled design. Entries are ordered by study type, then by relevance to isoniazid.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Ocular side effects of systemic drugs; lists drugs that *cause* conjunctivitis (e.g., isotretinoin, sulfonamides, salicylates), so it is not evidence of benefit |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Review | Annals of Ophthalmology | Review on rifampicin (no abstract available); relevant mainly to rifampicin's ocular effects |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Not classified | American Review of Respiratory Disease | Isoniazid prophylaxis in phlyctenular keratoconjunctivitis among Alaskan Eskimos (no abstract available; the most directly relevant older study) |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Annales d'oculistique | Use of isoniazid in local treatment of ocular tuberculosis (no abstract available) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal TB |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East African J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket after prior miliary TB |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Not classified | Cornea | *M. tuberculosis* presenting as chronic red eye (conjunctival TB) |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Not classified | Canadian J Ophthalmology | Conjunctival phlyctenulosis as a presenting sign of impending clinical TB |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Not classified | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 in children with primary TB; all had positive tuberculin tests |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva (no abstract available) |

---

## US Market Information

The five main authorizations are listed below. The approved indication text is empty in the records provided, so it is not shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040090 | isoniazid | Tablet | Marlex Pharmaceuticals, Inc. |
| ANDA080937 | Isoniazid | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA088235 | Isoniazid | Solution | CMP Pharma, Inc. |
| ANDA080936 | Isoniazid | Tablet | A-S Medication Solutions |
| ANDA040090 | isoniazid | Tablet | REMEDYREPACK INC. |

Dosage forms in the US market include oral tablets, a solution, and an injectable solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no efficacy evidence for isoniazid in conjunctivitis. The only trial is a Phase 3 safety comparison in latent TB, and the literature consists of case reports on TB-related eye disease and papers on drug-induced conjunctivitis. The high TxGNN score is best read as a link to tuberculous ocular disease, and safety data (package insert) is still missing, which blocks screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Narrowing the hypothesis to tuberculous or phlyctenular conjunctivitis, then reviewing whether systemic anti-TB therapy already covers it as standard care
- Full-text review of the 1965 and 1971 isoniazid ocular studies (no abstracts available)
- Route compatibility assessment (a local ocular formulation is not among the listed US dosage forms)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


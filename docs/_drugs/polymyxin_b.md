---
layout: default
title: Polymyxin B
parent: 僅模型預測 (L5)
nav_order: 1062
evidence_level: L5
indication_count: 3
---

# Polymyxin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Polymyxin B: From Antibacterial Therapy to Bacterial Conjunctivitis, Bronchitis, and Laryngotracheitis

## One-Sentence Summary

> Polymyxin B is a polypeptide antibiotic historically used against gram-negative bacterial infections (no original indication record is available in this evidence pack). TxGNN predicts three potential new indications — **bronchitis**, **laryngotracheitis**, and **conjunctivitis**. Of the three, only **bacterial conjunctivitis** is backed by substantial evidence (**3 clinical trials, including multiple Phase 3/4 RCTs**, plus **20 publications**, several of them head-to-head RCTs); the other two candidates currently have weak or no supporting evidence.

---

## Quick Overview

### Primary Candidate: Conjunctivitis (strongest evidence)

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no licenses/indication text on record) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

### All Predicted Indications — Comparison

| Rank | Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|-----------|-------------|-----------------|-----------------|-----------------|
| 1 | Bronchitis | 99.87% | L4 | S1 | Hold |
| 2 | Laryngotracheitis | 99.62% | L5 | S0 | Hold |
| 3 | Conjunctivitis | 99.06% | L1 | S3 | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap). Based on general pharmacological knowledge, Polymyxin B is a cyclic polypeptide antibiotic that binds to lipopolysaccharide (LPS) in the outer membrane of gram-negative bacteria, disrupting membrane permeability and causing bacterial cell death. It is primarily active against gram-negative organisms such as *Pseudomonas aeruginosa* and *Acinetobacter baumannii*.

**Conjunctivitis** is the most mechanistically and clinically coherent candidate: topical Polymyxin B, usually combined with trimethoprim (e.g., Polytrim), is already an established treatment for bacterial conjunctivitis, and this evidence pack effectively documents confirmatory head-to-head trials against moxifloxacin rather than a truly novel indication.

**Bronchitis** evidence is mechanistically plausible (gram-negative tracheobronchitis, e.g., *Pseudomonas*/*Acinetobacter* VAP/VAT) but the literature is dominated by studies using inhaled Polymyxin B as a **bronchoconstriction-provoking diagnostic agent** rather than a therapeutic agent, and includes at least one inhalation toxicity case report — the treatment and adverse-event signals are mixed and inconsistent.

**Laryngotracheitis** has no clinical trial or literature evidence at all — the prediction rests solely on the TxGNN knowledge-graph score, with no way to independently assess plausibility beyond the general antibacterial mechanism.

---

## Clinical Trial Evidence

### Bronchitis
Currently no related clinical trials registered.

### Laryngotracheitis
Currently no related clinical trials registered.

### Conjunctivitis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Head-to-head comparison of Polytrim (polymyxin B/trimethoprim) vs. moxifloxacin ophthalmic solution for pediatric conjunctivitis; both FDA-approved treatments compared for efficacy. |
| [NCT01227863](https://clinicaltrials.gov/study/NCT01227863) | Phase 3 | Unknown | 70 | RCT comparing two dexamethasone+neomycin+polymyxin B combination products (Maxinom® vs Maxitrol®) for acute bacterial conjunctivitis; completion/publication status unconfirmed. |
| [NCT01809483](https://clinicaltrials.gov/study/NCT01809483) | Phase 3 | Completed | 32 | Compared bandage contact lens vs. pressure patching for corneal erosion; polymyxin B likely used as background antibiotic rather than primary intervention — moderate relevance. |

---

## Literature Evidence

### Bronchitis (top 10 of 14 identified)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Cohort/Comparative | Infection | Compared polymyxin B with other antimicrobials for VAP/tracheobronchitis caused by *P. aeruginosa* or *A. baumannii*. |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Case series (salvage therapy) | Diagn Microbiol Infect Dis | Inhaled polymyxin B used as salvage treatment for pneumonia/tracheobronchitis from multidrug-resistant gram-negative bacilli (19 patients). |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case series | J Kansas Med Soc | *Pseudomonas* tracheobronchitis treated with systemic gentamicin plus polymyxin B aerosol. |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Case series (experimental) | Chest | Endobronchial polymyxin B experimental observations in chronic bronchitis. |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Case report (adverse event) | Ann Intern Med | Reports danger/toxicity associated with polymyxin B inhalation — important safety counter-signal. |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Provocation study (non-therapeutic) | Lung | Inhaled polymyxin B used to induce bronchial reactivity in asthma/chronic obstructive bronchitis (diagnostic, not therapeutic use). |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Provocation study (non-therapeutic) | Orvosi Hetilap | Polymyxin B sulfate-induced non-specific bronchial provocation in asthma/chronic bronchitis. |
| [7402949](https://pubmed.ncbi.nlm.nih.gov/7402949/) | 1980 | Provocation study (non-therapeutic) | Pneumonologia Polska | Compared exercise-induced bronchospasm with histamine/polymyxin B provocation testing. |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Mechanism study | Clin Auton Res | Guinea-pig model of polymyxin B-induced eosinophilic bronchitis, used to study cough mechanisms. |
| [11359434](https://pubmed.ncbi.nlm.nih.gov/11359434/) | 2001 | Mechanism study | Clin Exp Allergy | Polymyxin B-induced airway eosinophil accumulation and its effect on bronchial responsiveness in guinea pigs. |

### Laryngotracheitis
Currently no related literature available.

### Conjunctivitis (top 10 of 20 identified, RCTs prioritized)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Moxifloxacin vs. polymyxin B/trimethoprim sulfate in pediatric bacterial conjunctivitis. |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT (multicenter) | J Pediatr Ophthalmol Strabismus | Multicenter comparison of speed of clinical efficacy: polymyxin B/trimethoprim vs. moxifloxacin. |
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT (single-blind) | J Pediatrics | Moxifloxacin vs. polymyxin B-trimethoprim for acute conjunctivitis in children. |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT | J Antimicrob Chemother | Multicentre trial: trimethoprim-polymyxin B vs. neomycin-polymyxin B-gramicidin vs. chloramphenicol for presumptive bacterial conjunctivitis (230 patients). |
| [2540136](https://pubmed.ncbi.nlm.nih.gov/2540136/) | 1989 | RCT (review of 4 studies) | J Antimicrob Chemother | Trimethoprim-polymyxin B vs. chloramphenicol ophthalmic ointment across 4 pooled RCTs (528 patients). |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | RCT (double-blind) | Curr Med Res Opin | Trimethoprim-polymyxin B vs. chloramphenicol ointment; equally effective and well tolerated (42 patients). |
| [2370842](https://pubmed.ncbi.nlm.nih.gov/2370842/) | 1990 | RCT | Med Lett Drugs Ther | Independent evaluation of trimethoprim-polymyxin B for bacterial conjunctivitis. |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | Comparative review of topical ophthalmic antibacterials; notes polymyxin B's selectivity for gram-negative species. |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review/Guidance | J Pediatr Ophthalmol Strabismus | Guidance on controlling contagious bacterial conjunctivitis outbreaks, including antimicrobial selection. |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Cohort/Survey | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution. |

---

## US Market Information

Currently no US market authorization records available (`total_licenses = 0`, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available in this evidence pack (flagged as a **Blocking** data gap — TFDA/label warnings and contraindications — see Next Steps below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — Conjunctivitis only. Hold on Bronchitis and Laryngotracheitis.**

**Rationale:**
- **Conjunctivitis**: Multiple Phase 3/4 RCTs and a substantial RCT literature base (7+ RCTs) directly compare polymyxin B-containing products against established comparators (moxifloxacin, chloramphenicol). This largely confirms an already-recognized use rather than a purely novel prediction, so guardrails (safety/label confirmation) rather than full development are appropriate.
- **Bronchitis**: Evidence is mechanistically plausible but inconsistent — most studies use inhaled polymyxin B as a diagnostic bronchoprovocation agent, not a therapeutic agent, and at least one adverse-event case report raises safety concerns. Insufficient to proceed.
- **Laryngotracheitis**: No clinical trial or literature evidence exists; the prediction is model-score-only (L5). Not actionable at this time.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a **Blocking** data gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) documentation from DrugBank (**High** severity gap — needed for mechanistic-link validation)
- Confirmation of completion/publication status for NCT01227863 (currently "Unknown")
- If pursuing bronchitis further: independent therapeutic (non-provocation) efficacy data and formal safety assessment of inhaled use, given the existing toxicity case report
- No further action recommended for laryngotracheitis unless new clinical or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


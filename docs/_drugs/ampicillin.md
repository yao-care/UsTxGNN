---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum aminopenicillin antibiotic, historically proven effective against a wide range of gram-positive and gram-negative bacterial infections including respiratory tract, urinary tract, and soft tissue infections.
The TxGNN model predicts it may be effective for **Laryngitis**,
with **1 clinical trial** and **20 publications** currently identified — though most evidence is indirect, derived from historical case series of epiglottitis and related bacterial upper airway infections rather than controlled trials specifically evaluating ampicillin for laryngitis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in regulatory database (broad-spectrum antibiotic for bacterial infections) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | 0 licenses found in database search |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack. Based on established pharmacology, ampicillin is an aminopenicillin beta-lactam antibiotic that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs), blocking the final cross-linking step of peptidoglycan and causing bacterial lysis. Its spectrum covers many gram-positive organisms (streptococci, enterococci, *Listeria monocytogenes*) and selected gram-negative bacteria including non-resistant *Haemophilus influenzae* and susceptible Enterobacteriaceae.

Historically, bacterial laryngitis — especially acute epiglottitis caused by *Haemophilus influenzae* type b (Hib) — was a major indication for intravenous ampicillin, particularly in children during the 1970s and 1980s. Multiple case series document its successful use in this era. The mechanistic link is biologically sound: ampicillin penetrates respiratory mucosa adequately and achieves inhibitory concentrations against susceptible organisms, making it a reasonable candidate for upper airway bacterial infections in general.

However, the contemporary clinical relevance has been substantially diminished by two major shifts. First, widespread Hib vaccination since the late 1980s has made Hib-epiglottitis rare. Second, the remaining causative organisms for epiglottitis and bacterial laryngitis (non-typeable *H. influenzae*, Group A *Streptococcus*, *S. aureus*) now show high rates of beta-lactamase production. Current infectious disease guidelines favor ceftriaxone or cefotaxime over ampicillin for epiglottitis. The TxGNN score of 99.97% most likely reflects broad statistical co-occurrence between "upper airway bacterial infection" and ampicillin in the knowledge graph — a historical signal — rather than a contemporary clinical efficacy indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of CLAVAMOX® (amoxicillin/clavulanate) pediatric dry syrup in Japanese children with infections including laryngitis, pharyngitis, tonsillitis, bronchitis, and urinary tract infections (otitis media excluded). Not an ampicillin trial; provides only indirect context for beta-lactam safety in pediatric upper airway infections. Relevance grade: C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline Review | CoDAS | AGREE II quality assessment of clinical guidelines for laryngitis and pharyngitis management; highlights methodological gaps in current antibiotic treatment recommendations for these conditions |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Retrospective Observational | Otolaryngol Head Neck Surg | Hospital-level variation in perioperative antibiotic selection for laryngectomy; antibiotic choice significantly associated with rates of surgical site infection and antibiotic-induced complications |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case Report + Narrative Review | Ann Otol Rhinol Laryngol | Novel case of spontaneous laryngeal abscess in uncontrolled diabetes with historical literature review; notes that penicillin-class antibiotics have made spontaneous laryngeal abscesses rare in the modern era |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case Report | Auris Nasus Larynx | Post-bone-marrow-transplant laryngeal actinomycosis in a 14-year-old; treated with penicillin-class therapy (actinomycosis is a classic indication for high-dose penicillin/ampicillin) |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case Report | Auris Nasus Larynx | COVID-19 presenting as acute epiglottitis with extensive necrotic laryngeal lesions; beta-lactam antibiotics used for bacterial superinfection management |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Case Series | Anaesth Intensive Care | 161 children with acute epiglottitis (1975–1984); documents airway management complications and antibiotic treatment; historical context for ampicillin use in pediatric Hib epiglottitis |
| [5314768](https://pubmed.ncbi.nlm.nih.gov/5314768/) | 1971 | Case Series | Br Med J | Early adult epiglottitis case series; penicillin-class antibiotics were standard treatment in the pre-resistance era |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case Series | Ann Emerg Med | Three adult epiglottitis cases; highlights diagnosis by laryngoscopy and antibiotic management; notes risk of acute upper airway obstruction even in adults |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Case Series | West J Med | Nine adults with confirmed acute epiglottitis over 2 years; intubation required in 4; duration of symptoms shorter in intubated patients; penicillin-class antibiotics used in management |
| [1712371](https://pubmed.ncbi.nlm.nih.gov/1712371/) | 1991 | Prospective Cohort | J Clin Gastroenterol | Short-term antibiotic treatment of 19 Whipple's disease patients; 1 patient received ampicillin 2 g/day with clinical response — indirect evidence of ampicillin systemic efficacy in a chronic bacterial condition |

---

## All Predicted Indications Overview

This Evidence Pack contains 10 TxGNN-predicted indications. The table below summarizes all candidates to support prioritization.

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Reason |
|------|---------|-------------|----------------|----------|------------|
| 1 | Laryngitis | 99.97% | L4 | Hold | Historical link (Hib epiglottitis); resistance now limits clinical utility; no direct RCT |
| 2 | Ureaplasma urethritis | 99.36% | L5 | Hold | **Mechanistic contraindication**: Ureaplasma lacks a cell wall; all β-lactams are intrinsically ineffective |
| 3 | Gonococcal urethritis | 99.36% | L2 | Hold | Historical RCT evidence exists (L2), but **obsolete due to resistance** — WHO/CDC guidelines prohibit penicillins for gonorrhea since 1990s |
| 4 | Chronic rhinosinusitis | 99.34% | L3 | Research Question | Indirect β-lactam evidence (amoxicillin-clavulanate studies); β-lactamase prevalence 50–80% limits plain ampicillin |
| 5 | Chronic ethmoidal sinusitis | 99.33% | L3 | Research Question | One direct ampicillin bacteriology study (PMID 9438060); resistance an issue; amoxicillin-clavulanate preferred |
| 6 | Gingivitis | 99.28% | L4 | Research Question | High β-lactamase prevalence in gingival flora (2025 data); no direct ampicillin RCT; drug delivery studies only |
| 7 | Paranasal sinus neoplasm | 99.20% | L5 | Hold | **Category error**: ampicillin has no antitumor mechanism; TxGNN likely capturing infection-tumor co-occurrence |
| 8 | **Bacterial arthritis** | **99.11%** | **L3** | **Proceed with Guardrails** | **Best actionable candidate**: documented efficacy for Lyme arthritis, Listeria arthritis, enterococcal arthritis; Phase 4 RCT (NCT04563325, 180 children, Denmark) supports oral therapy; must select susceptibility-guided cases |
| 9 | Conjunctivitis | 99.04% | L4 | Research Question | Historical use in gonococcal conjunctivitis; topical antibiotics are first-line; no systemic ampicillin RCT |
| 10 | Pericoronitis | 99.04% | L4 | Research Question | High β-lactamase prevalence in pericoronitis flora; modern practice uses amoxicillin ± metronidazole; no ampicillin RCT |

> **Highlight**: Although laryngitis ranks #1 by TxGNN score, **Bacterial Arthritis (rank 8)** carries the strongest actionable recommendation. Ampicillin has well-documented, guideline-supported efficacy for specific bacterial arthritis subtypes (Lyme arthritis, Listeria joint infection, enterococcal arthritis), and a completed Phase 4 RCT supports its route of administration strategy in children.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-specific warnings, contraindications, or drug interaction data were retrievable from the current database query.

---

## Conclusion and Next Steps

### Primary Indication (Laryngitis) — Decision: Hold

**Rationale:**
While ampicillin has a historically plausible mechanistic connection to bacterial laryngitis (particularly Hib epiglottitis), the contemporary evidence is insufficient to support a formal repurposing programme. The TxGNN score of 99.97% represents a historical signal captured by the knowledge graph rather than a current clinical opportunity — modern resistance patterns and the near-elimination of Hib disease have made this association clinically obsolete.

**To proceed, the following is needed:**
- Prospective clinical trials evaluating ampicillin versus current standard-of-care (ceftriaxone, amoxicillin-clavulanate) for bacterial laryngitis or epiglottitis with culture-guided patient selection
- Contemporary resistance surveillance for laryngitis-associated pathogens in the target population
- Clarification of ampicillin regulatory status (the database returned 0 licenses, which may reflect a search limitation rather than true absence from the market)

---

### Most Actionable Candidate (Bacterial Arthritis, Rank 8) — Decision: Proceed with Guardrails

**Rationale:**
Bacterial arthritis is the highest-value repurposing candidate in this pack. Ampicillin has guideline-supported efficacy for specific bacterial arthritis subtypes — Lyme arthritis (100% *B. burgdorferi* susceptibility, IDSA-recommended), *Listeria monocytogenes* arthritis, and enterococcal arthritis — and a completed Phase 4 nationwide RCT in Denmark (NCT04563325, N=180) validates an oral-first antibiotic strategy for bone and joint infections in children.

**To proceed, the following is needed:**
- Culture and sensitivity testing to confirm ampicillin-susceptible pathogens before treatment
- Exclusion of gonococcal arthritis (ampicillin no longer effective due to resistance) and MRSA (intrinsically resistant)
- Confirmed drug regulatory status and access pathway for the intended treatment setting
- Pharmacovigilance plan for monitoring response and treatment failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


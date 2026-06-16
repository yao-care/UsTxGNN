---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 3
---

# Clotrimazole
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

# Clotrimazole: From Fungal Infections to Vulvovaginitis

## One-Sentence Summary

Clotrimazole is a broad-spectrum azole antifungal globally established for treating candidal infections—including vulvovaginal candidiasis, tinea pedis, and oropharyngeal candidiasis—but currently holds no marketing authorization in Taiwan.

The TxGNN model generated three predicted indications: **Vulvovaginitis** (score 99.59%), **Acne** (score 99.86%, highest TxGNN rank), and **Postmenopausal Atrophic Vaginitis** (score 99.46%); clinical evidence concentrates overwhelmingly on vulvovaginitis, supported by **multiple completed Phase 3 RCTs** and **20 publications**.

Evidence levels differ markedly across predictions—**L1 with "Proceed with Guardrails"** for vulvovaginitis versus **L4/Hold** for acne and **L4/Research Question** for postmenopausal atrophic vaginitis—making vulvovaginitis the only actionable candidate for near-term regulatory pursuit in Taiwan.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally established for fungal infections (tinea pedis, vulvovaginal and oropharyngeal candidiasis) |
| Predicted Indication — Best Evidence | Vulvovaginitis (TxGNN Score **99.59%**) |
| Predicted Indication — Highest TxGNN Rank | Acne (TxGNN Score **99.86%**) |
| Predicted Indication — Third | Postmenopausal Atrophic Vaginitis (TxGNN Score **99.46%**) |
| Evidence Level (Vulvovaginitis) | **L1** |
| Evidence Level (Acne / Postmenopausal Atrophic Vaginitis) | L4 / L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Vulvovaginitis: **Proceed with Guardrails** · Acne: **Hold** · Postmenopausal Atrophic Vaginitis: **Research Question** |

---

## Why is This Prediction Reasonable?

### Vulvovaginitis — The Core Actionable Finding

Although the formal MOA entry is unavailable in this Evidence Pack, published literature (Crowley & Gallagher, *J Appl Microbiology*, 2014) establishes that Clotrimazole is a synthetic imidazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), disrupting ergosterol biosynthesis and compromising fungal membrane integrity. This mechanism directly targets *Candida albicans*, the organism responsible for approximately 85–90% of vulvovaginal candidiasis (VVC) episodes.

Vulvovaginitis due to candidal infection is the most prevalent gynecologic diagnosis in primary care, and Clotrimazole vaginal tablets and creams have served as the global standard of care for over four decades. Local vaginal delivery achieves high mucosal drug concentrations while minimizing systemic exposure—an ideal pharmacokinetic profile for this topical infection. Phase 3 head-to-head comparisons confirm that Clotrimazole vaginal formulations are non-inferior to oral Fluconazole in severe VVC and that single-dose 500 mg administration is equivalent to multi-day 100 mg regimens, providing strong dosing flexibility evidence.

This TxGNN prediction for vulvovaginitis is best described as **confirmatory repurposing**: it validates what global regulators (US FDA, EMA) have recognized since the 1980s. Taiwan's registration gap represents a **market access opportunity** rather than a clinical efficacy question—the evidentiary bar for a Taiwan NDA would be substantially lower than for a novel indication.

### Acne — Mechanistic Mismatch

Acne vulgaris is driven by *Cutibacterium acnes* colonization, sebaceous gland hyperactivity, and follicular inflammation—processes in which fungi play no primary role. The only trial identified (NCT01244256) is a suspended Phase 2/3 study of a triple combination (beclomethasone + gentamicin + clotrimazole) where Clotrimazole most likely serves as a safeguard against antibiotic-induced candidal secondary infection rather than as the therapeutic agent. The TxGNN high score may reflect indirect knowledge-graph paths (e.g., Malassezia folliculitis co-diagnosed with acne), but this cannot be substantiated with current evidence. A "Hold" is appropriate until single-agent mechanistic or clinical data emerge.

### Postmenopausal Atrophic Vaginitis — Indirect Pathway

The core pathology of postmenopausal atrophic vaginitis is estrogen deficiency leading to vaginal epithelial atrophy, pH elevation (>4.5), and lactobacilli depletion—a hormonal mechanism that Clotrimazole cannot address. However, elevated pH and impaired mucosal immunity increase susceptibility to secondary candidal infection, and Clotrimazole may have a valid adjunct role in this context. The TxGNN high score likely reflects graph proximity between VVC, candidal susceptibility in menopause, and Clotrimazole rather than a direct mechanistic link. The single identified trial (NCT04292704) evaluates CO₂ laser therapy, not Clotrimazole. Prospective confirmatory data specifically in postmenopausal women are absent.

---

## Clinical Trial Evidence

### Vulvovaginitis

| Trial | Phase | Status | Enrollment | Key Findings |
|-------|-------|--------|------------|-------------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Completed | 466 | Non-inferiority trial: Clotrimazole 500 mg vaginal ovule vs 500 mg tablet in vaginal candidiasis; confirms formulation equivalence with a large sample |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Completed | 240 | Head-to-head RCT: Clotrimazole vaginal tablet vs oral Fluconazole for severe VVC; directly defines route preference and positions local therapy |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | Recruiting | 264 | International RCT: Clotrimazole + Lactulose combination vs Clotrimazole monotherapy for candidal vulvovaginitis; superiority design, primary endpoint Day 25 response |
| [NCT03562156](https://clinicaltrials.gov/study/NCT03562156) | Phase 3 | Completed | 438 | Double-blind placebo-controlled RCT of oteseconazole for recurrent VVC; highest methodological quality in the RVVC space, establishes the treatment benchmark against which future studies are measured |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Completed | 150 | Active-controlled trial: dequalinium chloride 10 mg vs Clotrimazole 100 mg for VVC; Clotrimazole serves as the gold-standard comparator, confirming its established status |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Completed | 140 | RCT: Clotrimazole vaginal tablets alone vs with adjunct oral Lactobacillus for prevention of recurrent VVC; explores maintenance strategy |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Completed | 1,524 | Effectiveness RCT in West Africa: single-dose tinidazole + fluconazole vs 7-day metronidazole + 3-day vaginal Clotrimazole for vaginal discharge; demonstrates real-world effectiveness of Clotrimazole-containing regimens |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | Completed | 84 | Dose-escalation study of ProF-001 vs Clotrimazole 1% vaginal cream; Clotrimazole as active comparator reinforces its role as the reference standard |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | Completed | 1,033 | Post-marketing safety surveillance of Clotrimazole 1% (Empecid L) vaginal cream under pharmacist guidance; largest safety cohort in the dataset |
| [NCT06480604](https://clinicaltrials.gov/study/NCT06480604) | N/A | Recruiting | 126 | Multi-strain probiotic adjunct for recurrent VVC; Clotrimazole used as standard-of-care background, indirectly confirming its SoC status |

### Acne

| Trial | Phase | Status | Enrollment | Key Findings |
|-------|-------|--------|------------|-------------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Three-component cream (beclomethasone 0.025% + gentamicin 0.1% + Clotrimazole 1%) for contaminated bilateral symmetric dermatosis; trial suspended before completion, individual Clotrimazole contribution cannot be isolated |

### Postmenopausal Atrophic Vaginitis

| Trial | Phase | Status | Enrollment | Key Findings |
|-------|-------|--------|------------|-------------|
| [NCT04292704](https://clinicaltrials.gov/study/NCT04292704) | N/A | Unknown | 205 | Fractional CO₂ laser as consolidation treatment for recurrent VVC; primary intervention is laser therapy, not Clotrimazole; may include postmenopausal women but does not assess antifungal treatment directly |

Currently no clinical trials directly evaluating Clotrimazole for postmenopausal atrophic vaginitis are registered.

---

## Literature Evidence

### Vulvovaginitis

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | RCT | Scientific Reports | Triple-blind RCT (n=126): Mycozin cream vs Clotrimazole 1% cream for vaginal candidiasis; both effective for symptom relief, non-inferiority confirmed |
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complementary Therapies in Medicine | Comparative RCT: Prangos ferulacea vaginal cream vs Clotrimazole cream for VVC; evaluates clinical and microbiological outcomes |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | Randomized trial: probiotics and lactoferrin as maintenance therapy for recurrent VVC; Clotrimazole used as background standard treatment |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | Foundational RCT (n=199): single-dose 500 mg vs 6-day 100 mg Clotrimazole vaginal tablets in three Dutch gynecologic clinics; equivalent efficacy established single-dose convenience dosing |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | Clinical Trial | Obstet Gynecol | Prospective double-blind study (n=42): Clotrimazole 500 mg weekly suppositories induced clinical remission in 90.4% of recurrent VVC patients; established weekly prophylaxis paradigm |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Systematic Review | J Women's Health | Systematic review of boric acid for recurrent VVC; contextualizes growing azole resistance in non-albicans *Candida* spp. and the limitations of Clotrimazole for resistant strains |
| [39362128](https://pubmed.ncbi.nlm.nih.gov/39362128/) | 2024 | Network Meta-analysis | Eur J Obstet Gynecol Reprod Biol | Bayesian network meta-analysis of maintenance pharmacological therapy for recurrent VVC; compares early (24-week) and late (48–52-week) recurrence risk across oral and topical agents including Clotrimazole |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | Mechanistic Study | J Appl Microbiology | Mechanistic investigation: Clotrimazole treatment induces measurable shifts in vaginal bacteriome composition and lipid metabolism, providing insight into recovery dynamics post-VVC |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Appl Microbiology | Comprehensive review of Clotrimazole as a pharmaceutical: mechanism (ergosterol synthesis inhibition via CYP51), clinical applications (tinea, VVC, oropharyngeal candidiasis), and emerging uses |
| [7482105](https://pubmed.ncbi.nlm.nih.gov/7482105/) | 1995 | Clinical Trial | Sex Transm Dis | Head-to-head: oral Fluconazole vs vaginal Clotrimazole for VVC; addresses patient compliance advantages of single oral dosing vs local therapy |

---

## Taiwan Market Information

Clotrimazole currently holds **no marketing authorization in Taiwan** (0 active licenses, 0 NDAs).

Globally, Clotrimazole is widely marketed under brand names including **Canesten** (Bayer), **Empecid**, and **Mycelex**, in formulations that include:
- Vaginal tablets (100 mg, 500 mg)
- Vaginal ovules (500 mg)
- Topical cream (1%, 2%)
- Oral lozenges (10 mg) for oropharyngeal candidiasis

The drug has been approved by the US FDA, EMA, Health Canada, and over 100 other regulatory authorities. A Taiwan TFDA registration application for the vulvovaginitis indication could leverage the extensive existing global data package through an abbreviated bridging strategy, substantially reducing the preclinical and clinical data burden.

---

## Safety Considerations

Detailed TFDA package insert data are currently unavailable for this drug in the Taiwan registry. Based on the global published clinical experience of 40+ years:

- **Drug Interactions**: No drug-drug interaction data were identified in the current Evidence Pack query. Oral systemic azoles (e.g., Fluconazole, Itraconazole) carry CYP450-mediated DDI risks; however, Clotrimazole used topically/vaginally has negligible systemic absorption, substantially reducing this concern.
- For complete contraindications, pregnancy/lactation warnings, and special population guidance, please refer to the current Canesten (Bayer) or equivalent manufacturer's prescribing information.

---

## Conclusion and Next Steps

### Indication 1 — Vulvovaginitis
**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs, a Phase 4 head-to-head trial (Clotrimazole vs. oral Fluconazole, n=240), a 1,033-patient post-marketing safety cohort, and over 20 publications spanning 40 years confirm Clotrimazole as first-line therapy for VVC globally. The Taiwan registration gap is a **market access gap, not an efficacy gap**.

**To proceed, the following is needed:**
- Prepare Taiwan TFDA NDA dossier leveraging existing global CMC, preclinical, and clinical data packages (505(b)(2)-equivalent bridging strategy)
- Obtain and review full package insert from a representative approved market (e.g., EU Canesten SmPC) to complete the TFDA-required prescribing information
- Develop a Taiwan-specific pharmacovigilance plan, including post-market monitoring for azole resistance signals
- Conduct local market access assessment: identify existing antifungal products available in Taiwan, pricing strategy, and HTA positioning

---

### Indication 2 — Acne
**Decision: Hold**

**Rationale:**
The mechanistic connection between Clotrimazole and acne pathogenesis is indirect and unsubstantiated. The single registered trial was suspended and involved a triple-component combination where Clotrimazole's independent contribution cannot be isolated.

**To proceed, the following is needed:**
- Pre-clinical mechanistic studies specifically evaluating Clotrimazole activity against Malassezia species in a folliculitis model
- Prospective single-agent clinical study in patients with microbiologically confirmed Malassezia folliculitis (often clinically misdiagnosed as acne) before any acne-specific claims are made

---

### Indication 3 — Postmenopausal Atrophic Vaginitis
**Decision: Research Question**

**Rationale:**
Clotrimazole addresses secondary candidal infection in postmenopausal women but cannot treat the primary estrogen-deficiency pathology. There are currently no clinical trials or publications directly supporting this indication.

**To proceed, the following is needed:**
- Epidemiological study to characterize the burden and frequency of candidal VVC specifically in Taiwanese postmenopausal women, stratified by HRT use
- Design a prospective pilot study evaluating Clotrimazole as adjunct antifungal therapy in postmenopausal women receiving HRT or vaginal estrogen, targeting a well-defined subpopulation rather than atrophic vaginitis broadly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


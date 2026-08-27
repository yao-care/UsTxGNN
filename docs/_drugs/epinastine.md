---
layout: default
title: Epinastine
parent: 僅模型預測 (L5)
nav_order: 659
evidence_level: L5
indication_count: 2
---

# Epinastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Epinastine (DB00751): Toward Allergic Urticaria

## One-Sentence Summary

Epinastine is a second-generation H1-antihistamine and mast cell stabilizer; the local regulatory record for its original approved indication is not available in this Evidence Pack (no NDA/license on file — drug is currently **not marketed** in this jurisdiction). The TxGNN model's strongest supported prediction is **Allergic Urticaria**, backed by **2 post-marketing clinical studies** and **10 relevant publications** (including RCTs on H1-antihistamine wheal/flare suppression). A second, much weaker prediction — **Rosacea Conjunctivitis** — has no supporting trials or literature and is flagged Hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license record on file); internationally marketed as **Alesion®** (Japan) for allergic rhinitis, eczema/dermatitis, urticaria and pruritus, per clinical-trial documentation in this pack |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| Market Status | Not Marketed (未上市, 0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is not available in this pack (data gap DG002). However, the literature evidence included here documents epinastine's pharmacology directly: it is a potent H1-receptor antagonist that also suppresses antileukotriene, anti-PAF and antibradykinin pathways, and it inhibits mediator release from mast cells and eosinophils (PMID 12845334). This is the standard mechanistic basis for treating histamine-mediated urticaria — H1-receptor blockade plus mast cell stabilization directly targets the wheal-and-flare pathophysiology of allergic urticaria.

Epinastine is already marketed internationally (Alesion®, Japan) with a labeled indication covering urticaria among other atopic conditions, and two large Japanese post-marketing surveillance studies (combined N ≈ 5,800) specifically evaluated its real-world use in patients with urticaria and pruritus. Several controlled comparative studies (e.g., PMID 10442525, 29723372, 19558008) confirm epinastine's histamine-wheal-suppressing potency alongside other approved second-generation antihistamines. This gives the TxGNN prediction a mechanistically direct and clinically corroborated basis, in contrast to the Rosacea Conjunctivitis prediction below, whose underlying pathophysiology (meibomian gland dysfunction, neurogenic inflammation, Demodex-related inflammation) is not primarily histamine-driven and is not supported by any trial or literature evidence in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02238223](https://clinicaltrials.gov/study/NCT02238223) | N/A (PMS) | Completed | 2,001 | Post-marketing surveillance of Alesion® (epinastine) tablets under real-world use, covering allergic rhinitis, asthma, eczema/dermatitis, **urticaria**, pruritus, prurigo and psoriasis vulgaris with itching |
| [NCT02238236](https://clinicaltrials.gov/study/NCT02238236) | N/A (PMS) | Completed | 3,793 | Post-marketing drug-use survey of Alesion® Dry Syrup in Japanese paediatric patients with allergic rhinitis, eczema/dermatitis, **urticaria** and pruritus |

Both trials are observational post-marketing surveillance (real-world safety/use data), not randomized controlled efficacy trials — they establish safety and usage patterns in urticaria populations but are not direct efficacy comparators.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/) | 1999 | RCT | Allergy | Double-blind crossover study: epinastine among six H1-antihistamines suppressing histamine-induced wheal and flare for 24h vs. placebo |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | RCT | An Bras Dermatol | Comparative suppression of histamine wheal/flare by major H1-antihistamines marketed in Brazil, relevant to urticaria/angioedema management |
| [19558008](https://pubmed.ncbi.nlm.nih.gov/19558008/) | 2009 | RCT | Ann Allergy Asthma Immunol | Comparison of first- vs. second-generation antihistamines in suppressing histamine- and allergen-induced skin reactions relevant to mast cell-driven urticaria |
| [12845334](https://pubmed.ncbi.nlm.nih.gov/12845334/) | 2000 | Review | Drugs of Today | Epinastine pharmacology update: H1-antihistaminic, antileukotriene, anti-PAF, antibradykinin activity; inhibits mast cell mediator release |
| [15510239](https://pubmed.ncbi.nlm.nih.gov/15510239/) | 2004 | Review | Drugs of Today | Epinastine hydrochloride reviewed for atopic disease, including allergic conjunctivitis, eczema, rhinitis and urticaria symptom control |
| [11829715](https://pubmed.ncbi.nlm.nih.gov/11829715/) | 2002 | Review | Expert Opin Investig Drugs | Antihistamines in late-phase development for allergic disease, including chronic idiopathic urticaria, driven by shared histamine-mediated mechanisms |
| [34387278](https://pubmed.ncbi.nlm.nih.gov/34387278/) | 2021 | Review | Curr Opin Allergy Clin Immunol | Receptor-affinity profiling of ophthalmic/systemic antihistamine agents including epinastine |
| [10876807](https://pubmed.ncbi.nlm.nih.gov/10876807/) | 2000 | Review | Nihon Yakurigaku Zasshi | Cetirizine pharmacology review citing epinastine as a comparator antihistamine for wheal-response suppression |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Cohort | Methods Find Exp Clin Pharmacol | Large-scale surveillance (n=1,742) of sedative profiles across H1-antihistamines including epinastine |
| [18524543](https://pubmed.ncbi.nlm.nih.gov/18524543/) | 2008 | — | J Dermatol Sci | Regulatory effects of antihistamines on dendritic cell/T-cell responses relevant to urticaria and atopic dermatitis pathogenesis |

---

## US Market Information

No NDA or marketing authorization is currently on file (0 licenses; market status: 未上市 / Not Marketed). Internationally, epinastine is marketed as **Alesion®** (Japan) in tablet and dry syrup formulations for allergic rhinitis, eczema/dermatitis, urticaria and pruritus, per the clinical trial records cited above.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or DDI data are currently on file for this drug — the local safety label has not yet been retrieved, which is a blocking data gap; see below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Allergic Urticaria) — **Hold** (Rosacea Conjunctivitis)

**Rationale:**
- Allergic Urticaria has a mechanistically direct rationale (H1-antagonism/mast cell stabilization), international marketing precedent for urticaria, and L2-level evidence (post-marketing surveillance in ~5,800 patients plus supportive RCTs on antihistamine efficacy), but no local NDA and no drug-specific placebo-controlled urticaria RCT — hence guardrails rather than a clean Go.
- Rosacea Conjunctivitis has no clinical trial or literature support and a mechanistically weak rationale (non-histamine-driven pathophysiology) — Hold, not pursued further at this time.

**To proceed, the following is needed:**
- Local drug label / warnings & contraindications (DG001, **blocking** — required before any S1 safety evaluation can proceed)
- Confirmed DrugBank mechanism-of-action record (DG002)
- A randomized, placebo-controlled trial of epinastine specifically in allergic/chronic urticaria (current evidence is PMS + indirect comparator RCTs, not disease-specific RCTs)
- Regulatory pathway assessment, since the drug currently holds no marketing authorization in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


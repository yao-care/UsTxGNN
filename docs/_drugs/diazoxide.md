---
layout: default
title: Diazoxide
parent: 僅模型預測 (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Alopecia

## One-Sentence Summary

Diazoxide is a KATP channel opener internationally recognized as the first-line treatment for hyperinsulinemic hypoglycemia (congenital hyperinsulinism), though its US regulatory record was not captured in this dataset's data collection.
TxGNN predicts multiple hair-related conditions as potential new indications; **alopecia** (TxGNN rank 4, score 99.91%) is the most evidence-supported actionable prediction, backed by **9 publications** consisting primarily of primate animal studies and narrative reviews.
The top-ranked TxGNN prediction (hypotrichosis simplex of the scalp, rank 1) carries zero supporting evidence (L5/Hold); this report therefore focuses on alopecia as the most viable repurposing candidate, while flagging two additional predictions of clinical note in the conclusion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperinsulinemic hypoglycemia (internationally recognized; not captured in this dataset) |
| Predicted New Indication | Alopecia (TxGNN rank 4; highest-evidence new indication) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (primate animal studies and narrative reviews; no human trials) |
| US Market Status | Not found in dataset |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Diazoxide is a potent opener of ATP-sensitive potassium (KATP) channels. In pancreatic β-cells, KATP channel opening hyperpolarizes the cell membrane and suppresses insulin secretion — the mechanism underlying its established use in hyperinsulinemic hypoglycemia. In hair follicles, KATP channels are expressed in dermal papilla cells and outer root sheath keratinocytes; their opening is believed to extend the anagen (active growth) phase and delay the catagen (regression) phase, thereby promoting hair retention and growth.

This mechanism is precisely the one shared with Minoxidil — the most widely used topical treatment for androgenetic alopecia. Both drugs are peripheral vasodilators that open KATP channels. The strongest evidence for Diazoxide's hair-related activity comes not from a designed clinical trial but from its own side-effect profile: hypertrichosis (excessive hair growth) is a well-documented adverse reaction observed in patients receiving oral Diazoxide for hyperinsulinism, with an incidence of 8.6% in a large Japanese post-marketing surveillance study (n = 384, PMID: 30083030). This constitutes indirect human proof-of-concept that systemic Diazoxide stimulates hair follicle proliferation.

A 1990 primate study (stumptailed macaques, PMID: 2085505) took direct advantage of this hypertrichotic property by applying 5% topical Diazoxide to the bald frontal scalp of adult macaques — the standard androgenetic alopecia model — and confirmed significant hair regrowth. A companion narrative review (PMID: 8326148) described both Minoxidil and Diazoxide as producing significant regrowth in this model. The critical unresolved question is safety: dermal absorption of a topical Diazoxide formulation could trigger systemic hypoglycemia and fluid retention, the same risks that limit its oral use. No human clinical trial has been conducted to test this formulation challenge.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Diazoxide in alopecia or any hair-growth indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Animal Study (primate) | J Dermatol Sci | Topical 5% Diazoxide induced hair regrowth in bald stumptailed macaques; study specifically designed to exploit the drug's known hypertrichotic side effect; monitored for systemic adverse events |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Narrative Review | J Invest Dermatol | Both Minoxidil and Diazoxide produced significant hair regrowth in the macaque androgenetic alopecia model; shared KATP/vasodilatory mechanism discussed; steroid 5α-reductase inhibitor comparison included |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Narrative Review | Drug Safety | Comprehensive review of drug-induced hair effects; Diazoxide listed among agents promoting hair growth via anagen phase prolongation; also catalogues drug-induced effluvium patterns |
| [3214817](https://pubmed.ncbi.nlm.nih.gov/3214817/) | 1988 | Narrative Review | Clin Dermatol | Early review of topical agents for male-pattern baldness; Diazoxide mentioned as a compound with documented hair-growth effects warranting further development |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Case Series | Arch Dis Child | Four neonates born to mothers treated with oral Diazoxide during late pregnancy; provides pharmacokinetic data (placental transfer confirmed) and indirect documentation of systemic hypertrichotic exposure in neonates |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Case Report | Pediatr Dermatol | Infant with generalized hypertrichosis from secondary topical Minoxidil exposure; paper explicitly names Diazoxide as a recognised cause of hypertrichosis alongside phenytoin and Minoxidil, confirming the shared drug-class mechanism |

---

## US Market Information

No US regulatory approvals were captured in this dataset (total NDA count: 0). Based on external knowledge, Diazoxide is marketed internationally as **Proglycem®** (oral capsules/suspension) for hyperinsulinemic hypoglycemia in neonates, infants, and children. A newer formulation, diazoxide choline extended-release tablet (DCCR / Camzyos-class pipeline), has been investigated in Prader-Willi syndrome (PMID: 37919617). The absence of an NDA record in this dataset likely reflects a data collection gap rather than the drug's true regulatory status.

---

## Safety Considerations

Formal package insert warnings and contraindications were not retrieved in this dataset. Based on published clinical literature, the following safety signals are directly relevant to any alopecia repurposing effort:

- **Systemic side effect profile (from hyperinsulinism use)**: Hypertrichosis (8.6%), fluid retention and edema (8.3%), cardiac failure-related events (3.4%), hyperglycemia, and neonatal thrombocytopenia — all documented in a 384-patient Japanese post-marketing surveillance study (PMID: 30083030)
- **Topical absorption risk**: The principal safety hurdle for a Diazoxide-based alopecia product. Dermal absorption of KATP openers is sufficient to cause systemic effects (as demonstrated by secondary Minoxidil exposure causing generalized hypertrichosis in an infant, PMID: 37042338); absorption of Diazoxide could trigger hypoglycemia and cardiac fluid retention
- **Pediatric-specific concern**: Necrotizing enterocolitis has been reported in neonates treated with Diazoxide (PMID: 33483452); this is likely irrelevant to an adult alopecia indication but illustrates the drug's risk profile in sensitive populations

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is biologically coherent — Diazoxide shares KATP channel-opening activity with Minoxidil and produces documented hair growth in a primate model — but the complete absence of human clinical trial data, combined with meaningful systemic safety risks from potential topical absorption, is insufficient to advance without further preclinical formulation work.

**To proceed, the following is needed:**
- **Topical formulation pharmacokinetics**: Measure systemic Diazoxide plasma levels after defined topical application in humans; establish whether a sub-hypoglycemic dose is achievable while retaining follicular efficacy
- **Dose-response in the primate model**: Confirm minimum effective concentration and systemic safety window using the stumptailed macaque model
- **Proof-of-concept pilot study**: Small open-label human study in androgenetic alopecia patients using a controlled-release or low-absorption topical formulation
- **Mechanistic characterization**: Quantify KATP channel subunit expression (Kir6.x / SUR isoforms) in human scalp dermal papilla cells to validate the target tissue biology
- **Minoxidil comparison**: Establish whether Diazoxide offers any efficacy or tolerability advantage to justify development alongside an established standard of care

---

**Prediction Landscape Note — Two Additional Signals Worth Flagging:**

**Rank 10 — Autosomal dominant hyperinsulinism due to Kir6.2 deficiency (Proceed with Guardrails):** This prediction reflects Diazoxide's *actual primary mechanism* — it directly binds the Kir6.2 (KCNJ11) subunit of the KATP channel. Diazoxide is already the international first-line treatment for congenital hyperinsulinism broadly; this specific Kir6.2-mutation subtype should be evaluated for genotype-specific responsiveness, as particular loss-of-function mutations may be especially Diazoxide-sensitive. The zero literature count in this dataset reflects a data collection gap, not a true evidence gap.

**Ranks 5 and 7 — Ambras hypertrichosis and hypertrichosis (disease) (Hold — Caution):** These predictions are **directionally incorrect**. Diazoxide *causes* hypertrichosis as a known side effect; using it to treat a condition of excessive hair growth would worsen the disease. These represent TxGNN false positives arising from co-occurrence statistics rather than therapeutic logic, and should not be pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


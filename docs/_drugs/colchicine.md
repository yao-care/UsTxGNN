---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 547
evidence_level: L5
indication_count: 3
---

# Colchicine
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

# Colchicine: From Gout to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an ancient alkaloid anti-inflammatory agent best known for treating gout and familial Mediterranean fever (FMF).
The TxGNN model's top-ranked prediction (score: 99.60%) identifies **Plasmodium falciparum malaria** as a novel repurposing candidate,
currently supported by **0 clinical trials** and **6 in vitro publications** that provide only indirect mechanistic evidence.
Notably, the second-ranked prediction — **FMF** — carries substantially stronger clinical backing (L1 evidence, guideline-endorsed first-line therapy) and carries a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout; familial Mediterranean fever |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 records returned in query) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, colchicine binds tubulin dimers and inhibits microtubule polymerization. This action disrupts neutrophil chemotaxis and degranulation, and suppresses NLRP3 inflammasome activation with downstream reduction in IL-1β secretion — the basis for its well-documented efficacy in crystal-induced arthropathy (gout) and autoinflammatory diseases such as FMF.

*Plasmodium falciparum* possesses its own tubulin-based cytoskeletal system that is essential for intraerythrocytic replication and cytokinesis. Several in vitro studies from 1984 to 2013 demonstrate that compounds targeting parasite cytoskeletal proteins can inhibit *P. falciparum* growth: tubulozoles disrupted parasite protein synthesis similarly to Colcemid (a structural colchicine analogue), and curcumin was shown to directly disrupt *P. falciparum* microtubule architecture. These findings provide a plausible indirect mechanistic analogy supporting the TxGNN prediction.

However, three critical gaps limit confidence in this prediction: (1) no published study has directly tested colchicine against *P. falciparum*; (2) plasmodial tubulins are structurally distinct from mammalian tubulins, making selectivity unpredictable; and (3) whether colchicine reaches pharmacologically relevant concentrations within infected erythrocytes has never been demonstrated. The mechanistic analogy is intellectually credible but lacks any direct experimental confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Colchicine in Plasmodium falciparum malaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS ONE | Curcumin disrupts *P. falciparum* microtubule structure and inhibits parasite proliferation — directly validates tubulin as an antimalarial drug target |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Tubulozoles suppress *P. falciparum* protein synthesis; Colcemid (colchicine analogue) produces equivalent effects — closest indirect link to colchicine itself |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biol Int Rep | Nine tubulin-binding agents tested against *P. falciparum*; cytoskeletal-targeting drugs show antimalarial activity; parasite tubulins noted to differ from mammalian proteins |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biol Int Rep | Confirms cytoskeletal compounds inhibit intraerythrocytic *P. falciparum* development; tubulozole-T (inactive in mammalian systems) identified as a selective candidate |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Cross-sectional | Clin Exp Immunol | Anti-intermediate-filament antibodies detected in 82% of acute malaria patients — evidence of cytoskeletal involvement in malaria immune pathogenesis |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / Molecular | Mol Cell Biol | pfmdr1 (ABC transporter) expression linked to chloroquine resistance phenotype — contextual background on *P. falciparum* drug resistance mechanisms |

---

## US Market Information

No FDA-approved licenses for Colchicine were returned in this dataset (0 records as of query date 2026-03-24).

> **Important:** Please verify the current status via the [FDA Orange Book](https://www.accessdata.fda.gov/scripts/cder/ob/), as Colchicine (brand names Colcrys® and Mitigare®) is known to hold US approvals for gout flare prevention and familial Mediterranean fever. The 0-record result likely reflects a query limitation rather than true absence of approval.

---

## Safety Considerations

**Key Warnings:** Based on published safety literature (PMID [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/)), colchicine has a **narrow therapeutic index** with no clinically reliable boundary between non-toxic, toxic, and lethal doses. Unintentional toxicity is common and frequently associated with serious or fatal outcomes; clinicians should exercise particular caution when prescribing outside established indications or combining with CYP3A4/P-glycoprotein inhibitors.

Please refer to the package insert for complete contraindications, warnings, and drug-drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns *Plasmodium falciparum* malaria the highest prediction score for colchicine, all available evidence is indirect — derived from in vitro studies of structurally analogous (non-colchicine) microtubule inhibitors on *P. falciparum*, none of which directly tested colchicine. The absence of any clinical trial data and the unresolved questions around parasite tubulin selectivity and erythrocytic pharmacokinetics prevent progression beyond hypothesis at this stage.

**To proceed, the following is needed:**
- Direct in vitro screening of colchicine against *P. falciparum* strains, including chloroquine-resistant isolates
- Pharmacokinetic studies confirming colchicine concentrations within infected erythrocytes reach antimalarial-relevant levels
- Structural bioinformatics analysis comparing plasmodial vs. human tubulin binding sites to assess selectivity potential
- Drug-drug interaction review with frontline antimalarials (artemisinin combination therapies)
- Safety profiling specific to malaria-endemic population demographics and common co-morbidities

---

> **Additional Predictions Summary**
>
> | Rank | Indication | Evidence Level | Recommendation |
> |------|-----------|----------------|---------------|
> | 1 | Plasmodium falciparum malaria | L4 | Hold |
> | **2** | **Familial Mediterranean fever (FMF)** | **L1** | **Proceed with Guardrails** |
> | 3 | Dermatofibrosarcoma protuberans (DFSP) | L5 | Hold |
>
> **FMF (rank 2)** deserves priority attention: multiple Phase 3 RCTs and decades of clinical use have established colchicine as the EULAR/ACR first-line treatment for FMF. The mechanistic fit is direct (tubulin inhibition → neutrophil suppression → NLRP3 inflammasome blockade → ↓IL-1β matches FMF's pyrin-inflammasome pathophysiology), and 1 recruiting clinical trial (NCT06838143) is enrolling colchicine-refractory FMF patients, signaling continued unmet need in this space.
> **DFSP (rank 3)** has no supporting literature and is a Hold with no near-term action recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


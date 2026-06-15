---
layout: default
title: Centella Asiatica
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 3
---

# Centella Asiatica
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

---

# Centella Asiatica: From Traditional Herbal Medicine to Insomnia

## One-Sentence Summary

Centella asiatica (Gotu Kola, 積雪草) is a traditional Ayurvedic and Southeast Asian medicinal herb with a long history of use for wound healing, skin conditions, and neurological support — but it holds no formal drug approval in any regulatory database reviewed.
The TxGNN model predicts it may be effective for **Insomnia**, with **2 clinical trials** and **1 publication** currently supporting this direction.
Evidence remains at the preclinical stage (zebrafish model), and no human trials have targeted insomnia as a primary endpoint.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal regulatory approval (traditional herbal use) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on published preclinical literature, Centella asiatica's primary bioactive compounds — the ursane triterpenoids **asiaticoside**, **asiatic acid**, and **madecassic acid** — are believed to exert central nervous system effects through multiple pathways. Key among these is modulation of GABAergic signalling: asiatic acid has been shown to act as a negative modulator of specific GABA-A receptor subtypes in Xenopus oocyte models (PMID 27062315), while animal studies suggest that the extract may raise brain GABA concentrations by inhibiting GABA-transaminase (GABA-T), the enzyme responsible for GABA degradation.

For insomnia specifically, a 2024 zebrafish larvae study (PMID 38812527) demonstrated that Centella asiatica ethanol extract suppressed hypocretin/orexin activity and downstream p38-MAPK and ERK1/2 signalling — pathways directly linked to the arousal-promoting system. This provides a plausible neurobiological basis: reduced orexin signalling promotes sleep onset and continuity, mirroring the mechanism of approved orexin-receptor antagonists such as suvorexant. Additionally, sleep deprivation-induced anxiety in rodents was attenuated by Centella asiatica extract through nitric oxide modulatory mechanisms (PMID 26848139), further connecting the herb to sleep-anxiety neurobiology.

The key translation gap is the absence of human pharmacokinetic data and any controlled clinical trial specifically targeting insomnia as a primary endpoint. The zebrafish model, while mechanistically informative, differs substantially from human sleep architecture, and the herb's bioavailability and blood-brain barrier penetration in humans remain poorly characterised.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | NA | Active, Not Recruiting | 30 | Brahmi-Gotu Kola oil foot massage (Padabhyanga) vs. sesame oil in perimenopausal women aged 40–55; sleep and mood disturbances are the primary endpoints. Centella asiatica is explicitly named, but delivery is topical/massage — not oral systemic — and it is combined with Brahmi. |
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Completed | 74 | Assessed oral "Inner Calm" supplement and topical "Super Calm" on skin redness, sensitivity, and inner wellness. Insomnia is not a primary endpoint; sleep/calm outcomes are secondary. Centella content in the formulation is unspecified. |

> ⚠️ **Note:** Neither trial was designed with insomnia as a primary endpoint. Relevance to insomnia indication is indirect (Grade B and Grade C respectively). No Phase 1/2/3 human trials targeting insomnia with Centella asiatica monotherapy have been registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Animal Model (In Vivo) | F1000Research | Centella asiatica ethanol extract reduced sleep latency and improved sleep duration in a zebrafish larvae insomnia model by inhibiting orexin, ERK1/2, Akt, and p38-MAPK signalling pathways. First direct mechanistic evidence linking the herb to insomnia neurobiology. |

---

## US Market Information

No drug approvals (NDA or equivalent) for Centella asiatica were found in the regulatory database reviewed. The herb is commercially available in many markets as an unregulated dietary supplement or cosmetic ingredient, but holds no formal pharmaceutical indication in the US.

---

## Safety Considerations

No formal safety data (package insert warnings, contraindications, or drug–drug interactions) was retrieved for Centella asiatica from the databases queried. Please refer to available monograph literature and the manufacturer's documentation for any supplement formulation under consideration.

Key practical cautions from published literature include:
- **Hepatotoxicity risk**: Rare cases of herb-induced liver injury have been reported with Centella asiatica supplements; liver function monitoring is advisable in prolonged use.
- **Anesthesia interactions**: Asiatic acid modulates GABA-A receptors, raising a theoretical interaction risk with anesthetic and sedative agents (PMID 26016167).
- **Pregnancy/lactation**: Safety data are absent; avoidance in pregnancy is generally recommended for herbal CNS-active agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence for Centella asiatica in insomnia is a single zebrafish larvae preclinical study (PMID 38812527); no human clinical trial has tested this herb for insomnia as a primary endpoint. Evidence level L4 is insufficient to justify investment in a formal repurposing programme without first establishing proof-of-concept in humans. The two registered trials are tangentially related and do not address insomnia monotherapy with a characterised Centella extract.

It is worth noting that the **anxiety** indication (TxGNN rank 2, score 99.08%) carries substantially stronger evidence — evidence level L3, with 4 clinical trials including one Phase 2 RCT (NCT03482063, n=141) and one trial with anxiety as an explicit primary endpoint (NCT02462642), plus 20 publications spanning animal models, mechanistic studies, and one small human clinical study in generalised anxiety disorder (PMID 20677602). If a development pathway is being assessed, **anxiety** represents a more evidence-supported entry point than insomnia.

**To proceed with the insomnia indication, the following is needed:**

- **Human PK/PD study**: Establish oral bioavailability of asiaticoside and asiatic acid, and confirm CNS penetration in humans.
- **Validated sleep endpoint study**: A small-scale (n=40–60) randomised, double-blind, placebo-controlled pilot trial using standardised Centella extract (e.g., TECA or CAW) with validated polysomnography or actigraphy endpoints.
- **Standardised extract specification**: Define the active fraction (triterpene content %, extraction method) to ensure reproducibility across studies.
- **Safety package**: Compile a formal safety dossier including hepatotoxicity monitoring protocol, DDI assessment against common sleep medications (benzodiazepines, z-drugs, melatonin agonists), and exclusion criteria for at-risk populations.
- **Regulatory pathway clarification**: Determine whether development as a botanical drug (per FDA Botanical Drug Guidance) or a dietary supplement is appropriate, as this affects the evidence threshold required.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


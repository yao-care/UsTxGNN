---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Amantadine: From Parkinson's Disease / Influenza A to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is a dopamine-enhancing agent and weak NMDA receptor antagonist, historically established for Parkinson's disease management and influenza A antiviral prophylaxis/treatment.
The TxGNN model ranks **Rasmussen Subacute Encephalitis** as the top predicted new indication with a score of 99.48%;
however, **no clinical trials** and **no published literature** currently support this specific repurposing direction, placing this candidate at the hypothesis stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease / Influenza A antiviral prophylaxis (derived from pharmacological context; not listed in current regulatory record) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed (0 registered licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology referenced throughout the evidence materials, amantadine functions primarily as a dopamine releaser/reuptake inhibitor and a weak uncompetitive NMDA receptor antagonist. Its efficacy in Parkinson's disease — particularly for motor symptoms and levodopa-induced dyskinesia — has been well established in clinical practice, and its antiviral mechanism against influenza A formed the basis of its original regulatory approvals.

Rasmussen Encephalitis is a rare, chronic, progressive autoimmune neuroinflammatory disorder affecting one cerebral hemisphere, characterized by refractory focal epilepsy, progressive hemiparesis, and cognitive decline. The TxGNN model's mechanistic rationale proposes two theoretical pathways: (1) NMDA receptor antagonism could attenuate glutamate-mediated excitotoxicity, which drives ongoing neuronal destruction in active neuroinflammation; (2) if a viral trigger underlies disease initiation — a hypothesis in some Rasmussen cases — amantadine's antiviral properties could theoretically be relevant.

Both pathways remain entirely speculative at this stage. Rasmussen Encephalitis is primarily treated with immunotherapy and, ultimately, hemispherectomy. The knowledge graph prediction is likely driven by indirect pathway topology rather than direct biological evidence. No case reports, preclinical studies, or mechanistic publications were identified linking amantadine specifically to this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Status

Amantadine has no registered licenses in the current regulatory database for the evaluated territory (0 active licenses, not marketed).

> **Contextual note:** Amantadine is approved by the US FDA under brand names including Symmetrel (influenza A / Parkinson's), Gocovri (extended-release, Parkinson's dyskinesia), and Osmolex ER. Its absence from the current regulatory record reflects the scope of this particular regulatory dataset, not a global absence of approval.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is at evidence level L5 — the TxGNN model identifies a knowledge graph connection, but no preclinical data, case reports, or clinical trials exist to anchor a development hypothesis for amantadine in Rasmussen Subacute Encephalitis.

**To proceed, the following is needed:**
- Mechanism of action documentation from DrugBank or primary literature (currently a blocking data gap)
- Preclinical studies or case reports examining amantadine or structural analogues (e.g., memantine) in autoimmune encephalitides
- Expert neurologist review of biological plausibility in the context of Rasmussen pathophysiology
- Safety profile retrieval (TFDA package insert or FDA labeling; currently a blocking data gap)

**Alternative recommendation:** Consider prioritizing **myelitis / post-polio syndrome (rank 3, L3)** for near-term evaluation — a double-blind RCT (PMID [7611638](https://pubmed.ncbi.nlm.nih.gov/7611638/)) and a Cochrane systematic review (PMID [25984923](https://pubmed.ncbi.nlm.nih.gov/25984923/)) already exist, and EFNS clinical guidelines reference amantadine for post-polio fatigue. Similarly, **PLA2G6-associated neurodegeneration (rank 4, L4)** has an analogous NBIA case series (PMID [31366412](https://pubmed.ncbi.nlm.nih.gov/31366412/)) offering cross-subtype mechanistic support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


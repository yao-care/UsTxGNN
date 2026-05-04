---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 1
---

# Beclomethasone Dipropionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Beclomethasone Dipropionate: From Asthma / Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Beclomethasone dipropionate (BDP) is a synthetic glucocorticoid corticosteroid with established use in asthma and allergic rhinitis via inhaled and intranasal routes.
The TxGNN model predicts it may be effective for **atopic eczema**, with a prediction score of **99.41%**.
Current evidence includes **no registered clinical trials** but **18 publications** — among them 1 randomized controlled trial from 1984 demonstrating significant benefit in severe pediatric atopic eczema.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma, Allergic Rhinitis (glucocorticoid class; no regulatory license data available) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L2 (1 RCT identified in literature) |
| Market Status | Not Marketed (0 approved licenses on record) |
| Number of Approved Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Beclomethasone dipropionate is a synthetic glucocorticoid that acts as a glucocorticoid receptor (GR) agonist. By suppressing the transcription factors NF-κB and AP-1, it inhibits downstream Th2 cytokines — notably IL-4, IL-13, and IL-31 — while reducing mast cell and eosinophil infiltration into target tissues. This mechanism underlies BDP's well-established efficacy in asthma and allergic rhinitis.

Atopic eczema is fundamentally a Th2-mediated inflammatory disease of the skin barrier. The pathological drivers BDP targets — Th2 cytokine excess, eosinophil recruitment, and mast cell activation — are precisely the same mechanisms central to atopic eczema flares. This is not an indirect connection: the mechanistic overlap is direct and biologically well-grounded. When delivered via oral or intranasal routes, BDP can achieve systemic immunomodulatory effects that extend beyond the reach of topical-only application, which is the biological basis for considering BDP as a repurposing candidate in this indication.

The TxGNN knowledge graph assigns a very high prediction score of 0.994 (99.41%), reflecting strong topological association between the BDP node and the atopic eczema node. This computational signal is reinforced by a double-blind, placebo-controlled RCT (Heddle et al., 1984) in which combined oral plus nasal BDP produced statistically significant improvement in 26 children with severe atopic eczema over 4 weeks. However, this trial is over 40 years old, and no contemporary registered trials have been identified — making this a promising but unvalidated hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | British Medical Journal | Double-blind, placebo-controlled crossover trial in 26 children with severe atopic eczema: combined oral + nasal BDP significantly improved symptoms vs. placebo over 4 weeks; mild HPA suppression noted |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | Clinical Trial | Acta Derm Venereol Suppl | Oral BDP achieved stable disease control in 10/14 children with severe atopic dermatitis (mean dose 1,000 µg/day); linear growth deceleration observed at maintenance doses |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | Formulation Study | AAPS PharmSciTech | BDP mixed micelles incorporated into biocompatible hydrogel for dermal delivery; validated in sub-chronic dermatitis animal model — supports novel delivery strategies |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | Clinical Observational | J Dermatol Treat | Wet-wrap steroid therapy in prepubertal children with atopic eczema monitored for short-term growth and bone turnover; systemic corticosteroid effects quantified |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids (including BDP) and HPA axis suppression: summarises systemic exposure risk and monitoring methods — directly relevant for safety assessment |
| [11488426](https://pubmed.ncbi.nlm.nih.gov/11488426/) | 2001 | Review | Jpn J Pharmacol | BDP and fluticasone confirmed as core inhaled glucocorticoids for allergic disease; contextualises BDP's class-level evidence for Th2-driven conditions |
| [8765824](https://pubmed.ncbi.nlm.nih.gov/8765824/) | 1996 | Experimental | J Allergy Clin Immunol | Topical steroids enhance in vitro spontaneous IgE production in atopic dermatitis patients — important safety signal regarding glucocorticoid use in this indication |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | Experimental | Immunopharmacol Immunotoxicol | Mouse model comparison of BDP vs. mometasone furoate: MF showed greater local anti-inflammatory potency with lower systemic effects than BDP — reference benchmark for drug positioning |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in asthma patients: delayed contact allergy and occasional immediate hypersensitivity documented — safety consideration for topical or systemic BDP use |
| [37023229](https://pubmed.ncbi.nlm.nih.gov/37023229/) | 2023 | Computational | J Chem Inf Model | DrugRep-KG framework validates knowledge graph approaches to drug repurposing; supports the computational basis of the TxGNN BDP–atopic eczema prediction |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Th2-suppressive mechanism of BDP aligns directly with atopic eczema pathology, and an early RCT provides proof-of-concept for oral/nasal BDP in severe paediatric disease. However, this evidence is over 40 years old, no current registered trials exist, key regulatory safety data are unavailable, and the drug holds no approved license in this market — the evidence base is insufficient to justify advancement to a formal repurposing program at this stage.

**To proceed, the following is needed:**
- Retrieve the full package insert (FDA/TFDA) to resolve blocking data gaps on warnings, contraindications, and paediatric safety profile
- Query DrugBank API to confirm and document the formal mechanism of action (resolves DG002)
- Conduct an updated systematic literature search for post-2000 clinical studies evaluating oral, intranasal, or systemic BDP specifically in atopic eczema
- Expand ClinicalTrials.gov search using broader terms (e.g., "beclomethasone dermatitis", "glucocorticoid atopic eczema") to verify absence of ongoing trials
- Evaluate route compatibility in detail: determine whether oral, nasal, or a novel formulation route (e.g., hydrogel micelles per PMID 30911861) is the intended repurposing pathway
- Assess HPA axis suppression and growth safety data before any paediatric use planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


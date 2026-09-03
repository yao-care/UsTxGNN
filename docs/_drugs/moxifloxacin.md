---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 944
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Bubonic Plague (Yersinia pestis)

## One-Sentence Summary

Moxifloxacin is a fourth-generation fluoroquinolone antibiotic; this evidence pack does not include Taiwan/US market or original-indication label data (drug not marketed, MOA field flagged as Data Gap). The TxGNN model generated **10 candidate indications** for this drug, but 9 of them (including the top-ranked "polyclonal hyperviscosity syndrome") have **no clinical trial or literature support** and are flagged by the evidence pack itself as likely knowledge-graph noise. The only candidate with real pharmacological support is **Bubonic Plague**, backed by **6 preclinical/PK-PD publications** but **zero clinical trials**.

> **Note on candidate selection:** Per the standard template, the headline indication would default to the TxGNN top rank (polyclonal hyperviscosity syndrome, score 99.98%). That candidate has no clinical trials, no literature, and an explicit rationale note calling it probable "knowledge-graph neighbor noise." This report instead centers on **Bubonic Plague (rank 10)**, the only candidate with genuine mechanistic and preclinical evidence, so the evaluation is not built on an unsupported signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Taiwan license data; drug not marketed locally) |
| Predicted New Indication | Bubonic Plague (Yersinia pestis infection) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L3 (in vitro/in vivo preclinical pharmacodynamic studies) |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed original mechanism-of-action documentation is not available (`original_moa`: Data Gap), and no Taiwan license/indication data exists because the drug is not marketed locally. However, moxifloxacin's pharmacological class is well established: it is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV, blocking DNA replication and causing bacterial cell death.

For Bubonic Plague specifically, this is not a speculative mechanistic leap. In vitro and in vivo pharmacodynamic studies in the evidence pack confirm moxifloxacin has potent bactericidal activity against *Yersinia pestis*, the causative agent of plague, via the same DNA gyrase/topoisomerase IV inhibition it uses against other susceptible organisms. Mouse models of systemic and pneumonic plague and dedicated in vitro PK/PD dosing-optimization studies both support this activity, and fluoroquinolones as a class (ciprofloxacin, levofloxacin, moxifloxacin) are already recognized options against *Y. pestis*.

By contrast, the other nine candidates surfaced by TxGNN for this drug (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, monoclonal gammopathy, acquired peripheral neuropathy-associated hematological disease, congenital hematological disorder, hematopoietic/lymphoid neoplasm) all carry near-identical TxGNN scores (>99.9%) but no plausible mechanistic link and, for most, zero supporting evidence. Where clinical trials or literature did surface for the hematology-adjacent candidates, they reflect moxifloxacin being used to treat *infections in patients who happen to have those blood diseases* (e.g., neutropenic fever, disseminated nocardiosis) — not treatment of the hematological disease itself. This is consistent with the evidence pack's own assessment that these are likely graph-proximity noise rather than genuine repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | In vitro PK/PD model | Antimicrobial Agents and Chemotherapy | Derived a moxifloxacin dosing regimen that optimizes killing of *Y. pestis* and prevents emergence of resistance |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | In vitro PK/PD model | Antimicrobial Agents and Chemotherapy | Compared moxifloxacin against other candidate antibiotics for *Y. pestis* in an in vitro pharmacodynamic model |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | In vivo/experimental animal | Antibiotiki i khimioterapiia | Moxifloxacin and other fluoroquinolones showed high efficacy (ED50 5.5–14.0 mg/kg) against FI+/FI- *Y. pestis* strains in mice |
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | In vivo/experimental animal | International Journal of Antimicrobial Agents | Moxifloxacin offered full protection in a mouse model of systemic and pneumonic plague, comparable to ciprofloxacin |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case report (adverse event) | Therapeutic Advances in Drug Safety | Case of moxifloxacin-induced tinnitus; notes FDA-recommended use of fluoroquinolones for plague among other indications |
| [26210091](https://pubmed.ncbi.nlm.nih.gov/26210091/) | 2015 | Case report | Ticks and Tick-borne Diseases | Case of *Francisella tularensis* (tularemia, not plague) infection in China — tangential relevance only |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the evidence pack flags this as a **blocking data gap** — TFDA warnings/contraindications and DDI data were not retrievable, which prevents a formal S1 safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bubonic Plague is supported by credible, mechanistically consistent preclinical evidence (in vitro PK/PD and animal models), but there are no human clinical trials, no market presence for this drug in the target region, and a blocking safety data gap (no TFDA/label warnings, contraindications, or DDI data available). The other nine TxGNN-predicted indications lack any credible mechanistic rationale or supporting evidence and should be deprioritized.

**To proceed, the following is needed:**
- Resolve blocking Data Gap DG001: obtain TFDA/official package insert (warnings, contraindications) before any S1 safety review
- Resolve High-severity Data Gap DG002: confirm formal MOA and original approved indications from DrugBank/label source
- If pursuing the plague indication: identify a regulatory pathway appropriate for a rare/biodefense indication (human efficacy data is inherently limited for this disease) and evaluate compassionate-use/expanded-access precedent
- Deprioritize or formally close out the remaining nine candidate indications given the absence of mechanistic plausibility or evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 883
evidence_level: L5
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Magnesium Hydroxide: From No Approved Indication (Unmarketed) to Active Peptic Ulcer Disease

## One-Sentence Summary

> Magnesium hydroxide has no approved indication currently on file in this evidence pack — the drug is not marketed and holds zero licenses.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **0 clinical trials** and **20 publications** currently supporting this direction, including two classic RCTs from the 1980s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is unmarketed, no license records available |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug entry (data gap DG002). No approved original indication or license record is on file either — the compound is not marketed and its regulatory history is undocumented in this evidence pack.

That said, the literature evidence collected for this prediction is internally consistent and mechanistically coherent: magnesium hydroxide is the classic antacid component in combination products such as Maalox and Mylanta. Its predicted mechanism — neutralizing secreted gastric acid, raising intragastric pH, and promoting endogenous prostaglandin/EGF-mediated mucosal protection — is a well-established pharmacological pathway for antacid therapy in active peptic ulcer disease, one that has been used clinically for decades.

Because the drug is grouped in the literature almost exclusively as part of aluminum-magnesium hydroxide antacid combinations, the predicted indication aligns closely with real-world, long-standing clinical use of this drug class, even though a formal MOA record and original indication text are not present in this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial: antacid/anticholinergic vs cimetidine vs placebo in 72 patients with active duodenal/prepyloric ulcers; antacid regimen significantly outperformed placebo in healing rate |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | RCT | Clin Gastroenterol | Review/trial data on antacids and anticholinergics in duodenal ulcer treatment |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT (H2RA comparator, not direct Mg evidence) | Clin Pharmacol Ther | 8-week multicenter RCT of nizatidine vs placebo in benign gastric ulcer; relevant as comparator-class evidence for acid-suppressive ulcer healing |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | Updates cellular/molecular mechanisms of gastric cytoprotection and ulcer healing by antacids beyond prostaglandins |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Animal study | Scand J Gastroenterol | Al(OH)3/Mg(OH)2 antacid prevented gastric lesions in rats dose-dependently via endogenous prostanoid pathways |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro/product evaluation | Med Pharm Rep | Evaluated acid-neutralizing capacity of marketed antacids, supporting pharmacodynamic basis of Mg(OH)2-containing products |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Clinical (retrospective) | Drugs Exp Clin Res | Retrospective study of 267 paediatric patients with peptic symptoms, evaluating efficacy of various pharmacological agents including antacids |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Clinical review | Fortschritte der Medizin | Reviews antacid neutralizing capacity and dosing strategy for adequate acid suppression in peptic ulcer disease |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical (comparative) | J Clin Gastroenterol | Compared postprandial buffering duration of sodium bicarbonate vs aluminum-magnesium hydroxide (Maalox) in duodenal ulcer patients |
| [31111054](https://pubmed.ncbi.nlm.nih.gov/31111054/) | 2019 | Animal study | BioMed Res Int | Hydrotalcite (Mg/Al-based) prevention/healing effects on NSAID-induced gastric injury in rats via EGF/PGE2 pathway |

---

## US Market Information

No license records are available — magnesium hydroxide is currently unmarketed in this jurisdiction (0 NDAs on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L2, anchored by two 1980s RCTs directly testing antacid regimens in active peptic ulcer healing, plus a broad base of supporting mechanistic and comparative studies. However, no clinical trials specifically target this indication, and the drug's own regulatory/MOA record is incomplete, so guardrails are warranted before advancing.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) package insert warnings and contraindications — currently a **blocking** data gap (DG001) preventing safety-stage (S1) evaluation
- Confirmed mechanism of action from DrugBank or another authoritative source (DG002)
- Original approved indication and licensing history, since none is currently on file for this drug
- A registered clinical trial specifically evaluating magnesium hydroxide (or its combination products) in active peptic ulcer disease to upgrade evidence beyond historical RCTs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


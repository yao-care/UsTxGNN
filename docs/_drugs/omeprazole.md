---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 993
evidence_level: L5
indication_count: 2
---

# Omeprazole
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

# Omeprazole: From Acid-Related GI Disorders to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI) generally used for acid-suppression therapy in gastrointestinal disorders; the evidence pack does not contain a documented original indication or license record for this specific candidate. The TxGNN model predicts it may be effective for **Duodenogastric Reflux (DGR)**, with **1 clinical trial** and **20 publications** currently identified, though the evidence is preliminary and includes an important animal-model safety signal that needs to be resolved before further development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no license/indication records; drug-level MOA also marked as a data gap) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 (Observational studies / small cohort studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism of action data is not available for this candidate. However, the evidence pack's repurposing analysis characterizes omeprazole as a PPI that inhibits gastric parietal cell H⁺/K⁺-ATPase, thereby reducing gastric acid secretion.

Duodenogastric reflux is fundamentally a motility problem involving reflux of bile and pancreatic secretions into the stomach — it is not primarily an acid-related pathology. The rationale for omeprazole's potential relevance is indirect: gastric acidity modulates the toxicity of refluxed bile acids (bile acids tend to be more mucosa-damaging in an acidic environment), so acid suppression could theoretically reduce mucosal injury from DGR even though it does not correct the underlying reflux mechanism itself.

Importantly, several animal studies in the evidence pack (PMID 10389684, 8943968, 15052437, 33027361) suggest that long-term acid blockade combined with DGR may **potentiate** gastric mucosal growth stimulation and carcinogenesis in rodent models. This is a significant countervailing signal that must be weighed against any therapeutic rationale and should be treated as a priority safety question rather than a supporting mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Evaluated endoscopic tri-modal imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from reflux disease (acid or bile). **Relevance Grade C** — this is a diagnostic imaging study, not a trial of omeprazole's efficacy in DGR; only indirectly related via the reflux-disease patient population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Cohort/small clinical study | Gut | Omeprazole 20 mg BID reduced duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus patients |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Cohort/small clinical study | Scand J Gastroenterol | Omeprazole's effect on antral duodenogastric reflux in Barrett oesophagus; suggests DGR may be reduced by omeprazole |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study | J Pediatr Gastroenterol Nutr | Prospective study of PPI therapy for oesophageal bile reflux in children |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Clinical study | Am J Gastroenterol | Compared duodenogastroesophageal reflux (DGER) severity between GERD patients responding vs. failing once-daily PPI therapy |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Clinical study | Gastroenterology | Examined relationship between pH, duodenogastroesophageal reflux, and bile acid concentration in causing esophageal damage |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Clinical study | J Gastrointest Surg | Bile reflux measurement in Barrett's esophagus; effect of medical acid suppression vs. Nissen fundoplication |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal experiment | Acta Cir Bras | Investigated whether omeprazole has a protective or promoting effect on gastric adenocarcinoma in rats with induced DGR |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal experiment | Dig Dis Sci | **Safety signal**: gastric acid blockade with omeprazole promoted gastric carcinogenesis induced by DGR in rats |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal experiment | Dig Dis Sci | **Safety signal**: DGR-induced foregut mucosal growth stimulation was potentiated by omeprazole-induced acid blockade |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal experiment | Gastric Cancer | **Safety signal**: PPI class drug (lansoprazole) promoted gastric carcinogenesis in rats with DGR, same class concern as omeprazole |

---

## US Market Information

No license or NDA records are present in the evidence pack for this candidate (`total_licenses: 0`, market status: **未上市 / Not Marketed**). No product-level dosage form or approved-indication information is available.

---

## Safety Considerations

Please refer to the package insert for safety information. The evidence pack contains no drug interaction records (DDI query: not found) and no documented warnings or contraindications for this candidate.

**Note:** Independent of the formal safety dataset, multiple animal studies identified in the literature evidence above (PMID 10389684, 8943968, 15052437, 33027361) raise a mechanistic concern that chronic acid suppression combined with DGR may promote gastric mucosal proliferation/carcinogenesis in rodent models. This signal has not been confirmed in humans but should be explicitly evaluated before any further development.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- TFDA warning/contraindication data (DG001) is marked as a **Blocking** gap, meaning the candidate cannot enter the S1 safety pre-assessment stage.
- The strongest supporting evidence (Duodenogastric Reflux) is rated **L3** with a decision stage of only **S1 / Research Question** — the earliest actionable stage — and is based on small cohort studies rather than controlled trials.
- The second predicted indication (Duodenal Obstruction) is weaker still (**L4**, decision stage S0, recommendation **Hold**), reflecting a largely mechanistic/indirect rationale (H. pylori eradication, not omeprazole, drives most reported benefit).
- Multiple animal studies suggest a potential carcinogenesis-promoting signal when acid suppression is combined with DGR, which is a material safety consideration rather than a supporting rationale.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (resolve DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank (resolve DG002)
- Human RCT-level evidence specifically evaluating omeprazole's clinical benefit in DGR (current evidence is limited to small cohort studies)
- A targeted risk assessment of the gastric carcinogenesis signal seen in rodent models before considering any chronic-use development pathway
- Clarification of regulatory/market status for this specific candidate (currently no license records)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Hyoscyamine
parent: 僅模型預測 (L5)
nav_order: 783
evidence_level: L5
indication_count: 1
---

# Hyoscyamine
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

# Hyoscyamine: From GI Antispasmodic Use to Gastroduodenitis

## One-Sentence Summary

Hyoscyamine is a muscarinic (M1–M3) anticholinergic, pharmacologically used to reduce GI smooth muscle spasm and glandular secretion (e.g., IBS, intestinal colic, pre-endoscopy premedication); it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Gastroduodenitis**, but this is currently supported by **0 clinical trials** and only **1 tangential publication**, and the evidence pack's own mechanistic review flags this as a likely graph-topology artifact rather than a true therapeutic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Taiwan (no TFDA license); known pharmacological use is symptomatic control of GI smooth muscle spasm and secretion |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no supporting trials) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Hyoscyamine is a muscarinic acetylcholine receptor (M1–M3) antagonist. Clinically it is used to reduce GI smooth muscle spasm and glandular secretion — for example in IBS, intestinal colic, and as premedication before endoscopy. Its action is purely symptomatic (antispasmodic/antisecretory) and does not include any anti-inflammatory or disease-modifying mechanism.

Gastroduodenitis, by contrast, is an inflammatory condition of the stomach and duodenum, commonly caused by *H. pylori* infection or NSAID-induced mucosal injury, and its treatment requires eradication therapy or mucosal protection, not smooth-muscle relaxation.

Because of this mismatch, the mechanistic rationale in the evidence pack itself concludes that hyoscyamine has no plausible disease-modifying mechanism for gastroduodenitis. The high TxGNN score (99.59%) most likely reflects topological similarity between "anticholinergic drug – GI symptom – GI disease" nodes in the knowledge graph, rather than a genuine therapeutic relationship. This is a case of a symptom modulator being confused with a disease-modifying agent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review | Endoscopy | Reviews international variation in IV sedation practice for endoscopy/colonoscopy (e.g., propofol use, informed consent); does not directly address hyoscyamine efficacy in gastroduodenitis |

## US Market Information

Hyoscyamine currently holds no license in Taiwan (market status: not marketed, 0 NDAs on record).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with zero clinical trials and a single, mechanistically unrelated publication. The evidence pack's own mechanistic analysis identifies a likely symptom-modulator-vs-disease-modifying mismatch, and a Blocking data gap on TFDA warnings/contraindications (DG001) prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — currently prevents S1 safety review)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Disease-specific preclinical or clinical evidence for gastroduodenitis beyond the single tangential review article
- Drug interaction (DDI) data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 1163
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

> Simvastatin is a well-established HMG-CoA reductase inhibitor (statin) used to lower LDL cholesterol.
> The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**,
> with **19 clinical trials** and **18 publications** currently supporting this direction.
> Notably, the underlying evidence itself indicates this is largely an already-established, guideline-recognized use of statins rather than a truly novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally captured in this jurisdiction's regulatory data (drug currently not marketed here); globally, simvastatin is an HMG-CoA reductase inhibitor approved for hypercholesterolemia/dyslipidemia |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available in this evidence pack (flagged as a data gap). Based on the mechanistic rationale captured alongside the prediction, simvastatin inhibits HMG-CoA reductase, reducing hepatic cholesterol synthesis and upregulating LDL receptor expression — the core pharmacological basis for treating familial hypercholesterolemia (FH).

FH is a genetic disorder of LDL receptor function (or related pathways) that causes markedly elevated LDL-C from birth. Because statins act directly on the LDL-receptor pathway, they are already the pharmacological backbone of FH management in current clinical guidelines — this is not really a "new" indication being uncovered, but rather a core, textbook use of the statin drug class.

The evidence pack's own rationale is explicit about this: *"此為 statin 藥理學核心適應症而非真正新用途"* — i.e., this is a core statin indication rather than a genuine repurposing signal. The high TxGNN score therefore likely reflects the model correctly recovering a strong, well-known drug–disease relationship in the knowledge graph, rather than identifying a novel off-label opportunity. This distinction matters for how the "new indication" label should be interpreted downstream.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: direct comparison of ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | RCT of alirocumab added on top of stable statin therapy in heFH/high-CV-risk patients not controlled by lipid-modifying therapy |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Placebo-controlled RCT of alirocumab in heFH patients inadequately controlled on background lipid-modifying therapy (incl. statins) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | RCT of alirocumab vs. placebo in children/adolescents with heFH on stable statin background therapy |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab in children/adolescents with homozygous FH on background treatment |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Efficacy/safety of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | RCT of ezetimibe + simvastatin vs. simvastatin alone in adolescents (10–17 y) with heFH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Post-marketing re-examination survey of VYTORIN (ezetimibe/simvastatin) safety and efficacy in routine practice |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Open-label comparison of renal effects of rosuvastatin vs. simvastatin in Fredrickson Type IIa/IIb dyslipidemia, including heFH |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2341 | Long-term safety/tolerability RCT of alirocumab in high-CV-risk hypercholesterolemia patients on background lipid-modifying therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane, Tier 1) | Cochrane Database Syst Rev | Systematic review of statins (including simvastatin) for children with FH |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline (Tier 1) | Circulation | 2026 ACC/AHA dyslipidemia management guideline, replacing the 2018 cholesterol guideline |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial: simvastatin with or without ezetimibe in FH, assessing atherosclerosis progression |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Outcomes Study | Journal of the American College of Cardiology | Statin treatment reduces coronary artery disease events and mortality in heterozygous FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review (Tier 2) | Expert Opinion on Drug Safety | Benefits and long-term safety/tolerability assessment of simvastatin in FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort (Tier 2) | Journal of Clinical Medicine | Simvastatin treatment and cellular immunity parameters in children with FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin specifically in FH patients |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | Cohort | International Angiology | Long-term efficacy/safety of ezetimibe/simvastatin combination in FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Study | Nutrition, Metabolism and Cardiovascular Diseases | Atorvastatin vs. simvastatin for LDL-C goal attainment in heterozygous FH |
| [1346327](https://pubmed.ncbi.nlm.nih.gov/1346327/) | 1992 | Observational | Lancet | Early report on simvastatin's effect on lipoprotein(a) |

---

## US Market Information

Simvastatin is currently **not marketed** in this jurisdiction — no NDA/license records are on file (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warnings, contraindications, and drug–drug interaction data for this jurisdiction are currently unavailable and have not yet been retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs, a Cochrane systematic review, and inclusion in the 2026 ACC/AHA dyslipidemia guideline (L1-level evidence) support statin therapy — including simvastatin — as standard-of-care for FH. However, this is best understood as confirming an already-established core use of the statin class rather than a novel repurposing opportunity, and the drug is not currently marketed in this jurisdiction, with the local safety label (warnings/contraindications) still an unresolved **blocking** data gap.

**To proceed, the following is needed:**
- Obtain the TFDA-equivalent package insert (warnings, contraindications) — currently a blocking gap for any safety review
- Obtain structured mechanism-of-action data via DrugBank API (currently a data gap)
- Confirm local regulatory/import pathway status, since the drug is presently unmarketed here
- Clarify internally that this "prediction" reflects an established clinical use rather than a genuine off-label repurposing signal, to avoid overstating novelty in downstream communications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


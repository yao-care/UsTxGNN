---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 1076
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Pravastatin is an HMG-CoA reductase inhibitor (statin) whose established use is lowering LDL cholesterol in hypercholesterolemia.
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
> with **1 clinical trial** and **13 publications** currently associated with this direction — though most of this evidence addresses adjunct or comparator therapies rather than pravastatin monotherapy directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia (inferred from drug class — HMG-CoA reductase inhibitor; not explicitly recorded in evidence pack) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pravastatin belongs to the statin (HMG-CoA reductase inhibitor) class, its efficacy in lowering LDL-cholesterol in hypercholesterolemia is well established, and mechanistically this places it in the same pharmacological family evaluated for HoFH.

However, the evidence pack itself flags an important caveat: HoFH patients typically have absent or severely dysfunctional LDL receptors, which limits pravastatin's LDL-lowering effect in this population. Clinically, HoFH management usually requires add-on therapies such as PCSK9 inhibitors or LDL apheresis rather than statin monotherapy. The one clinical trial captured for this indication (NCT03510715) evaluated alirocumab, not pravastatin, in pediatric HoFH patients — it demonstrates that background statin therapy (including pravastatin) is standard-of-care in this population, but does not directly test pravastatin's efficacy as a new HoFH treatment. The prediction is therefore mechanistically plausible as part of a combination regimen, but direct supporting evidence for pravastatin monotherapy in HoFH is currently weak.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab added to background lipid-lowering therapy (which may include statins such as pravastatin) in children/adolescents with HoFH; assessed LDL-C reduction at 12/24/48 weeks. Relevance grade C — supports statins as background therapy but does not directly test pravastatin efficacy in HoFH. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | Phase 4 RCT | Lancet HIV | Head-to-head comparison of pitavastatin vs pravastatin in dyslipidemia; supports pravastatin's clinical LDL-lowering profile and CYP-independent metabolism. |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Statins, including pravastatin, are efficacious and generally safe in children with familial hypercholesterolemia. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidemia management guideline referencing statin use across FH severity spectrum. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Comparative review noting pravastatin's lipid-lowering potency relative to other statins. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Discusses statin management of hyperlipidemia including homozygous familial hypercholesterolemia. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Mechanistic/Preclinical | Stem Cell Res Ther | iPSC-derived hepatocyte model of LDL-receptor-deficient FH, supporting disease mechanism relevant to statin response limits. |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Review of statin-class efficacy/safety in primary hypercholesterolemia and mixed dyslipidemia. |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Reviews combination lipid-lowering therapy context relevant to statin-refractory hypercholesterolemia (as seen in HoFH). |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology/therapeutic review of statin-class agents in hyperlipidaemia management. |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Case Report | Iran Biomed J | Genetic case study identifying LDLRAP1 variant causing familial hypercholesterolemia — relevant to underlying disease mechanism. |

---

## US Market Information

Pravastatin is currently **Not Marketed** in this jurisdiction's dataset, with **0 NDAs** recorded in the evidence pack. No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pravastatin's role as background statin therapy in HoFH is well supported by trial context, but the sole trial captured evaluates a PCSK9 inhibitor (alirocumab) rather than pravastatin itself, and literature directly testing pravastatin monotherapy in HoFH is limited (Evidence Level L2, relevance grade C). The prediction is biologically plausible but requires additional direct evidence before advancing further.

**To proceed, the following is needed:**
- Resolve blocking data gap: TFDA/FDA package insert warnings and contraindications (DG001)
- Resolve high-priority data gap: confirmed mechanism of action data via DrugBank (DG002)
- Direct clinical evidence on pravastatin efficacy specifically in HoFH patients (most current evidence is on adjunct/comparator agents)
- Clarification on positioning: pravastatin as background/combination therapy vs. standalone HoFH treatment, given typical LDL-receptor deficiency in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


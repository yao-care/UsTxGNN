---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
---

# Arginine
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

# Arginine: From Amino Acid Supplement to Gastroparesis

## One-Sentence Summary

L-Arginine is a conditionally essential amino acid serving as the direct precursor to nitric oxide (NO), clinically used in urea cycle disorders and as a nutritional supplement.
The TxGNN model predicts it may be effective for **Gastroparesis**, grounded in its role as the obligate substrate for neuronal nitric oxide synthase (nNOS) — the enzyme driving inhibitory motor neurotransmission throughout the gastrointestinal tract.
Current evidence includes **1 clinical trial** (Grade C relevance, not directly applicable) and **10 publications** (all animal/mechanistic studies), placing this solidly at the preclinical hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urea cycle disorders; nitric oxide precursor supplementation |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 NDAs on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

L-Arginine is the sole substrate for all three isoforms of nitric oxide synthase (NOS), including neuronal NOS (nNOS/NOS1), which is the dominant inhibitory neurotransmitter effector in the enteric nervous system. In the stomach and pylorus, nitrergic neurons release NO to drive smooth muscle relaxation — enabling pyloric opening, gastric accommodation, and coordinated antral peristalsis. Gastroparesis, regardless of etiology (diabetic, post-surgical, or idiopathic), consistently features loss of interstitial cells of Cajal (ICC) and impaired nitrergic transmission as central pathological features.

The causal link between arginine availability and gastroparesis is unusually direct: oral dexamethasone administration in mice depletes circulating L-arginine and produces a full gastroparesis phenotype, which is abrogated in GR(dim) mutant mice (PMID 25057793). Separately, multiple diabetic and Parkinsonian animal models show downregulated nNOS in gastric and pyloric tissue concurrent with delayed emptying (PMIDs 18312542, 35380456). Tetrahydrobiopterin (BH4), the essential NOS cofactor, shares the same downstream pathway — its deficiency also produces gastroparesis in neonatal mice (PMID 23639814), further validating NO synthesis as the nodal mechanism.

Supplementing L-arginine could, in principle, restore substrate availability to residual nNOS-expressing neurons, increase NO production, and rehabilitate pyloric relaxation and gastric accommodation. This is a coherent and testable hypothesis. The critical limitation is that it remains entirely unvalidated in humans: no clinical trial has examined arginine's effect on gastric emptying in gastroparesis patients, and the route-bioavailability question is non-trivial given that oral absorption may itself be impaired by delayed gastric emptying.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Unknown | 150 | Autologous islet cell transplantation after pancreatectomy for glycaemic control — arginine appears only as a stimulation test agent, not as a therapeutic intervention for gastroparesis |

> **Note:** The sole retrieved trial (NCT01702051) carries **Grade C relevance** (nearly unrelated). Its primary objective is islet transplantation, not gastroparesis treatment. No directly relevant clinical trials are currently registered for arginine in gastroparesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal Study | Endocrinology | **Most relevant**: Glucocorticoid-induced L-arginine depletion directly causes gastroparesis in mice; effect abolished in GR(dim) mutants — establishes arginine deficit as a mechanistic cause |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal Study | Am J Physiol Gastrointest Liver Physiol | Impaired nNOS-mediated nitrergic relaxation in pyloric sphincter of 6-OHDA Parkinson's disease rat — confirms nNOS/NO as direct gastroparesis target |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal Study | Neurogastroenterol Motil | Reduced nNOS expression in diabetic BB-rat jejunum — supports nNOS deficiency as contributor to diabetic gastroparesis |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal Study | Am J Physiol Gastrointest Liver Physiol | BH4 deficiency (NOS cofactor) induces gastroparesis in newborn mice — reinforces centrality of NO synthesis pathway |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal Study | Am J Physiol Gastrointest Liver Physiol | Synchronized gastric electrical stimulation rescues vagotomy-impaired gastric accommodation via nitrergic pathway in dogs |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal Study | Am J Physiol Gastrointest Liver Physiol | Sacral nerve stimulation improves gastric accommodation via spinal afferent/vagal efferent pathway — contextual motility mechanism |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal Study | World J Gastroenterol | Ghrelin and GHRP-6 restore gastric motor function in diabetic mice with gastroparesis |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal Study | Am J Physiol Gastrointest Liver Physiol | Hyperglycemia-induced gastric inhibition mediated by nodose ganglia KATP channels — contextual vagal mechanism |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case Report | Am J Case Rep | Lifestyle normalization of lactate in MELAS patient — arginine supplementation mentioned in mitochondrial disease context; peripheral relevance only |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal Study | Gastroenterology | Food protein anaphylaxis causes delayed gastric emptying in rats — mechanistic context for gastroparesis mediators |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is scientifically coherent and grounded in a causal animal model — L-arginine depletion has been directly shown to produce gastroparesis, and restoring arginine could rehabilitate nNOS-mediated gastric motility. However, all supporting evidence is preclinical (L4), no human trial data exists, and full safety and regulatory data are currently unavailable, making clinical advancement premature without further groundwork.

**To proceed, the following is needed:**

- **Human proof-of-concept study**: A Phase 1/2 trial assessing oral or IV L-arginine supplementation in gastroparesis patients (glucocorticoid-induced or diabetic subtypes are mechanistically best matched) with gastric emptying scintigraphy as primary endpoint
- **Plasma arginine measurement**: Confirm that gastroparesis patients exhibit lower circulating arginine levels compared to controls — this would directly validate the substrate-depletion hypothesis in humans
- **Formulation strategy**: Address the bioavailability paradox — oral absorption may itself be delayed in gastroparesis; IV or jejunal administration routes may need evaluation
- **MOA documentation**: Formal review of full arginine pharmacology (complete Data Gap DG002 via DrugBank API) to capture NOS isoform selectivity and off-target effects
- **Safety and contraindication review**: Obtain full warning and contraindication data (Data Gap DG001) before any clinical planning, particularly for renal insufficiency and arginine's known effects on insulin secretion and potassium levels
- **Regulatory pathway scoping**: Evaluate whether arginine-for-gastroparesis would require a new NDA or could proceed under existing supplement frameworks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


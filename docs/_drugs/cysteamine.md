---
layout: default
title: Cysteamine
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 10
---

# Cysteamine
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

# Cysteamine: From Nephropathic Cystinosis to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Cysteamine is a thiol-containing cystine-depleting compound, established internationally as first-line therapy for nephropathic cystinosis — a rare lysosomal amino acid transport disorder — though it currently holds no registered market authorization in this region.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nephropathic cystinosis (not registered in this market; internationally established use) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological context, cysteamine is a thiol-containing compound whose primary mechanism involves entering lysosomes and forming mixed disulfides with cystine. The resulting cysteamine–cysteine mixed disulfide exits the lysosome via the intact PQLC2 (lysine) transporter, bypassing the defective cystinosin transporter in cystinosis patients. Beyond this on-target cystine-depleting mechanism, cysteamine also possesses broader antioxidant properties through its free sulfhydryl (–SH) group, enabling it to scavenge reactive oxygen species (ROS) and participate in cellular redox reactions.

The theoretical basis for benefit in mitochondrial OXPHOS disorders lies in this antioxidant capacity. Mitochondrial OXPHOS disorders caused by nuclear DNA mutations (affecting genes encoding Complex I–V subunits or assembly factors) result in dysfunctional electron transport chain activity, generating excessive ROS and oxidative stress as a downstream consequence. Cysteamine's thiol group could theoretically reduce this oxidative burden on mitochondria, analogous to the rationale for using coenzyme Q10, idebenone, or MitoQ in mitochondrial disease management. The TxGNN knowledge graph likely captures the shared pathophysiological feature of organellar oxidative stress across lysosomal storage diseases and mitochondrial disorders, producing this network-proximity prediction.

However, this connection is highly speculative. Unlike cystinosis — where cysteamine acts via a direct, chemically defined, on-target mechanism to deplete lysosomal cystine — its proposed role in mitochondrial OXPHOS disorder is indirect, non-specific, and entirely unvalidated in human or animal studies. No clinical trial or preclinical publication specifically addresses this indication. The TxGNN prediction almost certainly reflects knowledge graph proximity between lysosomal storage diseases and mitochondrial disorders, rather than a true, actionable therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction is currently supported only by the model's knowledge graph inference (L5), with zero clinical trials and zero published literature specifically addressing cysteamine in mitochondrial oxidative phosphorylation disorders caused by nuclear DNA anomalies. The mechanistic link is indirect, non-specific, and entirely theoretical at this stage.

**To proceed, the following is needed:**
- Preclinical evidence (cell lines or animal models relevant to nuclear DNA-encoded OXPHOS disorders) demonstrating that cysteamine meaningfully reduces mitochondrial ROS or restores respiratory chain function
- Comparative mechanistic assessment of cysteamine's antioxidant potency against established mitochondrial antioxidants (CoQ10, idebenone, MitoQ) in relevant models
- Full MOA characterization from DrugBank or equivalent authoritative source (currently absent from this evidence pack)
- Toxicity and tolerability data in the target population (typically pediatric patients with severe multisystem disease)
- Regulatory pathway consultation, given the absence of any current regional market authorization and the ultra-rare disease context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


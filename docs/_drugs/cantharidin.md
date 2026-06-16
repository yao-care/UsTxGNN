---
layout: default
title: Cantharidin
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 1
---

# Cantharidin
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Cantharidin: From Traditional Chinese Medicine to Amenorrhea

## One-Sentence Summary

Cantharidin is a naturally occurring vesicant toxin derived from blister beetles (*Mylabris* spp.), historically classified as 斑蝥 in traditional Chinese medicine and studied for its cytotoxic and PP2A-inhibitory properties, but currently without any approved modern indication in the United States.
The TxGNN model predicts it may be effective for **Amenorrhea**, likely driven by ethnopharmacological associations in the knowledge graph.
However, with **0 clinical trials** and **0 publications** directly supporting this direction, the evidence base is entirely model-driven at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication (traditional/experimental use only) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no approved indication or detailed mechanism of action data is available in the evidence pack. Based on known pharmacological information, cantharidin is a potent protein phosphatase 2A (PP2A) inhibitor and the active vesicant constituent of *Mylabris* spp. (blister beetles). It has documented cytotoxic and anti-proliferative activity, and has been explored in preclinical cancer research. In traditional Chinese medicine, 斑蝥 has historically been used as an emmenagogue — a substance intended to stimulate or restore menstruation — which provides a plausible ethnopharmacological rationale for why the TxGNN knowledge graph links cantharidin to amenorrhea.

The TxGNN score of 0.994 likely reflects this traditional-use pathway and indirect biomolecular associations encoded in the training graph rather than a direct mechanistic chain. No established modern pharmacological mechanism connects PP2A inhibition to hypothalamic–pituitary–ovarian axis regulation or endometrial cycle control. This association should therefore be regarded as **highly speculative** pending any primary biomedical investigation.

It is also important to note that cantharidin carries a very narrow therapeutic window and significant systemic toxicity risk (nephrotoxicity, vesication, GI toxicity), which poses substantial safety barriers to clinical translation in a chronic condition such as amenorrhea.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Cantharidin is a potent cytotoxic natural compound (PP2A inhibitor); the following assessment is based on known compound pharmacology.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — natural toxin (terpenoid vesicant), PP2A inhibitor class |
| Myelosuppression Risk | Please refer to primary toxicology literature; systemic myelotoxicity has been reported in poisoning cases |
| Emetogenicity Classification | Please refer to primary toxicology literature; GI toxicity (nausea, vomiting, mucosal irritation) is a known systemic effect |
| Monitoring Items | Renal function (nephrotoxicity is a primary concern), hepatic function, CBC, urinalysis |
| Handling Protection | Must follow cytotoxic/vesicant handling regulations; cantharidin causes severe skin and mucous membrane blistering on contact |

---

## Safety Considerations

No US package insert data is available, as cantharidin has no approved indications and is not marketed in the United States. Cantharidin is a scheduled toxic substance with a well-documented narrow therapeutic window and vesicant properties. Please consult primary toxicology resources and institutional safety protocols before any handling or research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high score (99.42%) for amenorrhea most likely reflects traditional Chinese medicine ethnopharmacological signal in the knowledge graph rather than a validated modern mechanistic link; with zero supporting clinical trials or peer-reviewed publications, this candidate sits at L5 — model prediction only — and carries a significant unresolved toxicity profile that makes clinical translation premature.

**To proceed, the following is needed:**
- Mechanism of action clarification: establish whether PP2A inhibition has any plausible role in menstrual cycle or ovarian hormonal regulation
- Preclinical in vitro / in vivo efficacy studies specifically targeting amenorrhea models
- Dose–response and safety characterisation at sub-vesicant systemic exposures
- Formal DrugBank safety data retrieval (warnings, contraindications, DDI profile) to complete the S1 safety gate
- TFDA prescribing information review if any historical local data exists
- At minimum one Phase 1 clinical study establishing a safe dose range before any efficacy claim can be evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


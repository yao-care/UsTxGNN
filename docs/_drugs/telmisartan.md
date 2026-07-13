---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB) widely used for the management of hypertension and reduction of cardiovascular risk in high-risk patients.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina),
however **no clinical trials** and **no publications** currently support this specific direction — the prediction rests entirely on computational modeling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / cardiovascular risk reduction |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, telmisartan is an ARB that selectively antagonizes the angiotensin II type 1 receptor (AT1R), thereby inhibiting angiotensin II-mediated vasoconstriction, aldosterone secretion, and vascular smooth muscle proliferation. Uniquely among ARBs, telmisartan also acts as a partial PPARγ (peroxisome proliferator-activated receptor gamma) agonist, conferring pleiotropic anti-inflammatory and metabolic benefits beyond blood pressure reduction — a profile sometimes described as "metabosartan."

Prinzmetal angina (variant or vasospastic angina) is characterized by episodic coronary artery spasm causing transient myocardial ischemia, typically occurring at rest and often in the absence of significant fixed atherosclerotic stenosis. The theoretical mechanistic link is that AT1R blockade could attenuate angiotensin II-induced coronary vasoconstriction, while PPARγ activation may provide additional endothelial protective and anti-inflammatory effects that modulate vascular reactivity and smooth muscle tone.

However, this mechanistic connection is highly speculative. Prinzmetal angina is primarily driven by calcium-channel-dependent smooth muscle hyperreactivity rather than by RAS overactivation, and first-line treatments are calcium channel blockers and nitrates — not antihypertensives. There is no clinical trial or published peer-reviewed study demonstrating telmisartan's efficacy or safety specifically in Prinzmetal angina. The high TxGNN score (99.98%) reflects structural proximity within the knowledge graph, not clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert warnings, contraindications, and drug interaction data are all currently unavailable (flagged as a Blocking-severity data gap). Full safety profiling cannot be completed until this information is retrieved from the TFDA website.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, translational, or preclinical evidence specifically supporting telmisartan for Prinzmetal angina, and the mechanistic rationale — while theoretically arguable — is indirect and highly speculative relative to established vasospasm pathophysiology.

**To proceed, the following is needed:**
- Retrieve TFDA package insert (Blocking data gap) to establish a safety baseline before any further evaluation
- Obtain MOA data from DrugBank (High-severity gap) to formally characterize the AT1R/PPARγ mechanism and assess plausibility
- Conduct a class-effect literature review of ARBs in vasospastic angina to determine whether any precedent exists within the drug class
- Commission preclinical studies evaluating AT1R blockade in established coronary vasospasm models (e.g., ergonovine-induced spasm models) before any clinical exploration
- Review potential drug-drug interactions with standard Prinzmetal co-medications (calcium channel blockers, nitrates, statins)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


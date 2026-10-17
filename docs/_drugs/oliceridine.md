---
layout: default
title: Oliceridine
parent: Model Prediction Only (L5)
nav_order: 987
evidence_level: L5
indication_count: 4
monitor_inn: "OLICERIDINE"
predicted_indications: ["insomnia (disease)", "migraine disorder", "irritable bowel syndrome", "neurocirculatory asthenia"]
last_modified_at: 2026-10-14
description: "Oliceridine: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the data compiled for this report"
---

# Oliceridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Oliceridine: From Acute Pain Management to Insomnia

## One-Sentence Summary

Oliceridine is a G protein-biased mu-opioid receptor agonist given by injection, and it was developed for acute pain. The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is therefore based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the US license record has no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, oliceridine is a G protein-biased mu-opioid receptor agonist, and its use is in acute pain. Opioids can cause sedation, so a link to sleep is conceivable.

That link is weak. Opioids generally disrupt sleep architecture by reducing slow-wave and REM sleep. They also carry risks of tolerance, dependence, and respiratory depression. The high score (0.998) is a knowledge-graph prediction only. No clinical or mechanistic evidence supports it, and the link cannot be verified. The product's US market status is also "cancelled only".

**Other predicted indications (all L5, Hold):**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Migraine disorder | 99.16% | Opioids are sometimes used as rescue therapy, but guidelines generally discourage them because of medication-overuse headache, limited efficacy, and dependence risk. Any advantage of a biased agonist is speculative. |
| 3 | Irritable bowel syndrome | 99.07% | Some class-level plausibility exists, since eluxadoline, a mixed opioid receptor modulator, is approved for IBS-D. However, oliceridine is a systemic IV agent, and opioid-induced constipation and GI dysfunction argue against its use. |
| 4 | Neurocirculatory asthenia | 99.05% | This is a poorly defined functional or anxiety-related condition with no established opioid therapy and no supported mechanistic pathway. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210730 (cancelled) | OLINVYK (Trevena, Inc.) | Injection, solution | Not stated in the available data |

## Safety Considerations

**Drug Interactions:** The interaction check returned 100 interacting drugs. The first 20 returned include the following.

- **Major:** alvimopan, bupropion, aprepitant, morphine, dexamethasone, lorcaserin, clarithromycin, dolasetron, eliglustat
- **Moderate:** famotidine, hyoscyamine, loperamide, atropine, bisacodyl, glycopyrronium, cimetidine, picosulfuric acid, polyethylene glycol (3350 with electrolytes), dicyclomine, dronabinol

Interactions with other opioids (morphine) and with CYP-affecting drugs (clarithromycin, bupropion) deserve particular attention. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions rest on model scores alone, with no registered trials and no publications. The mechanistic rationale is weak or contradicted for each one, for example opioid disruption of sleep and opioid-induced GI dysfunction. The only US license is cancelled, and the safety and mechanism data are incomplete.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical or observational evidence linking biased mu-opioid agonism to the predicted indication
- Review of the cancelled status of NDA210730 and its implications for supply
- An assessment of whether an IV-only product can fit chronic or outpatient conditions such as insomnia, migraine, and IBS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


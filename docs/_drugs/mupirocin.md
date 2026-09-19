---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 945
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mupirocin: From Topical Antimicrobial Therapy to Pleural Empyema

## One-Line Summary

Mupirocin currently lacks formal approved indication data for Taiwan/USA; based on its mechanism of action, it can only be inferred to be used for **topical nasal/dermal antimicrobial therapy** (such as nasal MRSA decolonization, impetigo). The TxGNN model predicts it may be effective for **Pleural Empyema**, but **currently lacks any clinical trial or literature evidence support**. Moreover, the evidence package itself indicates that the mechanistic plausibility of this connection is weak, potentially resulting from knowledge graph topological bias.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original indications | No formal approved indication data (this drug is Not marketed in this region); inferred based on mechanism of action to be topical nasal/dermal antimicrobial (nasal MRSA decolonization, impetigo), **not confirmed by formal sources** |
| Predicted new indications | Pleural Empyema |
| TxGNN prediction score | 99.49% |
| Evidence level | L5 (model prediction only, no clinical trials or literature) |
| Market status | Not marketed |
| Number of approved cases | 0 |
| Recommended decision | Hold |

---

## Why is the Plausibility of This Prediction Questionable?

Mupirocin's formal mechanism of action data is currently missing (original_moa marked as Data Gap). However, based on the mechanistic inference provided in the evidence package, mupirocin is a topical antibiotic whose mechanism of action is inhibition of bacterial isoleucyl-tRNA synthetase. Its **clinical formulations are limited to topical nasal/dermal application**, with no systemic or intrapleural formulations and pharmacokinetic data.

Pleural empyema is typically caused by anaerobic bacteria or mixed streptococcal infection, requiring **systemic antibiotic therapy combined with drainage** to achieve effective control. Given mupirocin's known topical formulation characteristics, there is no evidence that it can penetrate the pleural space and achieve bactericidal concentrations, therefore the connection between the original (inferred) use and this predicted indication **lacks reasonable mechanistic linkage**. The evidence package assessment concludes that the high score assigned by TxGNN likely reflects topological similarity bias between the drug node and other antibiotic/infection-related nodes in the knowledge graph, rather than true pharmacological plausibility. This assessment also applies to the second-ranked prediction (punctate epithelial keratoconjunctivitis)—this disease is typically caused by viral or immune-related etiology, mupirocin lacks antiviral activity, and no approved ocular formulation exists.

---

## Clinical Trial Evidence

Currently no related clinical trial registrations.

(Query records: ClinicalTrials.gov and ICTRP queries for MUPIROCIN + pleural empyema on 2026-04-21 returned 0 results.)

---

## Literature Evidence

Currently no related literature data.

(Query records: PubMed query for MUPIROCIN + pleural empyema on 2026-04-21 returned 0 results.)

---

## Market Information

This drug is **Not marketed** in this region, with no approved cases (total_licenses = 0), therefore no licensing/formulation/indication data are available.

---

## Safety Considerations

Safety data are currently missing. Please refer to the product label for complete safety information.

**Note**: TFDA label warnings and contraindication data are missing and have been identified as **Blocking** level data gaps (DG001). Cannot proceed to S1 safety screening until this is completed.

---

## Conclusion and Recommendations

**Decision: Hold**

**Rationale:**
- Evidence level is only L5 (pure model prediction with no clinical trials or literature support)
- The evidence package's own mechanistic analysis indicates that mupirocin's topical formulation lacks reasonable mechanistic connection with the systemic treatment required for pleural empyema; the prediction score likely originates from knowledge graph topological bias rather than pharmacological plausibility
- This drug is Not marketed with no approved cases; fundamental safety and formulation data are insufficient

**Data/actions to be completed:**
- Obtain TFDA label warnings and contraindication data (DG001, Blocking, requires downloading and analyzing product label PDF)
- Confirm formally approved indications and mechanism of action (DG002, via DrugBank API query)
- Assess formulation/route of administration compatibility: confirm whether mupirocin exists in a systemic formulation capable of reaching the pleural space
- After completing the aforementioned data, re-evaluate whether it is necessary to proceed to S1 safety initial assessment

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


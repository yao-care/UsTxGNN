---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 599
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan: From Antitussive to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a widely used over-the-counter cough suppressant that acts on the medullary cough center, commonly found in cold and flu preparations worldwide.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **1 Phase 3 clinical trial** identified in the evidence search — though that trial targets Major Depressive Disorder rather than nasal cavity disease directly — and **no published literature** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antitussive (cough suppression) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (1 Phase 3 trial identified; note: trial targets MDD, not nasal cavity disease directly) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Approvals | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack. Based on established pharmacological knowledge, DXM is a low-affinity NMDA receptor antagonist and sigma-1 receptor agonist acting at the medullary cough center. It suppresses the cough reflex centrally, which is why it has been used as a first-line antitussive for decades.

The connection to nasal cavity disease is mechanistically coherent: nasal conditions such as allergic rhinitis and chronic sinusitis frequently drive **postnasal drip-induced cough** and airway hypersensitivity. DXM's suppression of the cough reflex arc directly addresses one of the most bothersome downstream symptoms of nasal cavity disease. Additionally, sigma-1 receptor agonism may inhibit release of neurogenic pro-inflammatory mediators (such as substance P and CGRP) at upper airway mucosal nerve terminals, offering a secondary anti-neuroinflammatory effect.

In this sense, the TxGNN prediction is not a radical leap — nasal cavity disease and antitussive therapy share overlapping pathophysiology. However, it is important to distinguish between treating a symptom of nasal disease (cough) and treating the nasal cavity disease itself. Whether DXM provides benefit beyond cough relief — for example, reducing mucosal inflammation, improving nasal patency, or altering disease course — remains unproven and requires direct clinical investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomized, double-blind, placebo-controlled trial evaluating DXM + bupropion sustained-release tablets in Chinese adult patients with **Major Depressive Disorder**. ⚠️ This trial targets MDD, not nasal cavity disease — the match was based on DXM as the active agent, not the disease indication. Results not yet available (expected completion: December 2026). |

> **⚠️ Evidence Caveat:** The single identified trial (NCT06958692) investigates a DXM/bupropion combination for Major Depressive Disorder. It does not directly assess nasal cavity disease. The evidence level L2 designation reflects the trial's Phase 3 design quality, but the **clinical relevance to nasal cavity disease is indirect at best**. No trials directly studying DXM for nasal cavity disease were found.

---

## Literature Evidence

Currently no related literature available for Dextromethorphan × Nasal Cavity Disease.

---

## Taiwan Market Information

Dextromethorphan currently has **no approved products** registered with the Taiwan FDA (TFDA). No license data is available.

> Note: DXM is widely approved internationally as an OTC antitussive (e.g., in the US, EU, Japan, and many other markets). The absence of a Taiwan registration does not reflect global regulatory status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable for this evidence pack. Given that DXM is known to interact with MAO inhibitors, serotonergic agents, and CYP2D6 substrates, a thorough safety review is essential before any clinical development proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for DXM in nasal cavity disease is plausible — its antitussive mechanism directly addresses a primary symptom of nasal conditions — but no direct clinical evidence exists, and the single Phase 3 trial identified targets MDD rather than any nasal indication. The TxGNN score is high (99.98%), suggesting strong graph-based structural similarity, but this likely reflects the shared upper respiratory disease topology in the knowledge graph rather than direct pharmacological validation.

**To proceed, the following is needed:**

- **Targeted clinical trial search**: Re-query ClinicalTrials.gov and ICTRP specifically for DXM in rhinitis, sinusitis, or postnasal drip with broader search terms (e.g., "dextromethorphan rhinitis," "DXM postnasal drip")
- **Literature gap closure**: Conduct a systematic PubMed/Embase search for DXM in nasal or upper airway conditions; the current search returned zero results and may have used overly narrow MeSH terms
- **MOA documentation**: Retrieve full DrugBank MOA entry (DG002 remediation) to support mechanistic write-up
- **Safety profile review**: Download Taiwan package insert or FDA label (DG001 remediation) to assess contraindications and DDI risks — particularly MAO inhibitor interaction and serotonin syndrome risk
- **Proof-of-concept study design**: If the above searches confirm no prior nasal cavity disease data, a small-scale PoC study (e.g., DXM vs. placebo in postnasal drip-associated cough secondary to chronic rhinitis) would be an appropriate next step before committing to a full Phase 2 design
- **Taiwan regulatory pathway**: Since DXM is not marketed in Taiwan, a full regulatory strategy (IND + NDA) would be required, adding timeline and cost considerations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


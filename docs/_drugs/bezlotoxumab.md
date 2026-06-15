---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Bezlotoxumab: From C. difficile Infection Recurrence Prevention to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab (brand name: Zinplava) is a fully human monoclonal antibody that neutralizes *Clostridium difficile* toxin B, clinically used to prevent CDI recurrence in high-risk adults receiving antibacterial therapy.
The TxGNN model predicts it may be effective for **Acute Female Pelvic Peritonitis**, but with **0 clinical trials** and **0 publications** supporting this direction, and an extremely weak mechanistic rationale, this prediction is most likely a knowledge graph false positive rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of *Clostridium difficile* Infection (CDI) recurrence (FDA-approved as Zinplava 2016; not captured in automated query — see note below) |
| Predicted New Indication | Acute Female Pelvic Peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (per automated query; likely a data pipeline gap — Zinplava holds BLA 761027) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bezlotoxumab is a fully human IgG1 monoclonal antibody with a single, narrowly defined mechanism: it binds directly to *C. difficile* toxin B and blocks its attachment to host intestinal epithelial cells. It has no broad anti-inflammatory, immunomodulatory, or anti-infective properties beyond this specific toxin neutralization. The drug does not kill bacteria, does not modulate the immune system globally, and has no known activity outside the gastrointestinal tract in the context of CDI.

The only imaginable indirect pathway connecting bezlotoxumab to pelvic peritonitis runs through a rare complication chain: severe CDI → toxic megacolon → intestinal perforation → secondary peritonitis potentially extending to the pelvic cavity. However, bezlotoxumab acts *upstream* to prevent CDI recurrence — it is not a treatment for peritonitis, toxic megacolon, or any established complication of CDI. Even in this highly indirect scenario, the drug would have no therapeutic role once peritonitis has developed.

More critically, acute female pelvic peritonitis is predominantly caused by ascending sexually transmitted pathogens (*Neisseria gonorrhoeae*, *Chlamydia trachomatis*, polymicrobial anaerobes) — none of which involve *C. difficile* toxin B in any way. The mechanism is simply not applicable. The elevated TxGNN score (99.89%) almost certainly reflects a knowledge graph artifact: pelvic/abdominal infection-related disease nodes cluster together in the KG, creating spurious high-score associations across biologically unrelated conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No market authorizations were captured by the automated query. This is flagged as a **data pipeline gap**: bezlotoxumab is approved by the US FDA under **BLA 761027** (Zinplava, approved October 21, 2016) for reducing CDI recurrence in adults receiving antibacterial therapy for CDI who are at high risk of recurrence. Manual verification against the FDA BLA database is recommended to correct this gap before any downstream regulatory analysis.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or literature evidence supporting bezlotoxumab in acute female pelvic peritonitis, and the mechanistic link between an anti-*C. difficile* toxin B antibody and a gynecological infectious disease is biologically implausible — this prediction is most parsimoniously explained as a knowledge graph false positive arising from shared pelvic/abdominal infection node clusters, not a genuine repurposing signal.

**To proceed, the following is needed:**

- **Fix the data pipeline gap**: Manually verify and import the FDA BLA 761027 (Zinplava) approval record; investigate why biologic/monoclonal antibody approvals are not being captured by the automated query
- **Retrieve full MOA data**: Query DrugBank API for DB13140 to resolve the current blocking data gap on mechanism of action
- **KG noise filtering**: Consider implementing a biological plausibility pre-filter to flag predictions where predicted indications share no known disease pathway, pathogen, or molecular target with the drug's established mechanism — this would have flagged this candidate before evidence collection was triggered
- **Do not proceed** to clinical feasibility assessment for this indication without a plausible mechanistic hypothesis that is independent of the TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


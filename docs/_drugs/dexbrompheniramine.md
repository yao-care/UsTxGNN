---
layout: default
title: Dexbrompheniramine
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 7
---

# Dexbrompheniramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dexbrompheniramine: From H1 Antihistamine to Allergic Urticaria

## One-Sentence Summary

Dexbrompheniramine is the pharmacologically active R-enantiomer of brompheniramine, a first-generation H1 antihistamine used for allergic symptoms. The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 clinical trials** and **0 publications** specifically documenting dexbrompheniramine in this indication — though H1 antihistamines as a drug class carry Phase 3 RCT-level evidence for urticaria, lending strong mechanistic credibility to the prediction despite the absence of isomer-specific data.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on file for this jurisdiction |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | Not marketed (no NDA on file) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Dexbrompheniramine is the dextrorotatory (R-) enantiomer of brompheniramine, belonging to the first-generation alkylamine antihistamine class. Detailed mechanism of action data for this specific isomer was not available from the sources collected in this evaluation. Based on established pharmacological knowledge for the drug class, dexbrompheniramine acts as a competitive antagonist at histamine H1 receptors, blocking histamine-mediated vasodilation, increased vascular permeability, and pruritus — the core pathophysiology driving allergic urticaria. As a first-generation agent, it also carries anticholinergic activity that may further reduce secretory responses in the skin and mucosa.

Allergic urticaria is driven by IgE-mediated mast cell degranulation releasing histamine, which triggers the characteristic wheal-and-flare reaction. H1 receptor antagonism is the first-line standard of care for this condition, with the drug class supported by multiple Phase 3 RCTs. The TxGNN model's prediction score of 99.99% (global rank #534) reflects the strong mechanistic alignment between dexbrompheniramine's pharmacological profile and the histamine-dependent pathogenesis of allergic urticaria.

The critical gap is the complete absence of dexbrompheniramine-specific clinical or published data in this indication. Efficacy data from the parent racemate (brompheniramine) and structurally related first-generation antihistamines (chlorpheniramine, diphenhydramine) would currently need to serve as indirect, class-level support. The prediction is biologically sound and consistent with established pharmacological principles, but isomer-level evidence remains absent.

## Clinical Trial Evidence

Currently no related clinical trials registered for dexbrompheniramine in allergic urticaria.

## Literature Evidence

Currently no related literature available for dexbrompheniramine in allergic urticaria.

## US Market Information

No NDA or product licenses are on file for dexbrompheniramine in this jurisdiction. The drug may appear as an active component in combination over-the-counter products (e.g., decongestant-antihistamine combinations) in some markets, but no standalone authorizations were retrieved.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The H1 antihistamine class has robust Phase 3 RCT support for allergic urticaria, and dexbrompheniramine's mechanism directly targets the histamine-mediated pathophysiology of this condition; however, complete absence of isomer-specific safety, MOA, and clinical data — combined with no approved market authorization in this jurisdiction — means evidence generation is required before any clinical deployment.

**To proceed, the following is needed:**
- Retrieve the full FDA label or equivalent package insert (warnings, contraindications, approved dosing for dexbrompheniramine)
- Confirm mechanism of action details via DrugBank API (DB00405)
- Conduct targeted literature search for brompheniramine (parent racemate) in urticaria to establish indirect class-level evidence
- Obtain a drug-drug interaction profile from standard DDI databases (no interactions were found in the current query)
- Assess whether dexbrompheniramine provides a clinical advantage (efficacy or tolerability) over established first- and second-generation H1 antihistamines already approved for urticaria
- Define target patient population, dosing route, and a feasibility assessment for prospective isomer-specific study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Bremelanotide
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
---

# Bremelanotide
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

# Bremelanotide: From Hypoactive Sexual Desire Disorder to Acne

## One-Sentence Summary

Bremelanotide (brand name Vyleesi®) is a melanocortin receptor agonist approved by the US FDA in 2019 for hypoactive sexual desire disorder (HSDD) in premenopausal women, though it carries no regulatory authorization in Taiwan.
The TxGNN model assigns it a perfect prediction score for **Acne**, placing it at rank 2 among all drug–disease predictions for this compound.
However, **zero clinical trials and zero publications** currently support this repurposing direction — the evidence base is model prediction only (Level L5), and the recommended position is **Hold** pending preclinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypoactive Sexual Desire Disorder (HSDD) in premenopausal women (US FDA-approved as Vyleesi®; no Taiwan authorization) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 100.00% |
| Evidence Level | L5 — model prediction only, no empirical studies |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bremelanotide is a synthetic cyclic heptapeptide analogue of α-melanocyte-stimulating hormone (α-MSH). It acts as a non-selective agonist at melanocortin receptors MC1R, MC3R, MC4R, and MC5R. Its approved indication — HSDD — is thought to be mediated primarily through central MC4R activation in the hypothalamus, where it modulates neural circuits involved in sexual desire. Detailed mechanism of action data was not retrievable from the current evidence pack; the receptor pharmacology described here reflects published literature on the melanocortin system.

The mechanistic case for acne rests on peripheral MC1R expression. MC1R is broadly expressed on sebocytes (sebaceous gland cells) and keratinocytes — both central to acne pathophysiology. The parent peptide α-MSH has demonstrated anti-inflammatory activity in preclinical models: it inhibits sebum secretion and suppresses pro-inflammatory cytokines (IL-6, TNF-α) that drive comedone inflammation. If Bremelanotide similarly engages MC1R on sebocytes, it could theoretically reduce sebaceous inflammation and follicular hyperkeratinization — two hallmarks of acne vulgaris.

That said, this mechanistic chain is entirely theoretical for Bremelanotide itself. No preclinical sebocyte or acne-model studies have tested the drug. Furthermore, the currently approved subcutaneous injection route presents a significant practical barrier for a condition that standard care manages with topical or oral agents. The TxGNN score likely reflects shared network topology between the melanocortin pathway and acne-related inflammatory nodes, rather than any empirical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Bremelanotide holds no regulatory authorization in Taiwan (0 approved products, market status: not marketed). No product license table is available.

For reference: in the United States, Bremelanotide was approved by the FDA in June 2019 under the brand name Vyleesi® (Palatin Technologies / AMAG Pharmaceuticals) for acquired, generalized HSDD in premenopausal women, administered as a 1.75 mg subcutaneous auto-injector.

---

## Safety Considerations

Please refer to the package insert for safety information.

Safety data (key warnings, contraindications, drug interactions) was not retrievable from the current evidence pack. Known class-level concerns for melanocortin agonists include transient increases in blood pressure and heart rate, nausea, flushing, and hyperpigmentation — the clinical significance of these effects in a new indication context would require dedicated assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigned Bremelanotide the highest possible prediction score for acne based on a biologically plausible but entirely indirect mechanistic link through peripheral MC1R expression on sebocytes. With zero supporting clinical trials, zero literature, and no preclinical acne models published, there is currently no empirical basis on which to advance this candidate. The route-of-administration mismatch (subcutaneous injection vs. skin-targeted therapy) adds a further translational barrier.

**To proceed, the following is needed:**

- **Preclinical in vitro proof-of-concept:** Assess Bremelanotide's effect on human sebocyte cell lines — specifically sebum lipid production, IL-6/TNF-α release, and MC1R/MC5R receptor expression under inflammatory conditions (e.g., P. acnes stimulation)
- **In vivo pharmacology:** Test in an established acne-relevant animal model (e.g., hamster ear comedogenicity model or sebaceous gland-humanized mouse) to confirm anti-seborrheic and anti-inflammatory activity
- **Route-of-administration feasibility:** Evaluate skin penetration and local bioavailability for topical or intradermal delivery, since systemic SC dosing is not practical for acne management
- **Receptor selectivity mapping:** Clarify which melanocortin receptor subtype (MC1R vs. MC3R/MC4R/MC5R) drives any putative anti-acne effect, to guide formulation and dose optimization
- **Safety profile characterization:** Obtain full package insert data (warnings, contraindications, drug interactions) before any indication expansion analysis proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


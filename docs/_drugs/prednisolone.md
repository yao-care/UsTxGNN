---
layout: default
title: Prednisolone
parent: Model Prediction Only (L5)
nav_order: 1077
evidence_level: L5
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Prednisolone: From Established Corticosteroid Use to Alopecia Areata

## One-Sentence Summary

Prednisolone is a systemic glucocorticoid sold in the US in oral, injectable and other forms. The source data does not list its original approved indications.
The TxGNN model predicts it may be effective for **Alopecia Areata**.
The pack retrieved **17 registered trials** and **20 publications**. Only **3 trials** concern alopecia areata, and none tests prednisolone as the primary intervention. One published placebo-controlled RCT of oral pulse prednisolone exists.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (rests on one published placebo-controlled RCT and systematic reviews, not a registered Phase 2/3 prednisolone trial) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Prednisolone is a glucocorticoid receptor agonist with broad anti-inflammatory and immunosuppressive effects. This is inferred from the drug class, not from the source data.

Alopecia areata is an autoimmune, T-cell-mediated loss of hair follicle immune privilege. A glucocorticoid is a plausible fit for suppressing this process. One retrieved study (PMID 30294905) suggests oral pulse steroids may act partly by changing serum and tissue TNF-α levels in alopecia areata.

Systemic steroids have two main limits in this disease: hair loss often relapses after withdrawal, and adverse effects accumulate with prolonged use. Both shape the guardrails below.

---

## Clinical Trial Evidence

The pack retrieved 17 registered trials. Most are systemic lupus erythematosus trials of unrelated drugs (efavaleukin alfa, ALPN-101, baricitinib, sirolimus and others). They appear to be keyword-match artifacts and are excluded. One headache nerve-block trial is also excluded. The relevant trials are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse **methylprednisolone** in severe, therapy-resistant alopecia areata. It is a direct systemic-steroid study in the target disease, but the drug is not prednisolone, so it supports class-level evidence only. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (observational) | Completed | 296 | Safety and effectiveness of tofacitinib in alopecia. Participants received tofacitinib with or without adjuvant prednisolone, so prednisolone is background therapy rather than the studied drug. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Needle-free DERMOJET versus a normal syringe for delivering local steroid injections in alopecia areata. It compares delivery devices and does not test prednisolone. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | Placebo-controlled oral pulse prednisolone in alopecia areata. The abstract notes that earlier steroid pulse studies were neither randomized nor placebo-controlled. |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares treatments for alopecia areata, including immunosuppressants, hair growth stimulants and contact immunotherapy. |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic review | Australas J Dermatol | Reviews RCT evidence for systemic treatments in alopecia areata, totalis and universalis. It notes that supporting evidence varies widely across treatments. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, side effects and prognostic factors of corticosteroid pulse therapy. It notes that outcomes vary. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | Reviews pulse-dose corticosteroid regimens and side effects in children with alopecia areata. Dosing regimens are not well established. |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Clinical study (not classified) | Dermato-endocrinology | Medium-dose prednisolone pulse therapy. Prednisolone appears effective in early stages, but significant side effects may force discontinuation. |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohort | J Dtsch Dermatol Ges | Sequential high- then low-dose systemic steroids in severe childhood alopecia areata. Response is fast, but relapse follows discontinuation. |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Retrospective study | J Eur Acad Dermatol Venereol | Continuation rates of azathioprine, methotrexate and cyclosporine as steroid-sparing agents in 138 patients with chronic alopecia areata. Prednisolone is among the systemic options tried. |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Mechanism study | J Cosmet Dermatol | Serum and tissue TNF-α changes as a possible mechanism of oral pulse steroids. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case report and focused review | J Dermatolog Treat | Dexamethasone oral mini-pulse gave durable remission in severe alopecia areata when JAK inhibitors were not an option. |

---

## US Market Information

The source data lists 20 authorizations. The five main ones are below. No approved-indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA076913 | Prednisolone Sodium Phosphate | Solution |
| ANDA075988 | Prednisolone Sodium Phosphate | Solution |
| ANDA040583 | Methylprednisolone Sodium Succinate | Injection, powder, lyophilized, for solution |
| NDA011856 | SOLU-MEDROL | Injection, powder, for solution |
| NDA017011 | Prednisolone Acetate | Suspension/drops |

Two of these five products contain methylprednisolone rather than prednisolone. The full set of forms also includes oral tablets, orally disintegrating tablets, syrup and injections.

---

## Safety Considerations

- **Class-level concerns:** Relapse after steroid withdrawal and cumulative adverse effects limit systemic steroid use in alopecia areata. Children need particular caution.

The pack has no package-insert warnings, contraindications or drug interaction data. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a plausible mechanism, a published placebo-controlled RCT of oral pulse prednisolone, and several systematic and narrative reviews of steroid pulse therapy. However, the registered trials are mostly off-target or use a different steroid (methylprednisolone). Relapse after withdrawal and cumulative toxicity also limit long-term use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently blocking safety screening
- Mechanism of action data from DrugBank
- Prednisolone-specific comparative evidence against methylprednisolone, dexamethasone and JAK inhibitors
- A defined dosing, duration and relapse-management plan, including monitoring for pediatric patients
- A confirmed original-indication record for prednisolone

Among the other predictions, **idiopathic steroid-sensitive nephrotic syndrome** (L1) is established standard of care rather than novel repurposing. The remaining predictions have little or no supporting evidence and are on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


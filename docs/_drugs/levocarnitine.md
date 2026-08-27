---
layout: default
title: Levocarnitine
parent: 僅模型預測 (L5)
nav_order: 853
evidence_level: L5
indication_count: 10
---

# Levocarnitine
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

# Levocarnitine: From Carnitine Deficiency to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Levocarnitine (L-carnitine, DrugBank DB00583) is an endogenous compound generally used to treat primary and secondary carnitine deficiency states.
The TxGNN model's top-ranked prediction for this drug is **Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome**, an ultra-rare COL4A1-related vascular syndrome, with a raw similarity score of **99.94%** —
however, **zero clinical trials and zero publications** currently support this specific pairing, and the evidence pack's own mechanistic review flags the score as a likely knowledge-graph artifact rather than a true biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Carnitine deficiency (primary/secondary) — general classification for levocarnitine; specific approved-label indication text was not available in this evidence pack |
| Predicted New Indication | Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for levocarnitine is not available in this evidence pack (recorded as data gap DG002, High severity). Based on general pharmacological knowledge, levocarnitine is an endogenous cofactor required to shuttle long-chain fatty acids across the inner mitochondrial membrane for β-oxidation, and it is clinically used to correct carnitine deficiency states affecting energy metabolism.

The predicted indication — autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome — is a rare hereditary disorder in the COL4A1/COL4A2 spectrum, driven by structural collagen defects in basement membranes rather than by any known disorder of fatty-acid or mitochondrial metabolism. There is no established biological pathway connecting carnitine-dependent energy metabolism to collagen-related vasculopathy.

Consequently, this specific prediction is **not considered mechanistically reasonable**. Despite an extremely high TxGNN similarity score, the query log confirms zero clinical trials, zero ICTRP records, and zero PubMed publications exist for this drug–disease pair. The evidence pack's own repurposing rationale explicitly states the high score "可能反映知識圖譜嵌入相似度而非真實機轉" (may reflect knowledge-graph embedding similarity rather than a genuine mechanistic relationship) — i.e., this is most likely a model artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Levocarnitine is currently **not marketed** under this evidence pack's data set, with **0 license/NDA records** on file. No authorization number, product name, dosage form, or approved-indication text is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/US label warnings and contraindications are recorded as a **Blocking**-severity data gap (DG001) in this evidence pack — this alone prevents the candidate from entering initial safety screening (S1), independent of the efficacy evidence discussed above.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (99.94% score) has no supporting clinical trials or literature, and the documented disease mechanism (COL4A1-related collagen vasculopathy) has no known biological link to carnitine/fatty-acid metabolism — this pairing is most likely a model artifact rather than a real signal.
- A Blocking-severity data gap (TFDA/US label warnings and contraindications, DG001) independently prevents this candidate from proceeding to safety pre-screening.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- At minimum one mechanistic or preclinical study directly linking carnitine metabolism to COL4A1-related vasculopathy before this specific candidate can be re-evaluated
- Given the near-total absence of evidence for this pairing, evaluation resources are better directed to the higher-quality candidates identified within the same evidence pack (see appendix below)

---

## Appendix: Other TxGNN-Predicted Indications for Levocarnitine (Same Evidence Pack)

This evidence pack ("TW-DB00583-multi") scored levocarnitine against 10 candidate indications. Raw TxGNN score rank does **not** track with evidence quality — the strongest actionable candidate (congestive heart failure) ranks only 9th by score but has the best clinical support in the set.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 99.94% | L5 | Hold | No trials/literature; no plausible mechanism (this report's subject) |
| 2 | Brain small vessel disease 1 with or without ocular anomalies | 99.94% | L5 | Hold | 19 PubMed hits are ocular-anomaly term mismatches (noise), not real evidence |
| 3 | Diabetic nephropathy | 99.91% | L3 | Research Question | 2 trials (withdrawn/unknown status) + strong CPT1A/FAO mechanistic literature; no confirmatory RCT |
| 4 | Rheumatoid arthritis | 99.87% | L2 | Research Question | Completed pilot RCT (n=15) + recruiting Phase 2 (n=60) + Phase 3 status-unknown (n=46); OCTN2/FAO mechanism |
| 5 | Sclerosing cholangitis | 99.75% | L4 | Hold | Observational mitochondrial/lipid association only; no interventional data |
| 6 | Gout | 99.74% | L4 | Hold | Shared SLC22/OCTN transporter association (Mendelian randomization) only; no carnitine interventional trials |
| 7 | Brachydactyly-syndactyly syndrome | 99.66% | L5 | Hold | No evidence; rare skeletal dysplasia with no plausible mechanism |
| 8 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.63% | L5 | Hold | No evidence; rare congenital syndrome with no plausible mechanism |
| **9** | **Congestive heart failure** | 99.47% | **L2** | **Proceed with Guardrails** | Completed Phase 2/3 RCT (n=268) + mechanistic FAO rationale; **strongest-evidence candidate in this pack** |
| 10 | Hypoalphalipoproteinemia | 99.45% | L4 | Hold | Association-only lipid/ABCA1 genetics literature; no interventional carnitine data |

**Recommendation:** If a repurposing report is needed for this drug candidate, congestive heart failure (Rank 9) warrants its own dedicated report given its L2 evidence level and "Proceed with Guardrails" status — this is available on request.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


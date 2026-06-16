---
layout: default
title: Cidofovir
parent: 僅模型預測 (L5)
nav_order: 529
evidence_level: L5
indication_count: 4
---

# Cidofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the **txgnn-pipeline** skill to guide report generation for a US TxGNN candidate.

---

# Cidofovir: From CMV Retinitis to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is an antiviral nucleotide analogue historically used to treat cytomegalovirus (CMV) retinitis in AIDS patients, and is no longer commercially available in the United States.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CMV retinitis (no current US regulatory record available) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, Cidofovir is an acyclic nucleoside phosphonate antiviral that inhibits viral DNA polymerase — it works against a broad range of DNA viruses including CMV, HSV, and adenovirus. Its efficacy in CMV retinitis among HIV/AIDS patients has been established clinically, and it remains active on a compassionate-use basis against drug-resistant viral infections.

The proposed link to sclerosing cholangitis relies on a single indirect pathway: CMV and Cryptosporidium infections in severely immunocompromised patients (HIV/post-transplant) can cause AIDS cholangiopathy, a biliary disease with histopathological features resembling sclerosing cholangitis. In this very narrow context, Cidofovir's anti-CMV activity could theoretically reduce infection-driven biliary injury.

However, this hypothesis has not been tested in any clinical study. Primary sclerosing cholangitis (PSC) — the dominant clinical entity — has an autoimmune etiology entirely unrelated to viral infections or antiviral mechanisms. The TxGNN high confidence score most likely reflects graph-structural proximity in the knowledge graph (CMV → cholangitis → PSC) rather than a genuine pharmacological relationship. This is a probable graph artifact and should be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Cidofovir has no active NDA records in the current US regulatory database and is not commercially marketed in the United States.

> Note: Cidofovir (brand name Vistide) was originally approved by the FDA in 1996 for CMV retinitis in AIDS patients but was subsequently discontinued from commercial distribution by its manufacturer. It may still be available through compassionate-use or compounding channels.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is pure model output (L5) with zero supporting clinical trials or literature for Cidofovir in sclerosing cholangitis. The mechanistic link is highly speculative and only conceivably relevant to a rare infectious subtype (AIDS cholangiopathy), not to primary sclerosing cholangitis, which is autoimmune in origin.

**To proceed, the following is needed:**

- Confirm whether the target indication is infectious AIDS cholangiopathy (where antiviral rationale exists) or autoimmune PSC (where it does not)
- Conduct a targeted literature search for Cidofovir or anti-CMV therapy in biliary/cholangiopathy settings
- Retrieve complete MOA data from DrugBank API (DG002 remediation)
- Retrieve US package insert for key warnings and contraindications (DG001 remediation) — required before any safety review can proceed
- Consult a hepatologist to assess clinical plausibility of the infectious-cholangiopathy niche hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


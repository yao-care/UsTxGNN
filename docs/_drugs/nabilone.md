---
layout: default
title: Nabilone
parent: 僅模型預測 (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
---

# Nabilone
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

# Nabilone: From Chemotherapy-Induced Nausea/Vomiting to Headache Disorder

## One-Sentence Summary

> Nabilone is a synthetic cannabinoid (CB1/CB2 receptor agonist) originally approved to treat chemotherapy-induced nausea and vomiting refractory to standard antiemetics.
> Among the 10 candidate indications TxGNN generated for this drug, **Headache Disorder** is the only one with real supporting evidence — **1 clinical trial** and **4 publications**, including one small RCT — and was selected as the focus of this report over TxGNN's raw top-ranked prediction (Migraine Disorder, 99.89%), which has **zero** supporting trials or literature and is flagged internally as a likely knowledge-graph noise prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (drug is unlicensed/未上市); internationally, nabilone is indicated for chemotherapy-induced nausea and vomiting refractory to conventional antiemetics (per literature within this evidence pack) |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.78% (rank 6213 of all candidates) |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Official DrugBank mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). However, one of the literature entries retrieved for this candidate (PMID 37314117) directly describes nabilone as "a synthetic analogue of delta-9-Tetrahydrocannabinol, an agonist of cannabinoid receptors (CB-1 and CB-2), approved to treat chemotherapy-induced vomiting refractory to antiemetics." This gives a working MOA even though the formal DrugBank field is empty.

The rationale linking nabilone to headache disorders rests on the endocannabinoid system's known role in trigeminovascular pain transmission and central sensitization — mechanisms implicated in both nausea/vomiting circuits and headache pathophysiology. This is not a purely theoretical leap: the strongest single piece of evidence in this pack is a randomized, active-controlled trial (PMID 23070400) testing nabilone specifically in **medication overuse headache (MOH)**, a condition mechanistically tied to central sensitization.

That said, the supporting clinical trial (NCT03422861) is only tangentially related — it studies nabilone for postoperative pain in IBD surgery patients, not headache, and was flagged internally as "Grade C" relevance (low direct relevance, included mainly on keyword overlap). The evidence base is therefore real but thin, resting mostly on one small RCT plus reviews/case series in adjacent GI and pain contexts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03422861](https://clinicaltrials.gov/study/NCT03422861) | N/A | Unknown | 80 | RCT of nabilone for postoperative acute pain control in IBD patients with chronic opioid use undergoing GI surgery. Not a headache-specific trial; internally graded "C" (low relevance) — included via keyword overlap rather than direct topical match. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23070400](https://pubmed.ncbi.nlm.nih.gov/23070400/) | 2012 | RCT | The Journal of Headache and Pain | Double-blind, active-controlled trial of nabilone for medication overuse headache (MOH); evaluated efficacy on pain, headache frequency, analgesic intake, and quality of life in 30 MOH patients. |
| [28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/) | 2017 | Review | Current Pain and Headache Reports | Primer on cannabis/cannabinoids for pain and headache, grounded in endocannabinoid system physiology. |
| [37314117](https://pubmed.ncbi.nlm.nih.gov/37314117/) | 2023 | Review (withdrawn) | Revista Española de Enfermedades Digestivas | Describes nabilone's approved CINV indication and CB1/CB2 agonism; explores use in refractory vomiting from GI dysmotility. Note: this publication has been withdrawn. |
| [31238887](https://pubmed.ncbi.nlm.nih.gov/31238887/) | 2019 | Case series | BMC Gastroenterology | Case series on nabilone in refractory chronic diarrhea, discussing endocannabinoid system's role in GI motility — supportive background, not headache-specific. |

---

## US Market Information

Nabilone currently has no drug license or marketing authorization record in Taiwan (0 NDAs; market status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information — key warnings, contraindications, and drug interaction data are not available in this evidence pack (DG001, flagged as Blocking for safety review).

One relevant signal surfaced elsewhere in this evidence pack: analysis of a separate candidate indication (manic bipolar affective disorder) notes that cannabinoid agonists, as a class, carry a known risk of inducing or worsening mania and psychotic symptoms. This is not formal labeling data but is worth carrying forward into any safety workup for nabilone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for headache disorder rests on a single small RCT in a specific headache subtype (MOH) plus a weakly-relevant clinical trial and supporting reviews — not yet sufficient for a Go or Guardrails decision. The drug is also unlicensed in Taiwan (0 NDAs), and the safety data gap (DG001) is classified as Blocking, meaning a formal S1 safety review cannot proceed until TFDA label data is obtained.

**To proceed, the following is needed:**
- TFDA label/package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed DrugBank MOA record (DG002)
- Additional trials or studies specific to headache/migraine subtypes beyond the single 2012 MOH RCT
- Assessment of pathway to market availability in Taiwan (currently no license)
- Psychiatric safety monitoring plan, given the class-level cannabinoid risk of mania/psychosis noted elsewhere in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


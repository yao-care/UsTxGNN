---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin type A receptor (ETA) antagonist approved in the US and EU for pulmonary arterial hypertension (PAH), though it is not currently registered in the local market.
The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation (PAVM)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (approved in US/EU as Letairis/Volibris; not registered locally) |
| Predicted New Indication | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed (local) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, ambrisentan is a selective ETA antagonist that competitively blocks endothelin-1 (ET-1) binding to ETA receptors on pulmonary vascular smooth muscle cells, reducing vasoconstriction and inhibiting smooth muscle proliferation — the core mechanism underlying its established efficacy in PAH.

Pulmonary arteriovenous malformation (PAVM) most commonly arises as a structural complication of hereditary hemorrhagic telangiectasia (HHT), a rare autosomal dominant disease caused by mutations in the *ENG* or *ACVRL1* genes. These mutations disrupt the TGF-β/BMP signaling axis, and downstream ET-1 overexpression is thought to contribute to the dysregulated angiogenesis characteristic of HHT. This provides an indirect — but not implausible — mechanistic basis for ETA blockade.

That said, the mechanistic link remains firmly inferential. The standard and curative treatment for PAVM is transcatheter embolization. Ambrisentan's established clinical role in HHT is specifically limited to co-existing PAH — a hemodynamic complication that is pathophysiologically distinct from the structural vascular malformations of PAVM itself. The sole supporting publication describes an HHT patient with PAH rather than PAVM directly, further underscoring that this prediction represents a research hypothesis rather than an actionable clinical candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World J Clin Cases | Case of HHT with co-existing pulmonary arterial hypertension; family genetic analysis identified ENG/ACVRL1 mutations; illustrates the HHT–ET-1–PAH overlap relevant to ambrisentan's mechanism, though PAVM itself is not the subject of treatment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.41%), the supporting evidence for ambrisentan in PAVM is confined to a single case report describing a related but distinct HHT-PAH phenotype, and no clinical trials exist for this application. The standard of care for PAVM is transcatheter embolization, not pharmacotherapy, making pharmacological ETA blockade a speculative rather than competitive therapeutic strategy.

**To proceed, the following is needed:**
- Preclinical studies evaluating ETA antagonism in HHT-associated PAVM animal or cellular models
- Case series or registry data documenting ambrisentan use in HHT patients with confirmed PAVM (distinct from those treated for co-existing PAH)
- Mechanistic studies quantifying ET-1/ETA pathway upregulation specifically within PAVM vascular lesions
- Full package insert review to characterize key warnings, contraindications, and drug–drug interactions (DDI data currently unavailable)

> **Note for prioritization:** Predictions ranked 2–4 in this evidence pack — PAH associated with congenital heart disease (L1, S3), HIV infection (L1, S2), and connective tissue disease (L2, S3) — carry substantially stronger clinical and mechanistic support, including completed Phase 2/3 trials and ambrisentan-specific literature. These subtypes are recommended for evaluation ahead of the PAVM indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


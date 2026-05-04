---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

---

# Bempedoic Acid: From Primary Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic Acid is an ATP-Citrate Lyase (ACL) inhibitor FDA-approved in the United States (as Nexletol®) for LDL-cholesterol reduction in adults with primary hypercholesterolemia or heterozygous familial hypercholesterolemia (HeFH), but is not yet marketed in Taiwan.
The TxGNN model's top-ranked prediction is hyperthyroidism (score 99.61%), though this carries no mechanistic basis and a Hold recommendation; the most clinically actionable prediction is **Homozygous Familial Hypercholesterolemia (HoFH)** (rank 6, score 99.48%), with **0 clinical trials** and **17 publications** — including a 2026 real-world study that directly evaluated bempedoic acid in HoFH patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Primary Hypercholesterolemia / Heterozygous Familial Hypercholesterolemia (FDA-approved; not yet approved in Taiwan) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (rank 6 overall) |
| Evidence Level | L3 — Observational studies and systematic reviews |
| Taiwan Market Status | ✗ Not marketed (0 Taiwan TFDA licenses) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Bempedoic acid inhibits **ATP-Citrate Lyase (ACL)**, an enzyme that sits upstream of HMG-CoA reductase in the hepatic cholesterol biosynthesis pathway. By blocking ACL, the drug reduces intracellular acetyl-CoA availability for cholesterol synthesis, which in turn upregulates hepatic LDL receptor (LDLR) expression and enhances plasma LDL clearance. Importantly, bempedoic acid requires activation by the liver-specific enzyme ACSVL1, which confines its activity to the liver and avoids the skeletal muscle exposure responsible for statin-induced myopathy — a key clinical advantage for statin-intolerant patients.

The mechanistic link between HeFH (the approved indication) and HoFH is direct: both diseases stem from LDLR gene mutations, differing only in severity. In HeFH, one functional LDLR allele remains, allowing LDLR-upregulating therapies to work well. In HoFH, both alleles are non-functional or severely impaired, which theoretically limits the LDLR-dependent component of bempedoic acid's effect. However, ACL inhibition also reduces hepatic VLDL secretion — a pathway independent of LDLR — providing partial LDL-C lowering even without functional receptors. This makes extension from HeFH to HoFH mechanistically plausible, though the expected magnitude of effect is smaller.

The literature base further supports this reasoning. A 2026 real-world study (Warden & Duell, PMID 41274797) directly evaluated bempedoic acid efficacy and tolerability in HoFH patients. Multiple expert reviews from 2021–2025 consistently position bempedoic acid as part of the combination therapy armamentarium for refractory familial hypercholesterolemia, particularly for patients who cannot tolerate statins. A 2018 large-animal study (PMID 29449335) demonstrated LDL-C lowering and atherosclerosis attenuation in LDLR-deficient Yucatan miniature pigs — a direct HoFH model — providing early mechanistic proof-of-concept.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bempedoic acid in homozygous familial hypercholesterolemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-World Study | J Clin Lipidology | Direct retrospective evaluation of bempedoic acid efficacy and tolerability specifically in HoFH patients |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Expert Review | JACC | Bempedoic acid as an emerging LDL-lowering therapy; discusses its role in FH management alongside PCSK9i and inclisiran |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Narrative Review | J Atherosclerosis & Thrombosis | HoFH treatment advances; highlights challenges of LDL-C reduction when LDLR function is absent and discusses emerging agents |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Narrative Review | Exp Mol Pathology | Innovative therapies for HoFH; covers ACL inhibition approach and combination strategies |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Drug Review | Cardiology in Review | Reviews lipid-lowering options for FH including bempedoic acid as adjunct to evinacumab and other agents |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Preventive Cardiology | Comprehensive review of LDL-C lowering strategies; positions bempedoic acid within the treatment hierarchy for difficult-to-treat dyslipidemia |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Current Cardiology Reports | Management of familial and refractory hypercholesterolemias beyond statins and PCSK9 inhibitors; includes bempedoic acid discussion |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Non-statin lipid-lowering drugs including bempedoic acid; covers indications in statin intolerance and residual LDL risk |
| [32243228](https://pubmed.ncbi.nlm.nih.gov/32243228/) | 2020 | Review | Postgraduate Medicine | Bempedoic acid as an emerging LDL-lowering agent targeting ApoB lipoproteins for ASCVD prevention |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Animal Study | Arteriosclerosis, Thrombosis & Vascular Biology | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient (LDLR+/− and LDLR−/−) Yucatan miniature pigs — a direct HoFH preclinical model |

---

## Safety Considerations

Taiwan TFDA prescribing information (warnings, contraindications, drug interactions) is not available, as bempedoic acid has not been submitted for Taiwan approval.

> Please refer to the FDA Nexletol® package insert for full safety information.

One safety point warrants explicit attention based on data within this Evidence Pack: bempedoic acid carries **embryotoxicity risk** in animal studies and is contraindicated during pregnancy. One of TxGNN's predicted indications (rank 10, pregnancy-associated osteoporosis) is therefore immediately disqualified on both mechanistic and safety grounds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for HoFH indication)*

**Rationale:**
A 2026 real-world study directly supports bempedoic acid use in HoFH, and the mechanistic rationale is sound — ACL inhibition provides LDLR-independent LDL-C reduction that can offer partial benefit even when both LDLR alleles are non-functional. Evidence meets L3 threshold with strong biological plausibility.

---

**Note on remaining TxGNN predictions — all Hold:**

| Rank | Predicted Indication | Reason for Hold |
|------|---------------------|-----------------|
| 1 | Hyperthyroidism | No ACL–thyroid axis mechanistic link; KG topology artifact |
| 2 | THRβ resistance | Nuclear receptor pathway; no intersection with ACL/cholesterol synthesis |
| 3 | Infectious bovine rhinotracheitis | Veterinary disease; irrelevant to human repurposing |
| 4 | Malignant catarrh | Veterinary disease; same KG contamination issue as rank 3 |
| 5 | CMV infection | No established antiviral mechanism for ACL inhibitors |
| 7 | Hyperthyroxinemia | Same thyroid-metabolic KG clustering as rank 1 |
| 8 | Drug-induced osteoporosis | Bempedoic acid is not the causative drug; no treatment rationale |
| 9 | Multiple endocrine neoplasia | KG endocrine node clustering; no mechanistic link |
| 10 | Pregnancy-associated osteoporosis | Safety contraindication (embryotoxicity) + no mechanistic basis |

---

**To proceed with HoFH evaluation, the following is needed:**

- **Complete safety dossier**: Obtain full FDA Nexletol® prescribing information or initiate Taiwan TFDA consultation to understand local submission requirements
- **MOA documentation**: Retrieve full DrugBank DB11936 record to formally document the ACL inhibition mechanism in the dossier
- **Full-text review**: Obtain and critically appraise PMID 41274797 (2026 real-world HoFH study) for specific LDL-C % reduction, sample size, duration, and adverse event profile
- **HoFH patient landscape in Taiwan**: Assess estimated patient population size and whether registry data exist to support a compassionate use or named-patient program prior to full NDA filing
- **Clinical trial gap**: Consider feasibility of a Taiwan Phase 2 open-label study in HoFH, given the complete absence of registered trials globally for this combination
- **NDA pathway**: Bempedoic acid has no Taiwan approval in any indication — a full NDA filing would be required; early scientific advice meeting with TFDA is recommended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


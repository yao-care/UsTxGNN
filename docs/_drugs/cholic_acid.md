---
layout: default
title: Cholic Acid
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Cholic Acid
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

Using the system prompt guidelines and the txgnn-pipeline context, here is the evaluation report:

---

# Cholic Acid: From Bile Acid Synthesis Disorder to HIV Infectious Disease

## One-Sentence Summary

Cholic acid (sodium cholate) is the principal primary bile acid produced by the human liver, and is approved by the US FDA under the brand Cholbam® for treating rare bile acid synthesis disorders — though this is not captured in the current regulatory database. The TxGNN model ranks **HIV Infectious Disease** as its top new indication with a prediction score of 99.79%; however, available evidence consists of **0 clinical trials** and **9 publications** — all in vitro studies or narrative reviews on topical antiviral use — and one study (PMID 16610808) reports that cholic acid derivatives **enhance** HIV-1 replication in T cells, constituting a direct negative signal against this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in queried US regulatory database (Cholbam® is FDA-approved for bile acid synthesis disorders — data gap in current dataset) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (per queried database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cholic acid is a surfactant-like sterol molecule: its amphipathic structure allows it to form mixed micelles that solubilise dietary fats and fat-soluble vitamins in the small intestine. In the early 1990s, researchers exploited this detergent property as a topical antiviral strategy — sodium cholate was found to disrupt the lipid envelope of HIV-1 in vitro and was incorporated into the Protectaid contraceptive vaginal sponge (alongside low-dose nonoxynol-9 and benzalkonium chloride). This local, membrane-disrupting mechanism — not any systemic pharmacological effect — is the entire historical basis for the HIV connection in the published literature.

The TxGNN knowledge graph prediction likely reflects indirect graph-level relationships: bile acid metabolism intersects with immune modulation, gut microbiome composition, and lipid homeostasis, all of which are altered in HIV/AIDS. These systems-biology adjacencies in the knowledge graph can drive high prediction scores without implying a direct therapeutic mechanism. There is currently no biological rationale for systemic oral cholic acid supplementation to suppress HIV replication or improve HIV clinical outcomes.

Critically, the evidence base contains a significant negative signal. The most mechanistically informative in vitro study (PMID 16610808, 2006) synthesised C-11 amino-functionalised cholic acid derivatives — compounds predicted to act as HIV-1 protease inhibitors — and found the opposite: they **induced** HIV-1 replication and promoted syncytia (multinucleated giant cell) formation in infected T cells. This is the first published report of pro-viral activity by a bile acid derivative, and it represents a safety concern rather than a therapeutic opportunity for this structural class.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | In vitro / Animal | Human Reproduction | Sodium cholate shows dose-dependent in vitro inhibition of HIV-1 reverse transcriptase activity; basis for the Protectaid vaginal sponge — strictly topical use |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro (virology) | Lancet | TNBP + sodium cholate (0.2%) fully sterilises HBV and HTLV-III (HIV) in blood factor concentrates; blood product sterilisation context, not therapeutic |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro | J Med Chem | ⚠️ **Negative signal:** C-11 amino-functionalised cholic acid derivatives induced HIV-1 replication and syncytia formation in infected T cells — pro-viral, not antiviral |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Observational Cohort | Pharmacotherapy | HIV patients on protease inhibitor therapy have elevated plasma bile acid concentrations; bile acids evaluated as a hepatotoxicity biomarker, not as a treatment |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Commentary | Hepatology | Discusses NASH clinical trial exclusion of HIV patients due to antiretroviral DDI concerns; cholic acid is not the study focus |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Review | Ann NY Acad Sci | Reviews anti-STD vaginal contraceptive sponge technology including sodium cholate-based formulations; narrative review, no original therapeutic data |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust NZ J Obstet Gynaecol | Reviews contraceptive options with STD protection potential in the HIV era; sodium cholate mentioned as a candidate topical microbicide concept |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | Reviews physical and chemical barrier methods for STD prevention; sodium cholate sponge cited in context of microbicide development |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | Methodological | ChemMedChem | Detergent Triton X-100 confounds HIV protease inhibitor binding assay results; methodology-only paper, tangential to cholic acid therapy |

---

## US Market Information

No US market authorization records were found in the queried database for cholic acid.

> **Pharmacist's Note:** Cholic acid is commercially available in the United States as **Cholbam®** (cholic acid capsules 50 mg and 250 mg), which received FDA approval in March 2015 for: (1) bile acid synthesis disorders due to single enzyme defects affecting bile acid production, and (2) adjunctive treatment of peroxisomal disorders including Zellweger spectrum disorders. This FDA approval appears absent from the current data source — a data gap requiring manual verification. Please confirm current market status via the FDA Orange Book or DailyMed before clinical decision-making.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top prediction for cholic acid (HIV infectious disease, score 99.79%) is not clinically actionable. The entire evidence base relates to topical, membrane-disrupting antiviral activity in 1990s-era contraceptive sponge research — a mechanism that is irrelevant to systemic antiviral therapy. The single most informative mechanistic study (PMID 16610808, 2006) shows a structurally-related cholic acid derivative **enhances** HIV replication, which represents a safety concern that further disqualifies this direction.

**To proceed on HIV, the following would be needed:**
- New mechanistic studies demonstrating systemic antiviral activity of unmodified cholic acid in human cells or animal HIV models
- Clear separation from the topical-use evidence base (which cannot support systemic indications)
- Resolution of the pro-viral signal in PMID 16610808 before any compound advancement

---

### ⚠️ Higher-Priority Indication Identified: Vitamin Deficiency Disorder (TxGNN Rank 5)

Among the 10 predicted indications evaluated in this Evidence Pack, **Vitamin Deficiency Disorder** (TxGNN score 99.71%, evidence level **L3**, recommendation: **Proceed with Guardrails**) represents a substantially more actionable repurposing opportunity and warrants prioritisation over the rank-1 HIV prediction.

**Why this is the stronger indication:**

- **Established mechanistic link:** Bile acid synthesis enzyme defects (e.g., HSD3B7, AKR1D1 deficiency) deplete the functional bile salt pool → impaired intestinal micellar solubilisation of fat-soluble vitamins A, D, E, and K → clinical vitamin deficiency syndromes (rickets, coagulopathy, failure to thrive, cholestatic liver disease). Oral cholic acid replacement restores bile salt concentrations and corrects fat-soluble vitamin absorption — this is a well-understood mechanism.
- **FDA approval precedent:** Cholbam® was approved in the US in 2015 for precisely this clinical context, confirming regulatory plausibility.
- **Supporting evidence:** 1 active post-marketing observational registry ([NCT03115086](https://clinicaltrials.gov/study/NCT03115086), n=55, 10-year follow-up) + multiple case series and retrospective cohort studies (PMIDs: 35392794, 40643170, 28902093, 39498929, 23415802, 30746501).

**To advance the Vitamin Deficiency Disorder indication:**
- Retrieve the Cholbam® NDA number and full prescribing information to resolve the DG001 safety data gap (key warnings, contraindications)
- Obtain DrugBank MOA data entry for cholic acid to resolve DG002
- Monitor NCT03115086 for interim safety and effectiveness data
- Review published paediatric dosing protocols from case series for bile acid synthesis defect populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill context confirmed — this is a US TxGNN drug repurposing evaluation report. Now generating the report from the Evidence Pack.

> **Structural note:** The top four TxGNN predictions (ranks 1–4) are all rated Hold/L5 with no clinical evidence. The first actionable predictions are **AIDS-Related Complex** (rank 5, L1) and **Congenital HIV** (rank 6, L1). The report focuses on these, consistent with the spirit of the output format.

---

# Atazanavir: From HIV-1 Infection to AIDS-Related Complex

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor used globally in combination antiretroviral therapy to suppress HIV replication and prevent disease progression.
The TxGNN model predicts it may be effective for **AIDS-Related Complex** (symptomatic HIV, CDC Stage B), with **2 completed Phase 3 trials** and **3 publications** directly supporting this application — and an additional **33 trials and 7 publications** backing the closely related **Congenital HIV (vertical transmission)** indication.

> **Prediction landscape note:** Ranks 1–4 (feline FIV, primate SIV, a rare neurological disorder, and an obsolete lipid classification) are all rated **Hold (L5)**. The first clinically actionable predictions are ranks 5 and 6, both rated **L1 — Proceed with Guardrails**. This report focuses accordingly.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (known HIV-1 protease inhibitor; not found in current FDA database) |
| Predicted New Indication | AIDS-Related Complex |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| US Market Status | ✗ Not found in current database (0 NDAs) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atazanavir is a second-generation HIV-1 protease inhibitor. It competitively inhibits the HIV-1 aspartate protease by binding tightly to the enzyme's active site, mimicking the natural substrate's transition state. This blocks proteolytic cleavage of the *gag* and *gag-pol* polyprotein precursors, preventing formation of mature, infectious viral particles. The resulting reduction in plasma viral load halts progressive CD4+ T cell depletion — the mechanism underlying all clinical benefit.

AIDS-Related Complex (ARC) refers to symptomatic HIV infection at CDC Stage B: conditions such as oral candidiasis, constitutional symptoms (fever, night sweats, weight loss), and moderate immunosuppression that precede full AIDS (CDC Stage C). Atazanavir's mechanism is designed precisely to interrupt this progression. This is not a speculative repurposing — it is a direct application of the drug's core pharmacology to a disease stage that shares identical viral pathophysiology with the original indication.

Congenital HIV (rank 6) — vertical mother-to-child transmission — involves the same HIV-1 replication mechanism but introduces important perinatal complexity: (1) ATV plasma trough levels (C_min) decline during the third trimester due to increased renal clearance and altered protein binding, necessitating therapeutic drug monitoring; (2) placental efflux transporters ABCB1, ABCG2, and ABCC2 modulate fetal drug exposure, with implications for neonatal protection; and (3) immature neonatal UGT1A1 substantially raises the risk of ATV-induced hyperbilirubinemia in newborns. Both predictions share an exceptionally strong mechanistic rationale — the key difference is the patient population and the additional pharmacokinetic vigilance required.

---

## Clinical Trial Evidence

Evidence compiled across AIDS-Related Complex (rank 5) and Congenital HIV (rank 6). Top 10 highest-relevance trials shown.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Pivotal open-label RCT comparing ATV+RTV or ATV+SQV vs LPV/RTV, each with TDF + nucleoside backbone, in treatment-experienced HIV subjects — a landmark trial in Atazanavir's regulatory approval pathway |
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | 96-week head-to-head comparison of ATV/RTV vs LPV/RTV + TDF/FTC in treatment-naïve HIV-1 subjects, evaluating long-term antiviral efficacy and metabolic tolerability |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | Open-label non-inferiority RCT comparing DTG/ABC/3TC vs ATV+RTV+TDF/FTC in ART-naïve HIV-1-infected women; provides direct efficacy benchmark for ATV-based regimens |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Multicenter non-inferiority RCT (SWORD-2) evaluating switch from PI/NNRTI/INI-based ART (including ATV) to DTG+RPV in virologically suppressed HIV-1 adults |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, Not Recruiting | 618 | ATLAS study: non-inferiority evaluation of switching from ATV-containing PI-based regimens to long-acting injectable cabotegravir+rilpivirine every 4 weeks; ongoing through 2029 |
| [NCT00207142](https://clinicaltrials.gov/study/NCT00207142) | Phase 4 | Completed | 252 | INDUMA study: Phase 4 RCT comparing maintenance with unboosted vs RTV-boosted Reyataz after viral suppression induction, assessing durability of HIV RNA < 50 copies/mL at 48 weeks |
| [NCT00135356](https://clinicaltrials.gov/study/NCT00135356) | Phase 4 | Completed | 219 | REAL study: RCT evaluating substitution to ATV/RTV for management of lipodystrophy syndrome in HIV-infected subjects, demonstrating tolerability advantage over older PIs |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II: PK, safety, and efficacy of ATV powder + RTV in HIV-infected children ≥3 months to <11 years (both treatment-naïve and experienced); key pediatric dosing validation |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: ATV powder + RTV safety, tolerability, and PK in HIV-infected infants ≥3 months to <6 years — foundational trial for the youngest pediatric dosing authorization |
| [NCT00326716](https://clinicaltrials.gov/study/NCT00326716) | Phase 1 | Completed | 69 | PK study confirming adequate ATV/RTV exposure during pregnancy vs. historical non-pregnant controls; critical for establishing maternal dosing in PMTCT regimens |

---

## Literature Evidence

Evidence compiled across AIDS-Related Complex (rank 5) and Congenital HIV (rank 6), sorted by evidence quality.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort | *Antiviral Therapy* | ATV+RTV achieves adequate drug exposure during pregnancy with or without tenofovir co-administration, supporting dosing adequacy of ATV-based PMTCT regimens across trimesters |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case-Control | *Eur J Clin Pharmacol* | European multi-registry case/non-case study quantifying congenital anomaly risk after fetal ARV exposure including ATV; most current population-level safety signal update |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort | *Front Immunology* | PHACS SMARTT study: 3,500+ HIV-exposed uninfected infants at 22 US sites, systematically assessing metabolic, cardiac, neurological, and neurodevelopmental outcomes after in utero ARV exposure |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | *JAMA Pediatrics* | Congenital anomaly rates in 2,580 HIV-exposed uninfected infants by specific ARV exposure including ATV; overall reassuring findings with agent-specific signal notes |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohort | *J Acquir Immune Defic Syndr* | Comparative cohort assessing differential effects of common cART regimens (ATV/RTV, EFV, others) on incidence of AIDS-defining neurological conditions, directly relevant to ARC progression monitoring |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort/Observational | *AIDS Reviews* | Analysis disentangling the contribution of HIV immunosuppression vs. ARV treatment (including ATV) on gastrointestinal adverse events; relevant to ARC patient symptom management |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In vitro / PK | *Reprod Toxicol* | First study quantifying ABCB1, ABCG2, and ABCC2 transporter effects on ATV and RTV placental transfer in rats; provides mechanistic basis for understanding fetal drug exposure during PMTCT |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | In vitro | *Antimicrob Agents Chemother* | Novel CNS-targeting HIV-1 PIs (GRL-08513/08613) with activity against drug-resistant strains and favorable BBB penetration — contextualizes Atazanavir's known limitations in treating HIV-associated neurocognitive disorders (HAND) |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cohort | *J AIDS Immune Res* | PHACS/SMARTT: newborn hearing screening referral rates in 1,435 HIV-exposed uninfected infants; evaluates ARV-associated hearing risk for neonatal monitoring protocols |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | *Clin Infect Dis* | Pharmacovigilance database analysis of neural tube defect signals comparing DTG vs non-DTG ART regimens (including ATV-based) in pregnancy; establishes comparative safety reference |

---

## US Market Information

No active US FDA authorizations were found for Atazanavir in the current database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | No records found | — | — |

> Atazanavir (brand: Reyataz, Bristol-Myers Squibb) is a known FDA-approved HIV-1 protease inhibitor. The absence of records in this database likely reflects brand-level discontinuation or data extraction scope. Generic atazanavir (300 mg/150 mg capsules) and pediatric powder formulations have been authorized by the FDA. Direct verification via the FDA Orange Book and the FDA Approved Drug Products database is strongly recommended before any market strategy decisions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Two unresolved data gaps require remediation before safety review can be completed:**
>
> - **DG001 (Blocking):** Package insert warnings and contraindications have not yet been extracted from the FDA label. This is a mandatory prerequisite for Stage S1 safety screening. Remediation: download and parse the FDA label PDF for Atazanavir (Reyataz).
> - **DG002 (High):** Mechanism of action data was not retrieved from DrugBank. Remediation: query the DrugBank API for DB01072.
>
> From known clinical pharmacology, priority safety areas include: indirect hyperbilirubinemia (UGT1A1 inhibition — particularly critical for neonates), nephrolithiasis and nephrotoxicity, PR interval prolongation (cardiac conduction), and extensive drug-drug interactions via CYP3A4 and P-glycoprotein pathways. These must be formally documented before regulatory or clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For **AIDS-Related Complex** and **Congenital HIV**, the mechanistic rationale is the strongest possible — it is the drug's own core pharmacology. Multiple completed Phase 3 trials and robust real-world cohort data confirm efficacy in HIV disease stages directly overlapping these indications. However, two blocking data gaps (package insert warnings, MOA data) prevent formal safety clearance, and the absence of active FDA NDA records requires regulatory verification before any commercialization or formulary strategy can proceed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse the FDA package insert for Atazanavir/Reyataz to extract contraindications, black box warnings, and DDI table — required to complete Stage S1 safety evaluation
- **[DG002 — High]** Query DrugBank API (DB01072) to formally document mechanism of action, drug categories, and toxicity data
- **Regulatory status verification:** Confirm current FDA authorization status via the Orange Book; determine whether brand Reyataz has been discontinued, and whether approved generic NDA holders cover HIV-1, pediatric (≥3 months), and pregnancy (PMTCT) indications
- **Perinatal PK monitoring plan:** For the Congenital HIV indication, develop a TDM protocol addressing third-trimester ATV C_min decline, transporter-mediated fetal exposure variability, and neonatal bilirubin surveillance
- **Dismiss ranks 1–4:** The top four TxGNN predictions (feline FIV, primate SIV, rare neurological disorder, obsolete lipid classification) are L5/Hold with no supporting evidence; no resources should be allocated unless new mechanistic or translational data emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


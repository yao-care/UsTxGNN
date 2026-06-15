---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab (Praluent) is a fully human monoclonal antibody that inhibits PCSK9 (proprotein convertase subtilisin/kexin type 9), approved globally for lowering LDL cholesterol in patients with hypercholesterolemia and atherosclerotic cardiovascular disease — though currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **Cholesterol Catabolic Process Disease** (a category encompassing familial hypercholesterolemia, dyslipidemias, and related cholesterol metabolism disorders),
with **1 Phase 3 clinical trial** and **19 publications** currently supporting this direction.

> **Note on prediction ranking**: The TxGNN model's top-ranked prediction (X-linked ichthyosis, rank 1) carries no biological rationale or clinical evidence (L5/Hold). This report focuses on the highest-evidence candidate — rank 5: Cholesterol Catabolic Process Disease (L2/Proceed with Guardrails) — which is directly aligned with the drug's established mechanism and represents the most actionable finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia & Atherosclerotic Cardiovascular Disease Prevention (US/EU approved; not registered in Taiwan) |
| Predicted New Indication | Cholesterol Catabolic Process Disease |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Approvals | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from the queried database. Based on the extensive literature returned in the evidence pack, alirocumab targets PCSK9 — a liver-secreted serine protease that binds LDL receptors on hepatocyte surfaces and routes them to lysosomal degradation. By neutralizing circulating PCSK9, alirocumab prevents LDL receptor destruction, allowing receptors to recycle to the hepatocyte surface. The net effect is a marked increase in LDL-C clearance from the bloodstream, typically reducing LDL-C by 50–60%.

Cholesterol catabolic process diseases are defined by impaired cholesterol metabolism or catabolism — most prominently familial hypercholesterolemia (FH, caused by mutations in LDLR, APOB, or PCSK9 genes), familial dysbetalipoproteinemia, and lipid disorders secondary to conditions such as HIV/antiretroviral therapy. The mechanistic alignment is direct and unambiguous: alirocumab's core pharmacological action is precisely to restore the impaired LDL receptor recycling that underlies these diseases. This is reinforced by genomic evidence — individuals with naturally occurring loss-of-function PCSK9 variants have lifelong low LDL-C and substantially reduced cardiovascular risk, establishing biological causality.

Beyond familial hypercholesterolemia, the evidence pack includes a completed Phase 3 trial (EPIC-HIV) examining PCSK9 inhibition in HIV-associated dyslipidemia, where antiretroviral drugs disrupt cholesterol catabolic pathways through a distinct mechanism. Experimental data further suggest alirocumab may prevent cholesterol gallstone formation via PPARα-mediated CYP7A1 upregulation — the rate-limiting enzyme in bile acid synthesis — extending its relevance to cholesterol catabolism beyond the cardiovascular domain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | PCSK9 inhibition in HIV-infected patients with treated HIV and elevated cardiovascular risk; assessed vascular inflammation, endothelial function, and non-calcified coronary plaque using non-invasive imaging — a population whose cholesterol catabolic pathways are disrupted by antiretroviral therapy, distinct from traditional statin-treated populations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Clinical Trial Analysis | Eur Heart J Cardiovasc Pharmacother | Alirocumab safety and efficacy from 47,296 patient-years (ODYSSEY OUTCOMES trial); confirmed persistent LDL-C reduction and significant decrease in recurrent ischemic cardiovascular events with a favorable long-term safety profile |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | RCT Post-hoc Analysis | Diabetes Care | ODYSSEY OUTCOMES post-hoc: alirocumab lowers both Lp(a) and LDL-C without increasing new-onset diabetes risk — a favorable safety signal distinguishing it from some other lipid-lowering strategies |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Review | Pharmacology & Therapeutics | Mechanistic comparison of alirocumab (extracellular PCSK9 blockade by monoclonal antibody) vs. inclisiran (intrahepatic PCSK9 siRNA); delineates distinct target engagement and clinical implications for cholesterol catabolic disease management |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduction Targeted Ther | Comprehensive PCSK9 bench-to-bedside review; extends alirocumab's mechanistic relevance to liver diseases, infectious diseases, autoimmune disorders, and oncology beyond primary hypercholesterolemia |
| [38191052](https://pubmed.ncbi.nlm.nih.gov/38191052/) | 2024 | Experimental Study | Metabolism Clin Exp | PCSK9 inhibition prevents and alleviates cholesterol gallstones via PPARα-mediated CYP7A1 activation in mouse models; directly implicates PCSK9/alirocumab in bile acid biosynthesis — a key arm of cholesterol catabolism |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atherosclerosis Rep | Homozygous FH treatment developments; alirocumab among novel pharmacological options for the most severe end of the cholesterol catabolic disorder spectrum |
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Review | European Heart Journal | Evolving lipid-lowering targets; alirocumab addresses LDL-C, apoB, and Lp(a) simultaneously, covering multiple key drivers of residual cardiovascular risk in dyslipidemia |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Review | Pharmacotherapy | State-of-the-art review of PCSK9-directed therapies; alirocumab and evolocumab established as evidence-based standard of care for statin-intolerant or inadequately controlled cholesterol disorders |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Literature Review | Medicina (Kaunas) | Familial hypercholesterolemia diagnostics and treatment landscape; PCSK9 inhibitors including alirocumab positioned as cornerstone therapy for LDLR/APOB/PCSK9 mutation carriers |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review/Update | Curr Opin Lipidology | Updated PCSK9-directed therapy overview; two landmark cardiovascular outcomes trials confirm marked LDL-C reduction and reduced cardiovascular risk, with novel PCSK9 inhibition strategies in development |

---

## Taiwan Market Information

No Taiwan regulatory approvals are on record for alirocumab (total licenses: 0 as of 2026-06-01). The drug is not currently marketed in Taiwan.

For reference, alirocumab is approved as **Praluent®** in the United States (FDA) and European Union (EMA) for:
- Adults with heterozygous familial hypercholesterolemia (HeFH) or established atherosclerotic cardiovascular disease (ASCVD) who require additional LDL-C lowering beyond maximally tolerated statin therapy
- Reduction of risk of myocardial infarction, stroke, and unstable angina requiring hospitalization in adults with established ASCVD

---

## Safety Considerations

Please refer to the Praluent® package insert for complete safety information.

Taiwan prescribing information (TFDA package insert) is not available as the drug has not been submitted for Taiwan approval. Drug interaction data returned zero entries from the DDI database query; as a monoclonal antibody, alirocumab is not metabolized by cytochrome P450 enzymes, which substantially reduces pharmacokinetic drug interaction risk in clinical practice.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alirocumab's PCSK9 inhibition mechanism is directly aligned with the pathophysiology of cholesterol catabolic process diseases, and the completed Phase 3 EPIC-HIV trial alongside 19 supporting publications provide L2-level evidence. However, the complete absence of Taiwan regulatory approval is a structural barrier that must be addressed before clinical deployment.

**To proceed, the following is needed:**
- **Taiwan regulatory pathway**: Initiate TFDA market authorization process for alirocumab (Praluent®); assess whether US FDA/EMA approval data package can support expedited review
- **MOA data remediation (DG002)**: Retrieve full mechanism of action from DrugBank API to complete mechanistic linkage analysis
- **Safety data remediation (DG001)**: Download and parse TFDA package insert PDF to extract Taiwan-specific warnings and contraindications (or cross-reference with US FDA label)
- **Taiwan patient population assessment**: Estimate FH prevalence, statin-intolerant population size, and unmet treatment need in Taiwan
- **Reimbursement feasibility**: Conduct health technology assessment (HTA) for National Health Insurance (NHI) coverage evaluation
- **Subgroup evidence gap**: EPIC-HIV is a specialized population (HIV+); consider whether Taiwan-specific Phase 3 or real-world evidence is needed for broader cholesterol catabolic disease indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


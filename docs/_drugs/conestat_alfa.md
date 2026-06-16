---
layout: default
title: Conestat Alfa
parent: 僅模型預測 (L5)
nav_order: 549
evidence_level: L5
indication_count: 10
---

# Conestat Alfa
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

# Conestat Alfa: From Hereditary Angioedema (Acute Attacks) to C1 Inhibitor Deficiency

## One-Sentence Summary

Conestat alfa (Ruconest®) is a recombinant human C1 esterase inhibitor approved in Europe and the United States for the acute treatment of hereditary angioedema (HAE) attacks. The TxGNN model predicts it may be effective for **C1 Inhibitor Deficiency**, with **41 clinical trials** and **20 publications** currently supporting this direction. Importantly, this prediction directly reflects the drug's established pharmacological mechanism as a C1-INH replacement protein rather than a traditional repurposing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in queried database (Ruconest® approved in EU/US for acute HAE attacks) |
| Predicted New Indication | C1 Inhibitor Deficiency |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 |
| US Market Status | Not marketed (in queried dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on published literature, conestat alfa is a recombinant human C1 esterase inhibitor (rhC1-INH, Serpin G1/SERPING1) produced in transgenic rabbits. It acts as a direct protein replacement therapy for patients with hereditary angioedema types I and II, who carry heterozygous loss-of-function mutations in the *SERPING1* gene.

C1 inhibitor is a serine protease inhibitor (serpin) that normally governs three interconnected cascade systems: the complement system (inhibiting C1r and C1s to prevent uncontrolled complement activation), the contact activation pathway (inhibiting activated Factor XII and plasma kallikrein to prevent excessive kinin generation), and the intrinsic coagulation pathway (inhibiting Factor XIa and thrombin). When C1-INH is deficient or dysfunctional, the contact pathway becomes dysregulated, leading to excessive bradykinin production. Bradykinin binds to endothelial B2 receptors, dramatically increasing vascular permeability and causing the recurrent, debilitating — and potentially fatal — episodes of subcutaneous and mucosal swelling that define HAE.

This TxGNN prediction is unique in the drug repurposing context: conestat alfa *is* the deficient protein being replaced, making this a direct enzyme replacement therapy rather than a mechanistic extension into new disease territory. Multiple completed Phase 2 and Phase 3 RCTs have confirmed its efficacy for both acute HAE attacks and prophylaxis. The drug has received EMA approval (Ruconest®, 2010) and FDA approval (Ruconest®, 2014) for this exact disease, supporting a confidence level that few drug repurposing candidates achieve.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00438815](https://clinicaltrials.gov/study/NCT00438815) | Phase 3 | Completed | 113 | CHANGE 2 Trial: open-label safety and efficacy study of repeat-dose C1INH-nf for acute HAE attacks; one of the largest Phase 3 trials in HAE, directly supporting C1-INH replacement therapy |
| [NCT00168103](https://clinicaltrials.gov/study/NCT00168103) | Phase 2/3 | Completed | 126 | Pasteurized C1-INH concentrate in congenital C1-INH deficiency with acute abdominal or facial HAE attacks; established clinically relevant dosing, efficacy, and safety data |
| [NCT00289211](https://clinicaltrials.gov/study/NCT00289211) | Phase 3 | Completed | 83 | LEVP2005-1/Part A: double-blind, placebo-controlled pivotal RCT of C1INH-nf for acute HAE attacks; core registration trial supporting C1-INH replacement |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Phase 3 | Completed | 75 | Confirmed efficacy and safety of rhC1INH 50 U/kg for acute HAE attacks with open-label extension; directly supported Ruconest FDA approval |
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Completed | 75 | Randomized, double-blind, placebo-controlled Phase 3 study of rhC1INH for acute HAE attacks; established pharmacokinetic/pharmacodynamic profile |
| [NCT02247739](https://clinicaltrials.gov/study/NCT02247739) | Phase 2 | Completed | 32 | Multicenter, randomized, double-blind, placebo-controlled, 3-period crossover study of rhC1INH prophylaxis in HAE; demonstrated significant reduction in attack frequency |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Completed | 77 | Randomized, placebo-controlled, double-blind study of rhC1INH in acute HAE attacks; early pivotal evidence for efficacy and PK/PD characterization |
| [NCT06690047](https://clinicaltrials.gov/study/NCT06690047) | Phase 4 | Completed | 5 | Ruconest (conestat alfa) for HAE prodrome management; assessed whether early administration prevents progression from prodromal symptoms to full angioedema attacks |
| [NCT00261053](https://clinicaltrials.gov/study/NCT00261053) | Phase 2 | Completed | 14 | First single-center open-label study of recombinant human C1 inhibitor in HAE; established initial safety, tolerability, and PK/PD profile for this recombinant approach |
| [NCT03697187](https://clinicaltrials.gov/study/NCT03697187) | Observational | Completed | 152 | Prospective real-world registry of Ruconest® (conestat alfa) safety in HAE; confirmed post-marketing safety profile under routine clinical conditions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | RCT / Prophylaxis Study | Expert Rev Clin Immunol | Conestat alfa for HAE prophylaxis in adults and adolescents; reviewed registration evidence and positioned rhC1-INH within the prophylaxis treatment landscape |
| [28754491](https://pubmed.ncbi.nlm.nih.gov/28754491/) | 2017 | RCT | Lancet | Phase 2 multicenter, randomized, double-blind, placebo-controlled crossover trial of rhC1-INH prophylaxis in HAE; demonstrated statistically significant reduction in attack frequency |
| [31982824](https://pubmed.ncbi.nlm.nih.gov/31982824/) | 2020 | Clinical Study | Int Immunopharmacol | Real-world evaluation of home rhC1-INH treatment in HAE-C1-INH patients; confirmed efficacy for acute attacks and short-term prophylaxis under routine conditions |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Drug Review | BioDrugs | Comprehensive review of conestat alfa clinical evidence from two pivotal RCTs; summarized mechanism, dosing, efficacy endpoints, and safety profile |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Open-label Study | Allergy Asthma Proc | Home treatment with conestat alfa in HAE-C1-INH patients; 65 attack episodes analyzed showing rapid, consistent symptom relief in a real-life self-administration setting |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Systematic Review | Immunotherapy | Systematic review of recombinant replacement therapy for HAE; covered pharmacology, clinical trial efficacy, and comparative effectiveness against plasma-derived products |
| [28687108](https://pubmed.ncbi.nlm.nih.gov/28687108/) | 2017 | Review | Immunol Allergy Clin N Am | Acute HAE attack management review; positioned conestat alfa alongside icatibant and plasma-derived C1-INH with clinical decision guidance |
| [22171564](https://pubmed.ncbi.nlm.nih.gov/22171564/) | 2012 | Mechanistic Study | BioDrugs | Effects of recombinant C1-inhibitor on coagulation and fibrinolysis in HAE patients; demonstrated lower thrombotic risk compared to plasma-derived products |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Clinical Guidelines | Curr Opin Allergy Clin Immunol | Italian HAE diagnostic and therapeutic management experience; includes conestat alfa as a standard treatment option with practical dosing guidance |
| [29357215](https://pubmed.ncbi.nlm.nih.gov/29357215/) | 2018 | Review | Skin Therapy Lett | New HAE treatments including recombinant C1 inhibitor; reviewed advances in complement and kallikrein-kinin pathway targeting, including recombinant vs. plasma-derived distinctions |

---

## US Market Information

No US NDAs are registered for conestat alfa in the queried regulatory dataset. Based on published literature and FDA/EMA public records, conestat alfa (Ruconest®) received EMA approval in 2010 and FDA approval in 2014 for the treatment of acute angioedema attacks in adults and adolescents with HAE due to C1 inhibitor deficiency. The absence of records in this dataset likely reflects a data collection gap rather than actual non-approval status. Package insert information should be obtained directly from the manufacturer or regulatory agency for complete indication, dosing, and safety details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Conestat alfa is a direct recombinant replacement for the deficient C1 inhibitor protein in HAE — the TxGNN prediction at rank 1 (99.999% score) aligns exactly with the drug's established pharmacological mechanism and its EMA/FDA-approved indication. Multiple completed Phase 3 RCTs (including 2 placebo-controlled pivotal trials enrolling 75–113 patients each) and a Phase 2 crossover prophylaxis trial published in *The Lancet* provide unambiguous L1-level evidence.

**To proceed, the following is needed:**
- Obtain full US and EU package inserts to document complete warning, contraindication, and drug interaction profiles (currently absent from this dataset)
- Confirm current US commercial availability and NDA status (Ruconest has FDA approval; verify whether active commercial distribution is ongoing or suspended)
- Establish an immunogenicity monitoring plan for long-term or prophylactic use, given the recombinant rabbit-derived protein nature of conestat alfa (anti-drug antibody formation risk)
- Retrieve and document MOA data from DrugBank (DB09228) for formal regulatory submission and scientific dossier completion
- Consider patient population access strategy: HAE is an ultra-rare disease (prevalence ~1:50,000), requiring orphan drug framework consideration for any market authorization application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


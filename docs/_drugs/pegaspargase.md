---
layout: default
title: Pegaspargase
parent: Model Prediction Only (L5)
nav_order: 1019
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia (Established Use) to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase (Oncaspar) is a long-acting asparagine-depleting enzyme used in the treatment of acute lymphoblastic leukemia (ALL). The TxGNN model predicts it may be effective for **precursor lymphoblastic lymphoma/leukemia**, supported by **over 40 registered clinical trials** and **20 publications**. This is most likely an established, guideline-standard use rather than a new repurposing finding. The US license record supplied has no indication text, so this needs confirming against the label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license record. The literature describes FDA approval for first-line ALL treatment |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (as scored; see caveat below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA103411) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on published literature, pegaspargase is a PEGylated form of E. coli-derived L-asparaginase. It depletes circulating asparagine. Lymphoblasts have low asparagine synthetase expression and depend on external asparagine, so depletion starves the leukemic cells and inhibits protein synthesis.

The predicted indication is the same biological disease family as ALL. Precursor lymphoblastic leukemia and lymphoma are closely related lymphoid neoplasms, and asparaginase is a backbone of pediatric-inspired regimens for both. This explains the very high model score and the large body of trials. Several trials directly cover lymphoblastic lymphoma alongside ALL, including LBL 2018 (NCT04043494) and Total Therapy XVII (NCT03117751).

**Caveat on evidence level.** Most large Phase 3 trials are regimen-level protocols, so they cannot isolate pegaspargase's own contribution. The L1 rating reflects the number of completed Phase 3 trials, not proof of a pegaspargase-specific effect.

---

## Clinical Trial Evidence

Ten of the most relevant trials are shown below. The remaining registered trials are mostly multi-drug ALL protocols.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03020030](https://clinicaltrials.gov/study/NCT03020030) | Phase 3 | Active, not recruiting | 560 | Treatment of newly diagnosed pediatric and adolescent ALL. Pegaspargase is a likely backbone component |
| [NCT04954326](https://clinicaltrials.gov/study/NCT04954326) | Phase 2 | Completed | 89 | Randomized comparison of liquid vs lyophilized pegaspargase (S95014) pharmacokinetics in newly diagnosed pediatric ALL |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2044 | French pediatric ALL protocol focused on optimal L-asparaginase use |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5000 | AIEOP-BFM ALL 2017 international collaborative protocol for children and adolescents |
| [NCT03117751](https://clinicaltrials.gov/study/NCT03117751) | Phase 2/3 | Active, not recruiting | 790 | Total Therapy XVII, a precision-medicine approach in ALL and lymphoblastic lymphoma |
| [NCT02881086](https://clinicaltrials.gov/study/NCT02881086) | Phase 3 | Completed | 1023 | Adult ALL or lymphoblastic lymphoma. Evaluates asparaginase intensification and nelarabine in T-ALL |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | Completed | 40 | Compares native asparaginase vs PEG-asparaginase during induction in relapsed or refractory pediatric ALL |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | MOAD salvage regimen including pegylated asparaginase for relapsed ALL |
| [NCT00184041](https://clinicaltrials.gov/study/NCT00184041) | Phase 2 | Completed | 47 | Intensified post-remission therapy containing PEG-asparaginase in adult ALL |
| [NCT00882206](https://clinicaltrials.gov/study/NCT00882206) | Phase 2 | Terminated | 15 | Decitabine and vorinostat added to chemotherapy with PEG-asparaginase. Terminated early, so limited weight |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231, Phase 3 testing bortezomib in newly diagnosed T-ALL and lymphoblastic lymphoma |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232. Dexamethasone and high-dose methotrexate improved outcomes in high-risk B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434, Phase 3 of nelarabine in newly diagnosed T-ALL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001. Compares efficacy and toxicity of calaspargase pegol vs pegaspargase in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Clinical trial | Blood Adv | GIMEMA LAL1913. Pegaspargase-modified risk-oriented program in adults aged 18–65 |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 trial | Int J Hematol | Efficacy, safety and pharmacokinetics of lyophilized pegaspargase in Japanese patients with untreated ALL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 trial | Leukemia | Long-term follow-up of venetoclax added to hyper-CVAD, nelarabine and pegylated asparaginase in T-ALL/LBL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert consensus on recognizing, preventing and managing asparaginase adverse events in adults |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Asparagine depletion mechanism; PEGylation reduces hypersensitivity and antibody formation |
| [31571395](https://pubmed.ncbi.nlm.nih.gov/31571395/) | 2020 | Cohort | Pediatr Blood Cancer | Rapid desensitization allowed pegaspargase to continue in 9 children with hypersensitivity |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103411 | ONCASPAR (Servier Pharmaceuticals LLC) | Injection, solution | Not listed in the supplied record |

---

## Cytotoxicity

Pegaspargase is an antineoplastic agent, but it is an enzyme rather than a conventional DNA-damaging cytotoxic. The entries below are general expectations and should be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted metabolic therapy (asparagine-depleting enzyme), always used in multi-drug regimens |
| Myelosuppression Risk | Generally low as a single agent. Myelosuppression in regimens mainly comes from companion chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function and bilirubin, amylase/lipase, glucose, triglycerides, coagulation parameters (fibrinogen, antithrombin), CBC, serum asparaginase activity |
| Handling Protection | Please refer to the package insert warnings and precautions and institutional hazardous-drug policy |

---

## Safety Considerations

The package insert warnings, contraindications and drug interaction data were not available in the source record. The following risks are documented in the supplied literature:

- **Hypersensitivity and silent inactivation**: reactions and neutralizing antibodies are common in ALL protocols. Desensitization has been used (PMID 31571395), and hypersensitivity forecasting is under study (NCT06195735).
- **Pancreatitis**: reported in pegaspargase-treated patients (PMID 10696127).
- **Hepatotoxicity**: risk is higher in adolescents, young adults and obese patients. Levocarnitine is being tested for prevention (NCT05602194; PMID 34528411).
- **Thrombosis**: a documented toxicity in the expert consensus (PMID 40109190).
- **Hypertriglyceridemia and hyperglycemia**: reported with pegaspargase, and hyperglycemia is linked in time to its administration (PMID 30823860, PMID 34931744).
- **Older adults**: tolerability is reduced in patients aged 55 or older (PMID 40858769).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The asparagine-depletion mechanism is direct and well established, and many Phase 2/3 trials and consensus literature cover lymphoblastic disease. However, this looks like a marketed, guideline-standard use rather than a novel repurposing. Most trial evidence is regimen-level, so pegaspargase's own contribution cannot be separated.

**To proceed, the following is needed:**
- Confirm the US label indication (the license record has no indication text) to establish whether this is on-label.
- Retrieve package insert warnings and contraindications.
- Add mechanism of action data from DrugBank.
- Set up monitoring for hepatic, pancreatic, coagulation and metabolic toxicity, plus a hypersensitivity management plan.

**Other predicted indications.** Chronic lymphocytic leukemia/small lymphocytic lymphoma (including the two subtype entries), follicular lymphoma and methylcobalamin deficiency type cblE have model scores only and no supporting evidence, so they should be held. The cblE entry is likely a false positive. Hodgkin lymphoma evidence is really about NK/T-cell lymphoma, which should be assessed as a separate entity.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


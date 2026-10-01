---
layout: default
title: Mercaptopurine
parent: Model Prediction Only (L5)
nav_order: 901
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Established Antimetabolite Use to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is an oral purine antimetabolite that is already marketed in the US and widely used in leukemia regimens.
The TxGNN model predicts it may be effective for **myeloid leukemia**.
The retrieved evidence is **29 clinical trials** and **20 publications**, but 6-MP is almost always given inside multi-drug regimens, so its individual contribution is hard to separate.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (see caveat below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Proceed with Guardrails |

The label-approved indication text is empty in the regulatory data, so the original indication is not listed. Several trials show 6-MP as a component of AML/APL regimens, but few test 6-MP itself. The L1 rating rests on completed Phase 3 trials and randomized studies where 6-MP is part of the regimen. Its independent effect is confounded.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Based on the retrieved evidence, mercaptopurine is a purine antimetabolite. Its thioguanine nucleotide metabolites are incorporated into DNA/RNA and inhibit de novo purine synthesis. Rapidly proliferating myeloid blasts depend heavily on nucleotide synthesis, so this mechanism is plausible in myeloid leukemia.

The clinical link is practical rather than purely theoretical. Randomized trials use 6-MP in AML induction (with daunorubicin and cytarabine) and in oral maintenance with methotrexate. Acute promyelocytic leukemia (APL) protocols commonly use maintenance with ATRA plus methotrexate and 6-MP.

Because no original indication is recorded, this may be a historical or label-adjacent use rather than a true repurposing. The prediction is supported mainly by APL and AML regimen studies, not by 6-MP monotherapy data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | Randomized maintenance vs observation in low/intermediate-risk APL. The maintenance arm uses an ATRA plus 6-MP/methotrexate-type regimen (directly relevant) |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Untreated APL. Maintenance with intermittent tretinoin vs tretinoin plus mercaptopurine and methotrexate, with or without arsenic trioxide in consolidation |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA 2005 APL protocol with maintenance of ATRA plus low-dose methotrexate and mercaptopurine |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000 risk-adapted APL therapy, ending in 2 years of maintenance with 6-MP, methotrexate and ATRA |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1068 | AIDA protocol testing intermittent ATRA vs standard methotrexate/6-MP maintenance in PCR-negative APL patients |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | APL treated with ATRA plus idarubicin, with ATRA + methotrexate + mercaptopurine maintenance and salvage |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Gemtuzumab ozogamicin doses vs a 2-year ATRA plus chemotherapy maintenance in intermediate/high-risk APL (maintenance likely includes 6-MP) |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | Androgen addition to post-remission therapy in elderly AML. Whether 6-MP is in the regimen cannot be confirmed |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax plus 6-mercaptopurine in relapsed/refractory AML (oral combination) |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | 6-MP plus valproic acid (or hydroxyurea plus valproic acid) in AML/high-risk MDS patients unfit for standard therapy |

Most of the other retrieved trials are lymphoblastic-leukemia protocols, APL trials without 6-MP as the study question, or unrelated designs (for example an economic analysis of transfusions).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92. Adding etoposide to daunorubicin, behenoyl cytarabine and 6-MP induction gave no beneficial effect in adult AML |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | Nationwide Japanese trial (433 enrolled, 360 evaluable). Daunorubicin vs aclarubicin, each with cytarabine, 6-MP and prednisolone. CR rates 63.7% vs 53.9% (P=0.0587) |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Two years of oral maintenance with daily 6-MP and weekly methotrexate in transplant-ineligible AML patients. Leukemia-free and overall survival were assessed |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Clinical trial | Cancer Investigation | Pilot of high-dose 6-MP plus intermediate-dose cytarabine in first remission of childhood AML. 14 of 17 patients reached complete remission on conventional induction |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Clinical study | Int J Hematol | Induction with behenoyl cytarabine, daunorubicin and 6-MP in 41 adults with AML. 71% achieved complete remission |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | Clinical study | Chin Med J (Taipei) | Cytarabine, daunorubicin and 6-MP induction in 34 adults with AML in Taiwan |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Clinical study | Cancer | 18 children with AML treated with cytarabine, daunorubicin, prednisolone and 6-MP or thioguanine. 78% initial remission, median survival 7 months |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Rinsho Ketsueki | Japanese review of current AML and APL therapy (no abstract available) |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Cohort | JAMA Oncol | Safety signal. Therapy for autoimmune disease is associated with therapy-related MDS and AML |
| [28835099](https://pubmed.ncbi.nlm.nih.gov/28835099/) | 2017 | Preclinical | Biomacromolecules | CD44-targeted hyaluronic acid–6-MP nanoprodrug designed to improve solubility and efficacy in AML |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA040528 | Mercaptopurine (Hikma Pharmaceuticals USA Inc.) | Tablet |
| NDA009053 | Mercaptopurine (Florida Pharmaceutical Products, LLC) | Tablet |
| NDA205919 | Mercaptopurine (Nova Laboratories, Ltd) | Oral suspension |
| ANDA216418 | Mercaptopurine (Hikma Pharmaceuticals USA Inc.) | Oral suspension |

The input lists 7 authorizations in total but shows only 5 records, with ANDA216418 appearing twice. Approved-indication text was not provided.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine antimetabolite / thiopurine) |
| Myelosuppression Risk | Moderate to high. Neutropenia is the main dose-limiting effect, and NUDT15 and TPMT variants markedly increase the risk |
| Emetogenicity Classification | Low (oral dosing) |
| Monitoring Items | CBC with differential, liver function, TPMT/NUDT15 genotype (or activity), metabolite levels where available |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Warnings, contraindications and drug interactions were not available in the input.

The retrieved literature also flags these points for 6-MP:
- **Neutropenia** is strongly associated with NUDT15 variants and TPMT status.
- **Hepatotoxicity** and, rarely, **hypoglycemia** have been reported.
- Allopurinol co-administration has been studied as a way to alter 6-MP metabolite profiles.
- Thiopurine exposure has been linked to secondary lymphoma and myeloid neoplasms in other populations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Completed Phase 3 and Phase 4 APL/AML trials, plus older randomized AML studies, include 6-MP in induction or maintenance, and the drug is marketed in the US. The evidence is confounded because 6-MP is always part of a multi-drug regimen, and most of the strongest trial data comes from APL rather than AML broadly. The lack of an original indication also suggests this may be historical use rather than true repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism-of-action data from DrugBank
- Confirmation that 6-MP is actually in the regimen for trials where it is only assumed (NCT00700544, NCT00962767)
- Results data showing what 6-MP contributes within APL/AML regimens, for example maintenance with vs without 6-MP
- A guardrail plan covering TPMT/NUDT15-guided dosing, blood count monitoring and adherence support

Other predictions for this drug (acute lymphoblastic leukemia, precursor lymphoblastic lymphoma/leukemia) also reach L1, but they reflect established standard-of-care use rather than novel repurposing. The remaining predictions have little or no supporting evidence, and most are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


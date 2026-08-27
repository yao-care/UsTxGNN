---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 900
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP, DB01033) is a purine analog antimetabolite classically used as backbone maintenance therapy for acute lymphoblastic leukemia (ALL) — this is confirmed later in this same evidence pack (see the drug's own rank-10 prediction, which the model essentially "rediscovers" as ALL), though the official TFDA indication text itself is a data gap since the drug is not currently marketed in Taiwan. The TxGNN model's top prediction is that it may also be effective for **Myeloid Leukemia**, with **29 clinical trials** and **20 publications** currently identified as supporting evidence, though most of this evidence is historical (1960s–1990s regimens) rather than contemporary practice.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (based on established pharmacology; official TFDA label text is a data gap — see below) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack). Based on known pharmacology, mercaptopurine is a thiopurine antimetabolite that is converted intracellularly to thioguanine nucleotides, which are incorporated into DNA/RNA and inhibit de novo purine synthesis — this mechanism underlies its established efficacy as ALL maintenance therapy.

The rationale for extending this to myeloid leukemia is mechanistic continuity rather than a novel biological hypothesis: 6-MP has historically been used as a component of post-remission/maintenance regimens for acute myeloid leukemia (AML) and acute promyelocytic leukemia (APL), typically combined with methotrexate (MTX) and, in APL, with ATRA. The proliferation-inhibiting mechanism (purine synthesis blockade) applies to any rapidly dividing hematopoietic blast population, not just lymphoblasts.

However, this evidence pack's own analysis flags an important caveat: most of the supporting trials use 6-MP as one component of a multi-drug maintenance regimen rather than as the primary therapeutic driver, and modern AML/APL treatment has largely moved toward other agents (e.g., arsenic trioxide, gemtuzumab ozogamicin, venetoclax combinations). The strongest and most contemporary signal is a small number of recent early-phase trials (e.g., NCT05506332, NCT06199557) directly testing 6-MP-based combinations in relapsed/refractory or unfit AML/MDS populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax + 6-mercaptopurine combination in relapsed/refractory AML (ApoAML trial) |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea+valproic acid or 6-MP+valproic acid in AML/high-risk MDS patients unfit for standard therapy |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | ATRA+chemo ± arsenic trioxide induction, with maintenance using intermittent tretinoin plus mercaptopurine and methotrexate, in untreated APL |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005: risk-adapted APL therapy with maintenance using ATRA + low-dose methotrexate + mercaptopurine |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1068 | AIDA protocol for newly diagnosed APL; maintenance with methotrexate and 6-mercaptopurine, plus ATRA |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | ATRA+idarubicin (AIDA) induction for APL; ATRA+methotrexate+mercaptopurine salvage therapy for relapse |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000 risk-adapted APL therapy; 2-year maintenance with 6-mercaptopurine, methotrexate and ATRA |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | GOELAMS SA-2002: post-remission maintenance ± androgens in elderly AML (6-MP-containing maintenance backbone; androgen is the primary variable) |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: maintenance vs. observation in low/intermediate-risk APL after prior treatment |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Gemtuzumab ozogamicin vs. 2-year ATRA+chemo maintenance as post-consolidation treatment in intermediate/high-risk APL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | International Journal of Hematology | JALSG-AML92: no added benefit from etoposide added to daunorubicin/cytarabine/6-MP induction in adult AML |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemotherapy and Pharmacology | Nationwide randomized trial: daunorubicin vs. aclarubicin combined with BHAC/6-MP/prednisolone in untreated AML |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | Journal of Clinical Oncology | Japan Leukemia Study Group: behenoyl cytarabine vs. cytarabine in induction/consolidation, ± ubenimex, adult AML |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | Journal of Korean Medical Science | Oral maintenance with 6-MP + methotrexate in AML patients ineligible for transplantation |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Cohort | Cancer Investigation | High-dose continuous IV 6-MP followed by intermediate-dose cytarabine during first AML remission (pediatric pilot) |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | Current therapy overview for AML and APL |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Cohort | International Journal of Hematology | Intensive individualized induction with BHAC, daunorubicin and 6-MP, followed by intensive consolidation in adult AML |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | Cohort | Chinese Medical Journal | Combination chemotherapy with cytarabine, daunorubicin and 6-MP for adult AML |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case series | Minnesota Medicine | Early historical report on AML treatment with 6-MP and cyclophosphamide |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Case series | Cancer | Childhood AML treated with cytarabine, daunorubicin, prednisolone, and mercaptopurine or thioguanine |

---

## Taiwan Market Information

No TFDA license records are present in this evidence pack — mercaptopurine's current status is recorded as **未上市 (Not Marketed)** with **0** licenses on file.

---

## Cytotoxicity

Mercaptopurine is an antineoplastic antimetabolite (purine analog / thiopurine class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite — thiopurine/purine analog) |
| Myelosuppression Risk | High — myelosuppression is the drug's core dose-limiting and therapeutic mechanism; risk is markedly increased in TPMT/NUDT15 poor-metabolizer genotypes |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests, TPMT/NUDT15 genotype or phenotype where available |
| Handling Protection | Should be handled per institutional cytotoxic/hazardous drug handling protocols |

No DrugBank-sourced toxicity data was available in this evidence pack (MOA is a High-severity data gap); the above reflects the well-established pharmacological class profile and should be confirmed against the official package insert once available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all recorded as data gaps in this evidence pack, and the DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by a large volume (29 trials, 20 publications) of L1-level evidence, but the mechanistic link is one of established historical use (6-MP as a maintenance-regimen component in AML/APL) rather than a novel repurposing signal, and much of the trial evidence is decades old with the drug playing a secondary role alongside other agents. The most clinically relevant contemporary signal is limited to two small early-phase trials (NCT05506332, NCT06199557) in relapsed/refractory or treatment-unfit populations.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap preventing safety pre-screening
- DrugBank/primary-literature mechanism of action data — currently a High-severity gap affecting mechanistic assessment
- Confirmation of the drug's officially approved original indication text (original_indications is empty in this record)
- Clinical/pharmacist review to distinguish "6-MP as adjunctive maintenance component" from "6-MP as a primary therapeutic driver" for myeloid leukemia before advancing further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


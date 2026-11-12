---
layout: default
title: Hyaluronidase
parent: Model Prediction Only (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
monitor_inn: "HYALURONIDASE"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
last_modified_at: 2026-11-12
description: "Hyaluronidase: predicted new indication Esotropia (evidence level L5). Approved use: Not recorded in the local data"
---

# Hyaluronidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Hyaluronidase: Esotropia
{: .text-alpha }

## One-Sentence Summary

Hyaluronidase is an enzyme that breaks down hyaluronan. It is used mainly to help other injected drugs spread through tissue.
The TxGNN model's top-ranked prediction is esotropia, but the best-supported direction is **Diabetic Retinopathy** (ranked 6th), where **3 clinical trials** (including 2 completed Phase 3 trials) and **18 publications** exist.
Most of the other top-10 predictions have little or no supporting evidence.

<!-- review:begin us-lic-20261106-hyaluronidase-4 -->

> **Review correction (2026-11-06)**: Originally stated: "It is used mainly to help other injected drugs spread through tissue, and it is part of several subcutaneous biologic formulations." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-hyaluronidase-4 -->

---

## Quick Overview

The top-ranked prediction (esotropia) has no supporting evidence. This report therefore also covers diabetic retinopathy, the best-supported candidate.

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | Esotropia L5 (adverse-event reports only); diabetic retinopathy L5 (nominal, outcomes unverified) |
| US Market Status | Marketed (active FDA-approved applications: 2 of 3; OTC monograph / unapproved listings: 6) |
| Number of FDA Applications | 3 (active: 2) |
| Recommended Decision | Hold (esotropia); Hold, with a research question for diabetic retinopathy |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, hyaluronidase degrades hyaluronan, a major component of the extracellular matrix and the vitreous gel. That property explains its use as a "spreading agent" in injections.

**Diabetic retinopathy (best-supported direction).** Injected into the vitreous, hyaluronidase can liquefy the vitreous gel, promote posterior vitreous detachment, and help clear vitreous hemorrhage. This is called pharmacologic vitreolysis. Supporting work includes:
- Animal studies in diabetic rats.
- Enzyme-induced vitreolysis that appears to slow retinopathy progression through the HIF-1α pathway.
- Recent work linking dysregulated hyaluronan metabolism to inflammation and angiogenesis in proliferative diabetic retinopathy.

Caveats: the efficacy results of the two large Phase 3 trials are not in the data compiled for this report. Ovine hyaluronidase was never established as a standard therapy for this condition, and anti-VEGF drugs and laser treatment are now the standard of care.

**Esotropia (top-ranked).** No mechanistic link to treatment was found. The only publication describes persistent diplopia and strabismus as a *complication* after cataract surgery under local anesthesia, where hyaluronidase is an adjuvant in the block. This is an adverse-event association, not a therapeutic one. The high model score is not supported by clinical evidence.

**Other predictions.**
- **Amenorrhea:** the only publication is a 1975 laboratory study of endogenous enzyme activity.
- **Dermatitis:** mostly indirect literature, and inhibitors of hyaluronidase appear to improve experimental dermatitis. That is the opposite of the direction needed.
- **Diabetic cataract:** indirect, with a 1978 study suggesting hyaluronidase may *increase* cystoid macular edema after surgery.
- **Renal tubular acidosis, acrodermatitis chronica atrophicans, neonatal dermatomyositis, esophageal malformation:** no trials or literature, and no plausible mechanism.

---

## Clinical Trial Evidence

No clinical trials are registered for esotropia. The trials below are for diabetic retinopathy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Vitrase (ovine hyaluronidase) intravitreal injection for clearance of severe vitreous hemorrhage; efficacy results not available in the data compiled |
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Replicate Phase 3 study of Vitrase for severe vitreous hemorrhage; efficacy results not available in the data compiled |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label study of intravitreal Vitrase to induce posterior vitreous detachment in moderate to severe non-proliferative diabetic retinopathy; small and uncontrolled, safety signal only |

---

## Literature Evidence

Diabetic retinopathy (selected from 18 publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Curr Pharm Biotechnol | Reviews pharmacologic vitreolysis; intravitreal ovine hyaluronidase was effective in clearing vitreous hemorrhage |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Exp Diabetes Res | Current and future pharmacotherapies for diabetic retinopathy |
| [19644368](https://pubmed.ncbi.nlm.nih.gov/19644368/) | 2009 | Review | Curr Opin Ophthalmol | Changing treatment paradigms in diabetic retinopathy |
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Basic/translational | Front Immunol | Dysregulated hyaluronan metabolism drives inflammation and angiogenesis in proliferative diabetic retinopathy |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Animal study | Invest Ophthalmol Vis Sci | Enzyme-induced vitreolysis can slow retinopathy progression via the HIF-1α pathway |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Animal study | Retina | Plasmin and hyaluronidase vitreolysis is feasible in diabetic rats |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | Animal study | Exp Eye Res | Effect of diabetes and hyaluronidase on the retinal endothelial glycocalyx in mice |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug profile | Drugs R D | Profile of ophthalmic ovine hyaluronidase (Vitrase) for vitreous hemorrhage and diabetic retinopathy |
| [34293791](https://pubmed.ncbi.nlm.nih.gov/34293791/) | 2022 | Pharmacokinetic study | Ophthalmic Plast Reconstr Surg | Examines whether retrobulbar hyaluronidase reaches the vitreous cavity |

Other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | Case report | Binocul Vis Strabismus Q | Esotropia: persistent diplopia and strabismus after cataract surgery under local anesthesia (a complication, not a treatment) |
| [37145319](https://pubmed.ncbi.nlm.nih.gov/37145319/) | 2024 | Review | Aesthetic Plast Surg | Dermatitis: allergic complications of hyaluronidase injection and management |
| [367238](https://pubmed.ncbi.nlm.nih.gov/367238/) | 1978 | Clinical study | Ann Ophthalmol | Diabetic cataract: a 25% incidence of cystoid macular edema in patients receiving hyaluronidase with local anesthetic, none in controls |

---

## US Market Information

The indication text is not recorded for any of them.

<!-- review:begin us-lic-20261106-hyaluronidase-1 -->

> **Review correction (2026-11-06)**: Originally stated: "10 of 10 licenses are valid, and the indication text is not recorded for any of them. Most of the products are subcutaneous biologic formulations in which hyaluronidase is a component." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-hyaluronidase-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA021640 | VITRASE | BAUSCH AND LOMB | Injectable; injection | Valid |
| BLA021665 | AMPHADASE | AMPHASTAR PHARM | Injectable; injection | Valid |
| BLA021716 | HYDASE | AKORN INC | Injectable; injection | Discontinued in Drugs@FDA |
| NDC 43742-2223 | Pest and Dustmite Formula | Deseret Biologicals, Inc. | Liquid | NDC listing, no FDA application (unapproved homeopathic) |
| NDC 43742-1548 | Pest and Dustmite Formula | Deseret Biologicals, Inc. | Liquid | NDC listing, no FDA application (unapproved homeopathic) |

Showing 5 of 9 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions:** 63 interactions were identified; all those listed are rated Minor. They include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), antihistamines (promethazine, chlorpheniramine, loratadine, cetirizine), local anesthetics (lidocaine, articaine), estrogens (estradiol, ethinylestradiol, conjugated estrogens), and aspirin.
- **Hypersensitivity (from the literature):** a 2024 review describes allergic complications of hyaluronidase injection that are often misdiagnosed.
- **Ocular signals (from the literature):** a 1978 study reported a higher incidence of cystoid macular edema with hyaluronidase added to anesthetic. Strabismus and diplopia have been reported after anesthetic blocks that used hyaluronidase.

<!-- review:begin us-lic-20261106-hyaluronidase-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Five further cancelled BLAs are on record: Opdivo Qvantig, Rybrevant Faspro (two entries), Vyvgart Hytrulo, and Tecentriq Hybreza." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-hyaluronidase-2 -->

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, esotropia, rests on a model score alone, and its only publication describes a complication rather than a treatment.
- Diabetic retinopathy is the only direction with real clinical-trial history, two completed Phase 3 trials. However, their efficacy outcomes were not available, and the program is historical. Anti-VEGF drugs and laser are now standard care. This direction is best treated as a research question rather than a Go.
- The drug is marketed in the US, and the package insert's warnings and contraindications are missing from the data.

<!-- review:begin us-lic-20261106-hyaluronidase-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US, with 10 of 10 licenses valid, and the package insert's warnings and contraindications are missing from the data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-hyaluronidase-3 -->

**To proceed, the following is needed:**
- The efficacy and safety results of NCT00198497 and NCT00198510 (published papers or registry results).
- The package insert warnings and contraindications, which are a blocking data gap.
- Detailed mechanism-of-action data from DrugBank.
- A comparison against current standards of care (anti-VEGF, laser, vitrectomy) to define any remaining unmet need.
- A route and formulation assessment, since the intravitreal route would need a product with an active license.
- Safety monitoring plans for hypersensitivity and ocular adverse events.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "10 of 10 licenses are valid, and t Most of the products are subcutaneous biologic formulations in which hyaluronidase is a component" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Five further cancelled BLAs are on record: Opdivo Qvantig, Rybrevant Faspro (two entries), Vyvgart Hytrulo, and Tecentriq Hybreza" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 10 of 10 licenses valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and it is part of several subcutaneous biologic formulations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


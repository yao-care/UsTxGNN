---
layout: default
title: Polidocanol
parent: Model Prediction Only (L5)
nav_order: 1059
evidence_level: L5
indication_count: 10
---

# Polidocanol
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

# Polidocanol: From Varicose Veins to Esophageal Varices with Bleeding

## One-Sentence Summary

Polidocanol is an injectable sclerosant, marketed in the US as Asclera. Published literature describes it as approved for varicose veins and spider veins, although the license record supplied does not state an indication.
The TxGNN model predicts it may be useful for **esophageal varices with bleeding**, a use that endoscopic sclerotherapy has long established.
The prediction is supported by **7 clinical trials** (only 1 rated directly relevant) and **20 publications**, including several randomized trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Varicose veins and spider veins (from the literature review PMID 29473522; the license record lists no indication text) |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 by the stated rules (the source pack labelled it L1, but only one completed Phase 3 trial is present, and its polidocanol arm is unconfirmed) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records listed, both for the same NDA (NDA021201) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank. The following rests on the drug's known pharmacology. Polidocanol is a detergent sclerosant. When injected into or beside a vein, it damages the endothelium, which leads to thrombosis and fibrosis and closes off the vessel. This local action is the same one used to treat varicose veins.

Esophageal varices are dilated veins caused by portal hypertension. Closing them with an injected sclerosant is a direct application of the same mechanism, and the trials and papers in this pack show it has been done in practice for decades. This prediction is therefore closer to confirming an established use than to discovering a new one. The empty original-indication field in the data is a data gap, not evidence of no prior use.

The main uncertainty is how sclerotherapy compares with alternatives such as band ligation. These trials mostly do not test polidocanol alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02361593](https://clinicaltrials.gov/study/NCT02361593) | N/A | Completed | 120 | Randomized trial of transparent cap-assisted endoscopic sclerotherapy with lauromacrogol (the same compound as polidocanol) in esophageal varices. Directly relevant (Grade A), but no results are in the data. |
| [NCT00161915](https://clinicaltrials.gov/study/NCT00161915) | Phase 3 | Completed | Not reported | Fibrin sealant injection versus band ligation, with or without polidocanol, for hemostasis and rebleeding prevention in bleeding esophageal varices. Whether polidocanol is a study arm cannot be confirmed (Grade B). |
| [NCT01923064](https://clinicaltrials.gov/study/NCT01923064) | N/A | Completed | 96 | Cyanoacrylate-lipiodol versus cyanoacrylate-lauromacrogol injection in gastric varices. Indirect (Grade C). |
| [NCT02468206](https://clinicaltrials.gov/study/NCT02468206) | N/A | Completed | 64 | Cyanoacrylate injection versus BRTO for preventing gastric variceal rebleeding. Polidocanol is not evidently involved (Grade C). |
| [NCT02468167](https://clinicaltrials.gov/study/NCT02468167) | N/A | Unknown | 70 | Cyanoacrylate versus BRTO in acute gastric variceal bleeding. Background on competing treatments only (Grade C). |
| [NCT02468180](https://clinicaltrials.gov/study/NCT02468180) | N/A | Unknown | 70 | Cyanoacrylate versus BRTO for primary prophylaxis of gastric variceal bleeding. Polidocanol is not evidently involved (Grade C). |
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | N/A | Unknown | 70 | EUS-guided coil plus cyanoacrylate versus BRTO in gastric varices. No polidocanol arm is evident (Grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | RCT | Endoscopy | Prospective study of cyanoacrylate plus polidocanol versus polidocanol alone in bleeding esophageal varices in patients with cirrhosis, in both emergency and long-term elective care. |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | RCT | Gastrointest Endosc | Ligation alone versus combined ligation and sclerotherapy for bleeding esophageal varices. |
| [10376453](https://pubmed.ncbi.nlm.nih.gov/10376453/) | 1999 | RCT | Endoscopy | Combined ligation and sclerotherapy versus ligation alone, testing whether the combination eradicates bleeding varices faster. |
| [35879573](https://pubmed.ncbi.nlm.nih.gov/35879573/) | 2022 | Prospective randomized study | Surg Endosc | Balloon compression-assisted injection sclerotherapy versus band ligation for eradicating esophageal varices. Polidocanol use is not confirmed in the abstract. |
| [9514542](https://pubmed.ncbi.nlm.nih.gov/9514542/) | 1998 | Comparative study | J Hepatol | Fibrin glue versus polidocanol sclerotherapy to prevent early rebleeding after esophageal variceal bleeding, comparing safety and efficacy. |
| [3069543](https://pubmed.ncbi.nlm.nih.gov/3069543/) | 1988 | Comparative study | Gastroenterol Clin Biol | In 74 patients with bleeding esophageal varices, intravariceal polidocanol (43 patients) was compared with perivariceal quinine-urea (31 patients). |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Review | Curr Clin Pharmacol | Evidence-based review of off-label uses of polidocanol, which is approved for varicose and spider veins. |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohort | Arch Pediatr | Efficacy and safety of paravariceal polidocanol sclerotherapy for cardiac varices in children and adolescents. |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Case series | Gut | Of 34 patients given 3% polidocanol injections, 20 (59%) developed esophageal stricture or dysphagia. |
| [1778718](https://pubmed.ncbi.nlm.nih.gov/1778718/) | 1991 | Case series | Int Surg | Of 457 patients treated with endoscopic injection sclerotherapy, 28 (6%) bled from the upper GI tract afterward. The title notes such gastric bleeding may be fatal. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021201 | Asclera (Methapharm, Inc) | Injection, solution | Not provided in the license record. The literature describes approval for varicose veins and spider veins. |

The pack lists this NDA twice, so it is shown here once.

## Safety Considerations

No package insert warnings or contraindications are available, and no drug interactions were found in the data. Please refer to the package insert for safety information.

The literature above reports these risks of endoscopic sclerotherapy:
- **Stricture and dysphagia**: 59% (20 of 34) of patients in one polidocanol series (PMID 6609102).
- **Post-treatment bleeding**: 6% of 457 patients bled after injection sclerotherapy, and gastric bleeding may be fatal (PMID 1778718).
- **Rebleeding and ulceration**: the pack notes both as risks, and the pediatric cardiac varices study (PMID 36509625) centers on rebleeding from band-ligation ulcers.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct and local, and decades of randomized and observational studies show polidocanol sclerotherapy is used for esophageal varices. However, the trials are mostly indirect, the one Phase 3 trial does not confirm a polidocanol arm, and the drug carries real stricture and bleeding risks. Use should be limited to experienced endoscopists and considered alongside or after band ligation.

The lower-ranked predictions are weaker:
- **Esophageal varices without bleeding**: a research question at L2, because the trials are not polidocanol-specific for prophylaxis.
- **Ranks 3 to 10**: Hold. They have no trials or literature and no plausible mechanism, and the scores likely reflect knowledge-graph artifacts.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the polidocanol arms in NCT00161915, and results from NCT02361593
- A head-to-head comparison of polidocanol sclerotherapy against band ligation in current guidelines
- Confirmation of the US regulatory position. Endoscopic use appears to be outside the varicose vein labeling of Asclera, so it would need to be handled as off-label use.
- Verification of the evidence level, since the pack's L1 label does not meet the L1 rule of at least two completed Phase 3 RCTs

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


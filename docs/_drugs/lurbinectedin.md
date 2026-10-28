---
layout: default
title: Lurbinectedin
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
monitor_inn: "LURBINECTEDIN"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "cytomegalovirus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "malignant catarrh", "infectious bovine rhinotracheitis", "Mills syndrome"]
last_modified_at: 2026-10-14
description: "Lurbinectedin: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the compiled data"
---

# Lurbinectedin
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

## Lurbinectedin: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Lurbinectedin is an injectable anticancer drug marketed in the US as ZEPZELCA. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge of the drug, lurbinectedin is an alkylating agent that binds guanines in the DNA minor groove and inhibits oncogenic transcription. It is known to be used in relapsed small cell lung cancer, which is a neuroendocrine tumour. This background is not drawn from the compiled data and should be verified.

Multiple endocrine neoplasia (MEN) syndromes involve tumors of endocrine and neuroendocrine tissue. A link between a transcription-inhibiting cytotoxic agent used in a neuroendocrine cancer and MEN-associated neuroendocrine tumors is plausible. It remains a hypothesis, however, because the TxGNN score is high (0.9944) but no trials or publications support it.

Other predicted indications were also reviewed. None has any supporting trial or publication, and all are rated L5 with a Hold recommendation:

- HIV infection, cytomegalovirus infection, rheumatoid arthritis and amyotrophic lateral sclerosis have no clear mechanistic rationale. A cytotoxic agent also carries immunosuppression and toxicity concerns in these populations.
- Feline AIDS, simian immunodeficiency virus infection, malignant catarrh, infectious bovine rhinotracheitis and Mills syndrome are veterinary or very rare conditions. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They are not relevant to human development.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213702 (cancelled) | ZEPZELCA (Jazz Pharmaceuticals, Inc.) | Injection, powder, lyophilized, for solution | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating-type agent, based on general knowledge) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC and liver function) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The first 20 reviewed include these main ones:
  - **Major**: aprepitant, dexamethasone, clarithromycin, cobicistat, deferiprone, samarium (153Sm) lexidronam, lumacaftor
  - **Moderate**: cimetidine, naltrexone, clotrimazole, glycerol phenylbutyrate, metreleptin, troglitazone, deferasirox, palifermin, strontium chloride Sr-89, ticagrelor, ivacaftor, mercaptopurine
  - **Minor**: levofloxacin

  Many of the major interactions involve CYP3A-modulating drugs. Concomitant use should be reviewed carefully.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the original indication and mechanism data are missing, and the US license is cancelled. The evidence level is L5.

**To proceed, the following is needed:**
- The FDA package insert, including approved indication, warnings and contraindications
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search for lurbinectedin in neuroendocrine tumours and MEN syndromes
- Clarification of the cancelled license status
- A risk-benefit assessment of cytotoxicity and the major drug interactions for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Streptozocin
parent: Model Prediction Only (L5)
nav_order: 1183
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

# Streptozocin: From Pancreatic Neuroendocrine Tumors (Presumed) to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Streptozocin is a nitrosourea alkylating agent. The data compiled for this report list no approved indication text, but its established clinical use is in pancreatic neuroendocrine tumors.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.
The second-ranked prediction, **small cell lung carcinoma**, has **2 publications** that mention streptozocin only indirectly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the license record has no indication text) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, streptozocin is a nitrosourea alkylating agent. It is taken up selectively by pancreatic beta cells through the GLUT2 transporter, which is why it is used against pancreatic neuroendocrine tumors.

For multiple sclerosis, the only rationale is that cytotoxic, immunosuppressive agents have been used in MS. This is weak. The 99.97% score is a model output with no trials or literature behind it. The known toxicity profile (kidney toxicity, myelosuppression, diabetogenic effects) makes a favorable benefit-risk balance unlikely for a chronic autoimmune condition.

**Other predictions in the top 10** (all Hold):
- **Small cell lung carcinoma (L4):** A biological analogy exists, since it is a high-grade neuroendocrine carcinoma. The retrieved papers concern pancreatic and carcinoid tumors, not SCLC, and SCLC is standardly treated with platinum-etoposide.
- **Pulmonary blastoma, well-differentiated fetal adenocarcinoma of the lung, primary pulmonary lymphoma, lymphosarcoma, rhabdomyosarcoma and two subtypes (parameningeal embryonal; embryonal extrahepatic bile duct) (L5):** Only a generic cytotoxic rationale, with no supporting data.
- **Hereditary breast ovarian cancer syndrome (L5):** Theoretical sensitivity of BRCA-deficient cells to DNA-damaging agents, but platinum and PARP inhibitors are preferred.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top prediction (relapsing-remitting multiple sclerosis). The following two publications were retrieved for the second-ranked prediction, small cell lung carcinoma:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25841679](https://pubmed.ncbi.nlm.nih.gov/25841679/) | 2013 | Review | Chinese Clinical Oncology | Overview of emerging therapies for pancreatic neuroendocrine tumors; does not address SCLC directly |
| [12115345](https://pubmed.ncbi.nlm.nih.gov/12115345/) | 2002 | Preclinical/Experimental | Cancer | 7-Hydroxytryptophan as a cytotoxic agent for carcinoids and serotonin-producing tumors (including SCLC); streptozocin is cited only as a conventional agent with disappointing results |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Zanosar | Powder, for solution | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (knowledge graph data link it to leukopenia, thrombocytopenia and anemia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; at minimum CBC, kidney and liver function, and blood glucose are relevant given the toxicity profile |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, leukopenia, anemia (including macrocytic anemia), blood coagulation disease, diabetes mellitus, diabetic ketoacidosis, infectious disease (including fungal infection and dermatophytosis), and pyoureter.
- **Drug Interactions:** The interaction query returned 100 records. Among those listed, the main ones are:
  - **Major:** iodinated contrast agents (iothalamic acid, diatrizoate, iopromide, iopamidol, iohexol, iodipamide, iodixanol, ioversol, ioxilan), deferiprone, and samarium (153Sm) lexidronam
  - **Moderate:** palifermin, strontium chloride Sr-89, mercaptopurine, roflumilast, chloramphenicol (including ophthalmic), zidovudine, and tetanus toxoid vaccine
  - **Minor:** levofloxacin

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (relapsing-remitting multiple sclerosis) is supported only by the model score, with no trials or literature. The drug's toxicity (kidney, bone marrow, diabetogenic) is hard to justify in a chronic autoimmune disease. The US license is cancelled, and label-level safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the original approved indication
- Preclinical or mechanistic evidence for streptozocin in MS, or a shift of focus to neuroendocrine-related predictions (e.g., SCLC) with direct supporting studies
- A benefit-risk assessment against established disease-modifying MS therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


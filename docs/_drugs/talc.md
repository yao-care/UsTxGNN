---
layout: default
title: Talc
parent: Model Prediction Only (L5)
nav_order: 1195
evidence_level: L5
indication_count: 10
monitor_inn: "TALC"
predicted_indications: ["thrombotic disease", "exostosis", "rheumatoid arthritis", "bronchitis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "vein disease", "fibromyalgia", "myositis fibrosa"]
last_modified_at: 2026-10-14
description: "Talc: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not available"
---

# Talc
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

## Talc: From No Documented Original Indication to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Talc (a mineral, magnesium silicate) has no approved indication recorded in the US regulatory data compiled for this report, and both of its US licenses are cancelled.
The TxGNN model predicts it may be effective for **thrombotic disease**, but there are **0 clinical trials** and only **11 publications**, and those publications describe talc as a *cause* of thrombosis and embolism, not a treatment.
This is a model-association artifact rather than a credible repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the license records) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 (mechanism and case-level literature only; the literature points to harm) |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Talc is a mineral (hydrated magnesium silicate) used in powder form, historically for procedures such as pleurodesis and as a pharmaceutical excipient. It is not a drug with a known receptor- or enzyme-based pharmacology.

The available literature does **not** support a therapeutic mechanism in thrombotic disease. Reports describe the opposite: intravenous talc from illicit drug use causes pulmonary granulomatosis, angiothrombotic pulmonary hypertension, and retinal and cerebral microembolization. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a treatment effect. Several retrieved papers (Trousseau syndrome, pneumothorax, chylothorax) are unrelated to talc as a treatment for thrombosis.

The other nine predictions (e.g., exostosis, rheumatoid arthritis, bronchitis, heparin cofactor 2 deficiency, fibromyalgia, myositis fibrosa) are likewise unsupported. Several are mechanistically implausible or run against talc's known inflammatory and fibrosing properties.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Review | Current Opinion in Oncology | Intrathoracic complications of malignancy; superior vena cava thrombosis linked to venous access devices. Not about talc as therapy. |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Case report | Archives of Neurology | Drug abuser with medullary infarctions and systemic talc granulomatosis after IV injection. |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Case report | Archives of Pathology & Laboratory Medicine | Pulmonary granulomatosis from injected tablet fillers; the main vascular lesion was thrombosis. |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Case series | Journal of the Canadian Association of Radiologists | Talc granulomatosis and angiothrombotic pulmonary hypertension in drug addicts. |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Case report | American Journal of the Medical Sciences | Retinal and cerebral microembolization of talc in a drug abuser. |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Case report | Deutsche Medizinische Wochenschrift | Acute right heart failure after IV heroin and crushed flunitrazepam tablets. |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Case report | Revista Clínica Española | Angiothrombotic pulmonary granulomatosis in IV drug users; talc provokes thrombotic phenomena in lung vessels. |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Not classified | International Ophthalmology | Foveal avascular zone enlarged in retinal vein occlusion; talc retinopathy mentioned as a vaso-occlusive condition. |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Case report | Texas Heart Institute Journal | Trousseau syndrome with occult colon cancer; unrelated to talc treatment. |

All retrieved papers are either case-level reports of talc-induced harm or unrelated to talc therapy. None shows a therapeutic benefit in thrombotic disease.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205555 | Steritalc (Novatech SA) | Powder | Not available (valid) |
| Not available | Sensitive Pocket Sun (Shantou Oushiya Biotechnology Co., Ltd) | Stick | Not available (cancelled) |

---

## Safety Considerations

The literature compiled for this report points to a safety signal rather than a repurposing opportunity:

- **Vascular and embolic harm**: Intravenous talc is associated with pulmonary granulomatosis, angiothrombotic pulmonary hypertension, and retinal and cerebral microembolization.
- **Respiratory harm**: Occupational and case reports link talc inhalation to airway disease, including endobronchitis, airway stricture, and pneumoconiosis.
- **Fibrosis and inflammation**: Talc is an inflammatory, fibrosing agent, which argues against benefit in conditions such as rheumatoid arthritis or myositis fibrosa.

No drug-interaction data were found, and no knowledge-graph contraindications were identified. Please refer to the package insert for formal warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9985 TxGNN score is not backed by any clinical trial, and the available literature describes talc as a cause of thrombosis and embolism. The predicted indication is therefore not supported mechanistically or clinically, and none of the other nine predictions has credible support either.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data
- Any prospective evidence of therapeutic benefit in thrombotic disease; without it, this candidate should not advance beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


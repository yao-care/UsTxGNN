---
layout: default
title: Talc
parent: Moderate Evidence (L3-L4)
nav_order: 1195
evidence_level: L4
indication_count: 10
---

# Talc
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Talc: From Pleurodesis to Thrombotic Disease

## One-Sentence Summary

Talc is sold in the US as a sterile powder (Steritalc) and as a cosmetic-type stick. Its established medical use in the retrieved literature is pleural sclerosis (pleurodesis). The TxGNN model predicts it may be effective for **thrombotic disease**, but there are **0 clinical trials** and only case-level literature, which mostly shows talc **causing** thrombosis, not treating it. This looks like a knowledge-graph artifact, not a real repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the label data provided (pleurodesis is inferred from the literature) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license entries (3 of them share NDA205555) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Talc is used as a pleural sclerosing agent and as an excipient or filler, and no therapeutic mechanism against thrombosis is documented.

The retrieved literature points the opposite way. When talc-containing tablets are injected intravenously by people who misuse drugs, the reported outcomes are:

- Pulmonary granulomatosis
- Angiothrombotic pulmonary hypertension
- Retinal and cerebral microembolization

The high score (99.85%) most likely reflects a knowledge-graph link between talc and thrombosis as an **adverse outcome**, not a treatment benefit. The other nine predicted indications (exostosis, rheumatoid arthritis, bronchitis, and others) are also rated Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the papers is an RCT. They are ordered by evidence type, then by year.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Review | Curr Opin Oncol | Intrathoracic complications of malignancy; catheter-related superior vena cava thrombosis. No talc therapy for thrombosis. |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Case series | J Can Assoc Radiol | Talc granulomatosis and angiothrombotic pulmonary hypertension in drug addicts (harm). |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Case-control | Int Ophthalmol | Enlarged foveal avascular zone in retinal vein occlusion (20 patients vs 41 controls). Talc retinopathy is mentioned only as another vaso-occlusive disease. |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Case report | Am J Med Sci | Retinal and cerebral talc microembolization in a drug abuser (harm). |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Case report | Arch Neurol | Medullary infarcts and systemic talc granulomatosis after IV methylphenidate (harm). |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Case report | Arch Pathol Lab Med | Pulmonary granulomatosis and thrombosis after IV injection of pentazocine tablets (cellulose, not talc). |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Case report | Rev Clin Esp | Angiothrombotic lung granulomatosis in IV drug users, with talc named as a cause. |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Case report | Tex Heart Inst J | Trousseau syndrome with occult colon cancer. Thrombosis is the disease, not a talc effect. |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Case report | Dtsch Med Wochenschr | Acute right heart failure after IV heroin and flunitrazepam. |
| [41646593](https://pubmed.ncbi.nlm.nih.gov/41646593/) | 2026 | Case report | Cureus | Surgical management of recurrent pneumothorax under ECMO. No talc treatment of thrombosis. |

**Takeaway:** the papers describe talc as a cause of thrombosis and vascular occlusion. None supports a treatment benefit.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205555 | Steritalc (Novatech SA; 3 identical entries) | Powder | Not listed in the data |
| Not available | Sensitive Pocket Sun (Shantou Oushiya Biotechnology Co., Ltd) | Stick | Not listed in the data |

---

## Safety Considerations

Literature signals (from the papers above, not from the label):
- Intravenous talc exposure is associated with pulmonary granulomatosis, pulmonary hypertension, and retinal or cerebral microembolization.
- Inhaled talc is associated with respiratory disease, including endobronchitis, bronchiolitis, and occupational respiratory morbidity.

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trials exist and the literature shows talc causing thrombotic and vascular harm. Nothing supports a therapeutic benefit, so this candidate should not advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications. This is blocking for safety screening.
- Mechanism of action data.
- Any prospective evidence that talc has an antithrombotic effect. Without it, the candidate should be dropped.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


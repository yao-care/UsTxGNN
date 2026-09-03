---
layout: default
title: Nisoldipine
parent: 僅模型預測 (L5)
nav_order: 968
evidence_level: L5
indication_count: 5
---

# Nisoldipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using no specific skill — this is a direct content-generation task per the provided report template, not a coding/debugging/brainstorming task.

---

# Nisoldipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Nisoldipine is a dihydropyridine calcium channel blocker generally used for essential hypertension; detailed original-indication and mechanism-of-action records are currently missing from the evidence pack. The TxGNN model predicts possible efficacy in **Pulmonary Hypertension owing to Lung Disease and/or Hypoxia** (WHO Group 3 PH), but this is currently supported by **0 clinical trials** and only **20 loosely-related mechanistic publications** on hypoxia biology in general — none of which study nisoldipine or this indication directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (dihydropyridine calcium channel blocker class; no TFDA-approved label text available — drug not marketed in Taiwan) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap, remediation pending via DrugBank API query). Based on general pharmacological class knowledge, nisoldipine is a dihydropyridine calcium channel blocker, a class whose members act primarily by inhibiting L-type calcium channels in vascular smooth muscle, producing vasodilation — the basis for its use in hypertension.

The predicted new indication, pulmonary hypertension owing to lung disease and/or hypoxia (WHO Group 3 PH), is mechanistically connected to nisoldipine's original use only through a shared theme of vascular tone regulation: hypoxic pulmonary vasoconstriction raises pulmonary vascular resistance, and calcium-channel blockade could theoretically counteract this. However, it is important to note that this class-level rationale applies most strongly to *vasoreactive* Group 1 pulmonary arterial hypertension (where nifedipine and diltiazem have an established, guideline-supported role) — not to Group 3 PH, where calcium channel blockers are generally **not recommended**, since they can worsen ventilation-perfusion mismatch and systemic hypotension without proven benefit.

The literature evidence retrieved for this candidate does not actually study nisoldipine or calcium channel blockers in the context of pulmonary hypertension; it consists of general reviews on hypoxia biology (brain aging, cognitive impairment, cancer hypoxia signaling, altitude physiology, etc.). This means the current evidentiary basis is disease-mechanism background rather than drug-specific support, and the mechanistic plausibility should be treated as speculative pending direct data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*Note: none of the retrieved literature studies nisoldipine directly; these are general hypoxia-biology publications used by the model as contextual signal for the predicted indication.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Reviews the four basic mechanisms of hypoxemia, including ventilation-perfusion mismatch relevant to lung-disease-related hypoxia |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's role in neurodegeneration vs. neuroprotection; general hypoxia pathophysiology |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical and molecular mechanisms of cognitive impairment from acute/chronic hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | General overview of hypoxia-mediated biological control across organ systems |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Deubiquitinase regulation of HIF under hypoxia; cancer-focused, not PH-specific |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumor hypoxia; oncology-focused |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Revista Médica del IMSS | High-altitude hypobaric hypoxia physiology and acclimatization |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Commentary | Journal of Applied Physiology | Brief commentary on hypoxia research translation |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Role of hypoxia in multiple sclerosis pathology |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Preclinical/Mechanistic | Advanced Science | ac4C/NAT10/HIF-1α feedback loop driving hypoxia tolerance in gastric cancer cells |

---

## US Market Information

Nisoldipine is currently **not marketed** in this jurisdiction (market status: 未上市, total licenses on file: 0). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields — key warnings, contraindications, and drug-drug interactions — are currently marked as data gaps in the evidence pack; TFDA label retrieval is flagged as a **Blocking** severity gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no drug-specific literature supporting nisoldipine's use in this indication — the retrieved literature addresses general hypoxia biology, not the drug or disease pairing. Combined with missing MOA data, missing safety/label data (a blocking gap), and the drug's current non-marketed status, the evidence is insufficient to advance beyond hypothesis generation.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings, contraindications) — currently a blocking data gap (DG001)
- Verified mechanism-of-action data via DrugBank API (DG002)
- Direct pharmacological or clinical evidence linking nisoldipine (or the dihydropyridine class) specifically to WHO Group 3 pulmonary hypertension, rather than general hypoxia biology
- Specialist clinical review of the known guideline caution against calcium channel blockers in Group 3 PH (risk of worsening V/Q mismatch and systemic hypotension) before any further development
- Preclinical or clinical trial data in a hypoxic pulmonary hypertension model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 662
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Eplerenone: From Hypertension to Pulmonary Hypertension (Multifactorial / Unclear Mechanism)

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor (MR) antagonist, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, but there are currently **0 registered clinical trials** and **0 publications** directly supporting this specific indication. The top-ranked prediction is therefore a computational signal only. The closest related prediction (pulmonary hypertension owing to lung disease and/or hypoxia) has 13 retrieved publications, mostly preclinical or indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 6 listed authorizations are cancelled) |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, eplerenone is a selective MR antagonist. It blocks the effects of aldosterone and related steroids on vascular tone, sodium handling, inflammation and fibrosis. Its efficacy in hypertension is established, and mechanistically it may be applicable to pulmonary vascular disease.

The score is very high (0.995), but it likely reflects knowledge-graph proximity to the word "hypertension" and to shared aldosterone and vascular-remodeling pathways. This category is distinct from systemic hypertension and from pulmonary arterial hypertension (PAH), so the model may be over-generalizing. No trial or literature evidence was supplied for this exact indication.

For the neighbouring prediction, pulmonary hypertension owing to lung disease and/or hypoxia, there is more supportive biology:
- Preclinical work shows that chronic intermittent hypoxia activates MR signaling and drives tissue fibrosis and remodeling (kidney, atrium), and that eplerenone attenuates these effects.
- Studies in PAH models show that aldosterone contributes to pulmonary vascular remodeling, and that eplerenone reduced pulmonary vascular remodeling in rodents.

These findings are indirect. They do not establish benefit on pulmonary pressure or clinical outcomes in patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication, and none for the four other predicted indications.

---

## Literature Evidence

No literature was available for the top-ranked indication. The table below shows the most relevant publications retrieved for the related prediction, **pulmonary hypertension owing to lung disease and/or hypoxia**. Study types are provisional and based mainly on titles and abstract excerpts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27230560](https://pubmed.ncbi.nlm.nih.gov/27230560/) | 2016 | Clinical study (design not confirmed) | Pol Arch Med Wewn | Examined eplerenone's effect on obstructive sleep apnea severity and arterial stiffness in resistant hypertension |
| [41483355](https://pubmed.ncbi.nlm.nih.gov/41483355/) | 2026 | Review | Curr Hypertens Rep | Evaluates aldosterone blockade for blood pressure control and oxygenation in OSA-related hypertension |
| [35043674](https://pubmed.ncbi.nlm.nih.gov/35043674/) | 2022 | Preclinical (rat) | Am J Physiol Lung Cell Mol Physiol | MR antagonists (eplerenone, spironolactone) in established PAH in the SU5416-hypoxia model; improved interventricular dependence |
| [29499691](https://pubmed.ncbi.nlm.nih.gov/29499691/) | 2018 | Preclinical | BMC Pulm Med | Eplerenone attenuated pulmonary vascular remodeling rather than right ventricular remodeling in PAH |
| [25001622](https://pubmed.ncbi.nlm.nih.gov/25001622/) | 2014 | Preclinical / mechanistic | Circulation | Hypoxia upregulates StAR, stimulating aldosterone synthesis in pulmonary artery endothelial cells and promoting vascular fibrosis |
| [27006450](https://pubmed.ncbi.nlm.nih.gov/27006450/) | 2016 | Preclinical / mechanistic | FASEB J | Aldosterone up-regulates Raptor (mTORC1) in pulmonary artery smooth muscle cells, promoting PAH |
| [35568141](https://pubmed.ncbi.nlm.nih.gov/35568141/) | 2022 | Preclinical (rat) | Cardiovasc Pathol | Eplerenone improved atrial remodeling induced by chronic intermittent hypoxia |
| [35346763](https://pubmed.ncbi.nlm.nih.gov/35346763/) | 2022 | Preclinical (rat) | Exp Gerontol | Chronic intermittent hypoxia induces renal fibrosis through MR activation |
| [15199296](https://pubmed.ncbi.nlm.nih.gov/15199296/) | 2004 | Review | Curr Opin Nephrol Hypertens | Glucocorticoid-mediated MR activation and hypertension |

Other retrieved papers (choroidal blood flow, liver cirrhosis, perivascular fat, renoprotection in rats) are off-target for this indication and are not listed.

---

## US Market Information

All six listed authorizations are cancelled. No approved indication text was available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021437 | Eplerenone (Mylan Pharmaceuticals Inc.) | Tablet, film coated | Not available |
| ANDA214663 | Eplerenone (Rising Pharma Holdings, Inc.) | Tablet | Not available |
| ANDA207842 | Eplerenone (Proficient Rx LP) | Tablet, coated | Not available |
| ANDA213812 | Eplerenone (Camber Pharmaceuticals, Inc.) | Tablet, film coated | Not available |
| ANDA206922 | Eplerenone (Accord Healthcare, Inc.) | Tablet, film coated | Not available |

One further authorization (ANDA208283, American Health Packaging, tablet, film coated) is also cancelled.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver disease, gallbladder disease, diabetic nephropathy, impaired renal function disease.
- **Drug Interactions**: 100 interactions were identified. Examples of **Major** interactions:
  - Aprepitant
  - Clarithromycin
  - Clotrimazole
  - Potassium chloride
  - Potassium citrate
  - Potassium bicarbonate

  Examples of **Moderate** interactions include corticosteroids (hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), aspirin, bupropion, dronabinol, nabilone and miconazole.
- **Practical concern**: for the renal and renovascular predictions, hyperkalemia and renal-function risk would need careful consideration.

Please refer to the package insert for key warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a model score alone (L5), with no trials or literature, and it may reflect generalization from the word "hypertension". The related hypoxia-associated pulmonary hypertension prediction (L4) has mechanistic and preclinical support, but this is indirect and does not show benefit on pulmonary pressure or clinical outcomes. It is better treated as a research question than a development candidate. The other predictions (malignant hypertensive renal disease, malignant renovascular hypertension, Braddock syndrome) have no supporting evidence. The acute malignant conditions would also need rapid-acting parenteral therapy, which an oral MR antagonist does not provide.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Clarification of the disease definition for the top-ranked prediction, and whether it overlaps with PAH or Group 3 pulmonary hypertension
- Systematic review of MR antagonist data in pulmonary hypertension, followed by clinical evidence such as a pilot trial if the signal holds
- Hyperkalemia and renal safety monitoring plan, including management of potassium-related interactions
- Clarification of current US marketing status, since all listed authorizations are shown as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


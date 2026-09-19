---
layout: default
title: Anemone Hepatica Var Obtusa Antimony Potassium Tar
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 0
---

# Anemone Hepatica Var Obtusa Antimony Potassium Tar
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

# Complex Homeopathic Preparation (containing pertussis-related components): Insufficient data, unable to complete drug repurposing analysis

## One-Sentence Summary

This product is a complex homeopathic preparation containing nine botanical/mineral/biological components, including traditional respiratory medicinal ingredients such as Atropa belladonna, Lobelia inflata, Antimony potassium tartrate, as well as Bordetella pertussis infected sputum (pertussis nosode).
The TxGNN model **failed to generate any predicted indications**, as this complex preparation has no corresponding ID in DrugBank, preventing the knowledge graph embedding calculation from being completed.
Currently there are **no clinical trials or literature** supporting its drug repurposing direction, with severely insufficient overall data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original indications | No data (component composition indicates traditional respiratory/pertussis use) |
| Predicted new indications | None (TxGNN did not generate predictions) |
| TxGNN prediction score | — |
| Evidence level | L5 (only model input, no actual research) |
| US market status | Not marketed (0 approvals) |
| Total number of approvals | 0 |
| Recommended decision | **Hold** |

---

## Why can't this prediction be assessed?

This product is a nine-component complex preparation with characteristics similar to homeopathic or traditional herbal complex preparations, with **no DrugBank ID** in modern drug databases, causing the TxGNN knowledge graph to fail to locate the drug node, with the prediction pipeline interrupting at the input stage.

The traditional use direction can be inferred from the component composition:

- **Bordetella pertussis infected sputum (nosode)**: A classic nosode preparation used in homeopathy for pertussis
- **Atropa belladonna / Hyoscyamus niger**: Containing atropine/scopolamine, with anticholinergic activity, traditionally used for smooth muscle spasm and respiratory symptoms
- **Lobelia inflata**: Containing lobeline, traditionally used as a respiratory stimulant, once used for bronchospasm
- **Antimony potassium tartrate (tartar emetic)**: Traditional expectorant, rarely used in modern times
- **Ipecac**: Traditional emetic/expectorant

This combination points toward **respiratory tract infection, pertussis, or chronic bronchitis** and other traditional indications, but all are within the homeopathic/traditional medicine context, lacking support from modern evidence-based medicine. In the absence of a DrugBank ID and TxGNN predictions, formal mechanism of action correlation analysis cannot be performed.

---

## Clinical trial evidence

No related clinical trials are currently registered.

---

## Literature evidence

No related literature is currently available for citation.

---

## US market information

This product has no NDA/BLA/ANDA approval records in the United States (query result: 0 approvals).

---

## Safety considerations

Please refer to the label warnings and contraindications.

> **Special note**: This product contains multiple known pharmacologically active components. Even when used in extremely low concentrations in homeopathic preparations, the following potential risks should be considered:
> - **Atropa belladonna / Hyoscyamus niger**: Contains tropane alkaloids; overdose may cause anticholinergic toxicity
> - **Antimony potassium tartrate**: Contains antimony, a heavy metal with toxicity
> - **Ipecac**: Prolonged use may cause cardiomyopathy
> - **Lobelia inflata**: Overdose may cause nausea, vomiting, and respiratory depression

---

## Conclusion and next steps

**Decision: Hold**

**Rationale:**
TxGNN cannot generate any drug repurposing predictions for this complex homeopathic preparation, primarily due to lack of DrugBank ID and modern pharmacological data; combined with no US market authorization record and completely missing safety data, the current conditions are not sufficient for conducting a drug repurposing assessment.

**To advance, the following data must be supplemented:**

1. **Drug identity confirmation**: Confirm whether there is a corresponding DrugBank entry, or identify a single main active ingredient (active moiety) for independent assessment
2. **MOA data**: Review the mechanism of action of each component, particularly the pharmacological literature on Atropa belladonna and Lobelia inflata
3. **Safety data**: Download and parse FDA/TFDA-related labeling PDFs, or consult the Homeopathic Pharmacopoeia
4. **Indication confirmation**: Confirm whether this complex preparation has any formal approved indications in any country
5. **Redesigned prediction input**: If the main active component is confirmed, TxGNN prediction workflow can be re-executed for the single component (such as lobeline or belladonna alkaloids)
6. **Clinical literature search**: Conduct separate PubMed searches using the INN of each component to collect individual component clinical or preclinical evidence

> ⚠️ **Disclaimer**: The results of this report are for research reference only and do not constitute medical advice. Drug repurposing candidates must undergo clinical validation before application in clinical practice.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Bexarotene
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Bexarotene: predicted new indication Primary cutaneous B-cell lymphoma (evidence level L5). Approved use: Primary cutaneous T-cell lymphoma (including primary cutaneous T-cell…"
monitor_inn: "BEXAROTENE"
predicted_indications: ["primary cutaneous B-cell lymphoma", "lymphosarcoma"]
---

# Bexarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Bexarotene: From Primary Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Bexarotene was originally used to treat primary cutaneous T-cell lymphoma (CTCL).
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma**, but **no clinical trials** are registered for this specific indication, and the **10 publications** found are mostly general reviews and case reports. Bexarotene is mentioned only in passing as a treatment for the T-cell forms.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary cutaneous T-cell lymphoma (including primary cutaneous T-cell non-Hodgkin lymphoma) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no direct studies) |
| US Market Status | Cancelled only (no currently valid US licenses) |
| Number of NDAs | 9 authorizations in total (2 NDAs and 7 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, bexarotene is a synthetic retinoid that selectively activates retinoid X receptors (RXR). It promotes apoptosis and slows proliferation in malignant T-cells, and its efficacy in cutaneous T-cell lymphoma is established.

The prediction is only partly convincing. Cutaneous B-cell lymphoma is biologically distinct from the T-cell forms: it has a different cell of origin and different signaling dependencies. The RXR-mediated mechanism therefore cannot be assumed to carry over. The very high TxGNN score is most likely driven by network proximity to the approved T-cell lymphoma indications, not by B-cell-specific biology. No B-cell-specific mechanistic data are available.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary cutaneous B-cell lymphoma.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31932947](https://pubmed.ncbi.nlm.nih.gov/31932947/) | 2020 | Review | Der Pathologe | Overview of cutaneous lymphoma presentation and treatment. Later-stage mycosis fungoides and Sézary syndrome need systemic therapy, including bexarotene. This concerns T-cell disease, not B-cell. |
| [31511903](https://pubmed.ncbi.nlm.nih.gov/31511903/) | 2019 | Review | Der Hautarzt | Same authors and content as above, in a dermatology journal. |
| [14616487](https://pubmed.ncbi.nlm.nih.gov/14616487/) | 2003 | Review | Australas J Dermatol | Management of primary cutaneous T- and B-cell lymphomas. Classical options include retinoids, phototherapy, radiotherapy and chemotherapy. |
| [19786826](https://pubmed.ncbi.nlm.nih.gov/19786826/) | 2009 | Review | Skin Pharmacol Physiol | New and experimental skin-directed therapies for cutaneous lymphomas, covering both T- and B-cell types. |
| [20806174](https://pubmed.ncbi.nlm.nih.gov/20806174/) | 2010 | Review | Ther Umsch | General overview of cutaneous lymphomas and the WHO/EORTC classification. |
| [29881891](https://pubmed.ncbi.nlm.nih.gov/29881891/) | 2018 | Case series | Der Hautarzt | Case series of 163 patients with primary cutaneous lymphoma from routine clinical practice. |
| [22508770](https://pubmed.ncbi.nlm.nih.gov/22508770/) | 2012 | Case series | Arch Dermatol | Five cases of a new T-cell lymphoma subtype (follicular helper T-cell). Not B-cell and not bexarotene-specific. |
| [23941646](https://pubmed.ncbi.nlm.nih.gov/23941646/) | 2013 | Case series | J Cutan Pathol | Diagnostic pitfalls of cutaneous follicular helper T-cell lymphoma, which can be mistaken for B-cell lymphoma. Rituximab failed in the case described. |
| [15861527](https://pubmed.ncbi.nlm.nih.gov/15861527/) | 2005 | Case report | Croat Med J | EBV-associated cutaneous B-cell lymphoma in a patient with mycosis fungoides, resolved with topical acyclovir. Bexarotene was not the treatment. |
| [15636695](https://pubmed.ncbi.nlm.nih.gov/15636695/) | 2004 | Case report | Clin Lymphoma | Lymphomatoid papulosis from childhood with anaplastic large-cell lymphoma of the small bowel. A T-cell spectrum disease. |

None of these publications reports bexarotene efficacy in B-cell lymphoma.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021055 | Targretin (Bausch Health US) | Capsule, liquid filled | Not listed in the license record |
| NDA021056 | Targretin (Bausch Health US) | Gel | Not listed in the license record |
| ANDA203174 | Bexarotene (Mylan) | Capsule, liquid filled | Not listed in the license record |
| ANDA215398 | Bexarotene (Amneal) | Gel | Not listed in the license record |
| ANDA209886 | Bexarotene (Upsher-Smith) | Capsule | Not listed in the license record |

All 9 authorizations (2 NDAs and 7 ANDAs) have a cancelled status. Bexarotene exists in both oral (capsule) and topical (gel) forms.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (rexinoid, selective RXR agonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Not quantified. Leukopenia appears among the drug-disease contraindication associations in the knowledge graph. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver function, thyroid function (the literature describes bexarotene-induced central hypothyroidism), pancreatic and metabolic status |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications and cautions (from knowledge graph associations, not label text):** liver failure, liver disease, pancreatitis, gallbladder and biliary tract disease, obstructive jaundice, hypothyroidism (including myxedema and congenital hypothyroidism), diabetes mellitus, diabetic ketoacidosis, leukopenia, and substance abuse/dependence.
- **Drug Interactions:** 100 interactions were recorded. Those retrieved include:
  - **Major:** GLP-1 agonists and related antidiabetic agents (albiglutide, dulaglutide, exenatide, alogliptin) and eluxadoline.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), cisapride, eliglustat and granisetron.
  - **Minor:** aprepitant, clarithromycin and clotrimazole.
- **Literature signal:** published reports describe bexarotene-induced central hypothyroidism in lymphoma patients.

For the full list of warnings, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any trial or B-cell-specific study. The literature mentions bexarotene only for T-cell disease, and the RXR mechanism cannot be assumed to apply to B-cell lymphoma. All US authorizations are also cancelled. The same data show that Sézary syndrome (a T-cell variant) has far stronger bexarotene evidence, including a terminated Phase 3 trial. That is an extension of the existing T-cell indication and not a true repurposing case.

**To proceed, the following is needed:**
- B-cell-specific preclinical data showing RXR pathway dependence or in vitro activity in cutaneous B-cell lymphoma models
- Detailed mechanism of action data
- Case series or early-phase clinical data in cutaneous B-cell lymphoma
- A decision on the route of administration (oral capsule vs. topical gel) suited to skin-limited B-cell disease
- Current package insert safety information (warnings and contraindications), including a thyroid, lipid and liver monitoring plan
- Verification of current US commercial availability, given the cancelled status of all authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


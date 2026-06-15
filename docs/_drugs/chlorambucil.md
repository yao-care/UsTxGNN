---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 505
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Using the `txgnn-pipeline` skill to confirm context. This is a TxGNN repurposing report for the US/Taiwan deployment. Now generating the report from the Evidence Pack.

---

# Chlorambucil: From Chronic Lymphocytic Leukemia to IGHV-Mutated CLL/SLL

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with decades of clinical use in B-cell malignancies, most notably chronic lymphocytic leukemia (CLL).
The TxGNN model predicts it may be specifically effective for **CLL/SLL with IGHV Somatic Hypermutation** — the favorable, post-germinal center subtype known to respond best to alkylating therapy — with indirect Phase 3 subgroup support placing this at Evidence Level **L2**.
No dedicated clinical trials or publications for this specific subtype were retrieved in this dataset (reflecting the drug's absence from the Taiwan registry), though the global CLL literature provides strong off-dataset support; this multi-indication evaluation additionally identifies primary pulmonary lymphoma (L3) and small cell lung carcinoma (L3) as exploratory research questions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia (globally recognized; not registered in Taiwan) |
| Predicted New Indication | CLL/SLL with IGHV Somatic Hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L2 |
| Taiwan Market Status | Not registered |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current data source (DrugBank returned no MOA record). Based on well-established pharmacology, chlorambucil is a bifunctional nitrogen mustard alkylating agent that forms inter-strand and intra-strand DNA cross-links, halting replication and transcription and ultimately inducing apoptosis in proliferating lymphocytes. Its oral bioavailability, manageable toxicity profile, and selective activity in slow-growing B-cell disease established it as a foundational CLL agent for over half a century.

CLL biology is governed critically by the somatic hypermutation status of the immunoglobulin heavy chain variable region (IGHV). The IGHV-mutated subtype — the entity predicted here — originates from post-germinal center memory B cells, carries a significantly more favorable prognosis, and is consistently more sensitive to alkylating agent–based regimens compared to the IGHV-unmutated subtype. Multiple prospective analyses confirm that IGHV-mutated patients treated with chlorambucil-based combinations achieve substantially longer progression-free survival (and in some cases durable plateau responses), while IGHV-unmutated patients require more intensive approaches such as BTK inhibitors or venetoclax.

The landmark CLL11 Phase 3 trial (obinutuzumab + chlorambucil versus rituximab + chlorambucil in treatment-naïve CLL) prespecified IGHV mutation status as a stratification and subgroup variable, providing indirect Phase 3 evidence that this biomarker modifies chlorambucil-based treatment outcomes. This indirect support forms the basis for the L2 classification. Although this dataset retrieved no results for this specific subtype (a consequence of Taiwan non-registration rather than absence of global evidence), international guidelines (ESMO, NCCN, iwCLL) consistently recognize chlorambucil + anti-CD20 combinations as a viable option for unfit or older patients with IGHV-mutated, low-risk CLL.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this dataset for this specific indication.

> **Context:** Indirect Phase 3 evidence is available from the CLL11 trial (NCT01010061), which enrolled treatment-naïve CLL patients and stratified outcomes by IGHV mutation status. That trial is not captured here because the dataset query targeted the highly specific disease name "CLL/SLL with IGHV somatic hypermutation" rather than CLL broadly.

---

## Literature Evidence

Currently no related literature available in this dataset for this specific indication.

> **Context:** The empty result reflects the specific subtype query, not the absence of chlorambucil evidence in CLL. Extensive peer-reviewed literature on chlorambucil in CLL — including IGHV-stratified analyses — exists in PubMed outside this dataset's query scope.

---

## Taiwan Market Information

Chlorambucil is not registered in Taiwan. No product licenses were found in the TFDA database.

> Chlorambucil (brand name: Leukeran) holds regulatory approval in multiple international markets — including the United States (FDA-approved for CLL, Hodgkin's lymphoma, non-Hodgkin's lymphoma, and Waldenström's macroglobulinemia) and the European Union — for B-cell malignancies. Its absence from the Taiwan registry represents a local registration gap, not a global approval gap.

---

## Cytotoxicity

Chlorambucil is an antineoplastic alkylating agent (nitrogen mustard class) and meets all criteria for the cytotoxicity section: it is used for hematologic malignancies, belongs to the nitrogen mustard/alkylating agent class, and is classified as conventional cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard / Alkylating agent (bifunctional) |
| Myelosuppression Risk | High — bone marrow suppression (neutropenia, thrombocytopenia, anemia) is the primary dose-limiting toxicity; onset is typically cumulative with prolonged oral dosing |
| Emetogenicity Classification | Low (oral administration; lower emetogenic potential than IV alkylating agents such as cyclophosphamide) |
| Monitoring Items | CBC with differential (at least every 2 weeks during therapy), liver function tests, renal function (chlorambucil clearance is hepatic), uric acid (tumor lysis risk in bulky disease) |
| Handling Protection | Must follow cytotoxic drug handling regulations — wear gloves and protective gown; do not crush or break tablets; dispose per hazardous waste protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (warnings, contraindications, and drug interactions) were not available in this dataset. The TFDA package insert query returned no records due to non-registration; DDI query returned no results. Refer to the Leukeran (chlorambucil) international prescribing information for complete safety details, including known risks of secondary malignancy and reproductive toxicity with long-term alkylating agent use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorambucil has internationally validated efficacy in CLL, and the IGHV-mutated subtype is mechanistically the population best positioned to benefit from alkylating agent–based regimens; indirect Phase 3 subgroup data from CLL11 provides sufficient scientific and clinical rationale to move forward with a focused evaluation, contingent on resolving the Taiwan regulatory data gaps.

**To proceed, the following is needed:**
- **Resolve DG001 (Blocking):** Download and parse the TFDA package insert PDF to extract Taiwan-specific warnings and contraindications before any S1 safety screening can proceed
- **Resolve DG002 (High):** Query the DrugBank API to retrieve the formal MOA, pharmacokinetics, and toxicity profile for mechanistic analysis
- **Confirm IGHV testing infrastructure:** Verify that standardized IGHV mutation testing (next-generation sequencing or Sanger) is available in the target clinical setting, as patient selection depends entirely on this biomarker
- **Assess competitive landscape:** Evaluate the current standard-of-care positioning of chlorambucil + obinutuzumab versus BTK inhibitors (ibrutinib, acalabrutinib) and venetoclax + obinutuzumab in IGHV-mutated, unfit CLL — chlorambucil-based therapy may still offer a cost-effective role in resource-limited or frail patient contexts
- **Consider companion precision indications:** Primary pulmonary lymphoma (rank 4, L3, 1 Phase II trial + clinical guidelines) merits a separate focused evaluation as a potentially actionable repurposing candidate with more direct evidence than the top-ranked IGHV-mutated CLL subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


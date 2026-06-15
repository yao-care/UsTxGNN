---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist (ERA), primarily used for pulmonary arterial hypertension (PAH) and prevention of digital ulcers in systemic sclerosis.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**,
with **1 indirectly related clinical trial** and **16 publications** currently available — most of which are mechanistic or preclinical rather than direct RA clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 — Preclinical and mechanistic studies |
| Taiwan Market Status | Not Marketed (0 TFDA licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on mechanistic context clues throughout this report and established pharmacology, Bosentan is a **dual endothelin receptor type A and B (ET~A~/ET~B~) antagonist**. Endothelin-1 (ET-1) is a potent vasoconstrictor and pro-inflammatory mediator produced by vascular endothelial cells.

The biological rationale for repurposing Bosentan in RA centers on the role of ET-1 in joint inflammation. ET-1 concentrations are significantly elevated in the synovial fluid of RA patients, where ET-1 acts through ET~A~/ET~B~ receptors to amplify the release of pro-inflammatory mediators including TNF-α and leukotriene B4 (LTB4), while also driving synovial angiogenesis — a key feature of RA pathology. Dual receptor blockade by Bosentan could therefore suppress synovial inflammation and slow joint destruction via this pathway.

The most compelling preclinical evidence comes from PMID 22249931, which directly demonstrated that Bosentan significantly ameliorated disease in a collagen-induced arthritis (CIA) mouse model — the gold-standard preclinical model of RA. Additional animal studies (PMID 18515326; PMID 16766656) show that the ET-1 pathway participates in arthritis-associated edema, neutrophil recruitment, and pain signaling (hypernociception) through a cascade involving IFN-γ, ET-1, and prostaglandins. Despite this mechanistic coherence, **no completed clinical trial has directly tested Bosentan in RA patients**; the only registered trial (NCT06957002) targets Giant Cell Arteritis (GCA), a distinct though mechanistically analogous vasculitic condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | ⚠️ Targets Giant Cell Arteritis (GCA), not RA. Tests whether 3 months of Bosentan added to standard glucocorticoid therapy is superior to glucocorticoids alone in failure-free survival at 12 months. Provides mechanistic analogy (ET-1 in large-vessel vasculitis) but does not constitute direct RA clinical evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Animal Study (CIA Model) | Inflammation Research | **Most relevant:** Bosentan directly ameliorated collagen-induced arthritis in mice; TNF-α upregulates endothelin system genes, establishing the mechanistic link for ERA therapy in RA |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Animal Study | Journal of Leukocyte Biology | ET-1 drives neutrophil accumulation and edema in zymosan-induced arthritis; ET~A~/ET~B~ receptor involvement confirmed in arthritis-related inflammation |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Animal Study | PNAS | IL-15 (elevated in RA) triggers pain hypernociception via a sequential IFN-γ → ET-1 → prostaglandin cascade; dual ERA (ET~A~/ET~B~) blockade inhibited this pathway |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Animal Study | Pain | IL-17 drives articular hypernociception in antigen-induced arthritis; provides context for cytokine-ET cross-talk in RA joint pain |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia Polska | An 8.5-year-old girl with concurrent Eisenmenger syndrome and juvenile RA received Bosentan for PAH; case documents Bosentan use in a patient with active RA (indirect clinical observation) |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Reviews vascular disease in connective tissue diseases; PAH prevalence in SLE, Sjögren's, and RA discussed; notes ET-1 as central mediator |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Disease Clinics of North America | PAH associated with CTDs including RA; supports the broader ET-1-mediated disease spectrum relevant to Bosentan's mechanism |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH as a complication of multiple CTDs including RA; ET-1 pathway as a shared pathological feature across rheumatic diseases |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | Overview of rheumatic skin diseases; broad review context for skin/joint disease intersections |
| [18238768](https://pubmed.ncbi.nlm.nih.gov/18238768/) | 2008 | Review | Am J Health-System Pharmacy | Reviews drug therapy for systemic sclerosis complications; provides clinical context for ERA use in autoimmune connective tissue disease |

---

## Market Information (Taiwan / TFDA)

No Taiwan regulatory authorizations found for Bosentan. The drug is not currently marketed in Taiwan (0 TFDA licenses as of data cutoff 2026-06-02).

> **Note:** Bosentan (brand name Tracleer®) holds regulatory approval in other jurisdictions, including the US FDA for PAH and the EMA for SSc-related digital ulcer prevention. Taiwan market status should be verified independently via the TFDA official website.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug-drug interactions) were not retrieved in this Evidence Pack.

> Please refer to the package insert for safety information. Known class effects for endothelin receptor antagonists include hepatotoxicity (liver enzyme elevations), teratogenicity (category X — dual contraception required), fluid retention, and interactions with CYP3A4/CYP2C9 substrates. Bosentan is a known inducer of CYP3A4 and CYP2C9, which creates clinically significant interactions with warfarin, cyclosporine, and hormonal contraceptives.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for Bosentan in RA is currently limited to preclinical (animal model) studies and mechanistic research (L4); no completed human clinical trials in RA exist. The biological hypothesis is scientifically credible — ET-1 is elevated in RA synovium and the CIA mouse model responded to Bosentan — but this is insufficient to support a clinical repurposing decision at this stage.

**To advance this candidate, the following is needed:**

- **Phase 1/2 clinical trial in RA**: A proof-of-concept trial directly testing Bosentan (or a newer ERA such as macitentan with a better safety profile) in active RA patients, potentially as add-on to methotrexate
- **Biomarker validation**: Confirm that serum/synovial ET-1 levels predict ERA response in RA patient subpopulations
- **MOA data**: Retrieve full DrugBank mechanism-of-action entry (DG002) to complete the mechanistic rationale
- **Safety data**: Retrieve TFDA package insert warnings and contraindications (DG001) before any clinical evaluation
- **Drug interaction assessment**: Bosentan's CYP induction profile is highly relevant given typical RA polypharmacy (MTX, NSAIDs, biologics); formal DDI analysis required
- **Regulatory pathway review**: Confirm US FDA and Taiwan TFDA current approval status; assess feasibility of an IND application for RA indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


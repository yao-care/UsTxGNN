---
layout: default
title: Omadacycline
parent: 僅模型預測 (L5)
nav_order: 991
evidence_level: L5
indication_count: 10
---

# Omadacycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Omadacycline: From Community-Acquired Bacterial Pneumonia to Mycoplasma pneumoniae Pneumonia

## One-Sentence Summary

Omadacycline (Nuzyra) is a third-generation tetracycline (aminomethylcycline) originally used to treat community-acquired bacterial pneumonia (CABP) and acute bacterial skin and skin structure infections (ABSSSI) in adults. The TxGNN model predicts it may also be effective for **Mycoplasma pneumoniae pneumonia** — particularly macrolide-resistant cases — with a **99.79% prediction score**, currently supported by **0 dedicated clinical trials** and **9 relevant publications** (mostly case reports and drug-class reviews).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Community-Acquired Bacterial Pneumonia (CABP), Acute Bacterial Skin and Skin Structure Infections (ABSSSI) — per evidence pack literature/rationale |
| Predicted New Indication | Mycoplasma pneumoniae pneumonia |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is flagged as a data gap (DG002) and not yet available from DrugBank. However, evidence extracted from the pack's repurposing rationale indicates that omadacycline, as a third-generation tetracycline, inhibits bacterial 30S ribosomal protein synthesis and has intrinsic in vitro activity against atypical pathogens such as *Mycoplasma pneumoniae* and *Chlamydophila* — a well-established class characteristic of tetracyclines, not a novel mechanism.

The original approved indication, CABP, is a broad category that already includes atypical-pathogen pneumonia as part of its causative spectrum. The new predicted indication — *M. pneumoniae* pneumonia specifically — is therefore mechanistically a subset of the original approved use rather than a distant repurposing target. This is reinforced by rank-6 evidence in the same pack ("post-bacterial disorder"), where the model surfaced omadacycline's own core registration trials (4 completed Phase 3 RCTs, >2,800 patients across the OASIS program), suggesting the knowledge graph correctly recognizes omadacycline's established antibacterial efficacy.

The clinical rationale for this specific indication is strongest in the context of **macrolide-resistant** *M. pneumoniae* infection, where first-line macrolides fail and tetracyclines serve as an established alternative class. Multiple case reports in the evidence (including pediatric off-label use) describe clinical success with omadacycline in exactly this scenario, which is consistent with — but does not yet constitute controlled-trial proof of — efficacy for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mycoplasma pneumoniae pneumonia specifically.

*(Note: 8 clinical trials exist for omadacycline's core approved indications — CABP and ABSSSI — see rank-6 "post-bacterial disorder" candidate in the source evidence pack; these are not specific to M. pneumoniae pneumonia and are not listed here.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33512346](https://pubmed.ncbi.nlm.nih.gov/33512346/) | 2021 | Review | The Medical Letter on Drugs and Therapeutics | Overview of antibacterial drug options for community-acquired pneumonia |
| [31169800](https://pubmed.ncbi.nlm.nih.gov/31169800/) | 2019 | Review (Drug Profile) | The Medical Letter on Drugs and Therapeutics | Introductory drug profile of omadacycline (Nuzyra), a new tetracycline antibiotic |
| [37728376](https://pubmed.ncbi.nlm.nih.gov/37728376/) | 2023 | PK Study | Expert Opin Drug Metab Toxicol | Pharmacokinetic evaluation of oral-only omadacycline for CABP; confirms activity against atypical bacteria |
| [37842004](https://pubmed.ncbi.nlm.nih.gov/37842004/) | 2023 | Case Report | Front Cell Infect Microbiol | Adolescent with macrolide-unresponsive *M. pneumoniae* pneumonia successfully treated with omadacycline |
| [39867285](https://pubmed.ncbi.nlm.nih.gov/39867285/) | 2025 | Case Report (Compassionate Use) | Infect Drug Resist | Down syndrome pre-schooler with critically ill macrolide-resistant *M. pneumoniae* pneumonia treated via compassionate-use omadacycline |
| [41356655](https://pubmed.ncbi.nlm.nih.gov/41356655/) | 2025 | Case Report | Clin Case Rep | 4-year-old with mixed CAP infection and multiple antimicrobial allergies treated with omadacycline |
| [39224609](https://pubmed.ncbi.nlm.nih.gov/39224609/) | 2024 | Case Report | Front Med | Pediatric case of severe *M. pneumoniae* pneumonia complicated by anti-IgLON5 antibody encephalitis |
| [39789442](https://pubmed.ncbi.nlm.nih.gov/39789442/) | 2025 | Case Report | BMC Infect Dis | Co-infection of Dabie bandavirus and *M. pneumoniae*, illustrating diagnostic complexity in atypical pneumonia |
| [41710381](https://pubmed.ncbi.nlm.nih.gov/41710381/) | 2026 | Case Report (Adverse Event) | Infect Drug Resist | Anticardiolipin antibody positivity and hypercoagulable state following IV omadacycline for *M. pneumoniae* pneumonia — safety signal |

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA/regional label warnings, contraindications, and drug-drug interaction data are not yet available (Blocking data gap DG001 — safety review at Stage S1 cannot proceed without this data).

One relevant safety signal was identified in the literature: a case report (PMID [41710381](https://pubmed.ncbi.nlm.nih.gov/41710381/)) describes new-onset anticardiolipin antibody positivity and a hypercoagulable state temporally associated with IV omadacycline therapy for *M. pneumoniae* pneumonia — this warrants monitoring attention but does not yet establish causality.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis is sound (tetracyclines have intrinsic activity against *M. pneumoniae*, and this pathogen falls within omadacycline's already-approved CABP spectrum), and multiple independent case reports — including compassionate-use in a high-risk pediatric patient — demonstrate real-world clinical success against macrolide-resistant strains. However, no controlled trials exist for this specific indication, use in pediatric patients is currently off-label, and core safety documentation (label warnings, contraindications, DDI) is missing.

**To proceed, the following is needed:**
- TFDA (or applicable local regulator) package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A prospective or retrospective controlled study specifically in macrolide-resistant *M. pneumoniae* pneumonia
- Pediatric safety and efficacy data, given the predominance of off-label pediatric case reports in current evidence
- Follow-up on the anticardiolipin antibody/hypercoagulability signal (PMID 41710381) before broader use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


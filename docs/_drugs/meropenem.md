---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Broad-Spectrum Antibacterial Therapy to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic that inhibits bacterial cell-wall synthesis; the evidence pack does not contain a specific approved-indication record for it (the drug is not currently marketed in Taiwan). The TxGNN model predicts it may be effective for **Bacterial Arthritis** (septic arthritis), with **1 indirectly-related clinical trial** and **20 publications** — mostly case reports and retrospective series on melioidosis/ESBL-related septic arthritis — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — meropenem is not marketed in Taiwan (0 licenses on file), so no approved-indication text exists to cite |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned from DrugBank in this evidence pack (flagged as data gap DG002). Based on the mechanistic rationale accompanying this prediction, meropenem is a broad-spectrum carbapenem that inhibits bacterial penicillin-binding proteins (PBPs), blocking peptidoglycan cell-wall synthesis. This gives it activity against many of the Gram-positive and Gram-negative organisms that commonly cause septic (bacterial) arthritis — including MSSA, Enterobacterales, and *Burkholderia pseudomallei* (melioidosis).

Because no confirmed original indication is on record here, similarity between "original" and "new" indication cannot be formally assessed. However, carbapenems as a class are well established in infectious-disease practice as empirical or targeted therapy for multidrug-resistant or mixed infections, including bone-and-joint infections. The literature evidence below reflects real-world use of meropenem in septic arthritis and osteoarticular infection (notably melioidosis-related and ESBL-producing-pathogen cases), which supports mechanistic plausibility even though it does not constitute a formal approved indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Trial of levofloxacin (not meropenem) to prevent bacteremia in children with acute leukemia/HSCT. Different drug and different indication from bacterial arthritis — only indirectly relevant (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Case report | Joint Bone Spine | Septic arthritis due to ESBL-producing *Klebsiella pneumoniae* successfully treated with meropenem plus amikacin combined with early arthroscopic washout |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective cohort | Le Infezioni in Medicina | Cohort of osteoarticular melioidosis characterizing bone/joint involvement; isolates assessed for carbapenem susceptibility |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective review | Indian J Med Microbiol | 22 cases of musculoskeletal melioidosis (osteomyelitis and septic arthritis); all isolates susceptible to meropenem |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Case report | J Med Case Rep | Disseminated melioidosis presenting with septic arthritis, initially misdiagnosed as tuberculosis, illustrating a challenge to routine antibiotic therapy |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case report | Pharmaceuticals (Basel) | Native hip septic arthritis caused by *Bacillus pumilus*/*Paenibacillus barengoltzii*, managed with long-term linezolid (relevant comparator case) |
| [39288382](https://pubmed.ncbi.nlm.nih.gov/39288382/) | 2024 | Case report + systematic review | J Infect Dev Ctries | Leptospirosis–melioidosis coinfection presenting as ARDS and osteomyelitis |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Retrospective study | Clinical Laboratory | Pathogen distribution and antimicrobial resistance analysis in bone-and-joint infections among young children |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Retrospective/antibiogram study | Eur J Orthop Surg Traumatol | Antibiogram development for empiric antibiotic strategy in non-spinal orthopaedic infections, including septic arthritis |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Preclinical (animal model) | Int J Antimicrob Agents | Colistin-containing cement spacer for carbapenemase-producing *K. pneumoniae* prosthetic joint infection in a rabbit model |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | In vitro study | J Bone Joint Surg Am | Thermal stability and elution kinetics of meropenem and other alternative antibiotics in PMMA bone cement for orthopaedic infection treatment |

---

## Taiwan Market Information

Meropenem currently holds **no TFDA marketing license in Taiwan** (0 licenses on file; market status: 未上市 / Not Marketed). No product name, dosage form, or approved-indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack — data gap DG001, severity Blocking.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L3 is supported by multiple retrospective series and case reports of meropenem used in septic/osteoarticular infections (notably melioidosis-related and ESBL-producing-pathogen septic arthritis), but there is no direct RCT evidence specific to bacterial arthritis and only one indirectly related clinical trial. Critically, TFDA safety data (warnings/contraindications) is a **Blocking**-severity data gap, so a formal S1 safety assessment cannot yet proceed.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently Blocking (DG001); required before any safety evaluation
- Confirmed mechanism-of-action data via DrugBank API — currently High priority gap (DG002)
- Direct comparative or interventional evidence for meropenem specifically in bacterial/septic arthritis (current evidence is largely case-report/cohort level for melioidosis and ESBL-related joint infection)
- Clarification of Taiwan market status — drug is currently unlicensed (0 TFDA licenses), so any repurposing pathway would require new licensing/registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


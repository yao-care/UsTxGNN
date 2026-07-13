---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic approved for treating serious Gram-positive bacterial infections, including complicated skin and soft tissue infections, bacteremia, and right-sided infective endocarditis.
The TxGNN model predicts it may be effective for **Osteoarthritis** (Score: 99.86%), but no supporting clinical trials were found; the 10 retrieved publications all concern daptomycin's use in treating bacterial bone/joint infections — a distinct clinical entity that is likely being confused with osteoarthritis at the knowledge graph level.
Of greater scientific interest, the **Rank #2 prediction (Rheumatoid Arthritis, L4)** carries credible mechanistic support from a 2025 animal study demonstrating daptomycin suppresses arthritis via NF-κB inhibition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-positive bacterial infections (skin/soft tissue infections, bacteremia, right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Not found in database |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, daptomycin is a cyclic lipopeptide antibiotic that inserts into bacterial cell membranes in a calcium-dependent manner, causing depolarization, loss of membrane potential, and bactericidal cell death. It is active against most clinically significant Gram-positive organisms, including MRSA and VRE.

The TxGNN prediction score of 99.86% for osteoarthritis is most likely an artifact of knowledge graph topology rather than biological plausibility. The critical distinction: "osteoarticular infections" (bacterial infections of bone and joints, a recognized daptomycin clinical use) and "osteoarthritis" (chronic degenerative cartilage disease) are biologically unrelated conditions that occupy neighboring nodes in the TxGNN knowledge graph. This proximity creates a statistical association without mechanistic causality. The repurposing rationale embedded in the evidence pack explicitly attributes the high score to this node-label confusion.

There is no established pathway by which an antibiotic would modify cartilage matrix degradation, chondrocyte apoptosis, or non-infectious synovial inflammation — the core biological processes of OA. Accordingly, this prediction should be treated as predictive noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **Important context**: All publications below describe daptomycin's use in treating **bacterial infections of bones and joints** (osteoarticular infections, periprosthetic joint infections). None of them study daptomycin as a treatment for osteoarthritis as a degenerative joint disease. They are retrieved due to keyword overlap and do not constitute repurposing evidence for OA.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospective cohort | International Orthopaedics | High-dose daptomycin + rifampicin evaluated for safety and efficacy in Gram-positive osteoarticular infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospective comparative | J Antimicrob Chemother | Daptomycin vs. standard therapy for osteoarticular infections associated with S. aureus bacteremia |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry / Observational | Medicina Clinica | EU-CORE Spain registry: daptomycin real-world outcomes including osteoarticular infection subset |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospective cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant-associated Gram-positive infections |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Case series | J Antimicrob Chemother | Clinical efficacy and safety of daptomycin in hip and knee periprosthetic joint infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey / Expert consensus | Int J Antimicrob Agents | Survey of ID physicians on antibiotic selection for prosthetic joint infections; daptomycin frequently cited |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro / Microbiological | The Journal of Antibiotics | Daptomycin MIC testing against S. aureus / S. epidermidis isolates from prosthetic joint infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Retrospective microbiological | Surgical Infections | 10-year microbiological profile of staphylococci in osteoarticular infections; antibiotic susceptibility trends |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Reports in Orthopedics | C. striatum septic arthritis in an OA patient referred for knee arthroplasty; daptomycin used for treatment |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case report | ASM Case Reports | Septic arthritis due to C. propinquum in a native joint; first isolation from synovial fluid |

---

## Safety Considerations

Please refer to the package insert for safety information.

**Key safety signal relevant to joint disease context**: One case report (PMID [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), 2023, *Am J Med Sci*) documented daptomycin-induced rhabdomyolysis that precipitated acute gouty arthritis via hyperuricemia — a notable adverse event chain in patients with pre-existing joint disease. Myopathy and rhabdomyolysis occur in approximately 0.2–0.5% of patients receiving daptomycin, and the risk is heightened with concomitant statin use or prolonged courses.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction (Rank #1, L5) has no biological plausibility. It is attributable to knowledge graph node confusion between "osteoarticular infections" (a well-recognized daptomycin clinical application) and "osteoarthritis" (a degenerative disease). None of the 10 retrieved publications provide any evidence of daptomycin modifying OA pathophysiology, and no mechanistic hypothesis can be constructed from available data.

---

**Noteworthy Alternative — Rheumatoid Arthritis (Rank #2, L4, Score 99.84%)**

This prediction is scientifically more credible and warrants separate evaluation:

- A 2025 mouse study (PMID [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/), *Int Immunopharmacol*) demonstrated that daptomycin suppresses collagen-induced arthritis (CIA) by inhibiting NF-κB signaling and downregulating IL-1β, IL-6, and TNF-α — the same cytokine targets as approved RA biologics.
- A follow-up 2025 paper (PMID [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/), *J Med Chem*) synthesized daptomycin-derived cyclic lipopeptides with enhanced anti-arthritis activity, suggesting structure-activity optimization is already underway.
- The cyclic lipopeptide scaffold may disrupt lipid raft-associated immune cell signaling, offering a novel TLR4/NF-κB axis intervention mechanism.

**To advance the RA hypothesis, the following is needed:**

- Retrieve complete MOA data from DrugBank (data gap DG002) to confirm membrane-level immune signaling disruption hypothesis
- Review full US FDA package insert (data gap DG001) to characterize the safety window for non-infectious, long-term use
- Assess the myotoxicity risk profile in the RA patient population, where dosing duration would far exceed typical infection treatment courses
- Evaluate route-of-administration feasibility: current IV-only formulation is unsuitable for chronic RA management; oral or subcutaneous delivery research is a prerequisite
- Design mechanistic cell-based studies in human synoviocytes and macrophages to validate the NF-κB/cytokine findings outside mouse CIA models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


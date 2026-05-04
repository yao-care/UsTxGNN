---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

No specific skill covers Evidence Pack report generation — the system prompt's v5 template applies directly. Generating the report now.

---

# Ertapenem: From Gram-Negative Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a once-daily carbapenem antibiotic used internationally for serious gram-negative bacterial infections, including complicated intra-abdominal infections, community-acquired pneumonia, and complicated urinary tract infections. The TxGNN model predicts it may be effective for **Bacterial Arthritis** — leveraging its broad gram-negative spectrum, excellent bone/synovial tissue penetration, and OPAT-friendly once-daily dosing — with **0 clinical trials** and **10 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in database; ertapenem (INVANZ) is known internationally for serious gram-negative infections — likely a data gap |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| US Market Status | Not found in database (data gap — ertapenem/INVANZ has known FDA approval) |
| Number of NDAs | 0 (database; see note in US Market section) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ertapenem is a 1-β-methyl carbapenem that inhibits bacterial cell wall synthesis by binding preferentially to penicillin-binding proteins PBP-2 and PBP-3. It has a broad antimicrobial spectrum covering gram-negative Enterobacteriaceae (including ESBL-producing strains), anaerobes, and some gram-positive organisms including methicillin-susceptible *Staphylococcus aureus*. Notably, it lacks activity against *Pseudomonas aeruginosa* and *Acinetobacter* — a key pharmacological distinction from meropenem and imipenem. Its extended half-life (~4 hours) and high protein binding enable once-daily IV dosing, a property that makes it uniquely suited to outpatient parenteral antimicrobial therapy (OPAT). Detailed mechanism of action data was not available in the database for this query; the above reflects established pharmacology from the primary literature.

Bacterial arthritis (septic arthritis) is a serious joint infection requiring prompt and often prolonged antibiotic therapy. Gram-negative organisms — including *Klebsiella pneumoniae*, *Citrobacter* spp., *Prevotella* spp., and anaerobes — account for a meaningful proportion of cases, particularly in elderly, immunocompromised, diabetic, or post-surgical patients. This pathogen profile aligns directly with ertapenem's antimicrobial spectrum. Ertapenem achieves adequate concentrations in synovial fluid and bone tissue, supporting its mechanistic applicability to musculoskeletal infections. Its role as a salvage agent for multidrug-resistant gram-negative septic arthritis is supported by the repurposing rationale in the Evidence Pack.

Case-level evidence demonstrates real-world use: ertapenem successfully treated *Klebsiella pneumoniae* septic wrist arthritis (PMID 22233826) and *Citrobacter koseri* septic arthritis with osteomyelitis in a diabetic patient (PMID 31352398). A large OPAT retrospective cohort (n=306, PMID 24709258) documented bone and joint infections as among the most common long-term ertapenem indications, with acceptable safety outcomes. A prospective cohort (PMID 31220276) further validated subcutaneous ertapenem as suppressive therapy for prosthetic joint infections when surgery was not feasible. Together, these data provide mechanistic and observational support for the TxGNN prediction — though no dedicated RCT exists for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ertapenem specifically in bacterial arthritis.

> **Note:** The second-ranked TxGNN prediction — *Staphylococcus aureus* infection (score: 99.28%) — is supported by **8 clinical trials** including an actively recruiting Phase 2 RCT (NCT04886284) directly evaluating cefazolin + ertapenem for MSSA bacteremia, and carries an **L2 evidence grade** with a "Proceed with Guardrails" recommendation. This may represent a stronger and more actionable near-term repurposing opportunity.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Retrospective Cohort | Antimicrob Agents Chemother | In 306 patients receiving long-term outpatient ertapenem, intra-abdominal infections were most common (38%), followed by pneumonia (12%); bone and joint infections were a key indication — long-term use was safe and effective |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Prospective Cohort | J Antimicrob Chemother | Off-label subcutaneous ertapenem as prolonged suppressive therapy in 10 patients with prosthetic joint infection or chronic osteomyelitis where optimal surgery was not feasible; supports use in musculoskeletal infections |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Retrospective Analysis | Clinical Laboratory | Pathogen distribution and antimicrobial resistance in bone and joint infections (BJIs) among children under 4 years; provides epidemiological context for empiric carbapenem selection |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Cohort / Comparative | J Antimicrob Chemother | Evaluated temocillin as an alternative to carbapenems (including ertapenem) for 3GC-resistant Enterobacterales BJIs; underlines carbapenems as current standard of care for resistant organisms in joints |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case Report | J Chemotherapy | *Klebsiella pneumoniae* septic wrist arthritis successfully treated with ertapenem + levofloxacin; direct clinical evidence for ertapenem efficacy in gram-negative septic arthritis |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case Report | BMJ Case Reports | *Citrobacter koseri* septic arthritis with osteomyelitis in a diabetic patient successfully treated with ertapenem; demonstrates salvage role for opportunistic gram-negative joint infections |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case Report | Anaerobe | First reported *Clostridium paraputrificum* native shoulder septic arthritis and osteomyelitis; anaerobic etiology within ertapenem's spectrum; treated with arthroscopic debridement plus antibiotics |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case Report + Review | J Investig Med High Impact Case Rep | *Prevotella bivia* septic arthritis in an immunocompetent adult; anaerobic gram-negative etiology directly covered by ertapenem; initially misdiagnosed, highlighting diagnostic challenges |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro / Translational | Diagn Microbiol Infect Dis | Auranofin (FDA-approved for rheumatoid arthritis) restored ertapenem susceptibility in carbapenem-resistant *E. coli* through synergy; potential combination strategy for refractory gram-negative joint infections |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Review | JAMA | Review of hidradenitis suppurativa diagnosis and treatment; limited direct relevance to bacterial arthritis — included for completeness |

---

## US Market Information

No US market records were returned by the database query for ertapenem (0 licenses found). This is most likely a **data gap** rather than a true absence of approval.

Ertapenem is marketed internationally as **INVANZ** (Merck & Co.) and holds FDA approval for multiple serious gram-negative infection indications. Please verify current US status and label language directly via:

- **FDA Orange Book**: search "ertapenem" at [https://www.accessdata.fda.gov/scripts/cder/ob/](https://www.accessdata.fda.gov/scripts/cder/ob/)
- **DailyMed**: full prescribing information at [https://dailymed.nlm.nih.gov](https://dailymed.nlm.nih.gov)

Known approved indications internationally include: complicated intra-abdominal infections, complicated skin/skin-structure infections, community-acquired pneumonia, complicated urinary tract infections, acute pelvic infections, and prophylaxis for colorectal surgery.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) was not returned by the database for this query.

Please refer to the **INVANZ package insert** for complete safety information. Key safety signals known from the published literature and clinical practice include:

- **Seizure risk**: Carbapenem class effect; risk is elevated in patients with central nervous system disorders, renal impairment, or those receiving high doses
- **Valproic acid interaction**: Carbapenems are known to significantly reduce serum valproate concentrations — this is a clinically important drug interaction that may precipitate seizures in patients on valproic acid for epilepsy
- **β-Lactam cross-sensitivity**: Patients with serious allergy to other β-lactams require careful risk-benefit assessment
- **Hypoalbuminemia**: Ertapenem is highly protein-bound; patients with serum albumin <2.5 g/dL may have suboptimal drug exposures (see PMID 40448546 in the MSSA bacteremia literature)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for ertapenem specifically in bacterial arthritis is currently limited to retrospective cohort studies, case reports, and observational data (L3), with no registered clinical trials targeting this indication. Mechanistic plausibility is strong and individual case reports are encouraging, but the evidence base does not yet support progression to formal development without additional structured investigation.

**To proceed, the following is needed:**

- **Resolve data gaps first**: Obtain the INVANZ package insert (FDA DailyMed or Merck label) to complete the safety profile — this is a blocking item (DG001)
- **Confirm US approval status**: Verify via FDA Orange Book; populate the US market information section with actual NDA data
- **Retrieve DrugBank MOA data**: Query DrugBank API for DB00303 to formally document mechanism of action (DG002 remediation)
- **Prospective registry or feasibility study**: Design a structured observational study of ertapenem OPAT in gram-negative septic arthritis, particularly in ESBL-producing organism cases
- **Define target population**: Focus on patients where gram-negative or anaerobic etiology is likely (elderly, diabetic, immunocompromised, post-surgical) and where OPAT is clinically advantageous
- **Prioritize the MSSA bacteremia indication in parallel**: Rank-2 prediction (*Staphylococcus aureus* infection, score 99.28%) has an actively recruiting Phase 2 RCT (NCT04886284: Cefazolin + Ertapenem for MSSA bacteremia), L2 evidence, and a "Proceed with Guardrails" recommendation — this represents a substantially stronger and more immediately actionable repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


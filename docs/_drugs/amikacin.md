---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Gram-Negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic used for serious gram-negative bacterial infections, including multidrug-resistant organisms such as *Pseudomonas aeruginosa* and *Enterobacteriaceae*.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**,
with **0 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious gram-negative bacterial infections (no current US market registration found in database) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (per current database query) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, amikacin is a semi-synthetic aminoglycoside antibiotic derived from kanamycin. It exerts bactericidal activity by irreversibly binding to the 30S ribosomal subunit of susceptible bacteria, disrupting mRNA translation and causing misreading of the genetic code — a mechanism that is effective across a wide spectrum of gram-negative organisms.

Paratyphoid fever is caused by *Salmonella enterica* serovars Paratyphi A, B, and C, which are gram-negative facultative intracellular bacilli. Amikacin demonstrates confirmed *in vitro* activity against *Salmonella paratyphi* species, and the available literature documents its use in complicated clinical scenarios including neonatal paratyphoid sepsis (PMID 17337835), acalculous cholecystitis due to *S. paratyphi* B (PMID 10505326), and quinolone-resistant *S. paratyphi* B meningitis in a newborn (PMID 9459410). These cases provide real-world precedent, particularly in situations where first-line agents have failed.

The primary limitation of this repurposing prediction lies in the intracellular biology of *Salmonella*: the bacteria replicate within macrophages, an environment where aminoglycosides — which are hydrophilic and poorly membrane-permeable — achieve subtherapeutic intracellular concentrations. Fluoroquinolones and third-generation cephalosporins remain the standard of care. However, in the context of extensively drug-resistant (XDR) enteric fever, amikacin is increasingly discussed as a last-resort salvage option, giving the TxGNN prediction a clinically meaningful niche despite limited prospective evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Comparative Clinical Series | Mikrobiyoloji Bulteni | Treatment outcomes in 48 pediatric paratyphi B patients; amikacin evaluated in strains resistant to classical treatment (ampicillin, chloramphenicol, co-trimoxazole) |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology and Oncology | Acalculous cholecystitis caused by *S. paratyphi* B in a child with acute leukemia; successfully treated with cefepime + amikacin + G-CSF |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | The Journal of Infection | Quinolone-resistant *S. paratyphi* B meningitis in a newborn; illustrates amikacin's role in resistant isolates |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case Report | Indian Journal of Pediatrics | Neonatal paratyphoid sepsis with multidrug-susceptible *S. Paratyphi* A; sepsis screening and management documented |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Clinical + Microbiological | Journal of the Indian Medical Association | 145 blood culture–positive enteric fever cases under 18 years; antibiotic sensitivity patterns of both *S. typhi* and *S. paratyphi* documented |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological Surveillance | Pakistan Journal of Biological Sciences | Isolation and microbiological characterization of *Salmonella paratyphi* from enteric fever patients; susceptibility profiling |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Retrospective Antibiogram Survey | JNMA | Blood culture isolates and antibiogram in a teaching hospital; amikacin sensitivity data for *Salmonella* species included |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Microbiological Study | Indian Journal of Pathology & Microbiology | 280 *S. typhi* strains; MDR strains (21.9%) resistant to chloramphenicol/ampicillin/co-trimoxazole remained sensitive to amikacin and ciprofloxacin |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological Study | The New Microbiologica | Surveillance of *S. typhi* and *S. paratyphi* in Jordan over 12 years (1988–2000); diarrheal disease epidemiology and microbiological characteristics |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Clinical Antibiogram Study | Medical Journal, Armed Forces India | In vitro susceptibility patterns of *S. typhi* and *S. paratyphi* A in 45 blood culture–positive enteric fever cases; reemergence of susceptibility to previously discarded agents |

---

## US Market Information

No registered licenses found in the current database query. Amikacin is widely available as a generic injectable formulation internationally; please verify with the relevant regulatory authority for current approval status and labeling.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is at Level 4 — composed primarily of case reports, retrospective antibiogram surveys, and microbiological surveillance studies. While *in vitro* activity against *Salmonella paratyphi* is established and isolated clinical use in resistant or complicated cases is documented, no prospective or controlled clinical trials have evaluated amikacin specifically for paratyphoid fever.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to complete the mechanistic link analysis
- Package insert data (key warnings, contraindications) to enable formal safety screening
- Prospective or comparative clinical trial evidence specifically evaluating aminoglycosides in MDR/XDR paratyphoid fever
- Pharmacokinetic data addressing intracellular concentrations of amikacin relevant to *Salmonella*-infected macrophage compartments
- Regulatory status confirmation with the relevant national authority (e.g., FDA, EMA) for current market approvals and labeled indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


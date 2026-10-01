---
layout: default
title: Sulfadiazine
parent: Model Prediction Only (L5)
nav_order: 1186
evidence_level: L5
indication_count: 2
---

# Sulfadiazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Sulfadiazine: From Sulfonamide Antibacterial to Pneumocystosis

## One-Sentence Summary

Sulfadiazine is an oral sulfonamide antibacterial marketed in the US as generic tablets.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are **0 registered clinical trials** and only **19 publications**, mostly older reviews and case reports.
Several of these papers concern sulfadiazine combined with pyrimethamine, mainly for toxoplasmosis, so the evidence for sulfadiazine alone in pneumocystosis is weak.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L4 (no trials; only reviews and case-level reports) |
| US Market Status | ✓ Marketed |
| Number of Licenses | 2 (both ANDAs; no NDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. From general pharmacology, sulfadiazine is a sulfonamide that inhibits dihydropteroate synthase (DHPS) in the folate synthesis pathway. Sulfonamide-based regimens such as trimethoprim-sulfamethoxazole are established therapy for *Pneumocystis* pneumonia, so a class-level mechanistic link is plausible, and the high TxGNN score is consistent with it.

The link is indirect, though. Sulfadiazine is not the standard agent for pneumocystosis. Its documented clinical role is mainly in toxoplasmosis, usually combined with pyrimethamine. The one report on the pneumocystosis question (PMID 2645082) also uses the pyrimethamine-sulfadiazine combination. Sulfadiazine's own contribution cannot be separated from pyrimethamine or from the general sulfonamide effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 19 publications retrieved, the 10 most relevant are shown. Several abstracts are missing, so those summaries rely on the title.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Clinical report (design not verifiable) | Clinical Pharmacy | Pyrimethamine-sulfadiazine for *Pneumocystis carinii* pneumonia and toxoplasmosis in AIDS |
| [5315969](https://pubmed.ncbi.nlm.nih.gov/5315969/) | 1971 | Clinical report (not classified) | Ann Intern Med | *Pneumocystis carinii* pneumonia treated with pyrimethamine and sulfadiazine |
| [2969023](https://pubmed.ncbi.nlm.nih.gov/2969023/) | 1988 | Not classified (title suggests review) | J Infect Dis | *Pneumocystis carinii* pneumonia: therapy and prophylaxis |
| [4580723](https://pubmed.ncbi.nlm.nih.gov/4580723/) | 1973 | Review | Transplant Proc | Diagnosis and treatment of pneumocystosis and toxoplasmosis in immunosuppressed hosts |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *Pneumocystis carinii* and *Toxoplasma gondii* |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Antiparasitic drugs overview; trimethoprim-sulfamethoxazole is the drug of choice for pneumocystis pneumonia, and sulfadiazine appears only in a malaria combination |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Review | Prim Care | Protozoan infections in AIDS; PCP is the most common opportunistic infection in AIDS |
| [12645193](https://pubmed.ncbi.nlm.nih.gov/12645193/) | 2002 | Case report | J Formos Med Assoc | Toxoplasma brain abscess with concurrent atypical PCP in an AIDS patient in Taiwan, treated with clindamycin plus sulfadiazine |
| [8248069](https://pubmed.ncbi.nlm.nih.gov/8248069/) | 1993 | Not classified | Presse Med | Sulfonamide intolerance is very frequent in HIV-infected patients, about 10 times more common than in the general population |
| [1088340](https://pubmed.ncbi.nlm.nih.gov/1088340/) | 1975 | Not classified | Ann Intern Med | Hazard of folinic acid with pyrimethamine and sulfadiazine |

No RCTs are present. Most papers are reviews from 1971-2002, and several concern toxoplasmosis rather than *Pneumocystis*.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA080084 | sulfADIAZINE (Chartwell RX, LLC) | Tablet (oral) | Not stated in the record |
| ANDA040091 | SULFADIAZINE (Epic Pharma, LLC) | Tablet (oral) | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records, which does not mean no interactions exist.
- **Literature signals (not label data)**:
  - Sulfonamide intolerance is much more common in HIV-infected patients (PMID 8248069).
  - Antiinfective drugs, including sulfonamides, can cause kidney injury through tubular obstruction (PMID 9562233).
  - Folinic acid combined with pyrimethamine and sulfadiazine has been flagged as hazardous (PMID 1088340).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The DHPS-based mechanism is plausible, but there are no registered trials and no direct evidence for sulfadiazine alone in pneumocystosis. Trimethoprim-sulfamethoxazole is the established sulfonamide therapy, and the supporting literature is dated and often about toxoplasmosis or combination regimens. The label warnings and contraindications are also missing, so safety screening cannot start.

The second prediction, punctate epithelial keratoconjunctivitis (score 99.36%), has no trials, no literature and no clear mechanistic rationale, so it should also be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed tablets
- Mechanism of action data from DrugBank
- A targeted search for direct sulfadiazine data in *Pneumocystis* (monotherapy versus combination)
- A comparison against trimethoprim-sulfamethoxazole to see whether sulfadiazine offers any advantage, such as in patients who cannot take it
- Confirmation that the oral tablet route suits pneumocystosis treatment and prophylaxis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


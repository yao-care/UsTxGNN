---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 1119
evidence_level: L5
indication_count: 10
monitor_inn: "RIBAVIRIN"
predicted_indications: ["chronic hepatitis B virus infection", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatoportal sclerosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related aortitis", "IgG4-related mesenteritis"]
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is an oral and inhaled-class nucleoside antiviral, originally used for chronic hepatitis C and respiratory syncytial virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**,
with **15 clinical trials** and **20 publications** retrieved. Most of these are HCV or HBV/HCV co-infection studies, so direct evidence for ribavirin in HBV is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection; respiratory syncytial virus infection |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (nominal, see note below) |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 5 (all cancelled) |
| Recommended Decision | Hold |

*Note on evidence level:* Under the grading rules, two completed Phase 3 trials would qualify for L1. Only one completed Phase 3 trial (NCT00114361) directly addresses ribavirin in HBV, and it tested a combination with peginterferon. The other Phase 3 trials are HCV-focused. The L1 label should therefore be read cautiously, and the effective strength of direct evidence is closer to L2.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, ribavirin is a guanosine nucleoside analogue with broad antiviral activity. It is thought to act by inhibiting IMPDH, depleting GTP pools, and shifting immune responses toward a Th1 profile. Its efficacy in HCV is established.

Direct anti-HBV activity of ribavirin is weak. Any benefit in HBV would most likely come from immunomodulation when combined with peginterferon or nucleos(t)ide analogues, and not from direct inhibition of viral replication. Both HBV and HCV are chronic hepatotropic viral infections, which explains why the knowledge graph links them. However, the contribution of ribavirin alone in HBV cannot be separated from the combination regimens in the available trials.

---

## Clinical Trial Evidence

The table lists the most relevant trials. Many of the 15 retrieved trials focus on HCV and are only indirectly relevant.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a + ribavirin vs peginterferon alone in HBeAg-negative chronic HBV (PARC study). Most directly relevant trial; results are not summarized in the data. |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot study of ribavirin added to HBV nucleoside analogue therapy to exploit its immunomodulatory properties. |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot study of interferon alpha-2b + ribavirin in chronic hepatitis B. |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a + ribavirin in HCV/HBV co-infection and chronic hepatitis C. |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pegylated interferon alfa-2b + ribavirin in dual chronic hepatitis B and D. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antivirals + ribavirin in HCV with decompensated cirrhosis. HBV relevance is indirect. |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon + ribavirin and IL-28B expression in genotype 1 HCV. Indirect relevance. |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | Surveillance and treatment study in chronic hepatitis C. Not an HBV efficacy trial. |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon/ribavirin in HCV genotype 2/3. Indirect relevance. |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | Completed | 72 | Sofosbuvir + daclatasvir ± ribavirin fixed-dose regimen in genotype 4 HCV. Indirect relevance. |

---

## Literature Evidence

All retrieved publications are reviews or general overviews; no randomized trial publications were found. Most discuss HBV and HCV together.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection; peginterferon + ribavirin was recommended for patients with positive HCV RNA. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual HCV/HBV infection; higher risk of disease progression than mono-infection. |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in chronic HBV and HCV. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and HBV infection outcomes; links to peginterferon + ribavirin response in HCV. |
| [29415584](https://pubmed.ncbi.nlm.nih.gov/29415584/) | 2018 | Review | Expert Rev Anti Infect Ther | Management of chronic viral hepatitis in hematological patients. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | Prevention of hepatocellular carcinoma in chronic HBV and HCV infection. |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | Management of chronic HBV and HCV infections. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review (type not classified) | Annu Rev Med | Treatment strategies for chronic hepatitis B and C; interferon and lamivudine results in HBV. |
| [20001618](https://pubmed.ncbi.nlm.nih.gov/20001618/) | 2009 | Review (type not classified) | Hemoglobin | Treatment and prevention of hepatitis B and C in thalassemia. |

---

## US Market Information

All five authorizations in the data are cancelled; no active US authorization is listed. Approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA079111 | Ribavirin (Aurobindo Pharma) | Tablet, film coated | Cancelled |
| ANDA079117 | Ribavirin (Aurobindo Pharma) | Capsule | Cancelled |
| NDA018859 | Ribavirin (Bryant Ranch Prepack) | Powder, for solution | Cancelled |
| ANDA207366 | Ribavirin (Navinta LLC) | Powder, for solution | Cancelled |
| Not specified | Ribavirinum (Hahnemann Laboratories) | Pellet | Cancelled |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the current package insert for official safety information.

- **Disease associations from the knowledge graph (not label text):** The knowledge graph links ribavirin to contraindication-type associations with several conditions. These include anemia and hemoglobinopathies (sickle cell anemia, hemolytic anemia, pancytopenia), cardiovascular disease (myocardial infarction, coronary artery disease, atherosclerosis), respiratory disease (COPD, asthma, interstitial lung disease, sarcoidosis), impaired renal function, cirrhosis of liver, autoimmune hepatitis, pancreatitis, and periodontitis. These should be verified against the official label.
- **Hemolysis and related effects:** The literature compiled for this report notes ribavirin-associated hemolysis and possible pulmonary toxicity as concerns in some populations. Case reports describe porphyria cutanea tarda emerging during peginterferon/ribavirin therapy.
- **Drug interactions:** The interaction query returned 100 records, but severity levels are all "Unknown". Listed partners include calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole, prednisone, amphotericin B, and morphine. The clinical significance of these interactions has not been graded.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 3 trial directly tests ribavirin (combined with peginterferon) in chronic HBV, and its results are not summarized. Most retrieved trials and all literature are HCV-focused or general reviews, and direct anti-HBV activity of ribavirin is weak. In addition, no active US authorization exists, and label-level safety data are missing, which blocks safety screening.

**To proceed, the following is needed:**
- Obtain and review the results of NCT00114361 (PARC) and NCT00275938 to determine whether ribavirin adds benefit over peginterferon alone in HBV
- Follow up on the pilot trial NCT03759782 (ribavirin plus nucleoside analogues in HBV)
- Retrieve the FDA package insert warnings and contraindications (currently a blocking data gap)
- Obtain detailed mechanism-of-action data from DrugBank
- Grade the severity of the listed drug interactions
- Develop a hemolysis, anemia, and cardiopulmonary monitoring plan for the HBV population
- Clarify the regulatory path, given that all US authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


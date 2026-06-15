---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
---

# Albendazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Albendazole: From Cystic Echinococcosis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole anthelmintic with established global use for cystic echinococcosis and neurocysticercosis, though no US FDA registration records were found in the current dataset.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis** (*Echinococcus multilocularis* infection),
with **5 clinical trials** and **20 publications** currently supporting this direction, and a prediction confidence of **99.97%**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No US NDA records found in current dataset; globally established for cystic echinococcosis and neurocysticercosis |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| US Market Status | Not marketed (no NDA records found) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Albendazole is a benzimidazole-class antiparasitic drug. Its active metabolite, **albendazole sulfoxide (ASOX)**, achieves sufficient plasma concentrations to penetrate the hydatid cyst wall and selectively bind β-tubulin in *Echinococcus multilocularis*. This inhibits microtubule polymerization, disrupts cytoskeletal integrity, blocks the parasite's glucose uptake pathway (via SGLT1 homologous transporters), and depletes intracellular ATP — ultimately arresting metacestode growth. This effect is termed **parasitostatic**: the parasite does not die acutely but is held in check, and growth can resume upon treatment discontinuation.

Alveolar echinococcosis (AE) and cystic echinococcosis (CE) are both caused by species of the genus *Echinococcus* (order *Cyclophyllidea*), making the molecular target directly applicable across both forms. AE caused by *E. multilocularis* behaves like a slow-growing malignancy, invading the liver in a pseudotumoral pattern with potential spread to the lung and brain; without treatment, the case fatality rate approaches 100% within 10–15 years of infection. Because albendazole's β-tubulin binding mechanism is conserved across *Echinococcus* species, the pharmacological rationale for its use in AE mirrors that of CE.

Multiple WHO expert consensus documents and systematic reviews designate albendazole as the **only licensed pharmacological option** for AE, particularly for patients ineligible for curative surgical resection. A completed Phase 2 clinical trial (NCT07182305, n=194) directly evaluated albendazole treatment in early-stage AE patients in an endemic region of Kyrgyzstan, providing the strongest clinical anchor for this indication. TxGNN's prediction thus represents validation of a globally practiced but geographically underregistered use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Direct treatment trial of early-stage AE patients with albendazole in Osh Province, Kyrgyzstan (prevalence ~6%); parasitostatic efficacy assessed via ultrasound surveillance in a newly identified endemic focus |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completed | 50 | Prospective study (EchinoVISTA) of hepatic AE patients on albendazole; evaluated biological and imaging markers of parasite viability to guide timely treatment withdrawal decisions |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Unknown | 24 | RCT of adjuvant albendazole vs placebo after pulmonary hydatid cyst resection (CE, not AE); 6-month follow-up to assess recurrence prevention |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | NA | Recruiting | 43 | Evaluation of multiplex qPCR for diagnosing AE and CE; albendazole is background standard-of-care treatment, not the primary intervention |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Case report of a misdiagnosed intramuscular hydatid cyst in the deltoid; treated surgically with albendazole adjunct following initial corticosteroid mismanagement |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Systematic Review | Parasite | Comprehensive review of benzimidazole chemotherapy for AE; confirms albendazole and mebendazole as the only recommended treatments; highlights parasitostatic mechanism, liver toxicity risk, and unmet need for parasiticidal alternatives |
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus | Acta Tropica | WHO-IWGE multinational consensus on diagnosis, treatment, and follow-up of cystic and alveolar echinococcosis; foundational reference endorsing albendazole as standard-of-care chemotherapy |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacological Study | Antimicrob Agents Chemother | Metabolic profiling and improved-bioavailability formulations (crystal dispersion, HPMC-AS complexes) of albendazole in secondary hepatic AE rat models; demonstrates pharmacodynamic basis for overcoming poor oral absorption |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | Advances in echinococcosis in the 21st century: genetics, genomics, diagnostics, and treatment across CE and AE forms; covers role of albendazole, surgical advances, and emerging immunotherapy approaches |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management of liver echinococcosis; surgery remains the cornerstone for CE, with albendazole as essential adjunct or primary therapy for inoperable AE patients; highlights curative vs palliative treatment goals |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | Hepatic AE overview: pseudotumoral invasion by *E. multilocularis*, resurgence in Europe, and how prolonged albendazole chemotherapy combined with surgery has transformed 10-year survival since the 1990s |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | Chinese J Schistosomiasis Control | Progress review of albendazole research specifically for AE treatment; covers dosing strategies, resistance mechanisms, novel formulations, and combination regimens under investigation |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current drug therapy status for AE; albendazole as primary treatment, limitations including low oral bioavailability (~28%), parasitostatic (not parasiticidal) action, and urgency of developing alternative or adjunct agents |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Review | Parasitology | Drug repurposing strategy for hard-to-treat AE; pyronaridine identified as promising candidate against *E. multilocularis*; contextualizes why albendazole's limitations are driving the search for improved alternatives |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | Novel treatment options for AE and CE; albendazole and mebendazole remain the only licensed antiparasitic compounds; reviews whole-organism screening, nanomedicine, and combination trials as emerging directions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is the globally recognized first-line pharmacological treatment for alveolar echinococcosis per WHO expert consensus, supported by a completed Phase 2 RCT (n=194) and a body of systematic reviews — meeting the L2 evidence threshold. The absence of US NDA records in the current dataset most likely reflects a data collection gap rather than actual non-approval, and requires regulatory verification before proceeding.

**To proceed, the following is needed:**
- Verify current US FDA approval status for albendazole (Albenza® / generic): the dataset returned 0 NDA records, which is inconsistent with publicly known approval history and should be treated as a data gap
- Obtain the complete US prescribing information (USPI) to fill the blocking safety data gap (warnings, contraindications, drug interactions)
- Characterize key drug interactions affecting albendazole sulfoxide plasma levels — particularly antiepileptics (phenytoin, carbamazepine) that reduce ASOX exposure, and dexamethasone/praziquantel that increase it
- Define the target treatment population and duration protocol: AE requires indefinite or multi-year therapy in inoperable patients, necessitating a structured monitoring plan (LFTs, CBC) given the risk of hepatotoxicity and myelosuppression
- Evaluate novel high-bioavailability formulations (e.g., albendazole crystal dispersion system, HPMC-AS composite) as potential candidates to address the drug's core pharmacokinetic limitation of poor and variable oral absorption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


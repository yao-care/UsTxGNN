---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Azathioprine: From Organ Transplant Rejection Prevention to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a thiopurine immunosuppressant internationally established for prevention of organ transplant rejection and treatment of rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)** — a biologically well-grounded finding strongly corroborated by five decades of global clinical use — with **50 clinical trials** and **20 publications** on record, earning an **L1 evidence rating**.
Although the highest raw TxGNN scores (ranks 1–4) correspond to rare genetic structural syndromes with no mechanistic link to azathioprine's immunosuppressive action, IBD (rank 5, score 99.52%) is the most clinically actionable prediction with the strongest evidence base and a direct immunological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention; rheumatoid arthritis (per international regulatory approvals; not registered in current regulatory database) |
| Predicted New Indication | Inflammatory Bowel Disease (IBD) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (0 registrations found) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Azathioprine is a prodrug converted in vivo to 6-mercaptopurine (6-MP) and subsequently to active 6-thioguanine nucleotides (6-TGN). These metabolites integrate into cellular DNA and block purine synthesis, thereby suppressing proliferation of both T and B lymphocytes. A secondary mechanism involves inhibition of Rac1 GTPase signaling, which induces T cell apoptosis independently of purine synthesis blockade. Together, these pathways substantially reduce intestinal mucosal immune over-activation and suppress pro-inflammatory cytokines including TNF-α and IL-6. Individual variation in TPMT (thiopurine S-methyltransferase) and NUDT15 genotypes governs the metabolic balance between therapeutic efficacy (via the 6-TGN pathway) and hepatotoxicity/myelotoxicity (via 6-methylmercaptopurine), making pre-treatment pharmacogenomic testing a clinical standard before initiating therapy.

Inflammatory bowel disease — encompassing Crohn's disease and ulcerative colitis — is characterized by aberrant activation of intestinal T lymphocytes, excessive cytokine production (TNF-α, IL-6, IL-1β), and failure of mucosal tolerance to the gut microbiome. The pathogenesis directly involves lymphocyte over-proliferation and dysregulated innate-adaptive immune cross-talk — precisely the pathways targeted by azathioprine's dual mechanism of lymphocyte proliferation suppression and T cell apoptosis induction. This mechanistic alignment makes azathioprine biologically well-suited for IBD, distinct from conditions such as rheumatoid arthritis where the same immunosuppressive logic applies.

Globally, azathioprine has been embedded in IBD clinical practice for over 50 years and is recommended in guidelines from the European Crohn's and Colitis Organisation (ECCO) and the American Gastroenterological Association (AGA) as a second-line maintenance therapy for steroid-dependent disease and as a combination partner with anti-TNF biologics to reduce immunogenicity. Its absence from the current regulatory database reflects a registration gap rather than any scientific uncertainty — the TxGNN model's high-confidence IBD prediction is independently validated by an extensive body of clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Large multi-center RCT comparing infliximab monotherapy, AZA monotherapy, and infliximab + AZA combination in biologic/immunomodulator-naïve Crohn's disease; AZA as active comparator confirms its standard-of-care role in IBD |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind RCT directly comparing AZA vs. mesalazine for prevention of clinical relapse in postoperative Crohn's disease with moderate/severe endoscopic recurrence |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified RCT comparing weekly subcutaneous methotrexate vs. oral AZA/6-MP for maintaining steroid-free remission in low-risk pediatric Crohn's disease over 1 year |
| [NCT04713631](https://clinicaltrials.gov/study/NCT04713631) | Phase 2 | Unknown | 40 | Factorial RCT evaluating artesunate and/or curcumin add-on in Crohn's patients on adequate AZA doses with persistent active disease; AZA serves as an established treatment scaffold |
| [NCT00521950](https://clinicaltrials.gov/study/NCT00521950) | N/A | Completed | 853 | First prospective RCT testing whether pre-treatment TPMT genotyping to guide AZA initial dosing is cost-effective and reduces adverse events in IBD patients requiring immunosuppression |
| [NCT02367326](https://clinicaltrials.gov/study/NCT02367326) | N/A | Completed | 400 | Large international clinical trial identifying composite clinical and laboratory scores that predict favorable thiopurine (including AZA) response in IBD patients |
| [NCT03553472](https://clinicaltrials.gov/study/NCT03553472) | N/A | Completed | 97 | Study identifying young IBD patients (<50 years) on immunosuppressants (including AZA) at elevated herpes zoster risk; directly informs vaccination and safety monitoring protocols |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Three-arm RCT comparing infliximab monotherapy, infliximab + AZA combination, and AZA monotherapy in moderate-to-severe active UC; terminated early but provided comparative data |
| [NCT04304950](https://clinicaltrials.gov/study/NCT04304950) | Phase 4 | Completed | 28 | Crossover study investigating whether morning vs. evening administration of AZA or 6-MP for IBD affects disease activity and patient outcomes |
| [NCT00849368](https://clinicaltrials.gov/study/NCT00849368) | Phase 1 | Completed | 6 | Dose-finding study evaluating the minimal allopurinol + AZA dose combination that produces therapeutic 6-TGN levels in IBD, with assessment of TPMT activity and clinical efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Research Article | Cell Reports Medicine | Identifies high prevalence of *Blautia wexlerae* in IBD patients with AZA therapy failure; this gut bacterium reduces 6-MP bioavailability and increases inflammatory macrophages, revealing a microbiome mechanism for AZA resistance |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | Comprehensive state-of-the-art clinical review of thiopurine (AZA, 6-MP, thioguanine) use in IBD, covering pharmacology, efficacy evidence, safety monitoring, and emerging findings including autophagy induction |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Reviews improved molecular understanding of AZA/6-MP in IBD with 45 years of clinical data; highlights Rac1-mediated T cell apoptosis as a key novel mechanism beyond purine synthesis inhibition |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Foundational review establishing the clinical framework for AZA/6-MP pharmacogenetics and 6-TGN/6-MMP metabolite monitoring in IBD; underpins TPMT-guided dosing practice |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Pharmacogenomics Study | Biomedicine & Pharmacotherapy | Demonstrates that TPMT gene methylation differs between very-early-onset and adolescent IBD patients, affecting AZA pharmacokinetics and supporting age-specific dosing adjustments |
| [39921705](https://pubmed.ncbi.nlm.nih.gov/39921705/) | 2025 | Retrospective Study | Expert Rev Clin Pharmacol | Real-world data confirming thiopurine effectiveness and safety in IBD patients with NUDT15 polymorphism; validates genotype-guided dosing to reduce thiopurine-induced leukopenia risk |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Review | Scand J Gastroenterol Suppl | Clinical update on AZA long-term efficacy and safety in IBD; documents Dutch regulatory approval for Crohn's disease and summarizes outcomes from clinical trials up to that point |
| [30954317](https://pubmed.ncbi.nlm.nih.gov/30954317/) | 2019 | Review | Gastroenterol Hepatol | Evaluates evidence on withdrawing aminosalicylates, thiopurines, and methotrexate in IBD patients in sustained remission; informs clinical decision-making on optimal treatment duration |
| [40126153](https://pubmed.ncbi.nlm.nih.gov/40126153/) | 2025 | Epidemiology/Trends | Scand J Gastroenterol | Describes temporal trends in IBD diagnostic and therapeutic practices; contextualizes the evolving but persistent role of thiopurines including AZA within modern biologic-era IBD care |
| [33305616](https://pubmed.ncbi.nlm.nih.gov/33305616/) | 2021 | Review | Pharmacogenomics | Reviews pharmacogenetic markers for IBD treatment response and adverse events; highlights TPMT/NUDT15 genotyping as a validated model for personalizing thiopurine therapy in clinical practice |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azathioprine has over five decades of clinical evidence in IBD — including multiple Phase 3 RCTs, meta-analyses, and Cochrane systematic reviews confirming efficacy for maintaining remission in both Crohn's disease and ulcerative colitis — and is embedded in major international guidelines as a standard second-line immunomodulator; the absence from the current regulatory database represents a registration gap, not an evidence gap.

**To proceed, the following is needed:**
- Retrieve the complete prescribing information (package insert) to document full warnings, contraindications, and drug-drug interaction profile
- Confirm US FDA regulatory status and identify the scope of approved indications in the US label
- Obtain DrugBank pharmacological data (MOA, drug categories, toxicity profiles) to complete the safety assessment framework
- Establish a pre-treatment pharmacogenomic testing protocol (TPMT and NUDT15 genotyping) to identify patients at high risk for myelotoxicity before initiating therapy
- Develop a haematological monitoring plan (CBC with differential, liver function tests, renal function) for ongoing surveillance during treatment
- Define clear IBD indication boundaries (Crohn's disease vs. ulcerative colitis; induction vs. maintenance; monotherapy vs. combination with biologics) for the intended target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


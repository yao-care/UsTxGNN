---
layout: default
title: Primaquine
parent: 僅模型預測 (L5)
nav_order: 1082
evidence_level: L5
indication_count: 8
---

# Primaquine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Primaquine: From Malaria to Pneumocystosis (Pneumocystis Pneumonia)

## One-Sentence Summary

> Primaquine is an 8-aminoquinoline antimalarial, established for over 70 years as the only agent capable of radical cure of *P. vivax*/*P. ovale* malaria and of blocking *P. falciparum* transmission.
> The evidence in this pack supports its established use in combination with clindamycin for **Pneumocystis jirovecii pneumonia (PCP)**,
> with **6 clinical trials (including a 290-patient Phase III RCT)** and **19 publications** — spanning guidelines, systematic reviews, and decades of clinical use — supporting this direction.
> Note: this pack also lists malaria itself (rank 7) as a "predicted" indication; given the depth of evidence, this is almost certainly a data-gap artifact (see Conclusion) rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (radical cure of *P. vivax*/*P. ovale*, transmission-blocking in *P. falciparum*) — established via literature evidence (FDA-licensed since 1952, PMID 22152065); not available from structured regulatory fields (data gap) |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* pneumonia, PCP) — as second-line therapy in combination with clindamycin |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L1 |
| US Market Status | Not marketed (per this dataset) — flagged as a likely data gap, see below |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available (data gap DG002). Based on the clinical and literature evidence contained in this pack, Primaquine is an 8-aminoquinoline whose active oxidative metabolites disrupt mitochondrial and redox function in susceptible organisms. This mechanism underlies its well-established antimalarial activity against *Plasmodium* liver hypnozoites and gametocytes.

The same oxidative/mitochondrial-disruption mechanism has been shown, since at least 1988 (PMID 3261959), to be active against *Pneumocystis jirovecii* — historically classified as a protozoan and now reclassified as a fungus, but sharing mitochondrial vulnerability to 8-aminoquinoline oxidative stress. When combined with clindamycin (which independently inhibits protein synthesis), the combination produces a well-documented synergistic effect against *Pneumocystis*.

Clindamycin–primaquine is not a novel hypothesis: it is an established, guideline-recognized second-line regimen for mild-to-moderate PCP in patients intolerant of or unresponsive to first-line trimethoprim-sulfamethoxazole (TMP-SMX), supported by a completed 290-patient Phase III RCT (NCT00000640) and referenced in the 2016 ECIL guidelines (PMID 27550993) and a 2025 network meta-analysis (PMID 39732393). The TxGNN score here largely reflects a well-established clinical practice rather than a novel mechanistic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Comparative RCT: dapsone/trimethoprim vs. clindamycin/primaquine vs. TMP-SMX for mild-to-moderate PCP in AIDS patients |
| [NCT00000717](https://clinicaltrials.gov/study/NCT00000717) | N/A | Completed | 50 | Safety and efficacy of clindamycin + primaquine for mild-moderate PCP |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Clindamycin-TMP/SMX for PCP after solid organ transplant; clindamycin-primaquine referenced as second-line alternative |
| [NCT07357103](https://clinicaltrials.gov/study/NCT07357103) | Phase 4 | Not yet recruiting | 416 | SPIRIT-PCP platform trial positioning second-line PCP therapies, likely to include clindamycin/primaquine arm |
| [NCT06691321](https://clinicaltrials.gov/study/NCT06691321) | N/A | Recruiting | 60 | Caspofungin for PCP in HIV/AIDS — same disease domain, not a direct primaquine test |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Phase 4 | Withdrawn | 0 | Oral corticosteroids in mild PCP — does not test primaquine directly |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27550993](https://pubmed.ncbi.nlm.nih.gov/27550993/) | 2016 | Guideline | J Antimicrob Chemother | ECIL guidelines for PCP treatment in non-HIV haematology patients; lists clindamycin-primaquine as an alternative regimen |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review/Meta-analysis | Clin Microbiol Infect | Network meta-analysis of RCTs comparing PCP treatment regimens in people with HIV |
| [3261959](https://pubmed.ncbi.nlm.nih.gov/3261959/) | 1988 | In vitro/In vivo | Antimicrob Agents Chemother | Foundational study: clindamycin + primaquine effective against *Pneumocystis carinii* in vitro and in vivo |
| [2060532](https://pubmed.ncbi.nlm.nih.gov/2060532/) | 1991 | Clinical study | Eur J Clin Microbiol Infect Dis | Clindamycin + primaquine as primary treatment for mild/moderate PCP in 36 AIDS patients; 91% response rate |
| [8086551](https://pubmed.ncbi.nlm.nih.gov/8086551/) | 1994 | Clinical trial (ACTG 044) | Clin Infect Dis | Prospective safety/efficacy study of clindamycin + primaquine for mild-moderate PCP |
| [2321069](https://pubmed.ncbi.nlm.nih.gov/2321069/) | 1990 | Clinical study | South Med J | Clindamycin/primaquine therapy and secondary prophylaxis against PCP in AIDS patients |
| [36969352](https://pubmed.ncbi.nlm.nih.gov/36969352/) | 2023 | Review | Avicenna J Med | Management of PCP in HIV and non-HIV immunocompromised patients |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Pneumocystis jirovecii: prevention and treatment overview |
| [36160421](https://pubmed.ncbi.nlm.nih.gov/36160421/) | 2022 | Review (safety) | Front Pharmacol | PCP medication selection in G6PD-deficient patients — directly relevant safety guardrail |
| [41552137](https://pubmed.ncbi.nlm.nih.gov/41552137/) | 2025 | Case report | Cureus | Primaquine-induced methemoglobinemia during empiric PCP treatment in an immunosuppressed transplant patient |

---

## US Market Information

No marketing authorization records are present in this dataset (`total_licenses = 0`). This is inconsistent with the extensive real-world clinical trial and literature evidence showing Primaquine has been an FDA-licensed antimalarial since 1952 and is in routine clinical use worldwide — this discrepancy is flagged as a data gap requiring resolution (see Conclusion) rather than treated as evidence of "unapproved" status.

---

## Safety Considerations

Official structured safety fields (key warnings, contraindications, drug interactions) are unavailable in this pack (data gap DG001, severity: Blocking). Please refer to the package insert for authoritative safety information.

For transparency, the following safety signals recur consistently across the literature evidence reviewed above and should inform any guardrail design:
- **G6PD deficiency / hemolysis risk**: Primaquine's oxidative metabolites can cause clinically significant hemolytic anemia in glucose-6-phosphate dehydrogenase (G6PD)-deficient individuals (PMID 36160421, 25943156). G6PD testing prior to use is standard practice in malaria treatment guidelines.
- **Methemoglobinemia**: Reported both alone and in combination with dapsone, including in immunosuppressed patients treated for PCP (PMID 8757424, 41552137).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clindamycin-primaquine for PCP is supported by L1-level evidence — a completed Phase III RCT, an international treatment guideline, and nearly four decades of clinical use in HIV and non-HIV immunocompromised patients — but the missing TFDA/official label data (DG001, Blocking) prevents this pack from completing a formal S1 safety review, and the known G6PD/hemolysis and methemoglobinemia risks require explicit protocol-level guardrails before clinical advancement.

**To proceed, the following is needed:**
- Resolve DG001: obtain official product label (warnings, contraindications, DDI) to complete S1 safety review
- Resolve DG002: confirm structured MOA data via DrugBank API
- Reconcile the "Not marketed / 0 licenses" regulatory status against the extensive documented approved use of Primaquine — this is likely a data collection gap rather than a true market-status finding, and should be corrected before this candidate is presented externally
- Mandatory G6PD deficiency screening protocol if advancing to clinical evaluation
- Separately re-evaluate rank 7 (malaria) as a data-integrity issue rather than a genuine repurposing candidate, since it is Primaquine's original, already-established indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

